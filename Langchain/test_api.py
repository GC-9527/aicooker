import requests
import json

# LangGraph API 地址
base_url = "http://127.0.0.1:2024"

print("=" * 60)
print("测试 LangGraph API")
print("=" * 60)

# 1. 测试 API 健康状态
try:
    response = requests.get(f"{base_url}/ok")
    print(f"\n✓ API 健康检查: {response.status_code}")
    print(f"  响应: {response.text}")
except Exception as e:
    print(f"\n✗ API 健康检查失败: {e}")

# 2. 列出可用的 graphs
try:
    response = requests.get(f"{base_url}/graphs")
    print(f"\n✓ 可用 Graphs:")
    graphs = response.json()
    for graph_id, graph_info in graphs.items():
        print(f"  - {graph_id}: {graph_info}")
except Exception as e:
    print(f"\n✗ 获取 Graphs 失败: {e}")

# 3. 测试 chief_agent
try:
    payload = {
        "input": {
            "messages": [
                {"role": "user", "content": "你好"}
            ]
        },
        "config": {
            "configurable": {
                "thread_id": "test_thread_1"
            }
        },
        "assistant_id": "chief_agent"  # 添加 assistant_id
    }
    
    print(f"\n✓ 测试 chief_agent...")
    response = requests.post(
        f"{base_url}/runs/stream",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 200:
        print(f"  状态码: {response.status_code}")
        print(f"  响应成功！")
        # 打印部分响应内容
        print(f"  响应预览: {response.text[:200]}...")
    else:
        print(f"  状态码: {response.status_code}")
        print(f"  错误: {response.text}")
        
except Exception as e:
    print(f"\n✗ 测试 chief_agent 失败: {e}")

print("\n" + "=" * 60)
