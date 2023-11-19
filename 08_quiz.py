class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

# 음료 객체 생성
Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

# 첫 번째 사용자 입력 받기
selected_beverage = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")
if selected_beverage == "커피" or selected_beverage == "녹차" or selected_beverage == "아이스티":
    # 두 번째 사용자 입력 받기
    try:
        quantity = int(input("수량을 입력하세요: "))
        if quantity > 0:
            if selected_beverage == "커피":
                total = Coffee.calculate(quantity)
            elif selected_beverage == "녹차":
                total = GreenTea.calculate(quantity)
            elif selected_beverage == "아이스티":
                total = IceTea.calculate(quantity)
            print(f"{selected_beverage} {quantity}잔의 총 가격은 {total}원 입니다.")
        else:
            print("잘못된 수량을 입력했습니다.")
    except ValueError:
        print("수량은 숫자로 입력해주세요.")
else:
    print("잘못된 음료를 선택했습니다.")
