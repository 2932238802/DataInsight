
### st 如何读取md 文件?

```python
import streamlit as st

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

markdown_text = read_markdown_file("README.md")
st.markdown(markdown_text, unsafe_allow_html=True)  
```