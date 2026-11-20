import json

with open('os_topics_data.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

def generate_prompt(topic):
    tag = topic['tag']
    module = topic['module']
    recent_count = topic['recent_count']
    total_count = topic['total_count']
    quizzes = topic['quizzes']
    output_path = f"D:/Users/LeNotFound/Desktop/新建文件夹/408/output/操作系统/{tag}.md"

    years_str = "、".join([f"{q['year']}#{q['qid']}" for q in quizzes])

    quiz_texts = []
    for i, q in enumerate(quizzes, 1):
        quiz_texts.append(f"""
---
### 真题 {i}：【{q['year']} 年 408 第 {q['qid']} 题】（{q['quiz_type']}）
原始题面及解析库内容：
{q['content']}
""")

    quizzes_joined = "\n".join(quiz_texts)

    prompt = f"""考点名称：{tag}
学科：操作系统
模块归属：{module}
近十年考查频次：{recent_count} 次（{years_str}）
历年总考查频次：{total_count} 次
输出文件路径：{output_path}

真题数据：
{quizzes_joined}

编写要求与规范：
1. 全文严禁使用任何Emoji。
2. 避免使用非必要的“xx与yy”句式，语言精炼、严谨、专业。
3. 公式使用标准LaTeX数学语法（$...$ 或 $$...$$）。
4. 严格按照以下五大模块结构编写：
   # 408 高频考点精讲：{tag}
   > **模块归属**：{module}  
   > **考点层级**：微观细分考点（近十年考查 $\ge 3$ 次）  
   > **适用对象**：408 计算机考研备考学生  
   ---
   ## 一、 考情档案
   - 近十年考查频次、历年总考查频次、出题形式（单项选择题 / 综合解答题等）
   - 命题特点分析（总结命题切入点与规律）
   - 近十年考查年份分布表格（ASCII文本表格，列出 2016~2025 各年份题号）
   ---
   ## 二、 具体考察内容
   - 核心概念与工作机制（精准定义、执行流程、状态转移等）
   - 核心定理推导与数学/算法模型（公式清晰，推导严谨）
   - 核心对比辨析（对比相关易混概念，条理清晰）
   ---
   ## 三、 近十年真题精讲（2016~2025）
   - 对所给的全部近十年真题进行逐题深度精讲：
     ### 【真题 X】<年份> 年 408 第 <题号> 题 · <考法主题>
     **题目**（题干完整内容，清晰排版选项 A, B, C, D）
     #### 【解析】（详尽剖析解题思路、核心推导步骤、干扰项逐项辨析与排除理由）
     **正确答案**：**<选项>**
   ---
   ## 四、 综合考法拓展
   - 综合大题应用与跨考点串联（若考查过大题，深入剖析评分标准与解题策略；若全为选择题，剖析常考综合形态与大题考查潜质）
   ---
   ## 五、 考点速记清单
   - 核心要点速记、计算公式汇总、避坑指南与解题口诀。
5. 完成后，使用 write_file 工具直接将整篇 Markdown 文档写入指定路径：{output_path}。写入成功后向调用方发送完成通知。
"""
    return prompt

if __name__ == '__main__':
    for t in topics[:3]:
        p = generate_prompt(t)
        print(f"Tag: {t['tag']}, Prompt len: {len(p)}")
