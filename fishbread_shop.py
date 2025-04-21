#주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들어야함.
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있다.


# i = 0
# while i < 10:
#     mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료) : ")
#     i += 1 # i = i + 1
#     if mode == "종료":
#         break

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료) : ") 
    if mode == "종료":
        print("시스템이 종료되었다네")    
        break 
    elif mode == "주문":
        pass
    elif mode == "관리자":      
        pass