import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("OpenAI API 테스트 도구")

# 사용자 입력
user_query = st.text_area("메시지를 입력하세요:", height=100, value="안녕, 너는 누구니? 모델명을 알려줄 수 있어?")
max_tokens = st.slider("최대 토큰 수:", min_value=50, max_value=500, value=200, step=50)
repeat_count = st.slider("반복 횟수:", min_value=1, max_value=50, value=1, step=1)

if st.button("테스트"):
    if user_query:
        for i in range(repeat_count):
            try:
                # OpenAI API 호출
                chat_completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_query}
                    ],
                    max_tokens=max_tokens
                )
                
                # 결과 표시
                st.subheader(f"AI 응답 (반복 {i+1}/{repeat_count}):")
                st.write(chat_completion.choices[0].message.content)
                
                # 반복 사이에 잠시 대기 (API 호출 제한을 고려)
                if i < repeat_count - 1:
                    time.sleep(1)
                    st.markdown("---")  # 구분선 추가
            except Exception as e:
                st.error(f"오류 발생 (반복 {i+1}/{repeat_count}): {str(e)}")
    else:
        st.warning("메시지를 입력해주세요.")

st.sidebar.markdown("### 사용 방법")
st.sidebar.markdown("1. 메시지를 입력하세요.")
st.sidebar.markdown("2. 최대 토큰 수를 조정하세요.")
st.sidebar.markdown("3. 반복 횟수를 선택하세요 (1-40).")
st.sidebar.markdown("4. '테스트' 버튼을 클릭하세요.")

