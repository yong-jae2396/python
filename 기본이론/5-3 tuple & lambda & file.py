# file = open("basic.txt", "w")

# # 파일에 텍스트를 씁니다
# file.write("Hello python Programming...!")

# file.close()

# with open("basic.txt", "w") as file:
#     # 파일에 텍스트를 씁니다
#     file.write("Hello Python Programming..!")
    

# with open("basic.txt", "r") as file:
#     # 파일을 읽고 출력합니다
#     contents = file.read()
# print(contents)

# 랜덤한 숫자를 만들기 위해 가져옵니다.
# import random
# # 간단한 한글 리스트를 만듭니다
# hanguls = list("가나다라마바사아자차카타파하")

# with open("info.txt", "w") as file:
#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)
#         # 텍스트를 씁니다
#         file.write("{}, {}, {}\n".format(name, weight, height))

# with open("info.txt", "r") as file:
#     for line in file:
#         # 변수를 선언합니다
#         (name, weight, height) = line.strip().split(", ")
        
#         # 데이터가 문제 없는지 확인합니다: 문제가 있으면 지나감
#         if(not name) or (not weight) or (not height):
#             continue
#         # 결과를 계산합니다.
#         bmi = int(weight) / (int(height) * int(height))
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상체중"
#         else:
#             result = "저체중"
        
#         # 출력합니다
#         print('\n'.join([
#             "이름 : {}",
#             "몸무게 : {}",
#             "키 : {}",
#             "BMI : {}",
#             "결과 : {}",
#         ]).format(name, weight, height, bmi, result))
#         print()

# join은 문자열에만 사용가능 map으로 변환하여 ::과 결합        
# numbers = [1, 2, 3, 4, 5, 6]        
# print("::".join(
#     map(str, numbers)
# ))

number = list(range(1, 10+1))

print("# 홀수만 출력하기")
print(list(filter(lambda 홀수 : 홀수 % 2 == 1, number )))

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda 중간수 : 중간수 >=3 and 중간수 < 7, number)))

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda 제곱수 : 제곱수 * 제곱수 < 50 , number)))
