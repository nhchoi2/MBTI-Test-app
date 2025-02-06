import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_handler import load_results
from utils.results_analysis import analyze_scores

st.set_page_config(page_title="검사 결과 시각화", page_icon="📊")

st.title("📊 MBTI 검사 결과 시각화")

# 데이터 불러오기
df = load_results()

if df.empty:
    st.warning("아직 저장된 검사 결과가 없습니다. 먼저 테스트를 진행하세요.")
else:
    st.subheader("📌 최근 검사 결과")
    
    # 최신 검사 결과 가져오기
    latest_result = df.iloc[-1]
    user_id = latest_result["user_id"]
    mbti_type = latest_result["mbti_type"]
    scores = [latest_result["E/I"], latest_result["S/N"], latest_result["T/F"], latest_result["J/P"]]
    
    st.write(f"**사용자 ID:** {user_id}")
    st.write(f"**MBTI 유형:** {mbti_type}")

    # 점수 기반 성향 해석
    analysis = analyze_scores(scores)
    
    st.subheader("📌 성향 분석 결과")
    for line in analysis:
        st.write(line)
    
    # MBTI 유형 분포 시각화
    st.subheader("📊 MBTI 유형 분포")
    mbti_counts = df["mbti_type"].value_counts()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(mbti_counts, labels=mbti_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)
    
    # 성향 점수 시각화
    st.subheader("📊 성향 점수 비교")
    
    fig2, ax2 = plt.subplots()
    ax2.bar(["E/I", "S/N", "T/F", "J/P"], scores, color=['blue', 'green', 'red', 'purple'])
    ax2.set_ylabel("점수")
    ax2.set_title("각 성향 점수 비교")
    st.pyplot(fig2)
    
    # 전체 데이터 표시
    st.subheader("📋 저장된 검사 결과")
    st.dataframe(df)
