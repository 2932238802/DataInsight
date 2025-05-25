
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# 设置字体
try:
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    print(f"设置中文字体失败，可能需要手动安装或配置字体: {e}")


# 真正的线性分析
class LinearRegressionAnalysis:
    """线性回归分析功能模块"""
    
    @staticmethod
    def ValidateColumns(df, x_col, y_col) -> bool:
        return (
            # x y 在里面
            # x和y 不同
            # 然后都不是空的
            x_col in df.columns 
            and y_col in df.columns 
            and x_col != y_col 
            and not df[[x_col, y_col]].empty
        )

    @staticmethod
    def PrepareData(df,x_col, y_col) -> tuple:
        
        # astype 强制转换数据类型为 float64，确保数值精度
        X = df[[x_col]].values.astype(np.float64)
        y = df[y_col].values.astype(np.float64)
        
        # ~ 逻辑非运算符
        # np.isnan()：检查数组中的每个元素是否为 NaN（Not a Number），返回布尔数组
        # axis=0：表示列方向（垂直方向）
        # axis=1：表示行方向（水平方向）
        valid_data = (~np.isnan(X).any(axis=1)) & (~np.isnan(y))
        return X[valid_data], y[valid_data]

    @staticmethod
    def TrainModel(X, y) -> LinearRegression:
        # 返回模型
        model = LinearRegression()
        model.fit(X, y)
        st.session_state.lrtrained_model = model
        return model

    @staticmethod
    def PlotResults(
            X,
            y,
            model, 
            X_col, 
            y_col,
            width,
            height,
            sct_color,
            sct_alpha,
            plt_color,
            plt_linekind,
            grid_is:bool,
            grid_alpha:float,
            predict_X = None,
            ):
        # fig 外观 图表的外观，如大小、保存
        # ax 坐标 数据图形，配置标题、轴标签
        fig, ax = plt.subplots(figsize=(width, height))
        all_x_for_plot = X
        all_y_for_plot = y
        if predict_X is not None :
            all_x_for_plot = np.concatenate((X,predict_X),axis=0)
            
            
            # 散点图
            # 散点图的颜色
            # 散点图的透明度
        ax.scatter(
                X, 
                y, 
                color=f'{sct_color}', 
                alpha=sct_alpha, 
                label=f'观测数据 (n={len(X)})'
                )
            
            # 线型图
            # X 是横坐标
            # y 是模型预测值
        ax.plot(
                    all_x_for_plot, 
                    model.predict(all_x_for_plot),
                    color=plt_color,
                    linestyle = plt_linekind, 
                    lw=2.5,
                    label = f'回归线: $Y = {model.coef_[0]:.2f}X + {model.intercept_:.2f}$\n$R^2 = {model.score(X, y):.3f}$'
                    )
            
        ax.set_xlabel(X_col, fontsize=12)
            
        ax.set_ylabel(y_col, fontsize=12)
            
        ax.set_title(
                f"{y_col}/{X_col} 回归分析", 
                pad=20, 
                fontsize=14, 
                fontweight='bold'
                )
            
            # 图例位置：左上角
            # frameon  图例边框
            # fontsize 字体
            # facecolor 背景颜色
            # ncol 
        ax.legend(
                loc=0, 
                frameon=True
                )
            
            # alpha 透明度
            # 网格线
            # TODO: 是否需要网格线
        ax.grid(
                visible=grid_is, 
                alpha=grid_alpha
                )
            
            # plt.tight_layout() 是一个用于自动调整子图参数的函数
            # 它会优化图形的布局
            # 确保子图（subplots）、标题、坐标轴标签等元素之间有足够的间距，避免内容重叠
        plt.tight_layout()
            
        return fig
                
            
        
        
        
        
        

