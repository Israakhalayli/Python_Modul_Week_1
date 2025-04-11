# Question 1#
#########
for i in range(1,11):
    print(i)

# Question 2 
#########
num = int(input("Enter thenumber: "))
print("Even numbers to", num, "are:")
for i in range(0, num + 1, 2):    
    print(i)
print("Even numbers to", num, "are:")
i = 0
while i <= num:    
    print(i)    
    i += 2

# Question 3
##########
start = int(input("Enter the first number: "))
end = int(input("Enter the last number: "))
print("the range between", start, "and", end, "are:")
for num in range(start, end + 1):    
    print(num)

# Question 4
########
num = int(input("Enter a number: "))
if num % 2 == 0:    
    print(num, "is an even number.")
else:    
    print(num, "is an odd number.")

# Question 5
#########
num = int(input("Enter a positive integer: "))
if num < 0:    
    print("Please enter a positive integer.")
else:
    x = 1
    for i in range(2, num + 1):        
         x*= i       
print(x)

# Question 6
########
n = int(input("Enter a number: "))
if n <= 1:        
    print("false")   
for i in range(2, int(n ** 0.5) + 1):        
    if n % i == 0:            
        print("is not a prime number.")
    else:
        print(n, "is a prime number.") 

# Question 7
#########
n = int(input("Enter a number: "))
fib_seq =[]
a,b = 0,1
while a<= n:
    fib_seq.append(a)
    a,b = b,a + b
print(fib_seq)

# Question 8
########
word = input("Enter a word :")
rev_word = word[::-1]
print("rev_word = ", rev_word)

# Question 9
#########
word = input("Enter a word :")
if word == word[::-1]:
    print("the word is a palindrome.")
else:
    print("the word is not a palindrome.")

  # Question 10
  # #######
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

x = weight / (height ** 2)

if x < 25:
    print("You are underweight.")
elif x < 30:
    print("Your weight is normal.")
elif x <= 40:
    print("You are overweight.")
else:
    print("You are severely overweight.")

  # Question 11
  # #######
  numbers = input("Enter numbers separated by spaces: ").split()
largest_three = sorted(numbers, reverse=True)[:3]
print("The largest three numbers are:", largest_three)

  # Question 12
  # #######
for i in range(1, 5): 
    print(f"Enter grades for Lesson {i}:")
    
    mid = float(input("Enter your midterm grade: "))
    fin = float(input("Enter your final grade: "))
    
    average = (mid * 0.4) + (fin * 0.6)
    
    if average < 50:
        print(f"Lesson {i}: FAILED\n")
    else:
        print(f"Lesson {i}: SUCCESSFUL\n")