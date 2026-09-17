@override
Widget build(BuildContext context) {
  final pct = total == 0 ? 0 : score * 100 / total;

  return Scaffold(
    appBar: AppBar(
      title: Text(gu ? 'પરિણામ' : 'Result'),
    ),
    body: Center(
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(
              Icons.emoji_events_outlined,
              size: 72,
            ),
            const SizedBox(height: 18),
            Text(
              gu ? 'તમારું પરિણામ' : 'Your Result',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const SizedBox(height: 14),
            Text(
              gu
                  ? 'સ્કોર: $score / $total'
                  : 'Score: $score / $total',
              style: Theme.of(context).textTheme.displaySmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 6),
            Text(
              '${pct.toStringAsFixed(1)}%',
              style: Theme.of(context).textTheme.headlineSmall,
            ),
            const SizedBox(height: 18),
            Text(
              gu
                  ? 'Attempted: $attempted • Attempted'
                  : 'Attempted: $attempted',
            ),
            const SizedBox(height: 28),
            FilledButton(
              onPressed: () {
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (_) => HomePage(),
                  ),
                );
              },
              child: Text(
                gu ? 'હોમ' : 'Home',
              ),
            ),
          ],
        ),
      ),
    ),
  );
}
