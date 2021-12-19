# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# for number in numbers:
#     if number % 2 == 0:
#         print("{} 는 짝수 입니다.".format(number))
#     else:
#         print("{} 는 홀수 입니다.".format(number))

# for number in numbers:
#     if len(str(number))  == 3:
#         print("{} 는 {} 자리수 입니다.".format(number,3))
#     elif len(str(number))  == 2:
#         print("{} 는 {} 자리수 입니다.".format(number,2))
#     else:
#         print("{} 는 {} 자리수 입니다.".format(number,1))

# list_of_list =[
#     [1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9]
# ]

# for lists in list_of_list:
#     for list_element in lists:
#         print(list_element)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# output = [[], [], []]

# for number in numbers:
#     output[(number + 2) % 3].append(number)
    
# print(output)

# pets = [
#     {"name" : "구름", "age" : 5},
#     {"name" : "초코", "age" : 3},
#     {"name" : "아지", "age" : 1},
#     {"name" : "호랑이", "age" : 1},
# ]

# print("# 우리 동네 애완 동물들")

# for pet in pets:
#     print(pet["name"], str(pet["age"]) + "살")

# numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
    
#     else:
#         counter[number] = 1        
    
    
# print(counter)


# character ={
#     "name" : "기사", 
#     "level" : 12,
#     "items" :{
#         "sword" : "불꽃의 검",
#         "armor" : "풀블레이트"
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
# }

# for key in character:
#     if type(character[key]) is dict:
#         for dicts in character[key]:
#             print(dicts,":",character[key][dicts])
#     elif type(character[key]) is list:
#         for lists in character[key]:
#             print(key, ":", lists)
#     else:
#         print(key, ":", character[key])

# for i in range(3, 10, 3):
#     print(i)

# key_list = ["name", "hp", "mp", "level"]
# vallue_list = ["기사", 200, 30, 5]
# character = {}
    
# for i in range(0, len(key_list)):
#     character[key_list[i]]= vallue_list[i]

# print(character)

# limet = 10000
# i = 1
# sum_vallue = 0
# while sum_vallue < limet:
#     i += 1
#     sum_vallue += i
     
# print("{}를 더할 때 {}을 넘으면 그때의 값은 {}입니다".format(i, limet, sum_vallue))

# max_value = 0
# a = 0
# b = 0

# for i in range(1, 101):
#     j = 100 - i
#     a = i * j  
#     if max_value < a:
#         max_value = a 
# print(max_value)

# def fibonacci(n):
#         return 1
#     if n == 2: 
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print("fibonacci(4) : ", fibonacci(4))
# def flatten(data):
#     output = []
#     for item in data:
#         if type(item) == list:
#             output += flatten(item)
#         else:
#             output.append(item)
#     return output
# exmple = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print("원본 : ", exmple)
# print("변환 : ", flatten(exmple))  

# numbers = list(range(1, 11))

# print("홀수만 출력하기")
# print(list(filter(lambda x : x % 2 == 1, numbers)))

# print("# 3 이상, 7 미만 추출하기")
# print(list(filter(lambda x : 3 <= x < 7, numbers)))

# print("# 제곱해서 50 미만 추출하기")
# print(list(filter(lambda x : x * x > 50, numbers)))
