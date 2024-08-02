while True:
     limit = input("\nEnter the limit for Fibonacci Series: ")
     if limit == "":
         break
     elif int(limit)<=0:
         print("Please enter a positive integer number.")
     else:
          n = int(limit)
          n1 = 0
          n2 = 1
          if n == 1:
             print(n1)
          else:
             print(n1, n2, end=" ")
             for i in range(0, n - 2):
               n3 = n1 + n2
               print(n3, end=" ")
               n1 = n2
               n2 = n3