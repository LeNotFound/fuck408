import json
import os
from prompt_builder import generate_prompt

with open('os_topics_data.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

os.makedirs('scratch_prompts', exist_ok=True)

for i, t in enumerate(topics):
    tag = t['tag']
    p = generate_prompt(t)
    path = f"scratch_prompts/{tag}.txt"
    with open(path, 'w', encoding='utf-8') as pf:
        pf.write(p)

print(f"Generated {len(topics)} prompt files in scratch_prompts/")
