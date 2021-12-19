output = 0
#리스트 내포
output = [i for i in range(1,101) if "{:b}".format(i).count("0") == 1 ]
for i in output:
    print("{} : {}".format(i , "{:b}".format(i)))

print("합계 : {}".format(sum(output)))


