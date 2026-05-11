import requests
import json

base_url = "http://127.0.0.1:2024"

print("=" * 60)
print("AI 私厨助手 - 完整测试")
print("=" * 60)

# 测试 1: 简单对话
print("\n【测试 1】简单对话测试")
print("-" * 60)

payload = {
    "input": {
        "messages": [
            {"role": "user", "content": "你好，请介绍一下你自己"}
        ]
    },
    "config": {
        "configurable": {
            "thread_id": "test_thread_1"
        }
    },
    "assistant_id": "chief_agent"
}

try:
    response = requests.post(
        f"{base_url}/runs/stream",
        json=payload,
        headers={"Content-Type": "application/json"},
        stream=True
    )
    
    if response.status_code == 200:
        print("✓ 请求成功！\n")
        print("AI 回复：")
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    data_str = line_str[6:]  # 去掉 'data: ' 前缀
                    if data_str != '[DONE]':
                        try:
                            data = json.loads(data_str)
                            if 'messages' in data:
                                for msg in data['messages']:
                                    if msg.get('type') == 'ai':
                                        print(msg.get('content', ''), end='', flush=True)
                        except:
                            pass
        print("\n")
    else:
        print(f"✗ 请求失败: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"✗ 错误: {e}")

print("\n" + "=" * 60)
print("测试完成！")
print("=" * 60)
