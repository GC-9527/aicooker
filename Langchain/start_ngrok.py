from pyngrok import ngrok
import time
import webbrowser

# 设置 ngrok authtoken（可选，免费版有速率限制）
# ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN")

print("=" * 60)
print("启动 ngrok 隧道")
print("=" * 60)

# 关闭现有的隧道
ngrok.kill()

# 创建 HTTP 隧道，指向本地 LangGraph API
print("\n正在创建隧道...")
public_url = ngrok.connect(2024, "http")

print(f"\n✓ 隧道已创建！")
print(f"  本地地址: http://127.0.0.1:2024")
print(f"  公共地址: {public_url}")

# 构造 LangSmith Studio URL
studio_url = f"https://smith.langchain.com/studio/?baseUrl={public_url}"
print(f"\n  LangSmith Studio 地址:")
print(f"  {studio_url}")

print("\n" + "=" * 60)
print("请在浏览器中访问上面的 LangSmith Studio 地址")
print("按 Ctrl+C 停止隧道")
print("=" * 60)

try:
    # 保持脚本运行
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\n停止隧道...")
    ngrok.kill()
    print("✓ 隧道已关闭")
