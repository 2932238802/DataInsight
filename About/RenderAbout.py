import streamlit as st

def RenderAbout():
    if "df" in st.session_state and st.session_state.df is None:
       st.info(
        f"""
        ## 🐈 欢迎来到 DataInsight 🐈

        **DataInsight** 🦣 致力于成为您在数学建模与数据可视化领域的得力助手
        我们提供强大的在线 Pyplot 图表生成功能，让复杂数据变得直观易懂 🦣

        通过我们的平台，您可以：
        *  🦤 快速将模型结果转化为精美图表
        *  🦤 轻松定制图表样式，满足个性化需求

        ** 🧝 DataInsight 采用会员订阅制 **
        # TODO:(version 2.0)

        ---

        #### 🥹 客户支持：
        遇到任何问题或有任何建议，请随时通过以下方式联系我们(虽然可能联系不到我们):
        *  📞 **联系电话**: 1234567890
        *  📮 **支持邮箱**: 1234567890@163.com

        *感谢您的信任与选择！*

        ---
        © 2025.5 LosAgelous(2932238802)工作室
        
        ---
        [项目源码](https://github.com/2932238802/DataInsight.git)
        """
    )