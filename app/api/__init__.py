from openai import OpenAI

client = OpenAI(
    api_key = "sk-NjRSZOI3hmr1sr76pvyIHxYUppOwygDUNtMCivAaKhuEzBUq",
    base_url = "https://api.fe8.cn/v1"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "你是谁，用中文回答",
        }
    ],
    model="minimax-m2.1",
)
print(chat_completion.choices[0].message.content)
