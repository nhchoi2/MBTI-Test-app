import pandas as pd

def analyze_scores(scores):
    """
    MBTI 검사 결과를 분석하여 해석을 제공하는 함수
    :param scores: [E/I, S/N, T/F, J/P] 성향 점수 리스트
    :return: 성향 분석 결과 (문장 리스트)
    """
    analysis = []

    dimensions = ["외향(E) / 내향(I)", "감각(S) / 직관(N)", "사고(T) / 감정(F)", "판단(J) / 인식(P)"]
    descriptions = [
        ("당신은 **외향적(E)** 성향이 강합니다.", "당신은 **내향적(I)** 성향이 강합니다."),
        ("당신은 **현실적(S)** 사고를 선호합니다.", "당신은 **창의적(N)** 사고를 선호합니다."),
        ("당신은 **논리적(T)** 의사결정을 선호합니다.", "당신은 **감정적(F)** 의사결정을 선호합니다."),
        ("당신은 **계획적(J)** 성향이 강합니다.", "당신은 **즉흥적(P)** 성향이 강합니다.")
    ]

    for i, (dim, desc) in enumerate(zip(dimensions, descriptions)):
        ratio = scores[i] / sum(scores[i:])
        if ratio >= 0.5:
            analysis.append(f"✔ {dim}: {desc[0]}")
        else:
            analysis.append(f"✔ {dim}: {desc[1]}")

    return analysis
