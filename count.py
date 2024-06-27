num = int (input('Enter and no.'))
count=0
while num!=0 :
    rem = num%10
    count += 1
    num=num//10
print(count)    
