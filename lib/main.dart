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
        theme: ThemeData(colorSchemeSeed: const Color(0xFF3949AB), useMaterial3: true, scaffoldBackgroundColor: const Color(0xFFF6F7FB), cardTheme: const CardThemeData(margin: EdgeInsets.zero, elevation: 1, clipBehavior: Clip.antiAlias), appBarTheme: const AppBarTheme(centerTitle: false, elevation: 0), inputDecorationTheme: const InputDecorationTheme(filled: true, fillColor: Colors.white, border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(14)), borderSide: BorderSide.none), enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(14)), borderSide: BorderSide.none), focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(14))))),
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

  @override void initState() { super.initState(); _load(); }

  Future<void> _load() async {
    final s = await rootBundle.loadString('assets/questions.json');
    final raw = jsonDecode(s) as List;
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      data = raw.cast<Map<String, dynamic>>();
      bookmarks = (prefs.getStringList('bookmarks') ?? []).toSet();
      mistakes = (prefs.getStringList('mistakes') ?? []).toSet();
    });
  }

  List<Map<String, dynamic>> forPaper(String id) => data.where((q) => q['paperId'] == id).toList();
  List<PaperInfo> get filtered => papers.where((p) => p.title.toLowerCase().contains(search.toLowerCase())).toList();

  Future<void> _openPractice({String? topic}) async {
    if (data.isEmpty) return;
    var qs = data.where((q) => topic == null || q['topic'] == topic).toList();
    if (qs.isEmpty) return;
    qs.shuffle(Random());
    if (qs.length > 20) qs = qs.take(20).toList();
    await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: topic == null ? 'Random Practice' : topic!, practice: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets)));
  }

  Future<void> _saveSets(Set<String> b, Set<String> m) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList('bookmarks', b.toList());
    await prefs.setStringList('mistakes', m.toList());
    if (mounted) setState(() { bookmarks = b; mistakes = m; });
  }

  @override
  Widget build(BuildContext context) {
    final readyCount = papers.where((p) => forPaper(p.id).isNotEmpty && forPaper(p.id).every((q) => q['source_verified'] == true)).length;
    return Scaffold(
      appBar: AppBar(title: const Text('GSET Paper-I'), actions: [
        Padding(padding: const EdgeInsets.only(right: 8), child: SegmentedButton<bool>(segments: const [ButtonSegment(value: true, label: Text('ગુજરાતી')), ButtonSegment(value: false, label: Text('English'))], selected: {gu}, onSelectionChanged: (s) => setState(() => gu = s.first))),
      ]),
      body: data.isEmpty ? const Center(child: CircularProgressIndicator()) : ListView(padding: const EdgeInsets.fromLTRB(16, 10, 16, 24), children: [
        Card(child: Container(decoration: const BoxDecoration(gradient: LinearGradient(begin: Alignment.topLeft, end: Alignment.bottomRight, colors: [Color(0xFF3949AB), Color(0xFF5C6BC0)])), padding: const EdgeInsets.all(20), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text('GSET Paper-I Test Series', style: Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.bold, color: Colors.white)),
          const SizedBox(height: 6), Text(gu ? 'Previous Year Papers • Solutions • Practice' : 'Previous Year Papers • Solutions • Practice', style: TextStyle(color: Colors.white70)),
          const SizedBox(height: 14),
          Row(children: [
            Expanded(child: _stat('${papers.length}', gu ? 'Papers' : 'Papers')),
            Expanded(child: _stat('${data.length}', gu ? 'Questions' : 'Questions')),
            Expanded(child: _stat('$readyCount/${papers.length}', gu ? 'Verified' : 'Verified')),
          ]),
        ]))),
        const SizedBox(height: 10),
        Wrap(spacing: 8, runSpacing: 8, children: [
          FilledButton.icon(onPressed: () => _openPractice(), icon: const Icon(Icons.shuffle), label: Text(gu ? 'Random Practice' : 'Random Practice')),
          OutlinedButton.icon(onPressed: mistakes.isEmpty ? null : () async { final qs = data.where((q) => mistakes.contains(q['id'])).toList(); await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: gu ? 'Mistakes' : 'Mistakes', practice: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets))); }, icon: const Icon(Icons.error_outline), label: Text('${gu ? 'Mistakes' : 'Mistakes'} (${mistakes.length})')),
          OutlinedButton.icon(onPressed: bookmarks.isEmpty ? null : () async { final qs = data.where((q) => bookmarks.contains(q['id'])).toList(); await Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: gu ? 'Bookmarks' : 'Bookmarks', practice: true, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets))); }, icon: const Icon(Icons.bookmark_outline), label: Text('${gu ? 'Bookmarks' : 'Bookmarks'} (${bookmarks.length})')),
        ]),
        const SizedBox(height: 14),
        TextField(decoration: InputDecoration(prefixIcon: const Icon(Icons.search), hintText: gu ? 'Paper શોધો...' : 'Search paper...', border: const OutlineInputBorder()), onChanged: (v) => setState(() => search = v)),
        const SizedBox(height: 14),
        Text(gu ? 'Previous Year Papers' : 'Previous Year Papers', style: Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight: FontWeight.bold)),
        const SizedBox(height: 6),
        ...filtered.map((p) {
          final qs = forPaper(p.id);
          final ready = qs.length == p.questions && qs.every((q) => q['source_verified'] == true);
          return Card(margin: const EdgeInsets.only(bottom: 10), child: ListTile(contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
            leading: CircleAvatar(backgroundColor: Theme.of(context).colorScheme.primaryContainer, child: Text(p.title.substring(0, 1), style: const TextStyle(fontWeight: FontWeight.bold))),
            title: Text('${p.title} — Paper-I'),
            subtitle: Text('${p.date} • ${p.questions} Questions${ready ? ' • Verified' : ' • ${qs.length}/${p.questions} loaded'}'),
            trailing: Icon(ready ? Icons.play_circle_outline : Icons.lock_outline),
            onTap: ready ? () => Navigator.push(context, MaterialPageRoute(builder: (_) => TestPage(data: qs, gu: gu, title: p.title, bookmarks: bookmarks, mistakes: mistakes, onStateChanged: _saveSets))) : () => _showNote(p, qs.length),
          ));
        }),
      ]),
    );
  }

  Widget _stat(String n, String label) => Column(children: [Text(n, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white)), Text(label, style: const TextStyle(fontSize: 12, color: Colors.white70))]);
  void _showNote(PaperInfo p, int count) => showDialog(context: context, builder: (_) => AlertDialog(title: Text(p.title), content: Text(gu ? '$count/${p.questions} પ્રશ્નો હાલ verified dataમાં ઉપલબ્ધ છે.' : '$count/${p.questions} questions are currently available in verified data.'), actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))]));
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
    if (!{'Z', 'X'}.contains(correct)) { if (selected == correct) score++; else m.add(q['id'].toString()); }
    setState(() => submitted = true); widget.onStateChanged(b, m);
  }

  void next() { if (i < widget.data.length - 1) setState(() { i++; selected = null; submitted = false; }); else _finish(); }
  void _finish() {
    if (finishing) return;
    finishing = true;
    timer?.cancel();
    final evaluated = widget.data.where((e) => !{'Z', 'X'}.contains(e['answer'])).length;
    if (!mounted) return;
    Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => ResultPage(title: widget.title, score: score, total: evaluated, attempted: answered, gu: gu, questions: widget.data, answers: answers, bookmarks: b, mistakes: m, onStateChanged: widget.onStateChanged, practice: widget.practice)));
  }

  Future<void> _confirmExit() async { final leave = await showDialog<bool>(context: context, builder: (_) => AlertDialog(title: Text(gu ? 'ટેસ્ટ છોડવી છે?' : 'Leave test?'), content: Text(gu ? 'હાલની ટેસ્ટની પ્રગતિ સાચવવામાં નહીં આવે. શું તમે બહાર નીકળવા માંગો છો?' : 'Current test progress will not be saved. Do you want to leave?'), actions: [TextButton(onPressed: () => Navigator.pop(context, false), child: Text(gu ? 'રહો' : 'Stay')), FilledButton(onPressed: () => Navigator.pop(context, true), child: Text(gu ? 'બહાર નીકળો' : 'Leave'))])); if (leave == true && mounted) Navigator.pop(context); }

  @override Widget build(BuildContext context) {
    final opts = List<String>.from(gu ? q['options_gu'] : q['options_en']); final correct = q['answer'] as String; final notEval = {'Z', 'X'}.contains(correct); final isCorrect = !notEval && selected == correct; final passage = ((gu ? q['passage_gu'] : q['passage_en']) ?? '').toString();
    return PopScope(canPop: false, onPopInvokedWithResult: (didPop, result) { if (!didPop) _confirmExit(); }, child: Scaffold(appBar: AppBar(title: Text('${widget.title} • ${i + 1}/${widget.data.length}'), actions: [IconButton(onPressed: () { setState(() { b.contains(q['id'].toString()) ? b.remove(q['id'].toString()) : b.add(q['id'].toString()); }); widget.onStateChanged(b, m); }, icon: Icon(b.contains(q['id'].toString()) ? Icons.bookmark : Icons.bookmark_border)), IconButton(tooltip: gu ? 'English' : 'ગુજરાતી', onPressed: () => setState(() => gu = !gu), icon: const Icon(Icons.translate)), Padding(padding: const EdgeInsets.only(right: 12), child: Center(child: Text(remaining, style: const TextStyle(fontWeight: FontWeight.bold))))]),
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
          ...List.generate(opts.length, (j) { final letter = String.fromCharCode(65 + j); final right = letter == correct; final chosen = selected == letter; Color? fill; if (submitted && right) fill = Colors.green.withValues(alpha: .15); if (submitted && chosen && !right) fill = Colors.red.withValues(alpha: .15); return Card(color: fill, child: RadioListTile<String>(value: letter, groupValue: selected, onChanged: submitted ? null : (v) => setState(() => selected = v), title: Text('$letter. ${opts[j]}'))); }),
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