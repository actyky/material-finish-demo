import streamlit as st
import fitz

st.title("실내재료마감표 자동검토 프로그램")

st.write("품질관리팀 PDF 자동검토 프로그램")

pdf_file = st.file_uploader(
    "실내재료마감표 PDF를 업로드하세요.",
    type=["pdf"]
)

if pdf_file:
    st.success("PDF 파일이 업로드되었습니다.")
    st.write("파일명 :", pdf_file.name)

    pdf_bytes = pdf_file.read()

    doc = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    st.write("PDF 페이지 수 :", len(doc))