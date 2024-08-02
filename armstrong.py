n=int(input("Enter number: "))
sum = 0
temp = n
while temp>0:
     digit = temp % 10
     sum += digit ** 3
     temp //= 10
if n == sum:
     print("Armstrong number")
else:
     print("Not an Armstrong number")