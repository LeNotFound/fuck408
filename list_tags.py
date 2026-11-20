import json

with open("tagData.json", "r", encoding="utf-8") as f:
    tag_data = json.load(f)
with open("quiz_database.json", "r", encoding="utf-8") as f:
    quiz_db = json.load(f)

ds = tag_data.get("数据结构", {})
res = []
for tag, items in ds.items():
    cnt_items = [it for it in items if 2016 <= it.get("year", 0) <= 2025]
    if len(cnt_items) >= 3:
        res.append((tag, cnt_items))

res.sort(key=lambda x: (-len(x[1]), x[0]))

print("High frequency tags list:")
for i, (tag, items) in enumerate(res, 1):
    years = [it["year"] for it in items]
    print(f"{i:02d}. {tag} ({len(items)}次): {years}")
