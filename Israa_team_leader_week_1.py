#Question1
for i in range(1,11):
    print(i , end="\t")
print()

#Question2 with for loop
number=int (input('enter the number: '))
print('even numbers up to this number are: ')
for i in range(0,number+1):
    if i%2==0: 
       print(i, end='\t')
print()

#Question2 with while loop
number = int(input('enter the number: '))
print ('even numbers up to this number are: ')
i=0
while i<= number:
    if i %2==0:
        print(i, end ='\t')
    i += 1
print()

#Question3 

start=int(input('enter the start: '))
end=int(input('enter the end: '))
print('numbers from the start to the end')
if start <= end:
    for i in range(start,end+1):
        print(i, end='\t')
else:
    for i in range(end,start+1):
        print(i,end='\t')
print()


#Question 4 Is this number odd or even
number= int(input('Enter a number?'))
if number %2==0:
    print('This number is odd')
else:
    print('This number is even')

#Question 5
number=int(input('Enter a number:')) 
factorial=1
if number >= 0:
    for i in range(1,number+1):
        factorial *= i
    print ('Factorial is :',factorial)
else:
    print('The number should be positive')
    

#Question 6
number=int(input('Enter the number: '))
prime=0
for i in range(2,number):
    if number%i==0:
        print('The number is not prime')
        break
    else:
        prime=1
if prime ==1:
    print ('This number is prime')


#Question 7

limit=int(input('enter the limit: '))
fib_sequence = [0, 1]  # Initial Fibonacci numbers
while True:
    next_number = fib_sequence[-1] + fib_sequence[-2]
    if next_number > limit:
        break
    fib_sequence.append(next_number)
print(' Fibonacci sequence is : ')
print(fib_sequence)


#Question 8
word=input('enter the word: ')
word=word[::-1]
print('Reverse this word is : ',word)
  

#Question9
word=input('enter the word: ')
palindrome=True
for i in range( len(word)//+1):
    if word[i]!=word[-(i+1)]:
        palindrome=False
        break
if palindrome:
    print('It is a palindrome word.')
else:
     print('It is not a palindrome word. ')

 
#Question10
height=int(input('Enter your height in meters: '))
weight=int(input('Enter your weight in kilograms: '))
bmi=weight/(height**2)
if bmi<25:
    print('Underweight')
elif 25<=bmi<30:
    print ('Normal')
elif 30<=bmi<=40:
    print('overweight')
else:
    print('overweight')

#Question11
first_number=int(input('enter the first number: '))
second_number=int(input('enter the second number: '))
thrid_number=int(input('enter the third number: '))

if first_number>=second_number and first_number>=thrid_number:
    print('The first number is the largest.')
if second_number>=first_number and second_number>=thrid_number:
    print('The second number is the largest.')
if thrid_number>=first_number and thrid_number>=second_number:
    print('The thrid number is the largest.')


#Question12
for i in range(1,5):
    midterm_grade=float(input('enter the midterm grade: '))
    final_grade=float(input('enter the final grade: '))
    average=0.4*midterm_grade + 0.6*final_grade
    if average < 50:
        print('Result:Failed')
        print('average:',average)
    else:
        print('Result:Successful')
        print('average:',average)
