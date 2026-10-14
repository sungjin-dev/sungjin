import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

#Firebase 중복 초기화 방지
if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
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
        st.rerun()   # redirect / render_template 같은 느낌이지만 리셋 갱신만 함.  st.switch_page() 다른 페이지 이동

# 새로고침 시 데이터 유지


if "login" not in st.session_state: 
    st.session_state["login"] = False

if st.session_state["login"]:
    st.title("나만의 다이어리")
    if st.button("로그아웃"): st.session_state["login"] = False; st.rerun()

else:
    tab1, tab2 = st.tabs(["로그인", "회원가입"])

    with tab1:
        l_id = st.text_input("아이디", key="l_id")
        l_pw = st.text_input("비번", type="password", key="l_pw")

        if st.button("로그인"):
            u = db.collection("users").document(l_id).get()
            if u.exists and u.to_dict()["password"] == l_pw:
                st.session_state["login"] = True; st.rerun()
    with tab2:
        n_id = st.text_input("새 아이디", key="n_id")
        n_pw = st.text_input("새 비번", type="password", key="n_pw")
        n_pn = st.text_input("새 전화번호", type="Phonenumber" key="n_pn")
        n_mail = st.text_input("새 이메일", type="Email" key="n_mail")

        if st.button("가입하기"):

            db.collection("users").document(n_id).set({"password": n_pw,
                                                       "Phonenumber": n_pn,
                                                       "Email": n_mail})
            st.success("회원가입 완료!")
    


