import json

with open('tagData.json', 'r', encoding='utf-8') as f:
    tag_data = json.load(f)

with open('quiz_database.json', 'r', encoding='utf-8') as f:
    quiz_db = json.load(f)

os_tags = tag_data.get('操作系统', {})

summary = []
for tag, quizzes in os_tags.items():
    recent = [q for q in quizzes if 2016 <= q.get('year', 0) <= 2025]
    if len(recent) >= 3:
        summary.append({
            'tag': tag,
            'recent_count': len(recent),
            'total_count': len(quizzes),
            'recent_quizzes': recent,
            'all_quizzes': quizzes
        })

# Sort descending by recent_count, then tag name
summary.sort(key=lambda x: (-x['recent_count'], x['tag']))
print(f'Found {len(summary)} tags')
for item in summary:
    years = [q['year'] for q in item['recent_quizzes']]
    print(f"{item['tag']}: 近十年 {item['recent_count']} 次, 全部 {item['total_count']} 次, 近十年年份: {years}")
