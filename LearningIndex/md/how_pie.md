
### 如何绘制饼状图

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['axes.unicode_minus'] = False  
excel_file_path = 'sales_summary.xlsx'

try:
    df = pd.read_excel(excel_file_path, sheet_name='Sheet1') 

    labels = df['类别']
    sizes = df['销售额']

    fig, ax = plt.subplots(figsize=(8, 8)) 
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',  
        shadow=True,        
        startangle=90       
    )
    ax.axis('equal')
    ax.set_title("各类别销售额占比")
    plt.show()
except FileNotFoundError:
    print(f"错误: 文件 '{excel_file_path}' 未找到。请检查路径。")
except KeyError as e:
    print(f"错误: Excel 工作表中未找到列: {e}。请检查你的列名。")
    print("根据示例，期望的列名是 '类别' 和 '销售额'。")
    if 'df' in locals(): 
        print(f"当前Excel文件中的列有: {df.columns.tolist()}")
except Exception as e:
    print(f"发生意外错误: {e}")

```