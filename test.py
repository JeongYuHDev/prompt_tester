import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime





# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("프롬프트 테스트 도구")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y년 %m월 %d일, %A. %H:%M")
    # 요일을 한국어로 변환
    weekdays = {
        'Monday': '월요일', 'Tuesday': '화요일', 'Wednesday': '수요일',
        'Thursday': '목요일', 'Friday': '금요일', 'Saturday': '토요일', 'Sunday': '일요일'
    }
    current_time = current_time.replace(now.strftime('%A'), weekdays[now.strftime('%A')])
    return current_time

# 사용자 입력
user_query = st.text_area("프롬프트를 입력하세요:", height=200)
max_tokens = st.slider("최대 토큰 수:", min_value=50, max_value=500, value=200, step=50)

# 파일에서 프롬프트 읽기
prompt = read_file(f"{os.getcwd()}/prompt/upgrade_query.md")
prompt = prompt.replace("{nowDateTime}", get_current_time())

if st.button("테스트"):
    if user_query:
        try:
            # OpenAI API 호출
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_query}
                ],
                max_tokens=max_tokens
            )
            
            # 결과 표시
            st.subheader("AI 응답:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"오류 발생: {str(e)}")
    else:
        st.warning("프롬프트를 입력해주세요.")

st.sidebar.markdown("### 사용 방법")
st.sidebar.markdown("1. 프롬프트를 입력하세요.")
st.sidebar.markdown("2. 최대 토큰 수를 조정하세요.")
st.sidebar.markdown("3. '테스트' 버튼을 클릭하세요.")