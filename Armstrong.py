num=407
rev=0
num1=num
while num!=0 :
    rem = num % 10
    rev = rev+rem**3
    num = num//10
print(rev)
if num1==rev :
    print("Yes number is a Armstrong") 
else :
    print("No number is  not aArmstrong") 