import json

with open("tagData.json", "r", encoding="utf-8") as f:
    tag_data = json.load(f)

ds = tag_data.get("数据结构", {})

for tag in ["二叉树遍历", "二叉树的遍历", "排序算法", "归并排序", "插入排序"]:
    if tag in ds:
        items = [it for it in ds[tag] if 2016 <= it.get("year", 0) <= 2025]
        print(f"=== {tag} ({len(items)}) ===")
        for it in items:
            print(" ", it["title"], it["quiz_type"], it["link"])
