import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="자취요리",
    page_icon="🍳",
)

# CSS
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

# CSV 파일 읽기
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

    # 난이도 표시
    time = recipe["cooking_time"]

    if time <= 5:
        st.write("난이도 : 🔥")

    elif time <= 10:
        st.write("난이도 : 🔥🔥")

    elif time <= 20:
        st.write("난이도 : 🔥🔥🔥")

    else:
        st.write("난이도 : 🔥🔥🔥🔥")

    st.write("## 👨‍🍳 조리 방법")
    st.write(recipe["method"])

# 상세페이지 상태 확인
if st.session_state.selected_recipe is not None:

    show_recipe_detail(
        st.session_state.selected_recipe
    )

# =========================
# 메인페이지
# =========================
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

    # 검색창
    ingredient = st.text_input(
        "",
        placeholder="재료를 입력하세요 (예: 계란, 밥, 김치)"
    )

    # 검색 기능
    if ingredient != "":

        st.write("")

        # 사용자 입력 재료 분리
        user_ingredients = [
            item.strip()
            for item in ingredient.split(",")
        ]

        results = []

        # CSV 반복
        for i, row in df.iterrows():

            # 레시피 재료 분리
            recipe_ingredients = [
                item.strip()
                for item in row["ingredients"].split(",")
            ]

            # 공통 재료 개수
            match_count = 0

            for user_item in user_ingredients:

                if user_item in recipe_ingredients:
                    match_count += 1

            # 하나라도 포함되면 저장
            if match_count > 0:

                results.append(
                    (match_count, row)
                )

        # 공통 재료 많은 순 정렬
        results.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        # 결과 출력
        if results:

            st.subheader("🍳 추천 레시피")

            for match_count, row in results:

                st.markdown("---")

                img_col, text_col = st.columns([1, 3])

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

                    st.write(
                        f"공통 재료 : {match_count}개"
                    )

        else:

            st.warning(
                "추천 가능한 레시피가 없습니다"
            )

    st.write("")
    st.write("")

    # 추천 레시피 TOP 3
    st.subheader("추천 레시피 TOP 3")

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
    st.subheader("빠른 추천")

    col4, col5, col6 = st.columns(3)

    # 전자레인지 요리
    with col4:

        if st.button("전자레인지 요리"):

            st.subheader("전자레인지 요리")

            microwave_list = [
                "전자레인지계란찜",
                "전자레인지떡볶이",
                "오트밀죽",
                "오트밀바나나죽",
                "치즈밥",
                "컵라면계란찜"
            ]

            filtered = df[
                df["name"].isin(microwave_list)
            ]

            for i, row in filtered.iterrows():

                st.image(
                    f"images/{row['image']}",
                    width=150
                )

                st.write(row["name"])
                st.write(f"{row['cooking_time']}분")

                st.markdown("---")

    # 5분 요리
    with col5:

        if st.button("5분 요리"):

            st.subheader("5분 요리")

            fast_list = [
                "간장계란밥",
                "계란부추볶음",
                "스크램블에그",
                "오트밀죽",
                "오트밀바나나죽"
            ]

            filtered = df[
                df["name"].isin(fast_list)
            ]

            for i, row in filtered.iterrows():

                st.image(
                    f"images/{row['image']}",
                    width=150
                )

                st.write(row["name"])
                st.write(f"{row['cooking_time']}분")

                st.markdown("---")

    # 자취생 야식
    with col6:

        if st.button("자취생 야식"):

            st.subheader("자취생 야식")

            night_list = [
                "치즈라면",
                "짜파게티",
                "떡볶이",
                "만두",
                "김피탕"
            ]

            filtered = df[
                df["name"].isin(night_list)
            ]

            for i, row in filtered.iterrows():

                st.image(
                    f"images/{row['image']}",
                    width=150
                )

                st.write(row["name"])
                st.write(f"{row['cooking_time']}분")

                st.markdown("---")

    # =========================
    # 💬 실시간 채팅
    # =========================

    st.subheader("💬 실시간 채팅")

    # 채팅 저장
    if "chat_messages" not in st.session_state:

        st.session_state.chat_messages = [
            "🙂 : 계란으로 뭐 만들 수 있나요?",
            "🍳 : 간장계란밥 추천!",
            "🔥 : 김치볶음밥도 맛있어요"
        ]

    # 채팅 박스
    with st.container(border=True):

        # 기존 채팅 출력
        for msg in st.session_state.chat_messages:

            st.write(msg)

        st.write("")

        # 입력창 + 버튼
        input_col, button_col = st.columns([5, 1])

        with input_col:

            user_chat = st.text_input(
                "",
                placeholder="채팅 입력...",
                label_visibility="collapsed"
            )

        with button_col:

            send = st.button("올리기")

        # 버튼 클릭
        if send:

            if user_chat.strip() != "":

                # 사용자 채팅 추가
                st.session_state.chat_messages.append(
                    f"🧑 : {user_chat}"
                )

                # 자동 응답
                bot_reply = None

                if "계란" in user_chat:
                    bot_reply = "🍳 : 간장계란밥 추천!"

                elif "김치" in user_chat:
                    bot_reply = "🔥 : 김치볶음밥 추천!"

                elif "야식" in user_chat:
                    bot_reply = "🌙 : 라면 + 만두 조합 ㄱㄱ"

                elif "밥" in user_chat:
                    bot_reply = "🍚 : 김치볶음밥 어때요?"

                elif "면" in user_chat:
                    bot_reply = "🍜 : 라면이나 비빔면 추천!"

                # 응답 추가
                if bot_reply:

                    st.session_state.chat_messages.append(
                        bot_reply
                    )

                st.rerun()

# =========================
# 공통 뒤로가기 버튼
# =========================

if st.session_state.selected_recipe is not None:

    st.write("")
    st.write("")

    if st.button("⬅ 메인으로 돌아가기"):

        st.session_state.selected_recipe = None
        st.rerun()