# 关于项目与开源部署指南

> 本项目基于分布式 Agent 架构与真题知识图谱重构而成，旨在为计算机考研学生提供高质量、细粒度的备考参考。

---

## 一、 开源仓库与在线部署

* **项目名称**：`fuck408`
* **开源仓库**：`https://github.com/LeNotFound/fuck408`
* **上线域名**：`https://fuck408.pages.dev`（基于 Cloudflare Pages 免费全球 CDN 托管）

---

## 二、 本地运行指南

本机已具备完整 Python 环境与 MkDocs 支持，可在项目根目录下执行：

### 1. 本地启动热重载开发服务器
```bash
mkdocs serve
```
启动后在浏览器访问：`http://127.0.0.1:8000/`，即可实时预览全站，支持编辑内容时浏览器自动无缝热刷新。

### 2. 编译生成纯静态网站
```bash
mkdocs build
```
执行后会在根目录生成 `site/` 纯静态文件夹，可直接脱离任何服务器环境，在本地无网离线浏览，或直接作为静态资源发布。

---

## 三、 Cloudflare Pages 零配置一键上线（fuck408.pages.dev）

借助 Cloudflare Pages，只需 1 分钟即可将本站免费上线为全球高可用站点：

### 方法 A：通过 GitHub 仓库自动集成（推荐）
1. 在 GitHub 创建空仓库 `fuck408`；
2. 在项目根目录执行 Git 提交并推送：
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit of fuck408 knowledge base"
   git branch -M main
   git remote add origin https://github.com/LeNotFound/fuck408.git
   git push -u origin main
   ```
3. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)，进入 **Workers & Pages** -> **Create application** -> **Pages** -> **Connect to Git**；
4. 选择 `fuck408` 仓库，并在构建配置中填写：
   * **Framework preset**：`MkDocs`
   * **Build command**：`pip install mkdocs-material && mkdocs build`
   * **Build output directory**：`site`
5. 点击 **Save and Deploy**，Cloudflare 将在数十秒内完成编译并分配 `fuck408.pages.dev` 域名。

### 方法 B：通过 Wrangler CLI 命令行直接上传
如果在本地已安装 `wrangler`，无需 Git 即可直接推送构建成果：
```bash
mkdocs build
npx wrangler pages deploy site --project-name=fuck408
```

---

## 四、 贡献与交流

欢迎提交 PR 或 Issue 增补最新真题解析、勘误与优化解题口诀。
