# Write your code here
a=[0]*32
i=0
inverse=''
n=123456
result=0
binN=bin(n)[2:] #! convert into binary
paddedbin=str(binN).rjust(32,'0')
print(paddedbin)
for x in paddedbin:
        if x=='0':
            inverse+='1'
        else:
            inverse+='0'

result=int(inverse,2)
print(result)
