#주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들어야함.
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있다.

class BreadShop:
    def __init(self):
        self.stock = {"팥붕어빵" : 10, "슈크림붕어빵" : 8,"초코붕어빵" : 5}
        self.sales = {"팥붕어빵" : 0, "슈크림붕어빵" : 0,"초코붕어빵" : 0}
        self.price = {"팥붕어빵" : 1000,"슈크림붕어빵" : 1200,"초코붕어빵" : 1500}

 #붕어빵 주문기능

    def order_bread(self):
        while True:
            bread_type = input("나만의 붕어빵을 선택해주세요(팥붕, 슈붕, 초붕) *뒤로 돌아가고싶으시다면 돌아가기를 입력하세요.")
            if bread_type == "돌아가기":
                print("이전 메뉴로 돌아갈까말까갈까말까")
                break
            if bread_type in self.stock:
                bread_count = int(input("주문할 수량을 입력해주세요 :"))
                if  self.stock[bread_type] > bread_count:
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] += bread_count
                    print(f'{bread_type}{bread_count}개가 판매되었습니다.')
                else:
                    print(f'재고가 부족합니다. 현재 주문 가능한 수량은 {self.stock[bread_type]}')
            else:
                print("정신체리고 똑바로 다시혀~")

#붕어빵 admin 기능
    def admin_mode(self):
        while True:
            bread_type = input("추가할 붕어빵 종류를 입력해주세요. * 뒤로 가시려면 돌아가기를 입력해주세요.")
            if bread_type == "돌아가기":
                break
            if bread_type in self.stock:
                bread_count = int(input("추가할 수량을 입력해주세요. :"))
                self.stock[bread_type] += bread_count
                print(f'{bread_type}의 재고가{bread_count}개가 추가 되었습니다. 현재 {self.stock[bread_type]}개입니다.]')
                print(f'현재 총 재고는 {self.stock}입니다.')
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")

    def calculate_sales(self):
    # total_sales = sum(sales[key] * price[key] for key in sales)
        total = 0
        for key in self.sales:
            total += (self.sales[key] * self.price[key])
        print(f'오늘의 총 매출은 {total}원 입니다.')