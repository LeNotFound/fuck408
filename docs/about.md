# 关于项目与开源部署指南

> 本项目基于分布式 Agent 架构与真题知识图谱重构而成，采用现代前端 VitePress 驱动，旨在为计算机考研学生提供高质量、细粒度的备考参考。

---

## 一、 开源仓库与在线部署

* **项目名称**：`fuck408`
* **开源仓库**：`https://github.com/LeNotFound/fuck408`
* **上线域名**：`https://fuck408.pages.dev`（基于 Cloudflare Pages 免费全球 CDN 托管）
* **底层驱动**：VitePress 1.x（Vite + Vue 3 + Shiki + MathJax 3 矢量渲染）

---

## 二、 本地运行指南

本机已具备 Node.js 运行时与 pnpm 支持，可在项目根目录下执行：

### 1. 本地启动极速热重载开发服务器
```bash
pnpm run docs:dev
```
启动后在浏览器访问：`http://localhost:5173/`，即可实时预览全站，支持编辑内容时浏览器毫秒级无缝热更新。

### 2. 编译生成纯静态网站
```bash
pnpm run docs:build
```
执行后会在 `docs/.vitepress/dist/` 目录生成高度优化的纯静态网站文件，可直接脱离任何后端服务进行离线浏览或部署至任意静态托管平台。

### 3. 本地预览构建成果
```bash
pnpm run docs:preview
```

---

## 三、 Cloudflare Pages 持续集成配置

在 Cloudflare Pages 控制台中将本项目构建配置设定如下：

* **Framework preset（框架预设）**：`VitePress`
* **Build command（构建命令）**：`pnpm run docs:build`
* **Build output directory（构建输出目录）**：`docs/.vitepress/dist`

配置完成后，每次向 GitHub 仓库的 `main` 分支执行 `git push`，Cloudflare 全球边缘网络将全自动拉取代码并在数十秒内完成编译发布。

---

## 四、 贡献与交流

欢迎提交 PR 或 Issue 增补最新真题解析、勘误与优化解题口诀。
