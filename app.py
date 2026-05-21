import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="자취요리",
    page_icon="🍳",
)

# 제목
st.markdown(
    """
    <h1 style='text-align: center;'>🍳 자취요리</h1>
    <h4 style='text-align: center; color: gray;'>
    자취생들을 위한 초간단 요리 추천
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# 검색창
df = pd.read_csv("recipes.csv")

col1, col2 = st.columns([5, 1])

with col1:
    ingredient = st.text_input(
        "",
        placeholder="재료를 입력하세요 (예: 계란, 밥, 김치)"
    )

with col2:
    search = st.button("검색")

# 검색 버튼 클릭 시
if search:

    st.write("")

    found = False

    # CSV 반복
    for i, row in df.iterrows():

        # 재료 검색
        if ingredient in row["ingredients"]:

            found = True

            st.markdown("---")

            # 카드 내부 가로 배치
            img_col, text_col = st.columns([1,3])

            # 왼쪽 이미지
            with img_col:

                st.image(
                    f"images/{row['image']}",
                    width=180
                )

            # 오른쪽 텍스트
            with text_col:

                st.subheader(row["name"])

                st.write(f"재료 : {row['ingredients']}")

    # 결과 없을 때
    if not found:

        st.warning("검색 결과가 없습니다 ")

st.write("")
st.write("")

# BEST 레시피
st.subheader(" 추천 레시피 TOP 3")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/egg_rice.jpg", use_container_width=True)
    st.write("간장계란밥")
    st.write("5분 완성")

with col2:
    st.image("images/kim.jpg", use_container_width=True)
    st.write("김치볶음밥")
    st.write("10분 완성")

with col3:
    st.image("images/mado.jpg", use_container_width=True)
    st.write("만두")
    st.write("7분 완성")

st.write("")
st.write("")

# 빠른 추천
st.subheader(" 빠른 추천")

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