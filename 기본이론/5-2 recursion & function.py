# 재귀 함수를 이용한 팩토리얼 구하기
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

문제 1 번
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)       
    return output        
example = [[1, 2, 3], [4, [5, 6],7, [8, 9]]]
print("원본 :", example)
print("변환 :", flatten(example))

# 문제 2 번
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 6
memo = {}
def 문제(남은사람수, 앉힌사람수):
    key = str((남은사람수, 앉힌사람수))    
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0 # 무효하니 0을 리턴
    if 남은사람수 == 0:
        return 1 # 유효하니 수를 세면 되서 1을 리턴
    # 재귀처리
    count = 0
    for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
        count += 문제(남은사람수 - i, i)
    # 메모화 처리
    memo[key] =count
    return count
print(문제(전체사람의수, 앉힐수있는최소사람수))
