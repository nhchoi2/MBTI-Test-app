import streamlit as st
import pandas as pd
from utils.data_handler import save_result

st.set_page_config(page_title="MBTI 테스트", page_icon="📝")

query_params = st.experimental_get_query_params()

if query_params.get("page") == ["test"]:
    st.title("📋 MBTI 테스트 진행")

# 질문 데이터 불러오기
df = pd.read_csv("data/mbti_questions.csv")

responses = {}

gender = st.radio("성별을 선택하세요:", ["Male", "Female", "Other"], key="gender")

user_id = st.text_input("사용자 ID를 입력하세요:", key="user_id")

st.subheader("📌 테스트 질문")
for index, row in df.iterrows():
    response = st.radio(row["question"], [row["option1"], row["option2"]], key=f"q{index}")
    responses[row["category"]] = responses.get(row["category"], 0) + (1 if response == row["option1"] else 0)

if st.button("📊 결과 제출"):
    if user_id.strip() == "":
        st.error("사용자 ID를 입력하세요!")
    else:
        scores = [responses.get("E/I", 0), responses.get("S/N", 0), responses.get("T/F", 0), responses.get("J/P", 0)]
        mbti_type = "".join([
            "E" if scores[0] >= 3 else "I",
            "S" if scores[1] >= 3 else "N",
            "T" if scores[2] >= 3 else "F",
            "J" if scores[3] >= 3 else "P"
        ])
        save_result(user_id, gender, mbti_type, scores)
        st.success(f"테스트 완료! 당신의 MBTI 유형은 {mbti_type} 입니다.")
        st.switch_page("results_visualization")
