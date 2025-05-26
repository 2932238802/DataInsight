from LinearRegression.LinearRegressionAnalysis import LinearRegressionAnalysis
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
from common import pltconfig


# 侧边栏个性化 线性回归 分析参数
def RenderLinearRegression(numerical_cols):
    
    #     st.selectbox(
    #     label,          # 下拉菜单的标签（字符串）
    #     options,        # 选项列表（必须是可迭代对象）
    #     index=0,        # 默认选中的选项索引（从0开始）
    #     format_func=str,# 格式化选项显示的函数
    #     key=None,       # 组件的唯一标识符
    #     help=None,      # 鼠标悬停时的帮助文本
    #     on_change=None, # 值改变时的回调函数
    #     args=None,      # 回调函数的参数
    #     kwargs=None,    # 回调函数的关键字参数
    #     disabled=False  # 是否禁用下拉菜单
    # )
    
    df = st.session_state.df
    for row_index_label in df.index:
        for col_name in df.columns:
            value = df.loc[row_index_label, col_name]
            reason = "无"
            is_empty = False
            if pd.isna(value):
                is_empty = True
                reason = "NaN/None"
            elif isinstance(value, str) and value.strip() == "":
                is_empty = True
                reason = "空或纯空格字符串"
            if is_empty:
                row_num = df.index.get_loc(row_index_label) + 1
                col_num = df.columns.get_loc(col_name) + 1
                st.error(
                    f"该表格存在空缺位置!\n"
                    f"位置: 行 '{row_index_label}' (第 {row_num} 行), "
                    f"列 '{col_name}' (第 {col_num} 列)。\n"
                    f"原因: {reason} (原始值: '{value}')"
                )
                return False
            
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.lrX = st.selectbox(
            "选择自变量X:", 
            numerical_cols, 
            index=0, 
            key="X_select"
            )
        
    with col2:
        st.session_state.lry = st.selectbox(
            "选择因变量y:", 
            numerical_cols, 
            index=1 if len(numerical_cols)>1 else 0, 
            key="y_select")
    
    
    # 选择高度和宽度
    lrcol_width,lrcol_height = st.columns(2)
    
    with lrcol_width:
        st.session_state.lrcol_width = st.selectbox(
            "选择图像宽度(10 较为合适英寸)",
            pltconfig.PLTWIDTH,
            index = 5 if len(pltconfig.PLTWIDTH) > 5 else len(pltconfig.PLTWIDTH) - 1,
            key = "lrwidth",
            help = "绘制图案的宽"
            )
        
    with lrcol_height:
        st.session_state.lrcol_height = st.selectbox(
            "选择图像高度(6 较为合适英寸)",
            pltconfig.PLTHEIGHT,
            index = 2 if len(pltconfig.PLTWIDTH) > 2 else len(pltconfig.PLTWIDTH) - 1,
            key = "lrheight",
            help = "绘制图案的高"
            )
        
    # 配置散点图的颜色 和 透明度
    lrcol_scatter_color,lrcol_scatter_alpha = st.columns(2)
    
    with lrcol_scatter_color:
        st.session_state.lrcol_scatter_color = st.selectbox(
                "选择散点图的颜色",
                pltconfig.COLOR,
                index = 0,
                key = "lrsct_color",
                help = "绘制图案的颜色"
                )
    
    # def slider(
    # label: str,
    # min_value: None = None,
    # max_value: None = None,
    # value: None = None,
    # step: int | None = None,
    # format: str | None = None,
    # key: Key | None = None,
    # help: str | None = None,
    # on_change: WidgetCallback | None = None,
    # args: WidgetArgs | None = None,
    # kwargs: WidgetKwargs | None = None,

    with lrcol_scatter_alpha:
        st.session_state.lrcol_scatter_alpha = st.slider(
            label="透明度([0,1])",
            min_value = 0.0,
            max_value = 1.0,
            value = 0.5,
            step = 0.05,
            key = "lrsct_alpha",
            help = "散点图的透明度"
        )
    
    
    lrcol_grid_is,lrcol_grid_alpha = st.columns(2)
    
    # radio(
    # label: str,
    # options: OptionSequence[T@radio],
    # index: int = 0,
    # format_func: (Any) -> Any = str,
    # key: Key | None = None,
    # help: str | None = None,
    # on_change: WidgetCallback | None = None,
    # args: WidgetArgs | None = None,
    # kwargs: WidgetKwargs | None = None,
    # *,
    # disabled: bool = False,
    # horizontal: bool = False,
    # captions: Sequence[str] | None = None,
    # label_visibility: LabelVisibility = "visible"
    
    with lrcol_grid_is:
        grid_is = st.radio(
            "是否需要网格线",
            ["是","否"],
            index = 0,
            key = "lrgrid_is"
        )
        if grid_is == "是":
            st.session_state.lrcol_grid_is = True
        else:
            st.session_state.lrcol_grid_is = False
        
    with lrcol_grid_alpha:
        st.session_state.lrcol_grid_alpha = st.slider(
            "网格线透明度([0,1])",
            min_value = 0.0,
            max_value = 1.0,
            value = 0.5,
            step = 0.05,
            key = "lrgrid_alpha"
        )
        
    lrcol_plt_color,lrcol_plt_kind = st.columns(2)
    # radio(
    # label: str,
    # options: OptionSequence[T@radio],
    # index: int = 0,
    # format_func: (Any) -> Any = str,
    # key: Key | None = None,
    # help: str | None = None,
    # on_change: WidgetCallback | None = None,
    # args: WidgetArgs | None = None,
    # kwargs: WidgetKwargs | None = None,
    # *,
    # disabled: bool = False,
    # horizontal: bool = False,
    # captions: Sequence[str] | None = None,
    # label_visibility: LabelVisibility = "visible"
    
    # 线的种类
    with lrcol_plt_kind:
        plt_kind = st.selectbox(
                "选择直线的种类",
                list(pltconfig.PLTKIND.keys()),
                index = 0,
                key = "lrplt_kind",
                help = "直线的种类"
                )
        st.session_state.lrcol_plt_kind = pltconfig.PLTKIND[plt_kind]

    with lrcol_plt_color:
        st.session_state.lrcol_plt_color = st.selectbox(
                "选择直线的颜色",
                pltconfig.COLOR,
                index = 0,
                key = "lrplt_color",
                help = "直线的颜色"
                )
    prediction_col1, prediction_col2 = st.columns(2)
    with prediction_col1:
            lr_input_for_predict = st.number_input(
                label=" 🦎 请输入你的预测区间 ",
                step=0.01,
                format="%.2f", 
                key = "lrpredict_val_input"
            )
            if lr_input_for_predict != 0.00:
                st.session_state.lr_userinput_for_predict = lr_input_for_predict
                
    with prediction_col2 :
        lr_userinput_for_format = st.number_input(
            label=" 🦆 请输入需要的精确位数",
            max_value=6,
            min_value=0,
            key = "lruserinput_for_format"
        )
        st.session_state.lr_userinput_for_format = lr_userinput_for_format
    
    analysis_is_ok:bool = False
    if st.button("🚀 开始分析", key="run_analysis"):
        PerformRegressionAnalysis()
    
    if st.button(" 🐚 预测 Y 值", key="predict_button"):
        PerformRegressionAnalysis()
        PerformRegressionAnalysisPredict()

# 主程序 ！！！
def PerformRegressionAnalysis()->bool:
    
    # 获取状态区
    # X_col 自变量的名字
    # y_col 因变量的名字
    df = st.session_state.df
    X_col = st.session_state.lrX
    y_col = st.session_state.lry
    width = st.session_state.lrcol_width
    height = st.session_state.lrcol_height
    sct_color = st.session_state.lrcol_scatter_color
    sct_alpha = st.session_state.lrcol_scatter_alpha
    plt_color = st.session_state.lrcol_plt_color
    plt_kind = st.session_state.lrcol_plt_kind
    grid_is:bool = st.session_state.lrcol_grid_is
    grid_alpha:float =  st.session_state.lrcol_grid_alpha
    
    if not LinearRegressionAnalysis.ValidateColumns(df, X_col, y_col):
        st.error("❌ 无效的列选择")
        return False
    
    try:
        X, y = LinearRegressionAnalysis.PrepareData(df, X_col, y_col)
        if len(X) < 2:
            raise ValueError("有效数据不足")
        
        
        model = LinearRegressionAnalysis.TrainModel(X, y)
        fig = LinearRegressionAnalysis.PlotResults(
            X = X,
            y = y,
            model = model, 
            X_col = X_col, 
            y_col = y_col,
            width = width,
            height =height,
            sct_color=sct_color,
            sct_alpha=sct_alpha,
            plt_color=plt_color,
            plt_linekind=plt_kind,
            grid_is= grid_is,
            grid_alpha= grid_alpha,
            predict_X = None
            )
        
        # if "lruser_input_for_predict" in st.session_state and st.session_state.lruser_input_for_predict is not None:
        #     st.session_state.regression_plot_predict = fig
        st.session_state.regression_plot = fig
        st.success("✅ 分析完成！")
        
        st.markdown("### 回归模型参数")
        st.write(f"**斜率 (Coef.):** {model.coef_[0]:.4f}")
        st.write(f"**截距 (Intercept):** {model.intercept_:.4f}")
        st.write(f"**决定系数 (R²):** {model.score(X, y):.4f}")
        
    except Exception as e:
        st.error(f"分析失败: {str(e)}")
        
    return True

def PerformRegressionAnalysisPredict():
    # 获取状态区
    # X_col 自变量的名字
    # y_col 因变量的名字
    df = st.session_state.df
    X_col = st.session_state.lrX
    y_col = st.session_state.lry
    width = st.session_state.lrcol_width
    height = st.session_state.lrcol_height
    sct_color = st.session_state.lrcol_scatter_color
    sct_alpha = st.session_state.lrcol_scatter_alpha
    plt_color = st.session_state.lrcol_plt_color
    plt_kind = st.session_state.lrcol_plt_kind
    grid_is:bool = st.session_state.lrcol_grid_is
    grid_alpha:float =  st.session_state.lrcol_grid_alpha
    
    if not LinearRegressionAnalysis.ValidateColumns(df, X_col, y_col):
        st.error("❌ 无效的列选择")
    
    try:
        X, y = LinearRegressionAnalysis.PrepareData(df, X_col, y_col)
        if len(X) < 2:
            raise ValueError("有效数据不足")
        
        predict_X_for_plot = None
        user_input_val = None
        if "lr_userinput_for_predict" in st.session_state and st.session_state.lr_userinput_for_predict is not None:
            user_input_val = st.session_state.lr_userinput_for_predict
            predict_X_for_plot = np.array([[user_input_val]]).astype(np.float64)
        else:
            predict_X_for_plot = None
        
        model = LinearRegressionAnalysis.TrainModel(X, y)
        fig = LinearRegressionAnalysis.PlotResults(
            X = X,
            y = y,
            model = model, 
            X_col = X_col, 
            y_col = y_col,
            width = width,
            height =height,
            sct_color=sct_color,
            sct_alpha=sct_alpha,
            plt_color=plt_color,
            plt_linekind=plt_kind,
            grid_is= grid_is,
            grid_alpha= grid_alpha,
            predict_X = predict_X_for_plot
            )
        
        st.session_state.regression_plot_predict = fig
        lr_decimal_places = st.session_state.lr_userinput_for_format
        predicted_y_value = None
        if predict_X_for_plot is not None:
            predicted_y_array = model.predict(predict_X_for_plot)
            predicted_y_value = predicted_y_array[0]
        
        st.success("✅ 预测分析完成！")
        st.success("🧬 预测结果:")
        st.write()
        if predicted_y_value is not None and user_input_val is not None:
            try:
                decimal_places = int(lr_decimal_places)
                if decimal_places < 0: decimal_places = 0 
                st.markdown(f"**对于输入值 {user_input_val}，预测的 Y 结果是 {predicted_y_value:.{decimal_places}f}**")
            
            except ValueError:
                st.warning(f"小数位数设置 ('{lr_decimal_places}') 无效，将使用默认格式显示预测结果")
                st.markdown(f"**对于输入值 {user_input_val}，预测的 Y 结果是 {predicted_y_value}**") 
       
        elif user_input_val is not None:
            st.markdown(f"**对于输入值 {user_input_val}，未能生成预测结果 请检查模型或输入 **")
        else:
            st.markdown("**没有提供用于预测的输入值**")
    except Exception as e:
        st.error(f"分析失败: {str(e)}")