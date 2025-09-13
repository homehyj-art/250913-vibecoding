import streamlit as st
import pandas as pd
import altair as alt

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 MBTI 유형별 국가 Top 10 비율")
st.write("업로드된 데이터를 기반으로 각 MBTI 유형에서 비율이 가장 높은 국가 상위 10개를 시각화합니다.")

# MBTI 유형 선택
mbti_types = df.columns[1:]  # 첫 번째는 Country, 나머지는 MBTI
selected_type = st.selectbox("분석할 MBTI 유형을 선택하세요:", mbti_types)

# Top 10 추출
top10 = df.nlargest(10, selected_type)[["Country", selected_type]].sort_values(by=selected_type, ascending=True)

# Altair 차트
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_type, title=f"{selected_type} 비율"),
        y=alt.Y("Country", sort="-x", title="국가"),
        tooltip=["Country", selected_type]
    )
    .properties(
        width=700,
        height=400,
        title=f"{selected_type} 비율이 높은 국가 Top 10"
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
