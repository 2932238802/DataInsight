import io
import matplotlib.pyplot as plt

def ConvertPltToBytes(fig, format: str = 'png', dpi: int = 300) -> bytes:
    
    """
    将 Matplotlib 图表转换为字节数据
    参数:
        fig (plt.Figure): 图表对象
        format (str): 图片格式 (png/jpg/pdf等)
        dpi (int): 输出分辨率
    返回:
        bytes: 二进制数据
    """
    buf = io.BytesIO()
    try:
        fig.savefig(buf, format=format, dpi=dpi, bbox_inches='tight')
        buf.seek(0) 
        return buf.getvalue()
    finally:
        buf.close() 
        plt.close(fig) 
