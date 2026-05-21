import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="자취요리",
    page_icon="🍳",
)

#css 추가
st.markdown("""
<style>

div.stButton > button {
    background-color: transparent;
    border: none;
    text-align: left;
    padding: 0;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

#csv 파일 읽기
df = pd.read_csv("recipes.csv")

# 상세페이지 상태 저장
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None

# 상세페이지 함수
def show_recipe_detail(recipe):

    st.title(f"🍳 {recipe['name']}")

    st.image(
        f"images/{recipe['image']}",
        width=400
    )

    st.write("## 📌 재료")
    st.write(recipe["ingredients"])

    st.write("## 🍽️ 카테고리")
    st.write(recipe["category"])

    st.write("## ⏰ 조리시간")
    st.write(f"{recipe['cooking_time']}분")

    st.write("## 👨‍🍳 조리 방법")
    st.write(recipe["method"])

    st.write("")

    # 뒤로가기 버튼
    if st.button("⬅ 뒤로가기"):

        st.session_state.selected_recipe = None
        st.rerun()

# 상세페이지 상태 확인
if st.session_state.selected_recipe is not None:

    # 상세페이지 출력
    show_recipe_detail(
        st.session_state.selected_recipe
    )

#메인페이지
else:
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

    #검생착 + 버튼
    ingredient = st.text_input(
        "",
        placeholder="재료를 입력하세요 (예: 계란, 밥, 김치)"
    )

    # 검색 버튼 클릭 시
    # 검색어 입력 시
    if ingredient != "":

        st.write("")

        # 사용자 입력 재료 분리
        user_ingredients = set(
            item.strip()
            for item in ingredient.split(",")
        )

        results = []

        # CSV 반복
        for i, row in df.iterrows():

            # 레시피 재료 분리
            recipe_ingredients = set(
                item.strip()
                for item in row["ingredients"].split(",")
            )

            # 교집합 계산
            intersection = (
                user_ingredients &
                recipe_ingredients
            )

            # 합집합 계산
            union = (
                user_ingredients |
                recipe_ingredients
            )

            # 유사도 계산
            similarity = (
                len(intersection) /
                len(union)
            )

            # 유사도 0 이상 저장
            if similarity > 0:

                results.append(
                    (similarity, row)
                )

        # 유사도 높은 순 정렬
        results.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        # 결과 출력
        if results:

            st.subheader("🍳 추천 레시피")

            for similarity, row in results:

                st.markdown("---")

                img_col, text_col = st.columns([1,3])

                # 이미지
                with img_col:

                    st.image(
                        f"images/{row['image']}",
                        width=180
                    )

                # 텍스트
                with text_col:

                    # 레시피 클릭
                    if st.button(
                        row["name"],
                        key=f"recipe_{row['id']}",
                        use_container_width=True
                    ):

                        st.session_state.selected_recipe = row
                        st.rerun()

                    st.write(
                        f"재료 : {row['ingredients']}"
                    )

                    # 유사도 표시
                    st.write(
                        f"유사도 : {similarity:.2f}"
                    )

        else:

            st.warning(
                "추천 가능한 레시피가 없습니다 "
            )

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