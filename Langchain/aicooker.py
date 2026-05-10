#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dotenv import load_dotenv
# 使用绝对路径加载 .env 文件
env_path = r'D:\develop\Pythonai\Langchain\.env'
load_dotenv(env_path)
print("环境变量加载成功")


# In[ ]:


import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")

search_tool = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"),
                           base_url=os.getenv("TAVILY_BASE_URL"),
                           max_results=5,
                           timeout=30,
                           topic = "general")


model = init_chat_model(
    model="qwen3-max",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key,
    temperature=1.5,
    max_tokens=1024,
    top_p=0.9
)


# In[ ]:





# In[ ]:


from langchain_core.messages import SystemMessage
from langchain.agents import create_agent

# LangGraph API 会自动处理持久化，不需要手动设置 checkpointer
# from langgraph.checkpoint.memory import InMemorySaver
# import sqlite3
# from langgraph.checkpoint.sqlite import SqliteSaver

config = {"configurable": {"thread_id": "thread_3"}}
system_prompt = """
你是一名私人厨师。收到用户提供的食材照片或清单后，请按以下流程操作：
1.识别和评估食材：若用户提供照片，首先辨识所有可见食材。基于食材的外观状态，评估其新鲜度与可用量，整理出一份“当前可用食材清单”。
2.智能食谱检索：优先调用 web_search 工具，以“可用食材清单”为核心关键词，查找可行菜谱。
3.多维度评估与排序：从营养价值和制作难度两个维度对检索到的候选食谱进行量化打分，并根据得分排序，制作简单且营养丰富的排名靠前。
4.结构化方案输出：把排序后的食谱整理为一份结构清晰的建议报告，要包含食谱信息、得分、推荐理由、食谱的参考图片，帮助用户快速做出决策。

请严格按照流程，优先调用 web_search 工具搜索食谱，搜索不到的情况下才能自己发挥。
"""
agent = create_agent(
    model=model,
    tools=[search_tool],
    system_prompt=system_prompt,
    # LangGraph API 会自动处理持久化，不需要传入 checkpointer
    debug=False)


# 注意：以下执行代码已注释，仅在手动运行此脚本时使用
# 然后正常调用
# multimodal_message = agent.invoke(
#     {"messages": [HumanMessage(content=[{"type": "image",
#          "url": "https://img.freepik.com/free-photo/arrangement-different-foods-organized-fridge_23-2149099882.jpg"},
#         {"type": "text", "text": "帮我看看这些食材能做些什么？"}])]},
#     config,
# )

# response = agent.invoke({"messages": [multimodal_message]}, config)
# for message in response["messages"]:
#     if message.type == "ai":
#         message.pretty_print()

