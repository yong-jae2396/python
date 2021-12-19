#기본 매개변수 예제
# def print_n_times(value , n = 2):
#     for i in range(n):
#         print(value)
# print_n_times("안녕하세요", 5)
#키워드 매개변수 예제
# def a(*values, n = 2):
#     for i in range(n):
#         for value in values:
#             print(value)
# a("안녕", "즐거움", n=3)

# def sum_all(start, end):
#     output = 0
#     for i in range(start, end + 1):
#         output += i
#     return output
# print("0 to 100:",sum_all(0, 100))
# print("0 to 1000:",sum_all(0, 1000))
# print("50 to 100:",sum_all(50, 100))
# print("500 to 1000:",sum_all(500, 1000))

# 문제 1 번
# def f(x):
#     return (x**2 + x*2+1)
# print(f(5))

# 문제 2 번
def mul(*values):
    output = 1
    for i in values:
        output = output * i
    return output
print(mul(5,7,9,10))
    
