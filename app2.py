import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

#Firebase 중복 초기화 방지
if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("성진의 메모장")

with st.form("input_form", clear_on_submit=True):
    task = st.text_input("할일을 적으세요")
    sub = st.form_submit_button("추가")

if sub and task:
    db.collection("todos").add({"content": task, "at": firestore.SERVER_TIMESTAMP})  #  병행 제어 기법
    st.success(f"'{task}' 추가됨!")



# 1. 입력 폼 만들기

with st.form("diary_input"):
    content = st.text_input("오늘의 일기")
    submit = st.form_submit_button("기록하기")

    if submit and content:
        db.collection("diary").add({"text": content, "date": "2024-05-20"})
        st.success("저장 완료!"); st.rerun()


# 2. 목록 출력 및 삭제

docs = db.collection("diary").stream()
for doc in docs:
    col1, col2 = st.columns([8,2])
    col1.info(doc.to_dict()["text"])
    if col2.button("삭제", key=doc.id):
        db.collection("diary").document(doc.id).delete()
        st.rerun()
