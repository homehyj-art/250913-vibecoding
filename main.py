import streamlit as st
import random

st.set_page_config(page_title="MBTI 공부법 추천", page_icon="📚", layout="centered")

st.title("📚✨ MBTI 공부 방법 추천기 ✨📚")
st.write("👉 나의 MBTI 유형을 선택하면, 딱 맞는 공부 방법을 알려줄게요!")

# MBTI 유형 리스트
mbti_types = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 공부 방법 추천 딕셔너리
study_tips = {
    "ISTJ": "📒 계획표를 세우고 꼼꼼히 따라가는 게 좋아요!",
    "ISFJ": "🖊️ 친절하게 정리하며 노트 필기하는 게 효과적이에요.",
    "INFJ": "🌌 조용한 공간에서 깊이 몰입하며 공부하는 게 좋아요.",
    "INTJ": "🎯 목표를 정하고 전략적으로 공부하면 효율적이에요.",
    "ISTP": "🔧 문제를 직접 풀어보며 손으로 익히는 게 좋아요.",
    "ISFP": "🎨 색깔펜, 그림 등을 활용해 창의적으로 공부해 보세요.",
    "INFP": "📖 스토리처럼 내용을 연결지어 외우면 잘 기억돼요.",
    "INTP": "🧩 개념을 분석하고 비교하며 논리적으로 정리하세요.",
    "ESTP": "⚡ 짧게 집중하고 자주 반복하는 학습법이 잘 맞아요.",
    "ESFP": "🎶 음악이나 활동적인 방법을 곁들이면 흥미가 유지돼요.",
    "ENFP": "🌈 친구들과 토론하면서 배우면 효과적이에요.",
    "ENTP": "💡 여러 방법을 시도해 보고 가장 재밌는 방법을 선택하세요.",
    "ESTJ": "📊 규칙적이고 체계적으로 계획을 세워 공부하세요.",
    "ESFJ": "👥 스터디 그룹에서 함께 공부하는 게 잘 맞아요.",
    "ENFJ": "🤝 다른 사람을 가르쳐 주면서 배우면 기억에 오래 남아요.",
    "ENTJ": "🚀 큰 목표를 설정하고 단계별로 성취해 나가세요."
}

# 선택 박스
user_mbti = st.selectbox("당신의 MBTI는 무엇인가요? 🤔", [""] + mbti_types)

if user_mbti:
    st.success(f"✨ {user_mbti} 유형에게 딱 맞는 공부법 ✨")
    st.markdown(f"### {study_tips[user_mbti]}")
    
    # 랜덤 재미 요소
    effects = ["🎉", "🔥", "🌟", "💯", "💡", "🚀"]
    st.markdown(f"오늘의 행운 이모지: {random.choice(effects)}")

    # 풍선 효과
    st.balloons()
