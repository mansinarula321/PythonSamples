result = 0
n=123456
for _ in range(32):
    result = result << 1
    print('after left shift'+str(result))
    bit = n % 2
    print('bit' + str(bit))
    result = result + bit
    print('result after bit add' + str(result))
    n = n >> 1 #! dividing n by 2
    print('n after right shift' + str(n))
print(result)
