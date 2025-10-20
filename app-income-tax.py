import streamlit as st

# 앱 제목
st.title("💰 소득 수준별 세금 계산기")

st.write("""
이 앱은 사용자의 **소득(income)** 을 입력받아  
소득 수준(저소득층 / 중간소득층 / 고소득층)에 따라  
자동으로 세금을 계산해줍니다.
""")

# 1️⃣ 사용자 입력
income = st.number_input("당신의 소득을 입력하세요 (만원 단위)", min_value=0, step=100)

# 2️⃣ 계산 로직
if income >= 10000:
    tax = income * 0.50
    level = "고소득층"
    rate = 50
elif income >= 5000:
    tax = income * 0.25
    level = "중간소득층"
    rate = 25
else:
    tax = income * 0.10
    level = "저소득층"
    rate = 10

# 3️⃣ 결과 출력
st.subheader("🧾 계산 결과")
st.write(f"**소득 수준:** {level}")
st.write(f"**세율:** {rate}%")
st.write(f"**예상 세금:** {tax:.1f}만원")

# 4️⃣ 시각화 (막대 그래프)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(["소득", "세금"], [income, tax])
ax.set_ylabel("금액 (만원)")
ax.set_title("소득과 세금 비교")
st.pyplot(fig)
