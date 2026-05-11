import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


# ==================================================
# 自动注册本地中文字体
# ==================================================
def register_chinese_font():
    """
    优先使用本地中文字体，找不到则使用 ReportLab 内置 STSong-Light。
    """
    font_candidates = [
        # Windows
        r"C:\Windows\Fonts\msyh.ttc",        # 微软雅黑
        r"C:\Windows\Fonts\msyh.ttf",
        r"C:\Windows\Fonts\simsun.ttc",      # 宋体
        r"C:\Windows\Fonts\simhei.ttf",      # 黑体

        # macOS
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/Library/Fonts/Songti.ttc",

        # Linux 常见字体
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/arphic/uming.ttc",
    ]

    for font_path in font_candidates:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont("ResumeFont", font_path, subfontIndex=0))
                print(f"已使用本地字体：{font_path}")
                return "ResumeFont"
            except Exception:
                try:
                    pdfmetrics.registerFont(TTFont("ResumeFont", font_path))
                    print(f"已使用本地字体：{font_path}")
                    return "ResumeFont"
                except Exception:
                    continue

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    print("未找到本地中文字体，已使用 ReportLab 内置字体：STSong-Light")
    return "STSong-Light"


FONT_NAME = register_chinese_font()


# ==================================================
# PDF 基础配置
# ==================================================
output_file = "郭超-AI应用开发工程师实习生-简历.pdf"

doc = SimpleDocTemplate(
    output_file,
    pagesize=A4,
    rightMargin=16 * mm,
    leftMargin=16 * mm,
    topMargin=12 * mm,
    bottomMargin=12 * mm
)

styles = getSampleStyleSheet()


# ==================================================
# 样式配置
# ==================================================
styles.add(ParagraphStyle(
    name="Name",
    fontName=FONT_NAME,
    fontSize=22,
    leading=26,
    alignment=1,
    spaceAfter=4
))

styles.add(ParagraphStyle(
    name="Target",
    fontName=FONT_NAME,
    fontSize=11,
    leading=15,
    alignment=1,
    spaceAfter=4
))

styles.add(ParagraphStyle(
    name="Info",
    fontName=FONT_NAME,
    fontSize=8.7,
    leading=12.5,
    alignment=1,
    textColor=colors.black,
    spaceAfter=6
))

styles.add(ParagraphStyle(
    name="SectionTitle",
    fontName=FONT_NAME,
    fontSize=12,
    leading=15,
    spaceBefore=5,
    spaceAfter=3,
    textColor=colors.black
))

styles.add(ParagraphStyle(
    name="NormalCN",
    fontName=FONT_NAME,
    fontSize=9,
    leading=12.8,
    spaceAfter=2,
    wordWrap="CJK"
))

styles.add(ParagraphStyle(
    name="SmallCN",
    fontName=FONT_NAME,
    fontSize=8.3,
    leading=11.6,
    textColor=colors.black,
    spaceAfter=2,
    wordWrap="CJK"
))

styles.add(ParagraphStyle(
    name="ProjectTitle",
    fontName=FONT_NAME,
    fontSize=9.7,
    leading=13,
    spaceAfter=1,
    wordWrap="CJK"
))

styles.add(ParagraphStyle(
    name="BulletCN",
    fontName=FONT_NAME,
    fontSize=8.55,
    leading=12,
    leftIndent=9,
    firstLineIndent=-9,
    spaceAfter=1.2,
    wordWrap="CJK"
))


story = []


# ==================================================
# 工具函数
# ==================================================
def section(title):
    story.append(Paragraph(title, styles["SectionTitle"]))
    story.append(HRFlowable(
        width="100%",
        thickness=0.8,
        color=colors.black,
        spaceBefore=0,
        spaceAfter=4
    ))


def bullet(text):
    story.append(Paragraph("• " + text, styles["BulletCN"]))


def project_header(name, tag="个人项目"):
    table = Table(
        [[
            Paragraph(name, styles["ProjectTitle"]),
            Paragraph(tag, styles["SmallCN"])
        ]],
        colWidths=[130 * mm, 38 * mm]
    )

    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    story.append(table)


# ==================================================
# 头部信息
# ==================================================
story.append(Paragraph("郭超", styles["Name"]))
story.append(Paragraph("求职意向：AI 应用开发工程师实习生", styles["Target"]))

story.append(Paragraph(
    "手机：19967860060 ｜ 邮箱：2041332483@qq.com ｜ GitHub：https://github.com/GC-9527<br/>"
    "现居：长沙 ｜ 期望城市：长沙 ｜ 到岗时间：随时 ｜ 实习周期：3个月以上 ｜ 每周到岗：4-5天<br/>"
    "可长期实习，稳定性强",
    styles["Info"]
))


# ==================================================
# 教育背景
# ==================================================
section("教育背景")

edu_table = Table(
    [[
        Paragraph("湖南工商大学 ｜ 本科 ｜ 大数据与人工智能", styles["NormalCN"]),
        Paragraph("2023.09 - 2026.06", styles["SmallCN"])
    ]],
    colWidths=[125 * mm, 43 * mm]
)

edu_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))

story.append(edu_table)
story.append(Paragraph(
    "核心方向：人工智能、Python 开发、Java 开发、RAG 知识库、大模型应用",
    styles["SmallCN"]
))


# ==================================================
# 专业技能
# ==================================================
section("专业技能")

bullet("编程语言：熟悉 Python、Java，具备基础软件开发与项目实现能力。")
bullet("AI 应用开发：熟悉大模型 API 调用、Prompt 设计、多轮对话、上下文管理。")
bullet("RAG 知识库：熟悉文档清洗、文本切分、Embedding、FAISS 向量检索、知识召回与问答生成流程。")
bullet("框架工具：熟悉 LangChain、FastAPI、Streamlit、Pandas、SQLite，了解 LangGraph、Pydantic。")
bullet("开发工具：熟悉 Git、GitHub、Cursor、Trae、Coze；了解 uni-app、Vue3、Android 打包。")


# ==================================================
# 项目经历
# ==================================================
section("项目经历")

project_header("AI 私厨助手")
story.append(Paragraph(
    "技术栈：FastAPI、LangChain、LangGraph、通义千问、Tavily Search、SQLite",
    styles["SmallCN"]
))
story.append(Paragraph(
    "项目地址：https://github.com/GC-9527/aicooker",
    styles["SmallCN"]
))
bullet("基于 FastAPI + LangChain + LangGraph 开发 AI 私厨助手，支持菜谱推荐、饮食建议、智能问答与联网搜索。")
bullet("负责大模型 API 接入、后端接口开发、联网搜索工具集成与历史对话存储。")
bullet("使用 SQLite 保存用户历史对话记录，提升连续问答体验。")

story.append(Spacer(1, 2))

project_header("学生手册智能问答系统")
story.append(Paragraph(
    "技术栈：Python、LangChain、RAG、FAISS、Embedding、通义千问",
    styles["SmallCN"]
))
story.append(Paragraph(
    "项目地址：https://github.com/GC-9527/student-handbook-qa-system",
    styles["SmallCN"]
))
bullet("基于学生手册构建 RAG 智能问答系统，支持校园规章、办事流程等内容问答。")
bullet("负责文档清洗、文本切分、Embedding 向量化、FAISS 向量索引构建。")
bullet("通过 LangChain 完成知识检索、上下文拼接、Prompt 构建与大模型问答生成。")

story.append(Spacer(1, 2))

project_header("健身助手 App")
story.append(Paragraph(
    "技术栈：uni-app、Vue3、Vite、uCharts、Android",
    styles["SmallCN"]
))
story.append(Paragraph(
    "项目地址：https://github.com/GC-9527/fitness-helper",
    styles["SmallCN"]
))
bullet("从 0 到 1 开发跨平台健身助手 App，实现动作库、训练记录、智能建议、成就系统和数据分析功能。")
bullet("使用 uni-app Storage API 实现本地数据存储，使用 uCharts 实现训练数据可视化。")
bullet("完成 Android APK 打包和真机测试，项目包含 13 个页面、102 个动作、10 个成就项。")


# ==================================================
# 其他项目
# ==================================================
section("其他项目")

bullet("RAG 向量知识库实践项目：使用 LangChain、DashScopeEmbeddings、FAISS 跑通文本处理、向量化、相似度检索和大模型问答流程。项目地址：https://github.com/GC-9527/practical-rag")
bullet("电影信息爬虫机器人：使用 Python、Pandas、CSV 完成电影数据采集、清洗、保存与接口调试。")
bullet("AI 情感伴侣系统：基于 Streamlit + LangChain 开发 AI 对话应用，接入大模型实现情感化回复。")


# ==================================================
# 自我评价
# ==================================================
section("自我评价")

story.append(Paragraph(
    "大数据与人工智能专业本科生，熟悉 Python、LangChain、RAG、大模型 API 与基础后端开发，"
    "具备多个 AI 应用项目实践经验。学习能力强，执行力强，可长期稳定实习，"
    "希望在 AI 应用工程化方向持续提升。",
    styles["NormalCN"]
))


# ==================================================
# 生成 PDF
# ==================================================
doc.build(story)

print(f"PDF 已生成：{output_file}")
