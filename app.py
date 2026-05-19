import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="자취요리",
    page_icon="🍳",
    layout="wide"
)

# 제목
st.markdown(
    """
    <h1 style='text-align: center;'>🍳 자취요리</h1>
    <h4 style='text-align: center; color: gray;'>
    자취생들을 초간단 요리 추천
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# 검색창
ingredient = st.text_input(
    "",
    placeholder="재료를 입력하세요 (예: 계란, 밥, 김치)"
)

# 추천 버튼
# 추천 버튼
if st.button("추천받기"):

    st.success(f"'{ingredient}' 재료 기반 추천 결과입니다!")

    st.subheader("🍳 추천 레시피")

    # 계란 입력 시
    if "계란" in ingredient:

        st.write("### 🍚 간장계란밥")
        st.write("- 재료: 계란, 밥, 간장")
        st.write("- 조리 시간: 5분")
        st.write("- 조리 방법")
        st.write("1. 계란을 굽는다")
        st.write("2. 밥 위에 올린다")
        st.write("3. 간장을 넣는다")

    # 김치 입력 시
    elif "김치" in ingredient:

        st.write("### 🌶 김치볶음밥")
        st.write("- 재료: 김치, 밥")
        st.write("- 조리 시간: 10분")

    # 만두 입력 시
    elif "만두" in ingredient:

        st.write("### 🥟 만두")
        st.write("- 재료: 냉동만두")
        st.write("- 조리 시간: 7분")

    # 아무것도 없을 때
    else:
        st.warning("추천 가능한 레시피가 없습니다 😢")

st.write("")
st.write("")

# BEST 레시피
st.subheader("🔥 BEST 레시피 TOP 3")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("간계밥.jpg", use_container_width=True)
    st.write("🍚 간장계란밥")
    st.write("⏰ 5분 완성")

with col2:
    st.image("김볶밥.jpg", use_container_width=True)
    st.write("🌶 김치볶음밥")
    st.write("⏰ 10분 완성")

with col3:
    st.image("만두밥.jpg", use_container_width=True)
    st.write("🥟 만두")
    st.write("⏰ 7분 완성")

st.write("")
st.write("")

# 빠른 추천
st.subheader("⚡ 빠른 추천")

col4, col5, col6 = st.columns(3)

with col4:
    st.button("전자레인지 요리")

with col5:
    st.button("5분 요리")

with col6:
    st.button("자취생 야식")

st.write("")
st.write("")

# 실시간 채팅 느낌
st.subheader("💬 실시간 채팅")

chat_box = st.container(border=True)

with chat_box:
    st.write("🙂 : 계란으로 뭐 만들 수 있나요?")
    st.write("🍳 : 간장계란밥 추천!")
    st.write("🔥 : 김치볶음밥도 맛있어요")
    st.write("🥟 : 냉동만두 에어프라이어 ㄱㄱ")