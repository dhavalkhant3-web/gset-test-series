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
        IconButton(tooltip: 'Account & Feedback', onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => AccountPage(gu: gu))), icon: const Icon(Icons.account_circle_outlined)),
        Padding(padding: const EdgeInsets.only(right: 8), child: SegmentedButton<bool>(segments: const [ButtonSegment(value: true, label: Text('ગુજરાતી')), ButtonSegment(value: false, label: Text('English'))], selected: {gu}, onSelectionChanged: (s) => setState(() => gu = s.first))),
      ]),
      body: data.isEmpty ? const Center(child: CircularProgressIndicator()) : ListView(padding: const EdgeInsets.fromLTRB(16, 10, 16, 24), children: [
        Container(
          padding: const EdgeInsets.fromLTRB(20,22,20,18),
          decoration: BoxDecoration(
            gradient: const LinearGradient(begin: Alignment.topLeft,end: Alignment.bottomRight,colors:[Color(0xFF5B5FEF),Color(0xFF7B61FF),Color(0xFF00A6A6)]),
            borderRadius: BorderRadius.circular(26),
            boxShadow:[BoxShadow(color:const Color(0xFF5B5FEF).withValues(alpha:.22),blurRadius:22,offset:const Offset(0,10))],
          ),
          child:Column(crossAxisAlignment:CrossAxisAlignment.start,children:[
            Row(children:[
              Container(width:48,height:48,decoration:BoxDecoration(color:Colors.white.withValues(alpha:.18),borderRadius:BorderRadius.circular(16)),child:const Icon(Icons.bolt_rounded,color:Colors.white,size:30)),
              const SizedBox(width:12),
              Expanded(child:Column(crossAxisAlignment:CrossAxisAlignment.start,children:[
                Text(gu?'આજનું Target 🎯':'Today’s Target 🎯',style:const TextStyle(color:Colors.white70,fontSize:13,fontWeight:FontWeight.w600)),
                const SizedBox(height:2),
                Text(gu?'Practice શરૂ કરો!':'Start your practice!',style:const TextStyle(color:Colors.white,fontSize:23,fontWeight:FontWeight.bold)),
              ])),
            ]),
            const SizedBox(height:16),
            const Text('20 random questions • instant feedback',style:TextStyle(color:Colors.white70)),
            const SizedBox(height:14),
            SizedBox(width:double.infinity,child:FilledButton.icon(style:FilledButton.styleFrom(backgroundColor:Colors.white,foregroundColor:const Color(0xFF4F46C5),padding:const EdgeInsets.symmetric(vertical:14)),onPressed:()=>_openPractice(),icon:const Icon(Icons.play_arrow_rounded),label:Text(gu?'હમણાં Practice કરો':'Practice Now',style:const TextStyle(fontWeight:FontWeight.bold)))),
            const SizedBox(height:16),
            Row(children:[
              Expanded(child:_stat('${papers.length}','Papers')),Expanded(child:_stat('${data.length}','Questions')),Expanded(child:_stat('${readyCount}/${papers.length}','Verified')),
            ]),
          ]),
        ),
        const SizedBox(height:14),
        Row(children:[
          Expanded(child:_homeActionCard(context,icon:Icons.shuffle_rounded,title:'Random',subtitle:'Practice',color:const Color(0xFF5B5FEF),onTap:()=>_openPractice())),
          const SizedBox(width:10),
          Expanded(child:_homeActionCard(context,icon:Icons.error_outline_rounded,title:'Mistakes',subtitle:'${mistakes.length} saved',color:const Color(0xFFF97316),onTap:mistakes.isEmpty?null:()async{final qs=data.where((q)=>mistakes.contains(q['id'])).toList();await Navigator.push(context,MaterialPageRoute(builder:(_)=>TestPage(data:qs,gu:gu,title:'Mistakes',practice:true,bookmarks:bookmarks,mistakes:mistakes,onStateChanged:_saveSets)));})),
          const SizedBox(width:10),
          Expanded(child:_homeActionCard(context,icon:Icons.bookmark_rounded,title:'Saved',subtitle:'${bookmarks.length} saved',color:const Color(0xFF00A6A6),onTap:bookmarks.isEmpty?null:()async{final qs=data.where((q)=>bookmarks.contains(q['id'])).toList();await Navigator.push(context,MaterialPageRoute(builder:(_)=>TestPage(data:qs,gu:gu,title:'Bookmarks',practice:true,bookmarks:bookmarks,mistakes:mistakes,onStateChanged:_saveSets)));})),
        ]),
        const SizedBox(height:18),
        Text(gu?'તમારો Progress':'Your Progress',style:Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight:FontWeight.bold)),
        const SizedBox(height:8),
        Card(child:Padding(padding:const EdgeInsets.all(14),child:Row(children:[
          Container(width:42,height:42,decoration:BoxDecoration(color:const Color(0xFFEEF2FF),borderRadius:BorderRadius.circular(14)),child:const Icon(Icons.auto_graph_rounded,color:Color(0xFF5B5FEF))),
          const SizedBox(width:12),
          Expanded(child:Column(crossAxisAlignment:CrossAxisAlignment.start,children:[
            Text(gu?'તમારી practice library તૈયાર છે':'Your practice library is ready',style:const TextStyle(fontWeight:FontWeight.w700)),
            const SizedBox(height:5),
            ClipRRect(borderRadius:BorderRadius.circular(8),child:LinearProgressIndicator(value:papers.isEmpty?0:readyCount/papers.length,minHeight:7)),
            const SizedBox(height:5),
            Text('${readyCount}/${papers.length} papers ready',style:Theme.of(context).textTheme.bodySmall),
          ])),
        ]))),
        const SizedBox(height:18),
        Text('Previous Year Papers',style:Theme.of(context).textTheme.titleLarge?.copyWith(fontWeight:FontWeight.bold)),
        const SizedBox(height:8),
        TextField(decoration:InputDecoration(prefixIcon:const Icon(Icons.search_rounded),hintText:gu?'Year અથવા paper શોધો...':'Search year or paper...',border:const OutlineInputBorder()),onChanged:(v)=>setState(()=>search=v)),
        const SizedBox(height:14),
        ...filtered.map((p){
          final qs=forPaper(p.id); final ready=qs.length==p.questions&&qs.every((q)=>q['source_verified']==true); final year=p.title.split(' ').last;
          return Card(margin:const EdgeInsets.only(bottom:10),child:InkWell(
            onTap:ready?()=>Navigator.push(context,MaterialPageRoute(builder:(_)=>TestPage(data:qs,gu:gu,title:p.title,bookmarks:bookmarks,mistakes:mistakes,onStateChanged:_saveSets))):()=>_showNote(p,qs.length),
            child:Padding(padding:const EdgeInsets.all(13),child:Row(children:[
              Container(width:58,height:58,decoration:BoxDecoration(gradient:LinearGradient(begin:Alignment.topLeft,end:Alignment.bottomRight,colors:ready?const[Color(0xFFEEF2FF),Color(0xFFE0E7FF)]:const[Color(0xFFF3F4F6),Color(0xFFE5E7EB)]),borderRadius:BorderRadius.circular(18)),child:Center(child:Text(year,style:TextStyle(fontWeight:FontWeight.w800,color:ready?const Color(0xFF4F46C5):Colors.grey[600])))),
              const SizedBox(width:14),
              Expanded(child:Column(crossAxisAlignment:CrossAxisAlignment.start,children:[
                Text('${p.title} • Paper-I',style:const TextStyle(fontWeight:FontWeight.w700,fontSize:16)),
                const SizedBox(height:4),Text('${p.date} • ${p.questions} Questions',style:Theme.of(context).textTheme.bodySmall),
                const SizedBox(height:7),Row(children:[
                  Icon(ready?Icons.verified_rounded:Icons.hourglass_bottom_rounded,size:15,color:ready?const Color(0xFF00A6A6):Colors.grey),const SizedBox(width:5),
                  Text(ready?'Verified & Ready':'${qs.length}/${p.questions} loaded',style:TextStyle(fontSize:12,fontWeight:FontWeight.w600,color:ready?const Color(0xFF008A8A):Colors.grey[700])),
                ]),
              ])),
              Container(width:40,height:40,decoration:BoxDecoration(color:ready?const Color(0xFF5B5FEF):Colors.grey[200],shape:BoxShape.circle),child:Icon(ready?Icons.play_arrow_rounded:Icons.lock_outline_rounded,color:ready?Colors.white:Colors.grey[600])),
            ])),
          ));
        }),
      ]),
    );
  }

  Widget _stat(String n,String label)=>Column(children:[Text(n,style:const TextStyle(fontSize:22,fontWeight:FontWeight.bold,color:Colors.white)),Text(label,style:const TextStyle(fontSize:12,color:Colors.white70))]);

  Widget _homeActionCard(BuildContext context,{required IconData icon,required String title,required String subtitle,required Color color,required VoidCallback? onTap}){
    final enabled=onTap!=null;
    return Card(elevation:1.5,child:InkWell(onTap:onTap,child:Padding(padding:const EdgeInsets.all(13),child:Column(crossAxisAlignment:CrossAxisAlignment.start,children:[
      Container(width:42,height:42,decoration:BoxDecoration(color:color.withValues(alpha:enabled ? .12 : .06),borderRadius:BorderRadius.circular(14)),child:Icon(icon,color:enabled?color:Colors.grey,size:23)),
      const SizedBox(height:10),Text(title,style:TextStyle(fontWeight:FontWeight.w800,color:enabled?null:Colors.grey)),const SizedBox(height:2),
      Text(subtitle,style:Theme.of(context).textTheme.bodySmall?.copyWith(color:enabled?color:Colors.grey)),
    ]))));
  }
  void _showNote(PaperInfo p, int count) => showDialog(context: context, builder: (_) => AlertDialog(title: Text(p.title), content: Text(gu ? '$count/${p.questions} પ્રશ્નો હાલ verified dataમાં ઉપલબ્ધ છે.' : '$count/${p.questions} questions are currently available in verified data.'), actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))]));
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