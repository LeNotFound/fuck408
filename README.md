# Fuck408：408 计算机考研近十年高频微考点全景题库

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=flat&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Hosted on Cloudflare Pages](https://img.shields.io/badge/Cloudflare_Pages-F38020?style=flat&logo=CloudflarePages&logoColor=white)](https://pages.cloudflare.com/)

> 针对 2016~2025 年 408 全国统考真题中考查频次 $\ge 3$ 次的全部 **89 个高频核心大考点**，基于微观知识图谱重构的专题横向穿透题库。

---

## 📌 项目初衷

传统考频表仅给到章级别（如“树与二叉树 20 次”），过于笼统。本项目将 408 全科真题细化为 247 个原子考点，重点提炼近十年考过不少于 3 次的高频考点，解决“考哪种类型最多”、“每种类型考什么套路”的实际复习痛点。

---

## 📊 四门课程考点覆盖

* **01 数据结构**（25 个考点，涵盖排序算法、B树、散列表、哈夫曼树、堆、二叉排序树等）
* **02 计算机组成原理**（22 个考点，涵盖中断I/O、补码、IEEE 754浮点数、寻址方式、大小端、Cache等）
* **03 操作系统**（24 个考点，涵盖虚拟页式管理、调度算法、地址翻译、进程状态、系统调用、PV同步等）
* **04 计算机网络**（18 个考点，涵盖ARQ协议、OSI模型、子网划分、TCP四次挥手/三次握手、滑动窗口等）

---

## 🚀 本地快速启动

### 依赖环境
确保已安装 Python 3.8+ 及相关依赖：
```bash
pip install mkdocs-material jieba pymdown-extensions
```

### 启动本地热重载预览
```bash
mkdocs serve
```
浏览器打开 `http://127.0.0.1:8000/` 即可访问。

### 编译生成纯静态网站
```bash
mkdocs build
```
静态页面将输出至 `site/` 目录。

---

## 🌐 Cloudflare Pages 一键上线指南 (fuck408.pages.dev)

1. 将本项目推送到你的 GitHub 仓库（例如 `LeNotFound/fuck408`）；
2. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)，进入 **Workers & Pages** -> **Create application** -> **Pages** -> **Connect to Git**；
3. 选择 `fuck408` 仓库；
4. 配置构建命令：
   * **Framework preset**：`MkDocs`
   * **Build command**：`pip install mkdocs-material jieba pymdown-extensions && mkdocs build`
   * **Build output directory**：`site`
5. 点击 **Save and Deploy** 即可完成部署并绑定自定义域名。
