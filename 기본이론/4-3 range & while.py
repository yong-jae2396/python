# 1 번 문제
for i in range(3,10,3):
    print(i)

# 2번 문제
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(4):
    character[key_list[i]] = value_list[i] 
print(character)

# 3번 문제
limit = 10000
i = 0
sum_value = 0
for count  in range(limit):
    i += 1
    if sum_value < limit:
        sum_value = sum_value + count
    else:
        break
print("{}를 더할때 {}을 넘으면 그때의 값은 {}입니다.".format(i,limit, sum_value))

# 4번 문제
max_value = 0
a = 0
b = 0

for i in range(101):
    b = 100 - i
    a += 1
    max_value = a * b
    if a > 100 and b == 1:
        print(max_value)
    # 최대값 구하기
    
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

