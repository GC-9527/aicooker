import json

# 读取 Jupyter Notebook 文件
notebook_path = r'D:\develop\Pythonai\Langchain\Langchain.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 查找并修改包含 checkpoint.db 的单元格
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for i, line in enumerate(cell['source']):
            if './resources/checkpoint.db' in line:
                # 替换路径
                cell['source'][i] = line.replace('./resources/checkpoint.db', 'D:/develop/Pythonai/resources/checkpoint.db')
                print(f"已修改第 {i+1} 行:")
                print(f"  原路径: ./resources/checkpoint.db")
                print(f"  新路径: D:/develop/Pythonai/resources/checkpoint.db")

# 保存修改后的文件
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("\n✓ 文件修改完成")
