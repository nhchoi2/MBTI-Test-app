import streamlit as st
import pandas as pd
from utils.data_handler import load_results

st.set_page_config(page_title="MBTI 성격 테스트", page_icon="🧠", layout="centered")

st.title("📊 MBTI 성격 테스트")

st.image("images/main.webp", use_container_width=True)

st.write("이 테스트는 MBTI 이론을 기반으로 당신의 성격 유형을 분석하는 검사입니다.")
st.write("왼쪽 메뉴에서 테스트를 시작하세요.")

st.sidebar.image("images/sidebar.webp", use_container_width=True)
st.sidebar.success("테스트를 시작하려면 아래 버튼을 눌러주세요.")

# 최근 검사 결과 불러오기
df = load_results()

if not df.empty:
    st.subheader("📌 최근 검사 결과")
    latest_result = df.iloc[-1]
    user_id = latest_result["user_id"]
    mbti_type = latest_result["mbti_type"]
    
    st.write(f"**사용자 ID:** {user_id}")
    st.write(f"**MBTI 유형:** {mbti_type}")
    
    if st.button("📊 결과 분석 보기"):
        st.query_params["page"] = "results_visualization"
else:
    st.info("아직 검사를 진행한 기록이 없습니다. 테스트를 시작해보세요!")

