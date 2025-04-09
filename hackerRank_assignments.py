#1. Arithmetic Operators (https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)
a = int(input())
b = int(input())


sum = a + b
sub = a - b
multi = a * b
print(sum)
print(sub)
print(multi)

#2. Find the Runner-Up Score! (https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)
n = int(input())
arr = list(map(int, input().split()))
arr = tuple(arr)
max_score = max(arr)
arr = list(arr)

while max_score in arr:
    arr.remove(max_score)

print(max(arr))


#3. Print Function (https://www.hackerrank.com/challenges/python-print/problem)

n = int(input())
for i in range(1, n+1):
    print(i, end="")


#4. Finding the percentage (https://www.hackerrank.com/challenges/finding-the-percentage/problem)
n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()


marks = student_marks[query_name]
average = sum(marks) / len(marks)

print(f"{average:.2f}")