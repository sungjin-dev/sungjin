import streamlit as st
import pandas as pd

st.title("나의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

col1, col2 = st.columns(2)
with col1:
    st.success("왼쪽 영역")
with col2:
    st.success("오른쪽 영역")

st.text_input("좋아하는 음식은?")


if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름")
    if st.form_submit_button("등록") and name :
        st.session_state.user_list.append(name)

st.button("클릭")

tasks = [
    "1. API 스펙 문서 작성",
    "2. 프론트엔드 컴포넌트 개발",
    "3. 배포 파이프라인(CI/CD) 구축",
]    

st.subheader("TO-DO-LIST")

for task in tasks:
    
    with st.container(border=True):
        st.write(task)

data = {
    '연도':[ 2016,	2017,	2018,	2019,	2020,	2021,	2022,	2023,	2024,	2025,	2026],
    '인구': [51218, 51362,	51585,	51765,	51836,	51770,	51673,	51713,	51751,	51685,	51609]
}


df = pd.DataFrame(data)

df = df.set_index('연도')

st.line_chart(df)
