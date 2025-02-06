import pandas as pd
import os
from datetime import datetime

RESULTS_FILE = "data/results.csv"
MAX_ENTRIES = 5  # 최근 5개만 유지

def save_result(user_id, gender, mbti_type, scores):
    """사용자의 MBTI 검사 결과를 저장하는 함수 (최대 5개 유지)"""
    test_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_entry = pd.DataFrame([[user_id, gender, test_date, mbti_type, *scores]], 
                              columns=["user_id", "gender", "test_date", "mbti_type", "E/I", "S/N", "T/F", "J/P"])
    
    if os.path.exists(RESULTS_FILE):
        df = pd.read_csv(RESULTS_FILE)
    else:
        df = pd.DataFrame(columns=["user_id", "gender", "test_date", "mbti_type", "E/I", "S/N", "T/F", "J/P"])
    
    # 같은 user_id의 기존 데이터 삭제 후 추가
    df = df[df["user_id"] != user_id]
    df = pd.concat([df, new_entry], ignore_index=True)
    
    # 최근 5개만 유지
    df = df.sort_values(by=["test_date"], ascending=False).groupby("user_id").head(MAX_ENTRIES)
    
    df.to_csv(RESULTS_FILE, index=False, encoding="utf-8-sig")

def load_results():
    """저장된 검사 결과 불러오기"""
    if os.path.exists(RESULTS_FILE):
        return pd.read_csv(RESULTS_FILE)
    return pd.DataFrame(columns=["user_id", "gender", "test_date", "mbti_type", "E/I", "S/N", "T/F", "J/P"])
