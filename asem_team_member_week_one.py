#Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.

for i in range(1, 11):
    print(i)


#Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops

num = int(input("Enter a number: "))

for i in range(1, num +1):
    if i % 2 == 0:
        print(i)

num = int(input("Enter a number: "))

i = 1
while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1



#Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values ​​(including the end value) on the screen.

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

for i in range(start, end + 1):
    print(i)


#Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



##Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. Factorial is the product of all positive integers between a number itself and 1. For example: if the user entered 5, the program should give the following output: Enter a number from the user: 5 Factorial: 120

num = int(input("Enter a positive integer: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial: 1")  # by definition, 0! = 1
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial:", factorial)


##Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number.")
    else:
        print("Not a prime number.")


##Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?

limit = int(input("Enter the limit for the Fibonacci sequence: "))

fibonacci = [0, 1]

while True:
    next_num = fibonacci[-1] + fibonacci[-2]
    if next_num > limit:
        break
    fibonacci.append(next_num)

print("Fibonacci sequence up to", limit, ":", fibonacci)


#Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

word = input("Enter a word: ")

reversed_word = ""

for char in word:
    reversed_word = char + reversed_word 

print("Reversed word:", reversed_word)


##Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

word = input("Enter a word: ")

reversed_word = ""


for char in word:
    reversed_word = char + reversed_word


if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")



##Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. (You can look on the internet for the weight index calculation) To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak, Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.


weight = float(input("Enter your weight in kilograms: "))


height = float(input("Enter your height in meters: "))


bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 30 <= bmi < 35:
    category = "Obesity Class I"
elif 35 <= bmi < 40:
    category = "Obesity Class II"
else:
    category = "Obesity Class III"


print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")



##Question 11: How to write a Python program that finds the largest of three numbers entered by a user?



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


print("The largest number is:", largest)



##Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be written one after the other.

for i in range(1, 5):
    print(f"\nLesson {i}")
    
    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter final grade: "))
    
    average = (midterm * 0.4) + (final * 0.6)
    
    print(f"Average: {average:.2f}")
    
    if average < 50:
        print("Result: FAILED")
    else:
        print("Result: SUCCESSFUL")



