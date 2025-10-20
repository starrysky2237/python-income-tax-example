income = int(input("당신의 소득(만원 단위)을 입력하세요: "))

if income >= 10000:
    tax = income * 0.50
    level = "고소득층"
elif income >= 5000:
    tax = income * 0.25
    level = "중간소득층"
else:
    tax = income * 0.10
    level = "저소득층"

print(f"\n소득 수준: {level}")
print(f"예상 세금: {tax:.1f}만원")
