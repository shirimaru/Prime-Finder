while True:
 def prime(n):
   if(n<=1):
     print("The number is not prime.")
     return
   for i in range(2, n):
     if(n%i==0):
       print("The number is not prime.")
       return
       # basically when the interpreter will check the if criteria here it will divide n by i and as soon as it finds any n
       # divided by i to have 0 remainder it will print else return will keep throwing it upward to if for checking.
   else:
     print("The number is prime.")
 n = int(input("Enter the number:"))
 prime(n)
