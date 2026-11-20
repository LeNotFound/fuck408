import subprocess
import os
import sys

workspace = r"D:\Users\LeNotFound\Desktop\新建文件夹\408"
css_url = "https://cdn.jsdelivr.net/npm/github-markdown-css/github-markdown.min.css"

def convert_md_to_pdf(md_filename):
    md_path = os.path.join(workspace, md_filename)
    if not os.path.exists(md_path):
        print(f"[跳过] 文件不存在: {md_filename}")
        return
    
    base_name = os.path.splitext(md_filename)[0]
    html_path = os.path.join(workspace, f"temp_{base_name}.html")
    pdf_path = os.path.join(workspace, f"{base_name}.pdf")
    
    print(f"\n正在转换: {md_filename} -> {base_name}.pdf")
    
    # 1. Pandoc Markdown -> Standalone HTML
    cmd_pandoc = [
        "pandoc", md_path,
        "-o", html_path,
        "--standalone",
        "--mathjax",
        "--metadata", f"title={base_name}",
        "-c", css_url
    ]
    res1 = subprocess.run(cmd_pandoc, capture_output=True, text=True)
    if res1.returncode != 0:
        print(f"Pandoc 转换失败: {res1.stderr}")
        return
    
    # 2. wkhtmltopdf HTML -> PDF with native Outlines
    cmd_pdf = [
        "wkhtmltopdf",
        "--outline",
        "--outline-depth", "3",
        "--header-right", "[page] / [topage]",
        "--header-font-size", "9",
        "--header-spacing", "5",
        "--footer-center", base_name,
        "--footer-font-size", "9",
        "--footer-spacing", "5",
        "--margin-top", "15mm",
        "--margin-bottom", "15mm",
        "--margin-left", "15mm",
        "--margin-right", "15mm",
        "--enable-local-file-access",
        html_path,
        pdf_path
    ]
    res2 = subprocess.run(cmd_pdf, capture_output=True, text=True)
    
    # 清理临时 HTML 文件
    if os.path.exists(html_path):
        os.remove(html_path)
        
    if res2.returncode == 0 and os.path.exists(pdf_path):
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"[成功] 生成 PDF: {base_name}.pdf ({size_mb:.2f} MB)")
    else:
        print(f"[失败] wkhtmltopdf 报错: {res2.stderr[:300]}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if target:
        convert_md_to_pdf(target)
    else:
        # 默认转换所有 4 门课精讲
        for i in [
            "01_数据结构_近十年高频考点精讲.md",
            "02_计算机组成原理_近十年高频考点精讲.md",
            "03_操作系统_近十年高频考点精讲.md",
            "04_计算机网络_近十年高频考点精讲.md"
        ]:
            if os.path.exists(os.path.join(workspace, i)):
                convert_md_to_pdf(i)
