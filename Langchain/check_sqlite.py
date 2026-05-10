import sqlite3
import os

# 数据库路径
db_path = r'D:\develop\Pythonai\Langchain\resources\checkpoint.db'

print("=" * 60)
print("SQLite 数据库连接检测")
print("=" * 60)

# 检查文件是否存在
if os.path.exists(db_path):
    print(f"✓ 数据库文件存在: {db_path}")
    print(f"  文件大小: {os.path.getsize(db_path)} bytes")
else:
    print(f"✗ 数据库文件不存在: {db_path}")
    exit(1)

try:
    # 尝试连接数据库
    conn = sqlite3.connect(db_path, check_same_thread=False)
    print("✓ 数据库连接成功")
    
    # 获取游标
    cursor = conn.cursor()
    
    # 查询所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if tables:
        print(f"\n✓ 找到 {len(tables)} 个表:")
        for table in tables:
            table_name = table[0]
            print(f"  - {table_name}")
            
            # 查询每个表的结构
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            print(f"    列信息:")
            for col in columns:
                print(f"      {col[1]} ({col[2]}) {'NOT NULL' if col[3] else ''} {'PRIMARY KEY' if col[5] else ''}")
            
            # 查询行数
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            print(f"    行数: {row_count}")
    else:
        print("\n✗ 数据库中没有表（可能需要调用 checkpointer.setup()）")
    
    # 关闭连接
    conn.close()
    print("\n✓ 数据库连接已关闭")
    
except sqlite3.Error as e:
    print(f"\n✗ 数据库错误: {e}")
except Exception as e:
    print(f"\n✗ 未知错误: {e}")

print("=" * 60)
