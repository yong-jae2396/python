# 3-1 문제
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0: 
        print(str(number) + "는 짝수입니다.")
    else:   
        print(str(number) + "는 홀수입니다.")

# 3-2 문제
for number in numbers:
    if len(str(number)) == 3:
        print(str(number) + "는 3 자리수입니다.")
    
    elif len(str(number)) == 2:
        print(str(number) + "는 2 자리수입니다.")
    
    else:
        print(str(number) + "는 1 자리수입니다.")
        
# 4 문제
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8,9]
]
a = 0
for b in range(2): 
    a += 1
    list_of_list[0].extend(list_of_list[a])
del list_of_list[1:]

for a in list_of_list[0]:
    print(a)
for line in list_of_list:
    for a in line:
        print(a)

# 5 문제
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output =[[], [], []]

for number in numbers:
    output[(number+2)%3].append(number)
print(output)