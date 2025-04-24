num=int(input('Podaj liczba'))
count_fizz=0
count_buzz=0
count_Fizzbuzz=0
x=1
for num in range (0,num):
   if x%3==0 and  x%5==0:
       print('FizzBuzz')
       count_Fizzbuzz=count_Fizzbuzz+1
       x=x+1
   if x%5==0:
         print('Buzz')
         count_fizz=count_fizz+1
         x=x+1
   elif x%3==0:
         print('Fizz')
         count_buzz=count_buzz+1
         x=x+1
   else:
         print(x)
         x=x+1
print('Wynik')
print(count_Fizzbuzz)  
print(count_fizz)   
print(count_buzz)
 