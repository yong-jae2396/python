try:
    a = [273, 103, 52, 57, 100]
    number = int(input("정수 입력(0 ~ 4까지 입력해주세요)> "))
    print(a[number])
except ValueError as exception:
    print("값의 문제가 있습니다. ")
except IndexError as exception:
    print("0~4까지 입력해주세요. ")
except Exception as exception: # 보통 예외 처리 마지막에 사용
    print("알 수 없는 예외가 발생했습니다. ") #예) 개발자에게 메일을 보낸다

raise Exception("안녕하세요")    
