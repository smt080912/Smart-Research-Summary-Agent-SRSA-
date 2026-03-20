import streamlit as st
from content_agent import ContentAgent

st.title("Smart Research & Summary Agent")

# 输入你的OpenAI API Key
api_key = st.text_input("输入你的OpenAI API Key:", type="password")

query = st.text_input("输入主题/关键词:")

if st.button("生成摘要"):
    if api_key == "" or query == "":
        st.warning("请填写API Key和主题！")
    else:
        agent = ContentAgent(api_key=api_key)
        with st.spinner("正在抓取资料并生成摘要..."):
            result = agent.generate_summary_from_query(query)
        st.markdown("### 摘要结果")
        st.write(result)

        # 提供导出Word按钮
        from docx import Document
        doc = Document()
        doc.add_heading(query, 0)
        doc.add_paragraph(result)
        doc_name = f"{query}_summary.docx"
        doc.save(doc_name)
        st.success(f"摘要已生成并保存为 {doc_name}")