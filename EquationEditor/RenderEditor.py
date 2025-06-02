import streamlit as st
import numpy as np
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.utilities.lambdify import lambdify

if 'current_expression' not in st.session_state:
    st.session_state.current_expression = ""

st.title("表达式形成器")

def AppendToExpression(char):
    """
    增加
    
    Args:
        char (_type_): 增加对应的字符
    """
    if st.session_state.current_expression is None:
        st.warning("Warning: current_expression was None")
        st.session_state.current_expression = ""
    st.session_state.current_expression += str(char)

def ClearExpression():
    """
    清空
    """
    st.session_state.current_expression = ""

def BackspaceExpression():
    """
    回退
    """
    # 删除最有一个字符
    st.session_state.current_expression = st.session_state.current_expression[:-1]

def YieldExpression():
    """
    生成表达式
    """
    if 'current_expression' in st.session_state and st.session_state.current_expression != None:
        expression_str = st.session_state.current_expression
        x_sym = symbols('x')
        transformations = standard_transformations + (implicit_multiplication_application,)
        try:
            parsed_expr = parse_expr(expression_str, transformations=transformations, local_dict={'x': x_sym, 'pi': np.pi, 'E': np.e})
            func = lambdify(x_sym, parsed_expr, modules=['numpy'])
            st.session_state.equation = func
            st.success("内部函数生成完成!")
        except Exception as e:
            st.error(f"表达式生成失败: {e}")
            st.session_state.equation = None

# 构建表达式
def RenderEditor():
    """
        实现输入表达式的功能
    """
    st.markdown("#### 构建表达式:")
    col1, col2, col3, col4 = st.columns(4)
    st.text_area("当前表达式:", value=st.session_state.current_expression, height=80, disabled=True, key="expr_display_key")
    with col1:
        st.button("7", on_click=AppendToExpression, args=("7",), use_container_width=True)
        st.button("4", on_click=AppendToExpression, args=("4",), use_container_width=True)
        st.button("1", on_click=AppendToExpression, args=("1",), use_container_width=True)
        st.button("0", on_click=AppendToExpression, args=("0",), use_container_width=True)
    with col2:
        st.button("8", on_click=AppendToExpression, args=("8",), use_container_width=True)
        st.button("5", on_click=AppendToExpression, args=("5",), use_container_width=True)
        st.button("2", on_click=AppendToExpression, args=("2",), use_container_width=True)
        st.button(".", on_click=AppendToExpression, args=(".",), use_container_width=True)
    with col3:
        st.button("9", on_click=AppendToExpression, args=("9",), use_container_width=True)
        st.button("6", on_click=AppendToExpression, args=("6",), use_container_width=True)
        st.button("3", on_click=AppendToExpression, args=("3",), use_container_width=True)
        st.button("x", on_click=AppendToExpression, args=("x",), use_container_width=True)
    with col4:
        st.button("← Del", on_click=BackspaceExpression, use_container_width=True)
        st.button("➕", on_click=AppendToExpression, args=("+",), use_container_width=True)
        st.button("➖", on_click=AppendToExpression, args=("-",), use_container_width=True)
        st.button("✖", on_click=AppendToExpression, args=("*",), use_container_width=True)

    col_func1, col_func2, col_func3, col_func4 = st.columns(4)
    with col_func1:
        st.button("sin()", on_click=AppendToExpression, args=("sin(",), use_container_width=True) 
        st.button("exp()", on_click=AppendToExpression, args=("exp(",), use_container_width=True)
        st.button("(", on_click=AppendToExpression, args=("(",), use_container_width=True)
        st.button("/", on_click=AppendToExpression, args=("/",), use_container_width=True)

    with col_func2:
        st.button("cos()", on_click=AppendToExpression, args=("cos(",), use_container_width=True)
        st.button("log()", on_click=AppendToExpression, args=("log(",), use_container_width=True) 
        st.button(")", on_click=AppendToExpression, args=(")",), use_container_width=True)
        st.button("**", on_click=AppendToExpression, args=("**",), use_container_width=True) 

    with col_func3:
        st.button("tan()", on_click=AppendToExpression, args=("tan(",), use_container_width=True)
        st.button("sqrt()", on_click=AppendToExpression, args=("sqrt(",), use_container_width=True)
        st.button("pi", on_click=AppendToExpression, args=("pi",), use_container_width=True)
        st.button("E", on_click=AppendToExpression, args=("E",), use_container_width=True) 

    with col_func4:
        st.button("abs()", on_click=AppendToExpression, args=("abs(",), use_container_width=True)
        st.button("log10()", on_click=AppendToExpression, args=("log10(",), use_container_width=True)
        
        st.button("Clear All", on_click=ClearExpression, use_container_width=True, type="primary")

    st.button(
        "生成表达式",
        key = "yield_expression",
        help = "根据表达式的合法性生成表示的表示",
        on_click= YieldExpression,
        use_container_width=True
    )
    
    st.markdown("---")