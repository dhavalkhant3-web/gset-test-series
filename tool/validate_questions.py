import json
from pathlib import Path

path = Path("assets/questions.json")
questions = json.loads(path.read_text(encoding="utf-8"))

assert isinstance(questions, list), "questions.json must contain a list"
assert len(questions) == 1070, f"Expected 1070 questions, found {len(questions)}"

required = {
    "id", "paperId", "question_en", "question_gu",
    "options_en", "options_gu", "answer",
}

ids = set()
paper_counts = {}

for i, q in enumerate(questions, 1):
    missing = required - q.keys()
    assert not missing, f"Question {i} missing fields: {sorted(missing)}"

    qid = str(q["id"])
    assert qid not in ids, f"Duplicate question id: {qid}"
    ids.add(qid)

    en = q["options_en"]
    gu = q["options_gu"]
    assert isinstance(en, list) and len(en) == 4, f"{qid}: options_en must have 4 options"
    assert isinstance(gu, list) and len(gu) == 4, f"{qid}: options_gu must have 4 options"

    answer = str(q["answer"])
    assert answer in {"A", "B", "C", "D", "X", "Z"}, f"{qid}: invalid answer key {answer}"

    paper = str(q["paperId"])
    paper_counts[paper] = paper_counts.get(paper, 0) + 1

assert len(paper_counts) == 20, f"Expected 20 papers, found {len(paper_counts)}"
assert sum(paper_counts.values()) == 1070

print(f"Question bank OK: {len(questions)} questions, {len(paper_counts)} papers, {len(ids)} unique IDs")
print("Paper counts:", dict(sorted(paper_counts.items())))
