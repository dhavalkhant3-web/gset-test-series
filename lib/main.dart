import 'dart:async';
import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:shared_preferences/shared_preferences.dart';

void main() => runApp(const GsetApp());

class GsetApp extends StatelessWidget {
  const GsetApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'GSET Paper-I Test Series',
        theme: ThemeData(colorSchemeSeed: const Color(0xFF5B5FEF), useMaterial3: true, scaffoldBackgroundColor: const Color(0xFFF5F7FF), cardTheme: const CardThemeData(margin: EdgeInsets.zero, elevation: 2, clipBehavior: Clip.antiAlias), appBarTheme: const AppBarTheme(centerTitle: false, elevation: 0, backgroundColor: Color(0xFFF5F7FF)), inputDecorationTheme: const InputDecorationTheme(filled: true, fillColor: Colors.white, border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(16)), borderSide: BorderSide.none), enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(16)), borderSide: BorderSide.none), focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(16)), borderSide: BorderSide(color: Color(0xFF5B5FEF), width: 1.4)))),
        home: const HomePage(),
      );
}

class PaperInfo {
  final String id, title, date;
  final int questions;
  const PaperInfo(this.id, this.title, this.date, this.questions);
}

const papers = <PaperInfo>[
  PaperInfo('2002_jan', 'January 2002', '20 January 2002', 50),
  PaperInfo('2002_dec', 'December 2002', '1 December 2002', 50),
  PaperInfo('2003_dec', 'December 2003', '7 December 2003', 50),
  PaperInfo('2004_jul', 'July 2004', '25 July 2004', 50),
  PaperInfo('2006_jul', 'July 2006', '2 July 2006', 50),
  PaperInfo('2008_dec', 'December 2008', '7 December 2008', 50),
  PaperInfo('2010_oct', 'October 2010', '24 October 2010', 60),
  PaperInfo('2011_oct', 'October 2011', 'October 2011', 60),
  PaperInfo('2013_sep', 'September 2013', 'September 2013', 60),
  PaperInfo('2013_dec', 'December 2013', 'December 2013', 60),
  PaperInfo('2014_oct', 'October 2014', 'October 2014', 60),
  PaperInfo('2016_sep', 'September 2016', '25 September 2016', 60),
  PaperInfo('2017_aug', 'August 2017', '27 August 2017', 60),
  PaperInfo('2018_sep', 'September 2018', '30 September 2018', 50),
  PaperInfo('2019_dec', 'December 2019', '29 December 2019', 50),
  PaperInfo('2021_dec', 'December 2021 (January 2022)', '23 January 2022', 50),
  PaperInfo('2022_nov', 'November 2022', 'November 2022', 50),
  PaperInfo('2023_nov', 'November 2023', 'November 2023', 50),
  PaperInfo('2024_dec', 'December 2024', 'December 2024', 50),
  PaperInfo('2025_nov', 'November 2025', '16 November 2025', 50),
];

class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool gu = true;
  List<Map<String, dynamic>> data = [];
  Set<String> bookmarks = {};
  Set<String> mistakes = {};
  String search = '';
  int todayDone = 0, xp = 0, streak = 0;
  int totalAttempted = 0, totalCorrect = 0, selectedNav = 0;
  final ScrollController _scroll = ScrollController();
  final GlobalKey _papersKey = GlobalKey();

  @override void initState() { super.initState(); _load(); }
  @override void dispose() { _scroll.dispose(); super.dispose(); }

  Future<void> _load() async {
    final raw = jsonDecode(await rootBundle.loadString('assets/questions.json')) as List;
    final prefs = await SharedPreferences.getInstance();
    final today = DateTime.now().toIso8601String().substring(0, 10);
    final stored = prefs.getString('gset_progress_day') ?? '';
    if (stored != today) {
      await prefs.setString('gset_progress_day', today);
      await prefs.setInt('gset_today_done', 0);
    }
    if (!mounted) return;
    setState(() {
      data = raw.cast<Map<String, dynamic>>();
      bookmarks = (prefs.getStringList('bookmarks') ?? []).toSet();
      mistakes = (prefs.getStringList('mistakes') ?? []).toSet();
      todayDone = prefs.getInt('gset_today_done') ?? 0;
      xp = prefs.getInt('gset_xp') ?? 0;
      streak = prefs.getInt('gset_streak') ?? 0;
      totalAttempted = prefs.getInt('gset_total_attempted') ?? 0;
      totalCorrect = prefs.getInt('gset_total_correct') ?? 0;
    });
  }

  List<Map<String, dynamic>> forPaper(String id) => data.where((q) => q['paperId'] == id).toList();
  List<PaperInfo> get filtered => papers.where((p) => p.title.toLowerCase().contains(search.toLowerCase())).toList();

  Future<void> _openPractice() async {
    if (data.isEmpty) return;
    final qs = [...data]..shuffle(Random());
    final selected = qs.take(min(10, qs.length)).toList();
    await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(
      data: selected, gu: gu, title: 'Daily Practice', practice: true,
      bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets,
    )));
    await _load();
  }

  Future<void> _saveSets(Set<String> b, Set<String> m) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList('bookmarks', b.toList());
    await prefs.setStringList('mistakes', m.toList());
    if (mounted) setState(() { bookmarks = b; mistakes = m; });
  }

  void _nav(int index) {
    if (index == 0) { setState(() => selectedNav = 0); return; }
    if (index == 1) {
      setState(() => selectedNav = 1);
      WidgetsBinding.instance.addPostFrameCallback((_) {
        final c = _papersKey.currentContext;
        if (c != null) Scrollable.ensureVisible(c, duration: const Duration(milliseconds: 450), curve: Curves.easeOutCubic);
      });
    } else if (index == 2) {
      _openPractice();
      setState(() => selectedNav = 0);
    } else {
      Navigator.push(context, MaterialPageRoute(builder: (_) => AccountPage(gu: gu))).then((_) {
        setState(() => selectedNav = 0);
        _load();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final ready = papers.where((p) => forPaper(p.id).isNotEmpty && forPaper(p.id).every((q) => q['source_verified'] == true)).length;
    final done = min(10, todayDone);
    final accuracy = totalAttempted == 0 ? 0 : (totalCorrect * 100 / totalAttempted).round();
    final level = (xp ~/ 500) + 1;
    final levelProgress = (xp % 500) / 500;

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 76,
        titleSpacing: 14,
        title: Row(children: [
          _logo(52),
          const SizedBox(width: 10),
          const Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('GSET Paper-I', style: TextStyle(fontSize: 19, fontWeight: FontWeight.w900)),
            Text('Learn • Practice • Succeed', style: TextStyle(fontSize: 11, color: Colors.black54)),
          ])),
        ]),
        actions: [
          IconButton(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => AccountPage(gu: gu))), icon: const Icon(Icons.account_circle_outlined, size: 28)),
          Padding(
            padding: const EdgeInsets.only(right: 8),
            child: SegmentedButton<bool>(
              showSelectedIcon: false,
              segments: const [ButtonSegment(value: true, label: Text('ગુજરાતી')), ButtonSegment(value: false, label: Text('English'))],
              selected: {gu},
              onSelectionChanged: (s) => setState(() => gu = s.first),
            ),
          ),
        ],
      ),
      body: data.isEmpty ? const Center(child: CircularProgressIndicator()) : RefreshIndicator(
        onRefresh: _load,
        child: ListView(
          controller: _scroll,
          padding: const EdgeInsets.fromLTRB(14, 5, 14, 92),
          children: [
            _hero(),
            const SizedBox(height: 12),
            Card(child: Padding(
              padding: const EdgeInsets.symmetric(vertical: 13, horizontal: 4),
              child: Row(children: [
                _metric(Icons.description_rounded, papers.length.toString(), gu ? 'પેપર' : 'Papers', const Color(0xFF2563EB)),
                _metric(Icons.quiz_rounded, data.length.toString(), gu ? 'પ્રશ્નો' : 'Questions', const Color(0xFF7C3AED)),
                _metric(Icons.verified_rounded, ready.toString() + '/' + papers.length.toString(), gu ? 'ચકાસાયેલ' : 'Verified', const Color(0xFF059669)),
                _metric(Icons.track_changes_rounded, '100%', gu ? 'પરીક્ષા ફોકસ' : 'Exam Focus', const Color(0xFFF59E0B)),
              ]),
            )),
            const SizedBox(height: 12),
            LayoutBuilder(builder: (_, c) {
              final target = _dashCard(const Color(0xFF0F9F86), const Color(0xFFE9FBF5), Icons.track_changes_rounded, gu ? 'આજનું Target 🎯' : "Today's Target 🎯", Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(done.toString() + (gu ? ' / 10 પ્રશ્નો' : ' / 10 Questions'), style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w900)),
                const SizedBox(height: 8),
                Row(children: [
                  Expanded(child: ClipRRect(borderRadius: BorderRadius.circular(8), child: LinearProgressIndicator(value: done / 10, minHeight: 8, backgroundColor: const Color(0xFFBFEDE2), color: const Color(0xFF10B981)))),
                  const SizedBox(width: 7),
                  Text((done * 10).toString() + '%', style: const TextStyle(fontWeight: FontWeight.w900, fontSize: 11)),
                ]),
                const SizedBox(height: 6),
                Text(done == 10 ? (gu ? '🎉 Target પૂર્ણ!' : '🎉 Target complete!') : (gu ? 'એક સમયે એક પ્રશ્ન! 💪' : 'One question at a time! 💪'), style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w700)),
              ]));
              final fire = _dashCard(const Color(0xFFEA580C), const Color(0xFFFFF0E8), Icons.local_fire_department_rounded, streak.toString() + (gu ? ' દિવસની સ્ટ્રીક' : ' Day Streak'), Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(gu ? 'સતત ચાલુ રાખો!' : 'Don’t break it!', style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w800)),
                const SizedBox(height: 8),
                Row(children: List.generate(4, (i) => Padding(padding: const EdgeInsets.only(right: 4), child: Icon(Icons.local_fire_department_rounded, size: 19, color: i < min(streak, 4) ? const Color(0xFFF97316) : const Color(0xFFFBD0B7))))),
              ]));
              final stars = _dashCard(const Color(0xFF6D28D9), const Color(0xFFF1EAFE), Icons.star_rounded, xp.toString() + ' XP • ' + (gu ? 'લેવલ ' : 'Level ') + level.toString(), Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                ClipRRect(borderRadius: BorderRadius.circular(8), child: LinearProgressIndicator(value: levelProgress, minHeight: 8, backgroundColor: const Color(0xFFDCCAF9), color: const Color(0xFF7C3AED))),
                const SizedBox(height: 6),
                Text((xp % 500).toString() + ' / 500 XP • ' + (500 - (xp % 500)).toString() + (gu ? ' XP બાકી — લેવલ ' : ' XP to Level ') + (level + 1).toString(), maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w700)),
              ]));
              if (c.maxWidth >= 600) return Row(children: [Expanded(child: target), const SizedBox(width: 9), Expanded(child: fire), const SizedBox(width: 9), Expanded(child: stars)]);
              return Column(children: [Row(children: [Expanded(child: target), const SizedBox(width: 9), Expanded(child: fire)]), const SizedBox(height: 9), stars]);
            }),
            const SizedBox(height: 12),
            LayoutBuilder(builder: (_, c) {
              final actions = [
                _action(Icons.shuffle_rounded, gu ? 'રેન્ડમ પ્રેક્ટિસ' : 'Random Practice', gu ? 'મિશ્ર પ્રશ્નો' : 'Mixed Questions', const Color(0xFF2563EB), _openPractice),
                _action(Icons.track_changes_rounded, gu ? 'દૈનિક ચેલેન્જ' : 'Daily Challenge', gu ? '10 પ્રશ્નો' : '10 Questions', const Color(0xFF059669), _openPractice),
                _action(Icons.menu_book_rounded, gu ? 'ભૂલ બુક' : 'Mistake Book', mistakes.length.toString() + (gu ? ' સાચવેલી' : ' saved'), const Color(0xFFF97316), mistakes.isEmpty ? null : () async {
                  await Navigator.push(context, MaterialPageRoute(builder: (_) => MistakeBookPage(gu: gu, data: data, mistakes: mistakes, bookmarks: bookmarks, onStateChanged: _saveSets)));
                  await _load();
                }),
                _action(Icons.bookmark_rounded, gu ? 'બુકમાર્ક્સ' : 'Bookmarks', bookmarks.length.toString() + (gu ? ' સાચવેલા' : ' saved'), const Color(0xFF7C3AED), bookmarks.isEmpty ? null : () async {
                  final qs = data.where((q) => bookmarks.contains(q['id'])).toList();
                  await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: gu ? 'બુકમાર્ક્સ' : 'Bookmarks', practice: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets)));
                  await _load();
                }),
              ];
              if (c.maxWidth >= 650) return Row(children: [for (int i=0; i<actions.length; i++) ...[Expanded(child: actions[i]), if (i < actions.length - 1) const SizedBox(width: 8)]]);
              return GridView.count(crossAxisCount: 2, shrinkWrap: true, physics: const NeverScrollableScrollPhysics(), mainAxisSpacing: 8, crossAxisSpacing: 8, childAspectRatio: 2.45, children: actions);
            }),
            const SizedBox(height: 14),
            LayoutBuilder(builder: (_, c) {
              final achievements = _section(gu ? 'તાજેતરની સિદ્ધિઓ 🏆' : 'Recent Achievements 🏆', Row(children: [
                _badge(Icons.play_circle_fill_rounded, 'First\nPractice', done > 0),
                _badge(Icons.check_circle_rounded, '10\nQuestions', done >= 10),
                _badge(Icons.local_fire_department_rounded, '3-Day\nStreak', streak >= 3),
                _badge(Icons.psychology_rounded, '100\nQuestions', totalAttempted >= 100),
              ]), const Text(gu ? 'ચાલુ રાખો →' : 'Keep going →', style: TextStyle(fontSize: 12, fontWeight: FontWeight.w800)));
              final progress = _section(gu ? 'તમારો Progress' : 'Your Progress', SizedBox(height: 112, child: Row(children: [
                SizedBox(width: 92, height: 92, child: Stack(alignment: Alignment.center, children: [
                  CircularProgressIndicator(value: accuracy / 100, strokeWidth: 9, backgroundColor: const Color(0xFFE5E7EB), color: const Color(0xFF10B981)),
                  Text(accuracy.toString() + '%', style: const TextStyle(fontSize: 19, fontWeight: FontWeight.w900)),
                ])),
                const SizedBox(width: 10),
                Expanded(child: Text(
                  gu ? 'પ્રયાસ: ' + totalAttempted.toString() + ' / ' + data.length.toString() + '\n' + mistakes.length.toString() + ' ભૂલો સાચવેલી.\nપ્રેક્ટિસ ચાલુ રાખો! 🚀' : 'Attempted: ' + totalAttempted.toString() + ' / ' + data.length.toString() + '\n' + mistakes.length.toString() + ' mistakes saved.\nKeep practicing! 🚀',
                  style: const TextStyle(fontSize: 12, height: 1.35, fontWeight: FontWeight.w700),
                )),
              ])));
              if (c.maxWidth >= 620) return Row(crossAxisAlignment: CrossAxisAlignment.start, children: [Expanded(child: achievements), const SizedBox(width: 10), Expanded(child: progress)]);
              return Column(children: [achievements, const SizedBox(height: 10), progress]);
            }),
            const SizedBox(height: 12),
            Card(
              child: InkWell(
                borderRadius: BorderRadius.circular(18),
                onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => WeakAreasPage(gu: gu, data: data, mistakes: mistakes, bookmarks: bookmarks, onStateChanged: _saveSets))),
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Row(children: [
                    Container(width: 46, height: 46, decoration: BoxDecoration(color: const Color(0xFFFFF1E8), borderRadius: BorderRadius.circular(14)), child: const Icon(Icons.insights_rounded, color: Color(0xFFEA580C))),
                    const SizedBox(width: 12),
                    Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(gu ? 'મારા નબળા વિષયો' : 'My Weak Areas', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w900)),
                      const SizedBox(height: 3),
                      Text(gu ? 'તમારા વિષયવાર પરિણામ પરથી લક્ષિત પ્રેક્ટિસ કરો' : 'Find topics that need more practice and start targeted revision', style: const TextStyle(fontSize: 12, height: 1.3)),
                    ])),
                    const Icon(Icons.chevron_right_rounded),
                  ]),
                ),
              ),
            ),
            const SizedBox(height: 18),
            Container(key: _papersKey, child: Row(children: [
              Container(width: 40, height: 40, decoration: BoxDecoration(color: const Color(0xFFE6EEFF), borderRadius: BorderRadius.circular(13)), child: const Icon(Icons.description_rounded, color: Color(0xFF2563EB))),
              const SizedBox(width: 10),
              Expanded(child: Text(gu ? 'અગાઉના વર્ષોના પેપર' : 'Previous Year Papers', style: Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight: FontWeight.w900))),
              IconButton(onPressed: () {}, icon: const Icon(Icons.tune_rounded)),
            ])),
            const SizedBox(height: 8),
            TextField(
              decoration: InputDecoration(prefixIcon: const Icon(Icons.search_rounded), hintText: gu ? 'પેપર શોધો...' : 'Search papers...'),
              onChanged: (v) => setState(() => search = v),
            ),
            const SizedBox(height: 10),
            ...filtered.map((p) {
              final qs = forPaper(p.id);
              final ok = qs.length == p.questions && qs.every((q) => q['source_verified'] == true);
              final year = RegExp(r'\d{4}').firstMatch(p.title)?.group(0) ?? '';
              return Card(
                margin: const EdgeInsets.only(bottom: 8),
                child: InkWell(
                  borderRadius: BorderRadius.circular(16),
                  onTap: ok ? () async {
                    await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: p.title, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets)));
                    await _load();
                  } : () => _showNote(p, qs.length),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 10),
                    child: Row(children: [
                      Container(
                        width: 60,
                        height: 54,
                        decoration: BoxDecoration(
                          gradient: LinearGradient(colors: ok ? const [Color(0xFFE7EEFF), Color(0xFFDCE5FF)] : const [Color(0xFFF3F4F6), Color(0xFFE5E7EB)]),
                          borderRadius: BorderRadius.circular(15),
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(ok ? Icons.description_rounded : Icons.hourglass_bottom_rounded, size: 24, color: ok ? const Color(0xFF4338CA) : Colors.grey[600]),
                            const SizedBox(height: 2),
                            Text(year, style: TextStyle(fontSize: 9, fontWeight: FontWeight.w900, color: ok ? const Color(0xFF4338CA) : Colors.grey[600])),
                          ],
                        ),
                      ),
                      const SizedBox(width: 10),
                      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Text(p.title + ' — Paper-I', maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontWeight: FontWeight.w900, fontSize: 14)),
                        const SizedBox(height: 3),
                        Text(p.date + ' • ' + p.questions.toString() + (gu ? ' પ્રશ્નો' : ' Questions'), maxLines: 1, overflow: TextOverflow.ellipsis, style: Theme.of(context).textTheme.bodySmall),
                        const SizedBox(height: 4),
                        Row(children: [
                          Icon(ok ? Icons.verified_rounded : Icons.hourglass_bottom_rounded, size: 15, color: ok ? const Color(0xFF059669) : Colors.grey),
                          const SizedBox(width: 4),
                          Expanded(child: Text(ok ? (gu ? 'ચકાસાયેલ અને તૈયાર' : 'Verified & Ready') : qs.length.toString() + '/' + p.questions.toString() + ' loaded', maxLines: 1, overflow: TextOverflow.ellipsis, style: TextStyle(fontSize: 11, fontWeight: FontWeight.w800, color: ok ? const Color(0xFF047857) : Colors.grey[700]))),
                        ]),
                      ])),
                      const SizedBox(width: 6),
                      Container(
                        height: 40, padding: const EdgeInsets.symmetric(horizontal: 12),
                        decoration: BoxDecoration(gradient: ok ? const LinearGradient(colors: [Color(0xFF2563EB), Color(0xFF4F46E5)]) : null, color: ok ? null : const Color(0xFFE5E7EB), borderRadius: BorderRadius.circular(14)),
                        child: Row(children: [
                          Icon(ok ? Icons.play_arrow_rounded : Icons.lock_outline_rounded, size: 19, color: ok ? Colors.white : Colors.grey[600]),
                          if (ok) ...[const SizedBox(width: 3), Text(gu ? 'શરૂ કરો' : 'Start', style: TextStyle(color: Colors.white, fontWeight: FontWeight.w900))],
                        ]),
                      ),
                    ]),
                  ),
                ),
              );
            }),
          ],
        ),
      ),
      bottomNavigationBar: NavigationBar(
        height: 68,
        selectedIndex: selectedNav,
        onDestinationSelected: _nav,
        destinations: const [
          NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home_rounded), label: gu ? 'હોમ' : 'Home'),
          NavigationDestination(icon: Icon(Icons.description_outlined), selectedIcon: Icon(Icons.description_rounded), label: gu ? 'પેપર' : gu ? 'પેપર' : 'Papers'),
          NavigationDestination(icon: Icon(Icons.shuffle_rounded), selectedIcon: Icon(Icons.play_arrow_rounded), label: gu ? 'પ્રેક્ટિસ' : 'Practice'),
          NavigationDestination(icon: Icon(Icons.person_outline_rounded), selectedIcon: Icon(Icons.person_rounded), label: gu ? 'પ્રોફાઇલ' : 'Profile'),
        ],
      ),
    );
  }

  Widget _logo(double size) => Container(
    width: size, height: size,
    decoration: BoxDecoration(gradient: const LinearGradient(colors: [Color(0xFF4338CA), Color(0xFF7C3AED)]), borderRadius: BorderRadius.circular(15), boxShadow: [BoxShadow(color: const Color(0xFF4338CA).withValues(alpha: .25), blurRadius: 12, offset: const Offset(0, 5))]),
    child: Stack(alignment: Alignment.center, children: [
      Icon(Icons.school_rounded, color: Colors.white, size: size * .62),
      Positioned(bottom: 3, child: Container(padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1), decoration: BoxDecoration(color: const Color(0xFFFBBF24), borderRadius: BorderRadius.circular(5)), child: const Text('GSET', style: TextStyle(fontSize: 8, fontWeight: FontWeight.w900, color: Color(0xFF172554)))))
    ]),
  );

  Widget _hero() => Container(
    height: 205,
    decoration: BoxDecoration(
      gradient: const LinearGradient(begin: Alignment.topLeft, end: Alignment.bottomRight, colors: [Color(0xFF111B55), Color(0xFF4F46E5), Color(0xFF0F9F86)]),
      borderRadius: BorderRadius.circular(26),
      boxShadow: [BoxShadow(color: const Color(0xFF4338CA).withValues(alpha: .25), blurRadius: 24, offset: const Offset(0, 10))],
    ),
    child: Stack(children: [
      Positioned(right: -35, top: -45, child: _circle(160, Colors.white.withValues(alpha: .08))),
      Positioned(right: 65, bottom: -55, child: _circle(150, const Color(0xFF22D3EE).withValues(alpha: .12))),
      Positioned(right: 16, top: 18, child: Icon(Icons.auto_graph_rounded, size: 120, color: Colors.white.withValues(alpha: .10))),
      Positioned(right: 26, bottom: 23, child: Row(children: [
        Icon(Icons.menu_book_rounded, size: 52, color: Colors.white.withValues(alpha: .25)),
        const SizedBox(width: 5),
        const Icon(Icons.emoji_events_rounded, size: 72, color: Color(0xFFFBBF24)),
      ])),
      Padding(
        padding: const EdgeInsets.fromLTRB(20, 18, 18, 16),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(gu ? 'નાના પગલાં,' : 'Small Steps,', style: const TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.w900, height: 1)),
          Text(gu ? 'મોટી સફળતા! 🚀' : 'Big Success! 🚀', style: const TextStyle(color: Color(0xFFFFD34E), fontSize: 26, fontWeight: FontWeight.w900, height: 1)),
          const SizedBox(height: 9),
          Text(gu ? 'આજે માત્ર 10 પ્રશ્નો.\nGSET journey રોજ આગળ વધારો.' : 'Just 10 questions today.\nBuild your GSET journey one day at a time.', style: const TextStyle(color: Colors.white70, fontSize: 13, height: 1.35, fontWeight: FontWeight.w600)),
          const Spacer(),
          FilledButton.icon(
            style: FilledButton.styleFrom(backgroundColor: const Color(0xFF8B5CF6), foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12), shape: const StadiumBorder()),
            onPressed: _openPractice,
            icon: const Icon(Icons.play_arrow_rounded),
            label: Text(gu ? 'હમણાં પ્રેક્ટિસ કરો' : 'Practice Now', style: TextStyle(fontWeight: FontWeight.w900)),
          ),
        ]),
      ),
    ]),
  );

  Widget _circle(double size, Color color) => Container(width: size, height: size, decoration: BoxDecoration(color: color, shape: BoxShape.circle));

  Widget _metric(IconData icon, String value, String label, Color color) => Expanded(child: Column(children: [
    Container(width: 34, height: 34, decoration: BoxDecoration(color: color.withValues(alpha: .12), shape: BoxShape.circle), child: Icon(icon, color: color, size: 19)),
    const SizedBox(height: 5),
    Text(value, style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w900)),
    Text(label, maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 10, color: Colors.black54)),
  ]));

  Widget _dashCard(Color color, Color background, IconData icon, String title, Widget child) => Container(
    padding: const EdgeInsets.all(13),
    decoration: BoxDecoration(color: background, borderRadius: BorderRadius.circular(19), border: Border.all(color: color.withValues(alpha: .18))),
    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [Icon(icon, color: color, size: 21), const SizedBox(width: 6), Expanded(child: Text(title, maxLines: 1, overflow: TextOverflow.ellipsis, style: TextStyle(color: color, fontWeight: FontWeight.w900, fontSize: 13)))]),
      const SizedBox(height: 9),
      child,
    ]),
  );

  Widget _action(IconData icon, String title, String subtitle, Color color, VoidCallback? tap) {
    final active = tap != null;
    return Card(elevation: 1, child: InkWell(
      onTap: tap,
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.all(10),
        decoration: BoxDecoration(
          gradient: active ? LinearGradient(colors: [color, color.withValues(alpha: .78)]) : null,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Row(children: [
          Container(width: 36, height: 36, decoration: BoxDecoration(color: Colors.white.withValues(alpha: active ? .18 : .45), shape: BoxShape.circle), child: Icon(icon, color: active ? Colors.white : Colors.grey, size: 20)),
          const SizedBox(width: 7),
          Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
            Text(title, maxLines: 1, overflow: TextOverflow.ellipsis, style: TextStyle(fontWeight: FontWeight.w900, color: active ? Colors.white : Colors.grey[700], fontSize: 12)),
            Text(subtitle, maxLines: 1, overflow: TextOverflow.ellipsis, style: TextStyle(fontSize: 9.5, color: active ? Colors.white70 : Colors.grey)),
          ])),
          if (active) const Icon(Icons.chevron_right_rounded, color: Colors.white70, size: 19),
        ]),
      ),
    ));
  }

  Widget _section(String title, Widget child, [Widget? trailing]) => Card(
    elevation: 1,
    child: Padding(padding: const EdgeInsets.fromLTRB(12, 12, 12, 10), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [Expanded(child: Text(title, maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w900))), if (trailing != null) trailing]),
      const SizedBox(height: 10),
      child,
    ])),
  );

  Widget _badge(IconData icon, String label, bool active) => Expanded(child: Column(children: [
    Container(width: 46, height: 46, decoration: BoxDecoration(color: active ? const Color(0xFFE6F7F1) : const Color(0xFFF1F3F7), shape: BoxShape.circle), child: Icon(icon, color: active ? const Color(0xFF059669) : const Color(0xFFB8C0CC), size: 24)),
    const SizedBox(height: 5),
    Text(label, textAlign: TextAlign.center, style: TextStyle(fontSize: 9.5, height: 1.15, fontWeight: FontWeight.w700, color: active ? null : Colors.grey)),
  ]));

  void _showNote(PaperInfo p, int count) => showDialog(context: context, builder: (_) => AlertDialog(
    title: Text(p.title),
    content: Text('This paper currently has ' + count.toString() + '/' + p.questions.toString() + ' loaded questions.'),
    actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))],
  ));
}

class AccountPage extends StatefulWidget {
  final bool gu;
  const AccountPage({super.key, required this.gu});
  @override State<AccountPage> createState() => _AccountPageState();
}

class _AccountPageState extends State<AccountPage> {
  late bool gu;
  bool phoneMode = false;
  bool obscure = true;
  final email = TextEditingController();
  final phone = TextEditingController();
  final password = TextEditingController();

  @override void initState() { super.initState(); gu = widget.gu; }
  @override void dispose() { email.dispose(); phone.dispose(); password.dispose(); super.dispose(); }

  void _comingSoon(String title) => showDialog(context: context, builder: (_) => AlertDialog(
    title: Text(title),
    content: Text(gu ? 'આ સુવિધા Firebase configuration પછી live થશે. હાલ UI અને flow તૈયાર છે.' : 'This feature will go live after Firebase configuration. The UI and flow are ready.'),
    actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))],
  ));

  @override Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    return Scaffold(
      appBar: AppBar(title: Text(gu ? 'મારું Account' : 'My Account'), actions: [IconButton(onPressed: () => setState(() => gu = !gu), icon: const Icon(Icons.translate))]),
      body: ListView(padding: const EdgeInsets.fromLTRB(16, 12, 16, 28), children: [
        Container(
          padding: const EdgeInsets.all(22),
          decoration: BoxDecoration(
            gradient: LinearGradient(begin: Alignment.topLeft, end: Alignment.bottomRight, colors: [cs.primary, cs.primaryContainer]),
            borderRadius: BorderRadius.circular(24),
            boxShadow: [BoxShadow(color: cs.primary.withValues(alpha: .18), blurRadius: 18, offset: const Offset(0, 8))],
          ),
          child: Row(children: [
            CircleAvatar(radius: 30, backgroundColor: Colors.white, child: Icon(Icons.person_rounded, size: 34, color: cs.primary)),
            const SizedBox(width: 16),
            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Text('GSET Student Account', style: TextStyle(color: Colors.white, fontSize: 19, fontWeight: FontWeight.bold)),
              const SizedBox(height: 4),
              Text(gu ? 'Login કરીને તમારી progress અને purchases સાચવો' : 'Login to save your progress and purchases', style: const TextStyle(color: Colors.white70, height: 1.3)),
            ])),
          ]),
        ),
        const SizedBox(height: 18),
        SegmentedButton<bool>(
          expandedInsets: EdgeInsets.zero,
          segments: const [ButtonSegment(value: false, label: Text('Email')), ButtonSegment(value: true, label: Text('Phone OTP'))],
          selected: {phoneMode},
          onSelectionChanged: (s) => setState(() => phoneMode = s.first),
        ),
        const SizedBox(height: 16),
        if (!phoneMode) ...[
          TextField(controller: email, keyboardType: TextInputType.emailAddress, decoration: const InputDecoration(prefixIcon: Icon(Icons.email_outlined), labelText: 'Email')),
          const SizedBox(height: 12),
          TextField(controller: password, obscureText: obscure, decoration: InputDecoration(prefixIcon: const Icon(Icons.lock_outline), labelText: 'Password', suffixIcon: IconButton(onPressed: () => setState(() => obscure = !obscure), icon: Icon(obscure ? Icons.visibility_outlined : Icons.visibility_off_outlined)))),
          Align(alignment: Alignment.centerRight, child: TextButton(onPressed: () => _comingSoon('Password Reset'), child: Text(gu ? 'Password ભૂલી ગયા?' : 'Forgot password?'))),
          FilledButton.icon(onPressed: () => _comingSoon('Login'), icon: const Icon(Icons.login_rounded), label: Text(gu ? 'Login કરો' : 'Login')),
          const SizedBox(height: 8),
          OutlinedButton(onPressed: () => _comingSoon('Create Account'), child: Text(gu ? 'નવું Account બનાવો' : 'Create new account')),
        ] else ...[
          TextField(controller: phone, keyboardType: TextInputType.phone, decoration: const InputDecoration(prefixIcon: Icon(Icons.phone_outlined), labelText: 'Mobile Number', hintText: '+91 XXXXX XXXXX')),
          const SizedBox(height: 14),
          FilledButton.icon(onPressed: () => _comingSoon('OTP Login'), icon: const Icon(Icons.sms_outlined), label: Text(gu ? 'OTP મોકલો' : 'Send OTP')),
        ],
        const SizedBox(height: 22),
        Card(child: Column(children: [
          ListTile(leading: const CircleAvatar(child: Icon(Icons.forum_outlined)), title: Text(gu ? 'Feedback & Suggestion' : 'Feedback & Suggestion'), subtitle: Text(gu ? 'Feedback, suggestion અથવા question report કરો' : 'Send feedback, suggestions or report a question'), trailing: const Icon(Icons.chevron_right), onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => FeedbackPage(gu: gu)))),
          const Divider(height: 1),
          ListTile(leading: const CircleAvatar(child: Icon(Icons.shopping_bag_outlined)), title: Text(gu ? 'My Test Series' : 'My Test Series'), subtitle: Text(gu ? 'Purchased test series અહીં દેખાશે' : 'Purchased test series will appear here'), trailing: const Icon(Icons.chevron_right), onTap: () => _comingSoon('My Purchases')),
        ])),
        const SizedBox(height: 14),
        Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(color: cs.surfaceContainerHighest, borderRadius: BorderRadius.circular(16)), child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Icon(Icons.cloud_outlined, color: cs.primary), const SizedBox(width: 10),
          Expanded(child: Text(gu ? 'Secure cloud login અને purchase sync Firebase configuration પછી connect થશે.' : 'Secure cloud login and purchase sync will connect after Firebase configuration.', style: const TextStyle(height: 1.35))),
        ])),
      ]),
    );
  }
}

class FeedbackPage extends StatefulWidget {
  final bool gu;
  final String? paper;
  final String? questionId;
  const FeedbackPage({super.key, required this.gu, this.paper, this.questionId});
  @override State<FeedbackPage> createState() => _FeedbackPageState();
}

class _FeedbackPageState extends State<FeedbackPage> {
  late bool gu;
  String category = 'Suggestion';
  final message = TextEditingController();
  final email = TextEditingController();
  final questionId = TextEditingController();
  final paper = TextEditingController();

  @override void initState() {
    super.initState();
    gu = widget.gu;
    if (widget.paper != null) paper.text = widget.paper!;
    if (widget.questionId != null) questionId.text = widget.questionId!;
    if (widget.questionId != null) category = 'Report Question';
  }
  @override void dispose() { message.dispose(); email.dispose(); questionId.dispose(); paper.dispose(); super.dispose(); }

  Future<void> submit() async {
    if (message.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(gu ? 'કૃપા કરીને message લખો.' : 'Please enter your message.')));
      return;
    }
    final prefs = await SharedPreferences.getInstance();
    final item = jsonEncode({'category': category, 'message': message.text.trim(), 'email': email.text.trim(), 'paper': paper.text.trim(), 'questionId': questionId.text.trim(), 'time': DateTime.now().toIso8601String()});
    final old = prefs.getStringList('feedback_items') ?? [];
    old.add(item);
    await prefs.setStringList('feedback_items', old);
    if (!mounted) return;
    await showDialog(context: context, builder: (_) => AlertDialog(
      icon: const Icon(Icons.check_circle_outline, size: 42),
      title: Text(gu ? 'Feedback Saved' : 'Feedback Saved'),
      content: Text(gu ? 'Feedback આ device પર સાચવાયો છે. Firebase connect થયા પછી cloud submission થશે.' : 'Feedback is saved on this device. Cloud submission will be enabled after Firebase is connected.'),
      actions: [FilledButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))],
    ));
    if (mounted) Navigator.pop(context);
  }

  @override Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    const categories = ['Suggestion', 'General Feedback', 'Report Question', 'Support'];
    return Scaffold(
      appBar: AppBar(title: Text(gu ? 'Feedback & Support' : 'Feedback & Support'), actions: [IconButton(onPressed: () => setState(() => gu = !gu), icon: const Icon(Icons.translate))]),
      body: ListView(padding: const EdgeInsets.fromLTRB(16, 12, 16, 28), children: [
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topLeft, end: Alignment.bottomRight, colors: [cs.secondary, cs.secondaryContainer]), borderRadius: BorderRadius.circular(22)),
          child: Row(children: [
            const Icon(Icons.chat_bubble_outline_rounded, size: 40), const SizedBox(width: 14),
            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(gu ? 'તમારો અવાજ મહત્વનો છે!' : 'Your voice matters!', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
              const SizedBox(height: 4),
              Text(gu ? 'Suggestion આપો અથવા પ્રશ્નમાં ભૂલ report કરો.' : 'Share a suggestion or report a question issue.', style: const TextStyle(height: 1.3)),
            ])),
          ]),
        ),
        const SizedBox(height: 18),
        DropdownButtonFormField<String>(initialValue: category, decoration: const InputDecoration(labelText: 'Feedback Type', prefixIcon: Icon(Icons.category_outlined)), items: categories.map((x) => DropdownMenuItem(value: x, child: Text(x))).toList(), onChanged: (v) => setState(() => category = v!)),
        const SizedBox(height: 12),
        TextField(controller: email, keyboardType: TextInputType.emailAddress, decoration: InputDecoration(prefixIcon: const Icon(Icons.email_outlined), labelText: gu ? 'Email (Optional)' : 'Email (Optional)')),
        const SizedBox(height: 12),
        TextField(controller: paper, decoration: InputDecoration(prefixIcon: const Icon(Icons.description_outlined), labelText: gu ? 'Paper (Optional)' : 'Paper (Optional)')),
        const SizedBox(height: 12),
        TextField(controller: questionId, decoration: InputDecoration(prefixIcon: const Icon(Icons.tag_outlined), labelText: gu ? 'Question ID (Optional)' : 'Question ID (Optional)')),
        const SizedBox(height: 12),
        TextField(controller: message, maxLines: 6, decoration: InputDecoration(alignLabelWithHint: true, prefixIcon: const Padding(padding: EdgeInsets.only(bottom: 82), child: Icon(Icons.edit_note_outlined)), labelText: gu ? 'તમારો Message' : 'Your Message', hintText: gu ? 'તમારો feedback અહીં લખો...' : 'Write your feedback here...')),
        const SizedBox(height: 16),
        FilledButton.icon(onPressed: submit, icon: const Icon(Icons.send_rounded), label: Text(gu ? 'Feedback Submit કરો' : 'Submit Feedback')),
        const SizedBox(height: 12),
        Text(gu ? 'નોંધ: હાલ feedback local device પર સાચવાય છે; live cloud portal Firebase પછી ચાલુ થશે.' : 'Note: Feedback is currently saved locally; the live cloud portal will be enabled after Firebase setup.', textAlign: TextAlign.center, style: Theme.of(context).textTheme.bodySmall),
      ]),
    );
  }
}

class TestPage extends StatefulWidget {
  final List<Map<String, dynamic>> data; final bool gu; final String title; final bool practice;
  final Set<String> bookmarks, mistakes; final Future<void> Function(Set<String>, Set<String>) onStateChanged;
  const TestPage({super.key, required this.data, required this.gu, required this.title, this.practice = false, required this.bookmarks, required this.mistakes, required this.onStateChanged});
  @override State<TestPage> createState() => _TestPageState();
}

class _TestPageState extends State<TestPage> {
  int i = 0, score = 0, answered = 0; String? selected; bool submitted = false; bool gu = false; late DateTime started; Timer? timer;
  final Map<int, String> answers = {};
  bool finishing = false;
  late Set<String> b, m;
  Map<String, dynamic> get q => widget.data[i];
  int get maxSeconds => widget.practice ? 20 * 60 : widget.data.length * 72;

  @override void initState() { super.initState(); gu = widget.gu; started = DateTime.now(); b = {...widget.bookmarks}; m = {...widget.mistakes}; timer = Timer.periodic(const Duration(seconds: 1), (_) { if (mounted && DateTime.now().difference(started).inSeconds >= maxSeconds) _finish(); else if (mounted) setState(() {}); }); }
  @override void dispose() { timer?.cancel(); super.dispose(); }
  String get remaining { final left = max(0, maxSeconds - DateTime.now().difference(started).inSeconds); final mm = (left ~/ 60).toString().padLeft(2, '0'); final ss = (left % 60).toString().padLeft(2, '0'); return '$mm:$ss'; }

  void submit() {
    if (selected == null || submitted) return;
    answers[i] = selected!; answered++;
    final correct = q['answer'] as String;
    if (!{'Z', 'X'}.contains(correct)) {
      final isRight = selected == correct;
      if (isRight) {
        score++;
      } else {
        m.add(q['id'].toString());
      }
      final topic = (q['topic'] ?? 'General').toString();
      _recordTopicStat(topic, isRight);
    }
    setState(() => submitted = true); widget.onStateChanged(b, m);
  }

  Future<void> _recordTopicStat(String topic, bool correct) async {
    final prefs = await SharedPreferences.getInstance();
    final attempts = Map<String, dynamic>.from(jsonDecode(prefs.getString('gset_topic_attempts') ?? '{}'));
    final rights = Map<String, dynamic>.from(jsonDecode(prefs.getString('gset_topic_correct') ?? '{}'));
    attempts[topic] = (attempts[topic] ?? 0) + 1;
    rights[topic] = (rights[topic] ?? 0) + (correct ? 1 : 0);
    await prefs.setString('gset_topic_attempts', jsonEncode(attempts));
    await prefs.setString('gset_topic_correct', jsonEncode(rights));
  }

  void next() { if (i < widget.data.length - 1) setState(() { i++; selected = null; submitted = false; }); else _finish(); }
  Future<void> _finish() async {
    if (finishing) return;
    finishing = true;
    timer?.cancel();
    final evaluated = widget.data.where((e) => !{'Z', 'X'}.contains(e['answer'])).length;
    final prefs = await SharedPreferences.getInstance();
    final today = DateTime.now().toIso8601String().substring(0, 10);
    final previousDay = prefs.getString('gset_progress_day') ?? '';
    var done = prefs.getInt('gset_today_done') ?? 0;
    var currentStreak = prefs.getInt('gset_streak') ?? 0;
    if (previousDay != today) {
      done = 0;
      final previous = DateTime.tryParse(previousDay);
      final nowDate = DateTime.parse(today);
      if (previous != null && nowDate.difference(previous).inDays == 1) {
        currentStreak += 1;
      } else {
        currentStreak = 1;
      }
      await prefs.setString('gset_progress_day', today);
    }
    done = min(10, done + widget.data.length);
    final currentXp = (prefs.getInt('gset_xp') ?? 0) + (score * 10);
    final totalAttempted = (prefs.getInt('gset_total_attempted') ?? 0) + answered;
    final totalCorrect = (prefs.getInt('gset_total_correct') ?? 0) + score;
    await prefs.setInt('gset_today_done', done);
    await prefs.setInt('gset_streak', currentStreak);
    await prefs.setInt('gset_xp', currentXp);
    await prefs.setInt('gset_total_attempted', totalAttempted);
    await prefs.setInt('gset_total_correct', totalCorrect);
    if (!mounted) return;
    Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => ResultPage(title: widget.title, score: score, total: evaluated, attempted: answered, gu: gu, questions: widget.data, answers: answers, bookmarks: b, mistakes: m, onStateChanged: widget.onStateChanged, practice: widget.practice)));
  }

  Future<void> _confirmExit() async { final leave = await showDialog<bool>(context: context, builder: (_) => AlertDialog(title: Text(gu ? 'ટેસ્ટ છોડવી છે?' : 'Leave test?'), content: Text(gu ? 'હાલની ટેસ્ટની પ્રગતિ સાચવવામાં નહીં આવે. શું તમે બહાર નીકળવા માંગો છો?' : 'Current test progress will not be saved. Do you want to leave?'), actions: [TextButton(onPressed: () => Navigator.pop(context, false), child: Text(gu ? 'રહો' : 'Stay')), FilledButton(onPressed: () => Navigator.pop(context, true), child: Text(gu ? 'બહાર નીકળો' : 'Leave'))])); if (leave == true && mounted) Navigator.pop(context); }

  @override Widget build(BuildContext context) {
    final opts = List<String>.from(gu ? q['options_gu'] : q['options_en']); final correct = q['answer'] as String; final notEval = {'Z', 'X'}.contains(correct); final isCorrect = !notEval && selected == correct; final passage = ((gu ? q['passage_gu'] : q['passage_en']) ?? '').toString();
    return PopScope(canPop: false, onPopInvokedWithResult: (didPop, result) { if (!didPop) _confirmExit(); }, child: Scaffold(appBar: AppBar(title: Text('${widget.title} • ${i + 1}/${widget.data.length}'), actions: [IconButton(onPressed: () { setState(() { b.contains(q['id'].toString()) ? b.remove(q['id'].toString()) : b.add(q['id'].toString()); }); widget.onStateChanged(b, m); }, icon: Icon(b.contains(q['id'].toString()) ? Icons.bookmark : Icons.bookmark_border)), IconButton(tooltip: gu ? 'પ્રશ્ન Report કરો' : 'Report Question', onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => FeedbackPage(gu: gu, paper: widget.title, questionId: q['id']?.toString()))), icon: const Icon(Icons.flag_outlined)),
        IconButton(tooltip: gu ? 'English' : 'ગુજરાતી', onPressed: () => setState(() => gu = !gu), icon: const Icon(Icons.translate)), Padding(padding: const EdgeInsets.only(right: 12), child: Center(child: Text(remaining, style: const TextStyle(fontWeight: FontWeight.bold))))]),
      body: Column(children: [
        LinearProgressIndicator(value: (i + 1) / widget.data.length),
        Material(
          color: Theme.of(context).colorScheme.surface,
          child: SizedBox(
            height: 54,
            child: ListView.separated(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              scrollDirection: Axis.horizontal,
              itemCount: widget.data.length,
              separatorBuilder: (_, __) => const SizedBox(width: 6),
              itemBuilder: (_, n) {
                final attemptedHere = answers.containsKey(n);
                return ChoiceChip(
                  label: Text('${n + 1}'),
                  selected: i == n,
                  avatar: attemptedHere ? const Icon(Icons.check, size: 16) : null,
                  onSelected: (_) => setState(() {
                    i = n;
                    selected = answers[n];
                    submitted = answers.containsKey(n);
                  }),
                );
              },
            ),
          ),
        ),
        Expanded(child: ListView(padding: const EdgeInsets.all(16), children: [
          if (passage.isNotEmpty) Card(child: Padding(padding: const EdgeInsets.all(12), child: Text(passage, style: const TextStyle(height: 1.35)))),
          if ((q['image_asset'] ?? '').toString().isNotEmpty) Padding(padding: const EdgeInsets.only(bottom: 12), child: ClipRRect(borderRadius: BorderRadius.circular(10), child: Image.asset(q['image_asset'], fit: BoxFit.contain))),
          Row(children: [Chip(label: Text(q['topic']?.toString() ?? 'General')), const SizedBox(width: 8), Chip(label: Text(q['difficulty']?.toString() ?? ''))]),
          const SizedBox(height: 10), Card(child: Padding(padding: const EdgeInsets.all(16), child: Text(gu ? q['question_gu'] : q['question_en'], style: Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight: FontWeight.w600, height: 1.35)))),
          const SizedBox(height: 12),
          ...List.generate(opts.length, (j) { final letter = String.fromCharCode(65 + j); final right = letter == correct; final chosen = selected == letter; Color? fill; if (submitted && right) fill = Colors.green.withValues(alpha: .15); if (submitted && chosen && !right) fill = Colors.red.withValues(alpha: .15); return Card(color: fill, child: 
            // Flutter 3.38 deprecates RadioListTile.groupValue/onChanged in favor of RadioGroup.
            // Keep the current behavior intact until the RadioGroup migration is made in a dedicated UI refactor.
            // ignore: deprecated_member_use
            RadioListTile<String>(value: letter, groupValue: selected, onChanged: submitted ? null : (v) => setState(() => selected = v), title: Text('$letter. ${opts[j]}'))); }),
          const SizedBox(height: 8),
          if (!submitted) FilledButton.icon(onPressed: selected == null ? null : submit, icon: const Icon(Icons.check), label: Text(gu ? 'જવાબ Submit કરો' : 'Submit Answer')),
          if (submitted) Card(child: Padding(padding: const EdgeInsets.all(14), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(notEval ? (gu ? '⚠️ સત્તાવાર key મુજબ evaluationમાં ગણાતો નથી.' : '⚠️ Not evaluated according to the official key.') : (isCorrect ? (gu ? '✅ સાચો જવાબ' : '✅ Correct') : (gu ? '❌ ખોટો જવાબ' : '❌ Wrong')), style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            if (!notEval) ...[const SizedBox(height: 8), Text('${gu ? 'સાચો જવાબ' : 'Correct Answer'}: $correct'), const Divider(), Text(gu ? q['explanation_gu'] : q['explanation_en'])],
            if (q['review_flag'] == true) ...[const SizedBox(height: 10), Container(width: double.infinity, padding: const EdgeInsets.all(10), decoration: BoxDecoration(color: Colors.amber.withValues(alpha: .16), borderRadius: BorderRadius.circular(8)), child: Text('⚠️ ${gu ? 'સમીક્ષા નોંધ / Review Note' : 'Review Note'}: ${q['review_note']}'))],
            const SizedBox(height: 10), Text(gu ? '💡 Exam Tip: ${q['tip_gu']}' : '💡 Exam Tip: ${q['tip_en']}'),
          ]))),
          if (submitted) FilledButton(onPressed: next, child: Text(i == widget.data.length - 1 ? (gu ? 'પરિણામ જુઓ' : 'View Result') : (gu ? 'આગળ' : 'Next'))),
        ])),
      ])));
  }
}

class MistakeBookPage extends StatelessWidget {
  final bool gu;
  final List<Map<String, dynamic>> data;
  final Set<String> mistakes, bookmarks;
  final Future<void> Function(Set<String>, Set<String>) onStateChanged;
  const MistakeBookPage({super.key, required this.gu, required this.data, required this.mistakes, required this.bookmarks, required this.onStateChanged});

  @override
  Widget build(BuildContext context) {
    final qs = data.where((q) => mistakes.contains(q['id'].toString())).toList();
    return Scaffold(
      appBar: AppBar(title: const Text(gu ? 'ભૂલ બુક' : 'Mistake Book')),
      body: qs.isEmpty
          ? Center(child: Text(gu ? 'હાલ કોઈ mistake saved નથી.' : 'No mistakes saved yet.'))
          : ListView(padding: const EdgeInsets.all(14), children: [
              Card(child: Padding(padding: const EdgeInsets.all(18), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Row(children: [const Icon(Icons.menu_book_rounded, size: 28, color: Color(0xFFEA580C)), const SizedBox(width: 10), Expanded(child: Text('${qs.length} questions to revise', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900)))]),
                const SizedBox(height: 8),
                Text(gu ? 'Wrong answer ને learning opportunity બનાવો: explanation વાંચો અને ફરી solve કરો.' : 'Turn wrong answers into learning: read the explanation, then solve them again.', style: const TextStyle(height: 1.35)),
                const SizedBox(height: 14),
                FilledButton.icon(
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: 'Mistake Revision', practice: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: onStateChanged))),
                  icon: const Icon(Icons.replay_rounded),
                  label: const Text('Mistake Revision Test'),
                ),
              ]))),
              const SizedBox(height: 10),
              ...qs.map((q) => Card(
                margin: const EdgeInsets.only(bottom: 8),
                child: ExpansionTile(
                  leading: const CircleAvatar(child: Icon(Icons.error_outline_rounded)),
                  title: Text(gu ? q['question_gu'] : q['question_en'], maxLines: 2, overflow: TextOverflow.ellipsis),
                  subtitle: Text((q['topic'] ?? 'General').toString()),
                  childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                  children: [
                    Text(gu ? q['explanation_gu'] : q['explanation_en'], style: const TextStyle(height: 1.35)),
                    const SizedBox(height: 8),
                    Text(gu ? '💡 ${q['tip_gu']}' : '💡 ${q['tip_en']}', style: const TextStyle(fontWeight: FontWeight.w700)),
                  ],
                ),
              )),
            ]),
    );
  }
}

class WeakAreasPage extends StatefulWidget {
  final bool gu;
  final List<Map<String, dynamic>> data;
  final Set<String> mistakes, bookmarks;
  final Future<void> Function(Set<String>, Set<String>) onStateChanged;
  const WeakAreasPage({super.key, required this.gu, required this.data, required this.mistakes, required this.bookmarks, required this.onStateChanged});
  @override State<WeakAreasPage> createState() => _WeakAreasPageState();
}

class _WeakAreasPageState extends State<WeakAreasPage> {
  Map<String, int> attempts = {};
  Map<String, int> correct = {};

  @override
  void initState() { super.initState(); _load(); }

  Future<void> _load() async {
    final p = await SharedPreferences.getInstance();
    final a = Map<String, dynamic>.from(jsonDecode(p.getString('gset_topic_attempts') ?? '{}'));
    final r = Map<String, dynamic>.from(jsonDecode(p.getString('gset_topic_correct') ?? '{}'));
    if (!mounted) return;
    setState(() {
      attempts = a.map((k, v) => MapEntry(k, (v as num).toInt()));
      correct = r.map((k, v) => MapEntry(k, (v as num).toInt()));
    });
  }

  @override
  Widget build(BuildContext context) {
    final topics = {...attempts.keys, ...correct.keys}.toList();
    topics.sort((a, b) {
      final aa = attempts[a] ?? 0, ab = attempts[b] ?? 0;
      final pa = aa == 0 ? 0 : (correct[a] ?? 0) / aa;
      final pb = ab == 0 ? 0 : (correct[b] ?? 0) / ab;
      return pa.compareTo(pb);
    });
    return Scaffold(
      appBar: AppBar(title: const Text(gu ? 'મારા નબળા વિષયો' : 'My Weak Areas')),
      body: topics.isEmpty
          ? Center(child: Text(widget.gu ? 'થોડા પ્રશ્નો solve કરો; પછી topic analysis અહીં દેખાશે.' : 'Solve a few questions and your topic analysis will appear here.'))
          : ListView(padding: const EdgeInsets.all(14), children: [
              Card(child: Padding(padding: const EdgeInsets.all(18), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                const Text('🎯 Targeted Practice', style: TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
                const SizedBox(height: 6),
                Text(widget.gu ? 'ઓછા accuracy વાળા topics પર focus કરો.' : 'Focus your revision on topics with lower accuracy.', style: const TextStyle(height: 1.35)),
              ]))),
              const SizedBox(height: 10),
              ...topics.map((topic) {
                final a = attempts[topic] ?? 0;
                final r = correct[topic] ?? 0;
                final pct = a == 0 ? 0 : (r * 100 / a).round();
                final topicQs = widget.data.where((q) => (q['topic'] ?? 'General').toString() == topic).toList();
                final revisionQs = topicQs.where((q) => widget.mistakes.contains(q['id'].toString())).toList();
                final practiceQs = revisionQs.isNotEmpty ? revisionQs : topicQs;
                return Card(
                  margin: const EdgeInsets.only(bottom: 9),
                  child: Padding(padding: const EdgeInsets.all(14), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [
                      Expanded(child: Text(topic, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w900))),
                      Container(padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 5), decoration: BoxDecoration(color: pct < 60 ? const Color(0xFFFFE8DD) : const Color(0xFFE7F8F1), borderRadius: BorderRadius.circular(10)), child: Text('$pct%', style: const TextStyle(fontWeight: FontWeight.w900))),
                    ]),
                    const SizedBox(height: 6),
                    Text('$r / $a correct • Mistakes: ${revisionQs.length}', style: const TextStyle(fontSize: 12)),
                    const SizedBox(height: 7),
                    LinearProgressIndicator(value: pct / 100, minHeight: 7),
                    const SizedBox(height: 10),
                    Align(alignment: Alignment.centerRight, child: FilledButton.icon(
                      onPressed: practiceQs.isEmpty ? null : () => Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: [...practiceQs]..shuffle(), gu: widget.gu, title: 'Targeted Practice • $topic', practice: true, bookmarks: widget.bookmarks, mistakes: widget.mistakes, onStateChanged: widget.onStateChanged))),
                      icon: const Icon(Icons.bolt_rounded, size: 18),
                      label: const Text(gu ? 'પ્રેક્ટિસ' : 'Practice'),
                    )),
                  ])),
                );
              }),
            ]),
    );
  }
}

class ResultPage extends StatelessWidget {
  final String title; final int score, total, attempted; final bool gu, practice;
  final List<Map<String, dynamic>> questions; final Map<int, String> answers;
  final Set<String> bookmarks, mistakes;
  final Future<void> Function(Set<String>, Set<String>) onStateChanged;
  const ResultPage({super.key, required this.title, required this.score, required this.total, required this.attempted, required this.gu, required this.questions, required this.answers, required this.bookmarks, required this.mistakes, required this.onStateChanged, required this.practice});
  @override Widget build(BuildContext context) {
    final pct = total == 0 ? 0.0 : score * 100.0 / total;
    return Scaffold(appBar: AppBar(title: Text(gu ? 'પરિણામ' : 'Result')), body: ListView(padding: const EdgeInsets.all(20), children: [
      Card(child: Padding(padding: const EdgeInsets.all(22), child: Column(children: [const Icon(Icons.emoji_events_outlined, size: 64), const SizedBox(height: 12), Text(title, style: Theme.of(context).textTheme.titleLarge, textAlign: TextAlign.center), const SizedBox(height: 10), Text('$score / $total', style: Theme.of(context).textTheme.displaySmall?.copyWith(fontWeight: FontWeight.bold)), Text('${pct.toStringAsFixed(1)}%', style: Theme.of(context).textTheme.headlineSmall), const SizedBox(height: 8), Text(gu ? 'પ્રયાસ કરેલા પ્રશ્નો: $attempted / ${questions.length}' : 'Attempted: $attempted / ${questions.length}')]))),
      const SizedBox(height: 14),
      Row(children: [Expanded(child: FilledButton.icon(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => ReviewPage(title: title, questions: questions, answers: answers, gu: gu))), icon: const Icon(Icons.fact_check_outlined), label: Text(gu ? 'Review' : 'Review'))), const SizedBox(width: 10), Expanded(child: OutlinedButton.icon(onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => TestPage(data: questions, gu: gu, title: title, practice: practice, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: onStateChanged))), icon: const Icon(Icons.refresh), label: Text(gu ? 'ફરી ટેસ્ટ' : 'Retry')))]),
      const SizedBox(height: 10), OutlinedButton.icon(onPressed: () => Navigator.pop(context), icon: const Icon(Icons.home_outlined), label: Text(gu ? 'હોમ' : gu ? 'હોમ' : 'Home')),
    ]));
  }
}

class ReviewPage extends StatelessWidget {
  final String title; final List<Map<String, dynamic>> questions; final Map<int, String> answers; final bool gu;
  const ReviewPage({super.key, required this.title, required this.questions, required this.answers, required this.gu});
  @override Widget build(BuildContext context) => Scaffold(appBar: AppBar(title: Text(gu ? 'જવાબોની સમીક્ષા' : 'Answer Review')), body: ListView.builder(padding: const EdgeInsets.all(14), itemCount: questions.length, itemBuilder: (_, i) {
    final q = questions[i]; final correct = q['answer'] as String; final selected = answers[i]; final notEval = {'Z', 'X'}.contains(correct); final ok = !notEval && selected == correct;
    return Card(margin: const EdgeInsets.only(bottom: 10), child: ExpansionTile(leading: CircleAvatar(child: Text('${i + 1}')), title: Text(gu ? q['question_gu'] : q['question_en']), subtitle: Text(selected == null ? (gu ? 'અનઉત્તરિત' : 'Unanswered') : '${gu ? 'તમારો જવાબ' : 'Your answer'}: $selected • ${notEval ? 'Not evaluated' : (ok ? 'Correct' : 'Wrong')}'), childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16), children: [Text('Correct Answer: ${notEval ? '—' : correct}'), const SizedBox(height: 8), if (!notEval) Text(gu ? q['explanation_gu'] : q['explanation_en'])]));
  }));
}