import streamlit as st

st.title("")

if "user_dict" not in st.session_state:
    st.session_state.user_dict = {}

with st.form("input_form"):                  # 약간 트랜잭션 느낌. form 태그 처럼 해당 폼 안에 입력값들이 한번에 커밋
    name = st.text_input("이름")  
    password = st.text_input("비밀번호")                                         # type="password" *** 이런식으로 뜨게 됨. 
    submitted = st.form_submit_button("등록")
    if submitted and name and password:                                         # .strip() 을 쓰면 공백
        st.session_state.user_dict[name] = password 


col1, col2 = st.columns(3)    
with col1:
    if st.session_state.get("user_dict") :
        st.success("로그인이 성공하였습니다") 
with col2:
    st.code(
        """#include <stdio.h>

int main() 
{
    int a[] = {11, 22, 33, 44, 55, 66};
    int b = 6;
    int c = 0;

    while (c < b) 
    {
        int d = (c + 2) - ((c + 2) / b * b);
        printf("%d ", *(a + d));
        c++;
    }

    return 0;
}
""")
    with st.form("input_form"):
        answer = st.text_input("정답")
        submitted = st.form_submit_button("제출하기")
    if submitted :
        if answer == "33 44 55 66 11 22":
         st.success("성공")

tasks = [
  "1.로그인 계정 firebase 서버 DB에 저장하기",
  "2. 추가 문제 업로드 하기",
  "3. 인터페이스 직관성 높이기"
]

st.subheader("금일 할일 목록")

for task in tasks:
  # border=True를 주면 각 반복 요소가 단정한 상자로 감싸짐

  with st.container(border=true):

    st.write(task)

