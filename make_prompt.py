import json

with open("tag_packets.json", "r", encoding="utf-8") as f:
    packets = json.load(f)

def make_prompt(tag_name):
    p = packets[tag_name]
    recent_count = p["recent_count"]
    total_count = p["total_count"]
    years = p["recent_years"]
    questions = p["questions"]
    
    q_texts = []
    for i, q in enumerate(questions, 1):
        q_texts.append(f"""
### 真题 {i}：{q['title']}（{q['quiz_type']}）
{q['content']}
""")
    
    questions_block = "\n".join(q_texts)
    
    prompt = f"""请编写 408 高频考点精讲文档：【{tag_name}】。

【考点信息】
- 科目：数据结构
- 考点名称：{tag_name}
- 模块归属：数据结构
- 近十年考查频次：{recent_count} 次（年份覆盖：{', '.join(str(y) for y in years)}）
- 历年总考查频次：{total_count} 次

【近十年对应真题库提取内容】
{questions_block}

【编写要求与体例规范】
1. 严格参考标准体例（可参照 `408高频考点精讲_01_哈夫曼树.md`）：
   - 顶部元数据：包含标题、模块归属、考点层级、适用对象。
   - 一、考情档案：近十年考频、总考频、出题形式、命题特点、近十年年份分布 ASCII 表格。
   - 二、具体考察内容：核心定义、数学原理/定理推导（使用规范 LaTeX 公式）、性质对比、算法过程。
   - 三、近十年真题精讲（2016~2025）：按年份顺序逐题深入解析，提供【题目】、【解析】（步骤详细推导、选项逐项辨析）、【正确答案】。注意原题选项与图文表述必须完整准确。
   - 四、核心解题套路与易错陷阱（或综合应用拓展）。
   - 五、考点速记清单。
2. 格式规范红线：
   - 全文严禁使用任何 Emoji。
   - 避免使用非必要的“xx与yy”句式。
   - 保证学术严肃性与推导规范。
3. 输出路径：必须写入到 `D:/Users/LeNotFound/Desktop/新建文件夹/408/output/数据结构/{tag_name}.md`。
4. 完成后请使用 send_message 向我汇报文件路径与完成情况。
"""
    return prompt

if __name__ == "__main__":
    import sys
    tag = sys.argv[1] if len(sys.argv) > 1 else "复杂度分析"
    prompt = make_prompt(tag)
    with open(f"prompt_{tag}.txt", "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"Generated prompt for {tag}, length: {len(prompt)}")
