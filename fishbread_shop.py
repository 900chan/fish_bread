#주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들어야함.
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있다.

stock = {#key값을 이용해서 value, 딕셔너리는 어떤 스토리 기반으로 데이터가 구성되었을 때 사용
    "팥붕어빵" : 10, 
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

sales = {
    "팥붕어빵" : 0, 
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

 #붕어빵 주문기능
def order_bread():
    while True:
        bread_type = input("나만의 붕어빵을 선택해주세요(팥붕, 슈붕, 초붕) *뒤로 돌아가고싶으시다면 돌아가기를 입력하세요.")
        if bread_type == "돌아가기":   
            print("이전 메뉴로 돌아갈까말까갈까말까")
            break
        if bread_type in stock:
            bread_count = int(input("주문할 수량을 입력해주세요 :"))
            if  stock[bread_type] > bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f'{bread_type}{bread_count}개가 판매되었습니다.')
            else:
                print(f'재고가 부족합니다. 현재 주문 가능한 수량은 {stock[bread_type]}')
        else:
            print("정신체리고 똑바로 다시혀~")

#붕어빵 admin 기능
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵 종류를 입력해주세요. * 뒤로 가시려면 돌아가기를 입력해주세요.")
        if bread_type == "돌아가기":
            break
        if bread_type in stock:
            bread_count = int(input("추가할 수량을 입력해주세요. :"))
            stock[bread_type] += bread_count
            print(f'{bread_type}의 재고가{bread_count}개가 추가 되었습니다. 현재 {stock[bread_type]}개입니다.]')
            print(f'현재 총 재고는 {stock}입니다.')
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")





 #붕어빵 main 화면
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료) : ") 
    if mode == "종료":
        print("시스템이 종료되었다네")    
        break 
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":      
        admin_mode()