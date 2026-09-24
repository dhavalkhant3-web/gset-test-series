import 'dart:async';
import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart' show kDebugMode;
import 'package:flutter/services.dart' show rootBundle;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_analytics/firebase_analytics.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await AppAnalytics.appOpened();
  runApp(const GsetApp());
}

class GsetApp extends StatelessWidget {
  const GsetApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'GSET Paper-I Test Series',
        theme: ThemeData(colorSchemeSeed: const Color(0xFF5B5FEF), useMaterial3: true, scaffoldBackgroundColor: const Color(0xFFF5F7FF), cardTheme: const CardThemeData(margin: EdgeInsets.zero, elevation: 2, clipBehavior: Clip.antiAlias), appBarTheme: const AppBarTheme(centerTitle: false, elevation: 0, backgroundColor: Color(0xFFF5F7FF)), inputDecorationTheme: const InputDecorationTheme(filled: true, fillColor: Colors.white, border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(16)), borderSide: BorderSide.none), enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(16)), borderSide: BorderSide.none), focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(16)), borderSide: BorderSide(color: Color(0xFF5B5FEF), width: 1.4)))),
        navigatorObservers: [FirebaseAnalyticsObserver(analytics: FirebaseAnalytics.instance)],
        home: const HomePage(),
      );
}

class FirebaseSync {
  static User? get user => FirebaseAuth.instance.currentUser;

  static Future<void> pullAndMerge(SharedPreferences prefs) async {
    final u = user;
    if (u == null) return;
    try {
      final ref = FirebaseFirestore.instance.collection('users').doc(u.uid).collection('app').doc('state');
      final snap = await ref.get();
      if (!snap.exists) {
        await pushLocal(prefs);
        return;
      }
      final cloud = snap.data() ?? {};
      final bookmarks = {...(prefs.getStringList('bookmarks') ?? []), ..._strings(cloud['bookmarks'])};
      final mistakes = {...(prefs.getStringList('mistakes') ?? []), ..._strings(cloud['mistakes'])};
      await prefs.setStringList('bookmarks', bookmarks.toList());
      await prefs.setStringList('mistakes', mistakes.toList());

      for (final key in ['gset_today_done', 'gset_xp', 'gset_streak', 'gset_total_attempted', 'gset_total_correct']) {
        final local = prefs.getInt(key) ?? 0;
        final remote = (cloud[key] as num?)?.toInt() ?? 0;
        await prefs.setInt(key, max(local, remote));
      }

      final localAttempts = _jsonMap(prefs.getString('gset_topic_attempts'));
      final localCorrect = _jsonMap(prefs.getString('gset_topic_correct'));
      final mergedAttempts = _mergeMax(localAttempts, _numMap(cloud['topicAttempts']));
      final mergedCorrect = _mergeMax(localCorrect, _numMap(cloud['topicCorrect']));
      await prefs.setString('gset_topic_attempts', jsonEncode(mergedAttempts));
      await prefs.setString('gset_topic_correct', jsonEncode(mergedCorrect));
      await pushLocal(prefs);
    } catch (_) {}
  }

  static Future<void> pushLocal(SharedPreferences prefs) async {
    final u = user;
    if (u == null) return;
    try {
      final ref = FirebaseFirestore.instance.collection('users').doc(u.uid).collection('app').doc('state');
      await ref.set({
        'bookmarks': prefs.getStringList('bookmarks') ?? <String>[],
        'mistakes': prefs.getStringList('mistakes') ?? <String>[],
        'gset_today_done': prefs.getInt('gset_today_done') ?? 0,
        'gset_xp': prefs.getInt('gset_xp') ?? 0,
        'gset_streak': prefs.getInt('gset_streak') ?? 0,
        'gset_total_attempted': prefs.getInt('gset_total_attempted') ?? 0,
        'gset_total_correct': prefs.getInt('gset_total_correct') ?? 0,
        'topicAttempts': _jsonMap(prefs.getString('gset_topic_attempts')),
        'topicCorrect': _jsonMap(prefs.getString('gset_topic_correct')),
        'updatedAt': FieldValue.serverTimestamp(),
      }, SetOptions(merge: true));
    } catch (_) {}
  }

  static Future<void> addFeedback(Map<String, dynamic> item) async {
    final u = user;
    if (u == null) return;
    try {
      await FirebaseFirestore.instance.collection('users').doc(u.uid).collection('feedback').add({
        ...item,
        'createdAt': FieldValue.serverTimestamp(),
      });
    } catch (_) {}
  }

  static Set<String> _strings(dynamic value) =>
      value is List ? value.map((e) => e.toString()).toSet() : <String>{};

  static Map<String, dynamic> _jsonMap(String? raw) {
    if (raw == null || raw.isEmpty) return {};
    try {
      final value = jsonDecode(raw);
      return value is Map ? Map<String, dynamic>.from(value) : {};
    } catch (_) {
      return {};
    }
  }

  static Map<String, dynamic> _numMap(dynamic value) =>
      value is Map ? Map<String, dynamic>.from(value) : {};

  static Map<String, dynamic> _mergeMax(Map<String, dynamic> a, Map<String, dynamic> b) {
    final result = <String, dynamic>{...a};
    for (final entry in b.entries) {
      final av = (result[entry.key] as num?)?.toInt() ?? 0;
      final bv = (entry.value as num?)?.toInt() ?? 0;
      result[entry.key] = max(av, bv);
    }
    return result;
  }
}

class AppAnalytics {
  static final FirebaseAnalytics instance = FirebaseAnalytics.instance;

  static Future<void> appOpened() async {
    try { await instance.logAppOpen(); } catch (_) {}
  }

  static Future<void> event(String name, {Map<String, Object>? parameters}) async {
    try { await instance.logEvent(name: name, parameters: parameters); } catch (_) {}
  }

  static Future<void> login(String method) async {
    try {
      await instance.logLogin(loginMethod: method);
      final uid = FirebaseAuth.instance.currentUser?.uid;
      if (uid != null) await instance.setUserId(id: uid);
    } catch (_) {}
  }
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
    await FirebaseSync.pullAndMerge(prefs);
    if (mounted) {
      final refreshed = await SharedPreferences.getInstance();
      setState(() {
        bookmarks = (refreshed.getStringList('bookmarks') ?? []).toSet();
        mistakes = (refreshed.getStringList('mistakes') ?? []).toSet();
        todayDone = refreshed.getInt('gset_today_done') ?? 0;
        xp = refreshed.getInt('gset_xp') ?? 0;
        streak = refreshed.getInt('gset_streak') ?? 0;
        totalAttempted = refreshed.getInt('gset_total_attempted') ?? 0;
        totalCorrect = refreshed.getInt('gset_total_correct') ?? 0;
      });
    }
  }

  List<Map<String, dynamic>> forPaper(String id) => data.where((q) => q['paperId'] == id).toList();
  List<PaperInfo> get filtered => papers.where((p) => p.title.toLowerCase().contains(search.toLowerCase())).toList();

  Future<void> _openPractice() async {
    if (data.isEmpty) return;
    final qs = [...data]..shuffle(Random());
    final selected = qs.take(min(10, qs.length)).toList();
    await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(
      data: selected, gu: gu, title: 'Daily Practice', practice: true,
      bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets,    )));
    await _load();
  }

  Future<void> _saveSets(Set<String> b, Set<String> m) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList('bookmarks', b.toList());
    await prefs.setStringList('mistakes', m.toList());
    if (mounted) setState(() { bookmarks = b; mistakes = m; });
    await FirebaseSync.pushLocal(prefs);
    await AppAnalytics.event('state_sync', parameters: {
      'bookmark_count': b.length,
      'mistake_count': m.length,
    });
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
              onSelectionChanged: (s) { setState(() => gu = s.first); AppAnalytics.event('language_change', parameters: {'language': s.first ? 'gujarati' : 'english'}); },
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
                ClipRRect(borderRadius: BorderRadius.circular(8), child: LinearProgressIndicator(value: levelProgress, minHeight: 8, backgroundColor: const Color(0xFFDCCAF9), color: const Color(0xFF7C3AED))),                const SizedBox(height: 6),
                Text((xp % 500).toString() + ' / 500 XP • ' + (500 - (xp % 500)).toString() + (gu ? ' XP બાકી — લેવલ ' : ' XP to Level ') + (level + 1).toString(), maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w700)),
              ]));
              if (c.maxWidth >= 600) return Row(children: [Expanded(child: target), const SizedBox(width: 9), Expanded(child: fire), const SizedBox(width: 9), Expanded(child: stars)]);
              return Column(children: [Row(children: [Expanded(child: target), const SizedBox(width: 9), Expanded(child: fire)]), const SizedBox(height: 9), stars]);
            }),
            const SizedBox(height: 12),
            LayoutBuilder(builder: (_, c) {
              final actions = [
                _action(Icons.shuffle_rounded, gu ? 'રેન્ડમ પ્રેક્ટિસ' : 'Random Practice', gu ? 'મિશ્ર પ્રશ્નો' : 'Mixed Questions', const Color(0xFF2563EB), _openPractice),
                _action(Icons.timer_rounded, gu ? 'મોક ટેસ્ટ' : 'Mock Test', gu ? '50 પ્રશ્નો • 60 મિનિટ' : '50 Questions • 60 Minutes', const Color(0xFF7C3AED), () async {
                  final qs = [...data]..shuffle(Random());
                  await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs.take(min(50, qs.length)).toList(), gu: gu, title: gu ? 'GSET મોક ટેસ્ટ' : 'GSET Mock Test', mock: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets)));
                  await _load();
                }),
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
              ]), Text(gu ? 'ચાલુ રાખો →' : 'Keep going →', style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w800)));
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
                onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => AnalyticsPage(gu: gu, data: data))),
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Row(children: [
                    Container(width: 46, height: 46, decoration: BoxDecoration(color: const Color(0xFFEDE9FE), borderRadius: BorderRadius.circular(14)), child: const Icon(Icons.analytics_rounded, color: Color(0xFF6D28D9))),
                    const SizedBox(width: 12),
                    Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(gu ? 'Performance Analytics' : 'Performance Analytics', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w900)),
                      const SizedBox(height: 3),
                      Text(gu ? 'તમારી accuracy અને topic-wise performance જુઓ' : 'View your accuracy and topic-wise performance', style: const TextStyle(fontSize: 12, height: 1.3)),
                    ])),
                    const Icon(Icons.chevron_right_rounded),
                  ]),
                ),
              ),
            ),
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
                          borderRadius: BorderRadius.circular(15),                        ),
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
        destinations: [
          NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home_rounded), label: gu ? 'હોમ' : 'Home'),
          NavigationDestination(icon: Icon(Icons.description_outlined), selectedIcon: Icon(Icons.description_rounded), label: gu ? 'પેપર' : 'Papers'),
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

  Widget _metric(IconData icon, String value, String label, Color color) => Expanded(child: Column(children: [    Container(width: 34, height: 34, decoration: BoxDecoration(color: color.withValues(alpha: .12), shape: BoxShape.circle), child: Icon(icon, color: color, size: 19)),
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
  bool phoneMode = false, obscure = true, busy = false;
  final email = TextEditingController();
  final phone = TextEditingController();
  final password = TextEditingController();
  final otp = TextEditingController();
  String? verificationId;

  @override
  void initState() {
    super.initState();
    gu = widget.gu;
  }

  @override
  void dispose() {
    email.dispose();
    phone.dispose();
    password.dispose();
    otp.dispose();
    super.dispose();
  }

  String _error(Object e) {
    if (e is FirebaseAuthException) {
      switch (e.code) {
        case 'invalid-email': return gu ? 'Email address ખોટું છે.' : 'Invalid email address.';
        case 'user-not-found': return gu ? 'આ email માટે account મળ્યું નથી.' : 'No account found for this email.';
        case 'wrong-password':
        case 'invalid-credential': return gu ? 'Email અથવા password ખોટો છે.' : 'Incorrect email or password.';
        case 'email-already-in-use': return gu ? 'આ email પહેલેથી registered છે. Login કરો.' : 'This email is already registered. Please login.';
        case 'weak-password': return gu ? 'Password ઓછામાં ઓછો 6 characters રાખો.' : 'Password must be at least 6 characters.';
        case 'too-many-requests': return gu ? 'ઘણા પ્રયાસ થયા. થોડા સમય પછી ફરી પ્રયાસ કરો.' : 'Too many attempts. Please try again later.';
        case 'operation-not-allowed': return gu ? 'Firebase Auth error: operation-not-allowed\\nCode: ${e.code}\\nMessage: ${e.message ?? '-'}' : 'Firebase Auth error: operation-not-allowed\\nCode: ${e.code}\\nMessage: ${e.message ?? '-'}';
        case 'network-request-failed': return gu ? 'Internet connection તપાસો.' : 'Please check your internet connection.';
        case 'configuration-not-found': return gu ? 'Firebase Phone Authentication configuration અધૂરી છે.' : 'Firebase Phone Authentication is not fully configured.';
        case 'invalid-verification-code': return gu ? 'OTP ખોટો છે.' : 'Invalid OTP.';
        case 'invalid-verification-id': return gu ? 'OTP session expire થઈ છે. ફરી OTP મોકલો.' : 'OTP session expired. Send a new OTP.';
        case 'quota-exceeded': return gu ? 'OTP quota પૂર્ણ થઈ છે. પછીથી પ્રયાસ કરો.' : 'OTP quota exceeded. Try again later.';
        default:
          final message = e.message ?? '';
          if (message.contains('FirebaseAuthHostApi.')) {
            return gu
                ? 'Firebase Auth connection error. નવી APK install કરીને ફરી પ્રયાસ કરો.'
                : 'Firebase Auth connection error. Install the latest APK and try again.';
          }
          return message.isNotEmpty ? message : (gu ? 'Firebase error આવ્યો.' : 'A Firebase error occurred.');
      }
    }
    return gu ? 'કંઈક error આવ્યું. ફરી પ્રયાસ કરો.' : 'Something went wrong. Please try again.';
  }

  Future<void> _run(Future<void> Function() action) async {
    if (busy) return;
    setState(() => busy = true);
    try {
      await action();
      if (mounted) ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(gu ? 'સફળતાપૂર્વક થયું ✅' : 'Done successfully ✅')));
    } catch (e) {
      if (mounted) ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(_error(e))));
    } finally {
      if (mounted) setState(() => busy = false);
    }
  }

  Future<void> _login() => _run(() async {
    await FirebaseAuth.instance.signInWithEmailAndPassword(email: email.text.trim(), password: password.text);
    final prefs = await SharedPreferences.getInstance();
    await FirebaseSync.pullAndMerge(prefs);
    await AppAnalytics.login('email');
  });

  Future<void> _register() => _run(() async {
    await FirebaseAuth.instance.createUserWithEmailAndPassword(email: email.text.trim(), password: password.text);
    final prefs = await SharedPreferences.getInstance();
    await FirebaseSync.pushLocal(prefs);
    await AppAnalytics.login('email_signup');
  });

  Future<void> _resetPassword() => _run(() async {
    await FirebaseAuth.instance.sendPasswordResetEmail(email: email.text.trim());
  });

  Future<void> _sendOtp() async {
    final value = phone.text.trim();
    if (value.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(gu ? 'Mobile number લખો.' : 'Enter mobile number.')));
      return;
    }
    if (!value.startsWith('+') || value.length < 10) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(gu ? '+91 સાથે valid mobile number લખો.' : 'Enter a valid mobile number with country code, e.g. +91XXXXXXXXXX.')));
      return;
    }
    await _run(() async {
      // Development-only Firebase Phone Auth test mode. This is intentionally
      // enabled only in debug builds so production keeps Play Integrity/reCAPTCHA.
      if (kDebugMode) {
        await FirebaseAuth.instance.setSettings(
          appVerificationDisabledForTesting: true,
        );
      }
      final completer = Completer<void>();
      await FirebaseAuth.instance.verifyPhoneNumber(
        phoneNumber: value,
        verificationCompleted: (credential) async {
          try {
            await FirebaseAuth.instance.signInWithCredential(credential);
            final prefs = await SharedPreferences.getInstance();
            await FirebaseSync.pullAndMerge(prefs);
            await AppAnalytics.login('phone');
            if (!completer.isCompleted) completer.complete();
            if (mounted) setState(() {});
          } catch (e) {
            if (!completer.isCompleted) completer.completeError(e);
          }
        },
        verificationFailed: (e) {
          if (!completer.isCompleted) completer.completeError(e);
        },
        codeSent: (id, _) {
          verificationId = id;
          if (mounted) {
            setState(() {});
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(gu ? 'OTP મોકલાયો છે. 📲' : 'OTP sent. 📲')));
          }
          if (!completer.isCompleted) completer.complete();
        },
        codeAutoRetrievalTimeout: (id) => verificationId = id,
      );
      await completer.future;
    });
  }

  Future<void> _verifyOtp() => _run(() async {
    final id = verificationId;
    if (id == null) throw FirebaseAuthException(code: 'invalid-verification-id');
    final credential = PhoneAuthProvider.credential(verificationId: id, smsCode: otp.text.trim());
    await FirebaseAuth.instance.signInWithCredential(credential);
    final prefs = await SharedPreferences.getInstance();
    await FirebaseSync.pullAndMerge(prefs);
    if (mounted) setState(() => verificationId = null);
  });

  Future<void> _logout() async {
    await FirebaseAuth.instance.signOut();
    try { await FirebaseAnalytics.instance.setUserId(id: null); } catch (_) {}
    if (mounted) setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final user = FirebaseAuth.instance.currentUser;
    return Scaffold(
      appBar: AppBar(
        title: Text(gu ? 'મારું Account' : 'My Account'),
        actions: [IconButton(onPressed: () => setState(() => gu = !gu), icon: const Icon(Icons.translate))],
      ),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(16, 12, 16, 28),
        children: [
          Container(
            padding: const EdgeInsets.all(22),
            decoration: BoxDecoration(
              gradient: LinearGradient(begin: Alignment.topLeft, end: Alignment.bottomRight, colors: [cs.primary, cs.primaryContainer]),
              borderRadius: BorderRadius.circular(24),
            ),
            child: Row(children: [
              CircleAvatar(radius: 30, backgroundColor: Colors.white, child: Icon(Icons.person_rounded, size: 34, color: cs.primary)),
              const SizedBox(width: 16),
              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                const Text('GSET Student Account', style: TextStyle(color: Colors.white, fontSize: 19, fontWeight: FontWeight.bold)),
                const SizedBox(height: 4),
                Text(user == null
                    ? (gu ? 'Login કરીને progress cloud માં સાચવો' : 'Login to save your progress to cloud')
                    : (user.email ?? user.phoneNumber ?? 'Signed in'),
                    style: const TextStyle(color: Colors.white70, height: 1.3)),
              ])),
            ]),
          ),
          const SizedBox(height: 18),
          if (user != null)
            Card(child: ListTile(
              leading: const CircleAvatar(child: Icon(Icons.cloud_done_outlined)),
              title: Text(gu ? 'Cloud Sync ચાલુ છે' : 'Cloud Sync is active'),
              subtitle: Text(gu ? 'તમારી progress Firebase માં sync થાય છે.' : 'Your progress is synced with Firebase.'),
              trailing: FilledButton(onPressed: busy ? null : _logout, child: Text(gu ? 'Logout' : 'Logout')),
            ))
          else ...[
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
              Align(alignment: Alignment.centerRight, child: TextButton(onPressed: busy ? null : _resetPassword, child: Text(gu ? 'Password ભૂલી ગયા?' : 'Forgot password?'))),
              FilledButton.icon(onPressed: busy ? null : _login, icon: const Icon(Icons.login_rounded), label: Text(gu ? 'Login કરો' : 'Login')),
              const SizedBox(height: 8),
              OutlinedButton.icon(onPressed: busy ? null : _register, icon: const Icon(Icons.person_add_alt_1), label: Text(gu ? 'નવું Account બનાવો' : 'Create new account')),
            ] else ...[
              TextField(controller: phone, keyboardType: TextInputType.phone, decoration: const InputDecoration(prefixIcon: Icon(Icons.phone_outlined), labelText: 'Mobile Number', hintText: '+91 XXXXX XXXXX')),
              const SizedBox(height: 14),
              if (verificationId == null)
                FilledButton.icon(onPressed: busy ? null : _sendOtp, icon: const Icon(Icons.sms_outlined), label: Text(gu ? 'OTP મોકલો' : 'Send OTP'))
              else ...[
                TextField(controller: otp, keyboardType: TextInputType.number, decoration: const InputDecoration(prefixIcon: Icon(Icons.pin_outlined), labelText: 'OTP')),
                const SizedBox(height: 12),
                FilledButton.icon(onPressed: busy ? null : _verifyOtp, icon: const Icon(Icons.verified_outlined), label: Text(gu ? 'OTP Verify કરો' : 'Verify OTP')),
              ],
            ],
          ],
          const SizedBox(height: 22),
          Card(child: Column(children: [
            ListTile(leading: const CircleAvatar(child: Icon(Icons.forum_outlined)), title: Text(gu ? 'Feedback & Suggestion' : 'Feedback & Suggestion'), subtitle: Text(gu ? 'Feedback, suggestion અથવા question report કરો' : 'Send feedback, suggestions or report a question'), trailing: const Icon(Icons.chevron_right), onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => FeedbackPage(gu: gu)))),
            const Divider(height: 1),
            ListTile(leading: const CircleAvatar(child: Icon(Icons.shopping_bag_outlined)), title: Text(gu ? 'My Test Series' : 'My Test Series'), subtitle: Text(gu ? 'Purchased test series અહીં દેખાશે' : 'Purchased test series will appear here'), trailing: const Icon(Icons.chevron_right), onTap: () => showDialog(context: context, builder: (_) => AlertDialog(title: const Text('Coming Soon'), content: Text(gu ? 'Paid test-series unlock આગળના step માં connect કરીશું.' : 'Paid test-series unlock will be connected in the next step.'), actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))]))),
          ])),
        ],
      ),
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

  void _selectMockAnswer(String? value) {
    if (value == null) return;
    setState(() {
      selected = value;
      answers[i] = value;
      answered = answers.length;
    });
  }

  Future<void> submit() async {
    if (selected == null || submitted) return;
    answers[i] = selected!; answered = answers.length;
    final correct = q['answer'] as String;
    if (!{'Z', 'X'}.contains(correct)) {
      final isRight = selected == correct;
      if (isRight) {
        score++;
      } else {
        m.add(q['id'].toString());
      }
      final topic = (q['topic'] ?? 'General').toString();
      await _recordTopicStat(topic, isRight);
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

  void next() {
    if (widget.mock) {
      if (i < widget.data.length - 1) {
        setState(() {
          i++;
          selected = answers[i];
          submitted = false;
        });
      } else {
        _finish();
      }
      return;
    }
    if (i < widget.data.length - 1) setState(() { i++; selected = null; submitted = false; }); else _finish();
  }

  Future<void> _finish() async {
    if (finishing) return;
    finishing = true;
    timer?.cancel();
    final evaluated = widget.data.where((e) => !{'Z', 'X'}.contains(e['answer'])).length;
    if (widget.mock) {
      score = 0;
      m = {...m};
      for (var n = 0; n < widget.data.length; n++) {
        final item = widget.data[n];
        final correct = item['answer'] as String;
        final selectedAnswer = answers[n];
        if (!{'Z', 'X'}.contains(correct) && selectedAnswer != null) {
          final isRight = selectedAnswer == correct;
          if (isRight) score++; else m.add(item['id'].toString());
          final topic = (item['topic'] ?? 'General').toString();
          await _recordTopicStat(topic, isRight);
        }
      }
      answered = answers.length;
      await widget.onStateChanged(b, m);
    }
    AppAnalytics.event('test_complete', parameters: {'mode': widget.mock ? 'mock' : (widget.practice ? 'practice' : 'paper'), 'question_count': widget.data.length, 'score': score});
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
    await prefs.setInt('gset_streak', currentStreak);    await prefs.setInt('gset_xp', currentXp);
    await prefs.setInt('gset_total_attempted', totalAttempted);
    await prefs.setInt('gset_total_correct', totalCorrect);
    await FirebaseSync.pushLocal(prefs);
    if (!mounted) return;
    Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => ResultPage(title: widget.title, score: score, total: evaluated, attempted: answered, gu: gu, questions: widget.data, answers: answers, bookmarks: b, mistakes: m, onStateChanged: widget.onStateChanged, practice: widget.practice, mock: widget.mock)));
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
                    submitted = !widget.mock && answers.containsKey(n);
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
          ...List.generate(opts.length, (j) { final letter = String.fromCharCode(65 + j); final right = letter == correct; final chosen = selected == letter; Color? fill; if (!widget.mock && submitted && right) fill = Colors.green.withValues(alpha: .15); if (!widget.mock && submitted && chosen && !right) fill = Colors.red.withValues(alpha: .15); return Card(color: fill, child: 
            // Flutter 3.38 deprecates RadioListTile.groupValue/onChanged in favor of RadioGroup.
            // Keep the current behavior intact until the RadioGroup migration is made in a dedicated UI refactor.
            // ignore: deprecated_member_use
            RadioListTile<String>(value: letter, groupValue: selected, onChanged: submitted && !widget.mock ? null : (v) => widget.mock ? _selectMockAnswer(v) : setState(() => selected = v), title: Text('$letter. ${opts[j]}'))); }),
          const SizedBox(height: 8),
          if (widget.mock)
            FilledButton.icon(
              onPressed: selected == null ? null : next,
              icon: const Icon(Icons.arrow_forward_rounded),
              label: Text(i == widget.data.length - 1 ? (gu ? 'મોક ટેસ્ટ Submit કરો' : 'Submit Mock Test') : (gu ? 'આગળ' : 'Next')),
            )
          else if (!submitted)
            FilledButton.icon(onPressed: selected == null ? null : submit, icon: const Icon(Icons.check), label: Text(gu ? 'જવાબ Submit કરો' : 'Submit Answer')),
          if (widget.mock)
            Row(children: [
              if (i > 0) Expanded(child: OutlinedButton(onPressed: () => setState(() { i--; selected = answers[i]; }), child: Text(gu ? 'પાછળ' : 'Previous'))),
              if (i > 0) const SizedBox(width: 8),
              Expanded(child: OutlinedButton(onPressed: i < widget.data.length - 1 ? next : _finish, child: Text(i == widget.data.length - 1 ? (gu ? 'ટેસ્ટ પૂર્ણ કરો' : 'Finish Test') : (gu ? 'છોડો / આગળ' : 'Skip / Next')))),
            ]),
          if (submitted && !widget.mock) FilledButton(onPressed: next, child: Text(i == widget.data.length - 1 ? (gu ? 'પરિણામ જુઓ' : 'View Result') : (gu ? 'આગળ' : 'Next'))),
          if (submitted && !widget.mock) Card(child: Padding(padding: const EdgeInsets.all(14), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(notEval ? (gu ? '⚠️ સત્તાવાર key મુજબ evaluationમાં ગણાતો નથી.' : '⚠️ Not evaluated according to the official key.') : (isCorrect ? (gu ? '✅ સાચો જવાબ' : '✅ Correct') : (gu ? '❌ ખોટો જવાબ' : '❌ Wrong')), style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            if (!notEval) ...[const SizedBox(height: 8), Text('${gu ? 'સાચો જવાબ' : 'Correct Answer'}: $correct'), const Divider(), Text(gu ? q['explanation_gu'] : q['explanation_en'])],
            if (q['review_flag'] == true) ...[const SizedBox(height: 10), Container(width: double.infinity, padding: const EdgeInsets.all(10), decoration: BoxDecoration(color: Colors.amber.withValues(alpha: .16), borderRadius: BorderRadius.circular(8)), child: Text('⚠️ ${gu ? 'સમીક્ષા નોંધ / Review Note' : 'Review Note'}: ${q['review_note']}'))],
            const SizedBox(height: 10), Text(gu ? '💡 Exam Tip: ${q['tip_gu']}' : '💡 Exam Tip: ${q['tip_en']}'),
          ]))),
          
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
      appBar: AppBar(title: Text(gu ? 'ભૂલ બુક' : 'Mistake Book')),
      body: qs.isEmpty
          ? Center(child: Text(gu ? 'હાલ કોઈ mistake saved નથી.' : 'No mistakes saved yet.'))
          : ListView(padding: const EdgeInsets.all(14), children: [
              Card(child: Padding(padding: const EdgeInsets.all(18), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Row(children: [const Icon(Icons.menu_book_rounded, size: 28, color: Color(0xFFEA580C)), const SizedBox(width: 10), Expanded(child: Text(gu ? '${qs.length} પ્રશ્નો રિવિઝન માટે' : '${qs.length} questions to revise', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900)))]),
                const SizedBox(height: 8),
                Text(gu ? 'ખોટા જવાબમાંથી શીખો: સમજણ વાંચો અને ફરી પ્રશ્ન ઉકેલો.' : 'Turn wrong answers into learning: read the explanation, then solve them again.', style: const TextStyle(height: 1.35)),
                const SizedBox(height: 14),
                FilledButton.icon(
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: 'Mistake Revision', practice: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: onStateChanged))),
                  icon: const Icon(Icons.replay_rounded),
                  label: Text(gu ? 'ભૂલ રિવિઝન ટેસ્ટ' : 'Mistake Revision Test'),
                ),
              ]))),
              const SizedBox(height: 10),
              ...qs.map((q) => Card(
                margin: const EdgeInsets.only(bottom: 8),
                child: ExpansionTile(
                  leading: const CircleAvatar(child: Icon(Icons.error_outline_rounded)),
                  title: Text(gu ? q['question_gu'] : q['question_en'], maxLines: 2, overflow: TextOverflow.ellipsis),
                  subtitle: Text((q['topic'] ?? (gu ? 'સામાન્ય' : 'General')).toString()),
                  childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                  children: [                    Text(gu ? q['explanation_gu'] : q['explanation_en'], style: const TextStyle(height: 1.35)),
                    const SizedBox(height: 8),
                    Text(gu ? '💡 ${q['tip_gu']}' : '💡 ${q['tip_en']}', style: const TextStyle(fontWeight: FontWeight.w700)),
                  ],
                ),
              )),
            ]),
    );
  }
}

class AnalyticsPage extends StatefulWidget {
  final bool gu;
  final List<Map<String, dynamic>> data;
  const AnalyticsPage({super.key, required this.gu, required this.data});
  @override State<AnalyticsPage> createState() => _AnalyticsPageState();
}

class _AnalyticsPageState extends State<AnalyticsPage> {
  int attempted = 0, correct = 0;
  Map<String, int> attempts = {}, rights = {};

  @override
  void initState() { super.initState(); _load(); }

  Future<void> _load() async {
    final p = await SharedPreferences.getInstance();
    final a = p.getInt('gset_total_attempted') ?? 0;
    final r = p.getInt('gset_total_correct') ?? 0;
    final am = Map<String, dynamic>.from(jsonDecode(p.getString('gset_topic_attempts') ?? '{}'));
    final rr = Map<String, dynamic>.from(jsonDecode(p.getString('gset_topic_correct') ?? '{}'));
    if (!mounted) return;
    setState(() {
      attempted = a;
      correct = r;
      attempts = am.map((k, v) => MapEntry(k, (v as num).toInt()));
      rights = rr.map((k, v) => MapEntry(k, (v as num).toInt()));
    });
  }

  @override
  Widget build(BuildContext context) {
    final accuracy = attempted == 0 ? 0 : (correct * 100 / attempted).round();
    final topics = {...attempts.keys, ...rights.keys}.toList();
    topics.sort((a, b) {
      final aa = attempts[a] ?? 0, ab = attempts[b] ?? 0;
      final pa = aa == 0 ? 0 : ((rights[a] ?? 0) * 100 / aa).round();
      final pb = ab == 0 ? 0 : ((rights[b] ?? 0) * 100 / ab).round();
      return pa.compareTo(pb);
    });
    return Scaffold(
      appBar: AppBar(title: Text(widget.gu ? 'મારું Analytics' : 'My Analytics')),
      body: ListView(
        padding: const EdgeInsets.all(14),
        children: [
          Card(child: Padding(
            padding: const EdgeInsets.all(18),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(widget.gu ? 'તમારું Performance' : 'Your Performance', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
              const SizedBox(height: 14),
              Row(children: [
                Expanded(child: _stat(Icons.quiz_rounded, attempted.toString(), widget.gu ? 'પ્રયાસ' : 'Attempted')),
                Expanded(child: _stat(Icons.check_circle_rounded, correct.toString(), widget.gu ? 'સાચા' : 'Correct')),
                Expanded(child: _stat(Icons.percent_rounded, '$accuracy%', widget.gu ? 'Accuracy' : 'Accuracy')),
              ]),
              const SizedBox(height: 16),
              LinearProgressIndicator(value: accuracy / 100, minHeight: 9),
              const SizedBox(height: 8),
              Text(widget.gu ? 'Accuracy = સાચા જવાબ ÷ કુલ attempted' : 'Accuracy = correct answers ÷ total attempted', style: const TextStyle(fontSize: 11)),
            ]),
          )),
          const SizedBox(height: 12),
          Card(child: Padding(
            padding: const EdgeInsets.all(18),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(widget.gu ? '📊 Topic-wise Performance' : '📊 Topic-wise Performance', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900)),
              const SizedBox(height: 12),
              if (topics.isEmpty)
                Text(widget.gu ? 'હજુ topic data નથી. પ્રશ્નો solve કરો.' : 'No topic data yet. Solve some questions first.')
              else
                ...topics.map((topic) {
                  final a = attempts[topic] ?? 0;
                  final r = rights[topic] ?? 0;
                  final pct = a == 0 ? 0 : (r * 100 / a).round();
                  return Padding(
                    padding: const EdgeInsets.only(bottom: 13),
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Row(children: [
                        Expanded(child: Text(topic, style: const TextStyle(fontWeight: FontWeight.w800))),
                        Text('$pct%  ($r/$a)', style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w800)),
                      ]),
                      const SizedBox(height: 6),
                      LinearProgressIndicator(value: pct / 100, minHeight: 7),
                    ]),
                  );
                }),
            ]),
          )),
          const SizedBox(height: 12),
          Card(child: Padding(
            padding: const EdgeInsets.all(18),
            child: Text(
              widget.gu
                ? '💡 Tip: ઓછા accuracy વાળા topic પર Targeted Practice કરો.'
                : '💡 Tip: Use Targeted Practice for topics with lower accuracy.',
              style: const TextStyle(fontWeight: FontWeight.w700, height: 1.35),
            ),
          )),
        ],
      ),
    );
  }

  Widget _stat(IconData icon, String value, String label) => Column(children: [
    Icon(icon, size: 27),
    const SizedBox(height: 5),
    Text(value, style: const TextStyle(fontSize: 19, fontWeight: FontWeight.w900)),
    Text(label, style: const TextStyle(fontSize: 11)),
  ]);
}

class TargetedPracticePage extends StatefulWidget {
  final bool gu;
  final List<Map<String, dynamic>> data;
  final String topic;
  final Set<String> bookmarks, mistakes;
  final Future<void> Function(Set<String>, Set<String>) onStateChanged;
  const TargetedPracticePage({super.key, required this.gu, required this.data, required this.topic, required this.bookmarks, required this.mistakes, required this.onStateChanged});
  @override State<TargetedPracticePage> createState() => _TargetedPracticePageState();
}

class _TargetedPracticePageState extends State<TargetedPracticePage> {
  @override
  Widget build(BuildContext context) {
    final qs = widget.data.where((q) => (q['topic'] ?? 'General').toString() == widget.topic).toList()..shuffle(Random());
    final selected = qs.take(min(20, qs.length)).toList();
    return Scaffold(
      appBar: AppBar(title: Text(widget.gu ? 'Targeted Practice' : 'Targeted Practice')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Card(child: Padding(
            padding: const EdgeInsets.all(18),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(widget.gu ? '🎯 Weak Topic Practice' : '🎯 Weak Topic Practice', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
              const SizedBox(height: 8),
              Text(widget.topic, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
              const SizedBox(height: 6),
              Text(widget.gu ? '${selected.length} પ્રશ્નો • Focused revision' : '${selected.length} questions • Focused revision'),
            ]),
          )),
          const Spacer(),
          SizedBox(width: double.infinity, child: FilledButton.icon(
            onPressed: selected.isEmpty ? null : () => Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(
              data: selected, gu: widget.gu,
              title: widget.gu ? 'Targeted: ${widget.topic}' : 'Targeted: ${widget.topic}',
              practice: true,
              bookmarks: widget.bookmarks, mistakes: widget.mistakes,
              onStateChanged: widget.onStateChanged,
            ))),
            icon: const Icon(Icons.play_arrow_rounded),
            label: Text(widget.gu ? 'Practice શરૂ કરો' : 'Start Practice'),
          )),
        ]),
      ),
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
      appBar: AppBar(title: Text(widget.gu ? 'મારા નબળા વિષયો' : 'My Weak Areas')),
      body: topics.isEmpty
          ? Center(child: Text(widget.gu ? 'થોડા પ્રશ્નો solve કરો; પછી topic analysis અહીં દેખાશે.' : 'Solve a few questions and your topic analysis will appear here.'))
          : ListView(padding: const EdgeInsets.all(14), children: [
              Card(child: Padding(padding: const EdgeInsets.all(18), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(widget.gu ? '🎯 લક્ષિત પ્રેક્ટિસ' : '🎯 Targeted Practice', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
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
                      label: Text(widget.gu ? 'પ્રેક્ટિસ' : 'Practice'),
                    )),
                  ])),
                );
              }),
            ]),
    );
  }
}

class ResultPage extends StatelessWidget {
  final String title; final int score, total, attempted; final bool gu, practice, mock;
  final List<Map<String, dynamic>> questions; final Map<int, String> answers;
  final Set<String> bookmarks, mistakes;
  final Future<void> Function(Set<String>, Set<String>) onStateChanged;
  const ResultPage({super.key, required this.title, required this.score, required this.total, required this.attempted, required this.gu, required this.questions, required this.answers, required this.bookmarks, required this.mistakes, required this.onStateChanged, required this.practice, this.mock = false});
  @override Widget build(BuildContext context) {
    final pct = total == 0 ? 0.0 : score * 100.0 / total;
    return Scaffold(appBar: AppBar(title: Text(gu ? 'પરિણામ' : 'Result')), body: ListView(padding: const EdgeInsets.all(20), children: [
      Card(child: Padding(padding: const EdgeInsets.all(22), child: Column(children: [const Icon(Icons.emoji_events_outlined, size: 64), const SizedBox(height: 12), Text(title, style: Theme.of(context).textTheme.titleLarge, textAlign: TextAlign.center), const SizedBox(height: 10), Text('$score / $total', style: Theme.of(context).textTheme.displaySmall?.copyWith(fontWeight: FontWeight.bold)), Text('${pct.toStringAsFixed(1)}%', style: Theme.of(context).textTheme.headlineSmall), const SizedBox(height: 8), Text(gu ? 'પ્રયાસ કરેલા પ્રશ્નો: $attempted / ${questions.length}' : 'Attempted: $attempted / ${questions.length}')]))),      const SizedBox(height: 14),
      Row(children: [Expanded(child: FilledButton.icon(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => ReviewPage(title: title, questions: questions, answers: answers, gu: gu))), icon: const Icon(Icons.fact_check_outlined), label: Text(gu ? 'Review' : 'Review'))), const SizedBox(width: 10), Expanded(child: OutlinedButton.icon(onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => TestPage(data: questions, gu: gu, title: title, practice: practice, mock: mock, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: onStateChanged))), icon: const Icon(Icons.refresh), label: Text(gu ? 'ફરી ટેસ્ટ' : 'Retry')))]),
      const SizedBox(height: 10), OutlinedButton.icon(onPressed: () => Navigator.pop(context), icon: const Icon(Icons.home_outlined), label: Text(gu ? 'હોમ' : 'Home')),
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