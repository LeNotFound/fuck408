import os
import re

TAGS_METADATA = [
    {
        "id": "topic-01",
        "tag": "排序算法",
        "freq_10yr": 13,
        "freq_total": 24,
        "module": "排序",
        "summary": "八大内部排序算法体系、时空复杂度、稳定性定理、比较与移动次数、链式存储适配性"
    },
    {
        "id": "topic-02",
        "tag": "B树",
        "freq_10yr": 6,
        "freq_total": 10,
        "module": "树与二叉树 / 查找",
        "summary": "多路平衡查找树、阶数定义、树高与关键字容量上下界、插入上溢分裂与删除借键合并、B+树对比"
    },
    {
        "id": "topic-03",
        "tag": "哈夫曼树",
        "freq_10yr": 6,
        "freq_total": 9,
        "module": "树与二叉树",
        "summary": "最优二叉树定义、严格二叉树性质、WPL计算与非叶累加法、加权平均码长、变长前缀编码"
    },
    {
        "id": "topic-04",
        "tag": "散列表",
        "freq_10yr": 6,
        "freq_total": 9,
        "module": "查找",
        "summary": "散列函数构造、开放定址法与拉链法、一次与二次聚集、墓碑标记逻辑删除机制、ASL计算"
    },
    {
        "id": "topic-05",
        "tag": "链表",
        "freq_10yr": 6,
        "freq_total": 9,
        "module": "线性表",
        "summary": "单链表、双向链表、循环链表、快慢指针三大黄金应用、单链表原地逆置范式与综合大题"
    },
    {
        "id": "topic-06",
        "tag": "堆的概念",
        "freq_10yr": 5,
        "freq_total": 8,
        "module": "树与二叉树 / 排序",
        "summary": "完全二叉树顺序存储、大根堆与小根堆偏序性质、O(n)建堆级数证明、向上/向下筛选、Top-K应用"
    },
    {
        "id": "topic-07",
        "tag": "复杂度分析",
        "freq_10yr": 5,
        "freq_total": 9,
        "module": "绪论及基本概念",
        "summary": "渐近符号严格数学定义、循环步长设参换元、双重循环级数求和、主定理递归分析、时空权衡"
    },
    {
        "id": "topic-08",
        "tag": "特殊矩阵",
        "freq_10yr": 5,
        "freq_total": 5,
        "module": "数组与特殊矩阵",
        "summary": "对称矩阵与三角矩阵压缩映射、三对角带状矩阵下标公式、稀疏矩阵三元组顺序表与十字链表"
    },
    {
        "id": "topic-09",
        "tag": "二叉排序树",
        "freq_10yr": 4,
        "freq_total": 6,
        "module": "树与二叉树 / 查找",
        "summary": "BST定义与中序严格单调性定理、动态插入与删除不可逆性、ASL计算、顺序存储BST判别算法大题"
    },
    {
        "id": "topic-10",
        "tag": "二叉树的遍历",
        "freq_10yr": 4,
        "freq_total": 7,
        "module": "树与二叉树",
        "summary": "先序/中序/后序递归与栈实现、中序相邻性极值定理、双序列唯一重构定理、遍历序列重合充要条件"
    },
    {
        "id": "topic-11",
        "tag": "入栈出栈序列",
        "freq_10yr": 4,
        "freq_total": 9,
        "module": "栈、队列及数组",
        "summary": "栈LIFO代数约束、卡特兰数分治递推与反射原理证明、Knuth栈混洗312禁形判定、辅助栈状态机模拟"
    },
    {
        "id": "topic-12",
        "tag": "关键路径",
        "freq_10yr": 4,
        "freq_total": 6,
        "module": "图结构及应用",
        "summary": "AOE网与工程调度、四大时间参数(ve, vl, e, l)递推、活动时间余量极值、多关键路径协同压缩"
    },
    {
        "id": "topic-13",
        "tag": "拓扑排序",
        "freq_10yr": 4,
        "freq_total": 7,
        "module": "图结构及应用",
        "summary": "AOV网偏序线性延拓、Kahn入度消除算法与DFS逆后序、拓扑序列唯一性充要条件与判定算法大题"
    },
    {
        "id": "topic-14",
        "tag": "数组查找",
        "freq_10yr": 4,
        "freq_total": 6,
        "module": "查找",
        "summary": "顺序查找哨兵机制、折半查找判定树高度与比较次数推导、分块查找最优参数均值不等式证明"
    },
    {
        "id": "topic-15",
        "tag": "最小生成树",
        "freq_10yr": 4,
        "freq_total": 6,
        "module": "图结构及应用",
        "summary": "割定理剪切粘贴证明、Prim加点法与Kruskal并查集加边法、MST唯一性充分/充要条件、TTL跨科联动"
    },
    {
        "id": "topic-16",
        "tag": "顺序表",
        "freq_10yr": 4,
        "freq_total": 7,
        "module": "线性表",
        "summary": "随机存取寻址原理、动态数组扩容均摊O(1)势能分析、双指针相向对撞、后缀极值维护与算法大题"
    },
    {
        "id": "topic-17",
        "tag": "二叉树遍历",
        "freq_10yr": 3,
        "freq_total": 4,
        "module": "树与二叉树",
        "summary": "拓扑树形与遍历逆推、中序相邻祖先后代约束、二叉表达式树带括号中缀输出综合大题、线索二叉树"
    },
    {
        "id": "topic-18",
        "tag": "图的概念",
        "freq_10yr": 3,
        "freq_total": 6,
        "module": "图结构",
        "summary": "握手定理与度数方程、极大连通分量与极小连通子图、回路判定定理、必定连通的最小边数界限"
    },
    {
        "id": "topic-19",
        "tag": "外部排序",
        "freq_10yr": 3,
        "freq_total": 3,
        "module": "排序",
        "summary": "外存I/O读写代价模型、败者树选小优化比较、置换-选择排序工作区吞吐、严格k叉最佳归并树虚段推导"
    },
    {
        "id": "topic-20",
        "tag": "平均查找长度",
        "freq_10yr": 3,
        "freq_total": 5,
        "module": "查找",
        "summary": "ASL成功与失败形式化数学定义、散列表失败分母模数本质、墓碑探测机制、装填因子理论模型"
    },
    {
        "id": "topic-21",
        "tag": "归并排序",
        "freq_10yr": 3,
        "freq_total": 5,
        "module": "排序",
        "summary": "分治思想、Merge比较次数上下界严格推导、归并趟数与归并树形态、主定理O(n log n)证明与稳定性"
    },
    {
        "id": "topic-22",
        "tag": "插入排序",
        "freq_10yr": 3,
        "freq_total": 3,
        "module": "排序",
        "summary": "直接插入哨兵机制、比较与移动次数求和、折半插入与希尔排序增量序列、基本有序小规模最优适用"
    },
    {
        "id": "topic-23",
        "tag": "树的概念",
        "freq_10yr": 3,
        "freq_total": 6,
        "module": "树与二叉树",
        "summary": "树度数方程与边数恒等式、正则k叉树节点关系定理证明、树高上下界推导、森林向二叉树映射"
    },
    {
        "id": "topic-24",
        "tag": "邻接矩阵",
        "freq_10yr": 3,
        "freq_total": 6,
        "module": "图结构",
        "summary": "MGraph类型定义、无向图对称压缩、有向图行出列入、矩阵幂次图论路径意义、近四年3道大题"
    },
    {
        "id": "topic-25",
        "tag": "队列",
        "freq_10yr": 3,
        "freq_total": 6,
        "module": "栈、队列及数组",
        "summary": "循环队列假溢出与空满三大消歧方案、输入受限双端队列阻隔效应、多轨列车调度Dilworth定理与链式复用"
    }
]

def build_master_document():
    input_dir = "output/数据结构"
    master_path = "01_数据结构_近十年高频考点精讲.md"
    
    # Check if all files exist
    missing = []
    for meta in TAGS_METADATA:
        tag = meta["tag"]
        file_path = os.path.join(input_dir, f"{tag}.md")
        if not os.path.exists(file_path):
            missing.append(tag)
    if missing:
        print(f"Waiting for files to finish: {missing}")
        return False
    
    print("All 25 files exist. Building master document...")
    
    doc_lines = []
    
    # Document header
    doc_lines.append("# 408 计算机考研 · 数据结构近十年（2016~2025）高频考点精讲汇总\n")
    doc_lines.append("> **学科归属**：全国硕士研究生招生考试 · 408 计算机学科专业基础综合 · 数据结构  ")
    doc_lines.append("> **考查年代**：2016 年 ～ 2025 年（近十年统考真题全覆盖）  ")
    doc_lines.append("> **收录门槛**：近十年考查频次 $\\ge 3$ 次的全部核心考点（共计 25 个高频考点）  ")
    doc_lines.append("> **编写规范**：严格恪守学术严肃性，无任何口语化与 Emoji 图标，杜绝非必要并列句式；配备严谨的数学推导、算法分析、近十年真题无遗漏全解及大题设计模板。\n")
    doc_lines.append("---\n")
    
    # Global Navigation TOC Table
    doc_lines.append("## 全局高频考点导航目录（按近十年考频降序排列）\n")
    doc_lines.append("| 序号 | 考点名称 | 近十年考频 | 历年总频次 | 所属模块 | 核心考核维度 | 锚点直达 |")
    doc_lines.append("| :---: | :--- | :---: | :---: | :--- | :--- | :---: |")
    
    for idx, meta in enumerate(TAGS_METADATA, 1):
        tag = meta["tag"]
        tid = meta["id"]
        freq_10 = meta["freq_10yr"]
        freq_tot = meta["freq_total"]
        mod = meta["module"]
        summ = meta["summary"]
        doc_lines.append(f"| {idx:02d} | **{tag}** | **{freq_10} 次** | {freq_tot} 次 | {mod} | {summ} | [进入精讲](#{tid}) |")
    
    doc_lines.append("\n---\n")
    
    # Append content of each topic
    for idx, meta in enumerate(TAGS_METADATA, 1):
        tag = meta["tag"]
        tid = meta["id"]
        freq_10 = meta["freq_10yr"]
        mod = meta["module"]
        file_path = os.path.join(input_dir, f"{tag}.md")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        
        # Add Anchor and Section Header
        doc_lines.append(f'<div id="{tid}"></div>\n')
        doc_lines.append(f"# 【高频考点 {idx:02d}】{tag}（近十年考查 {freq_10} 次 · {mod}）\n")
        doc_lines.append(f"[返回全局导航目录](#全局高频考点导航目录按近十年考频降序排列)\n")
        doc_lines.append(content)
        doc_lines.append("\n\n---\n")
    
    full_text = "\n".join(doc_lines)
    
    # Emoji validation
    emojis = re.findall(r'[\U00010000-\U0010ffff]', full_text)
    if emojis:
        print(f"Warning: Found {len(emojis)} emojis: {set(emojis)}")
    else:
        print("Emoji check passed: 0 emojis found.")
    
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    file_size_mb = os.path.getsize(master_path) / (1024 * 1024)
    line_count = len(full_text.splitlines())
    word_count = len(full_text)
    print(f"Master file successfully created at: {os.path.abspath(master_path)}")
    print(f"File size: {file_size_mb:.2f} MB ({os.path.getsize(master_path)} bytes)")
    print(f"Total lines: {line_count}, Total characters: {word_count}")
    return True

if __name__ == "__main__":
    build_master_document()
