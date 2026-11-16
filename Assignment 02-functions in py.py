
#1.Even or odd function
#write a function is_even(n) that returns "Even" if the number is even,otherwise "Odd".

def is_even(n):
    return n%2==0
n=7
if is_even(n):
    print(f"{n} is Even")
else:
     print(f"{n} is Odd")   

#2.Largest of two numbers.
#Write a function Largest(a,b)that returns the larger number.

def find_largest(a,b):
    if a>b:
        return a
    else:
        return b 
        
a=30
b=67
result=find_largest(a,b)
print("The Largest Number is :",result)   


#3.Print Numbers
#Write a function print_numbers(n) that prints numbers from 1 to n using loop

def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(10)       


#4.Sum of Numbers
#Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    return sum(range(1,n+1))

print(sum_n(5))    


#5.Multiplication Table
#Write a function table(n) that prints the Multiplication table of n from 1 to 10.

def table(n):
    for i in range(1,11):
      print(f"{n} x {i}={n*i}")

table(4)


'''6.Count even Numbers
Write a function that takes a list and returns how many even numbers i contains.
Example:
Count_even([1,2,3,4,6])'''

def count_even(numbers):
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    return count
    
my_list=[1,2,3,4,6]
print(count_even(my_list))    


#7.Find Maximum
#Without using max(),write a function that returns the largest number in a list.

def largest_num(n):
    if not n:
        return None
    largest=n[0]
    for num in n[1:]:
       if num>largest:
        largest=num
    return largest
    
list=[1,55,67,23,-5,98]
print("Largest number:",largest_num(list))   


'''8.FizzBuzz
write a function that prints numbers from 1 to 100.
If divisible by 3,print"Fizz".
If divisible by 5,print"Buzz".
If divisible by both,print"FizzBuzz".'''

def FizzBuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i) 
            
FizzBuzz()            


#9.Palindrome Checker
#Write a function that return True if a string is a Palindrome.

def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
        
string="madam"
print(is_palindrome(string))        


#10.Count Vowels
#Write a function that counts the vowels in a string.

def count_vowel(s):
    count=0
    for ch in s:
        if ch.lower() in "aeiou":
            count +=1
    return count
    
string="Hello World"
print("Number of vowels:",count_vowel(string))    


#11.Second Largest Number
#Write a function that returns the second largest number in a list without using sort().

def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second

# Example
numbers = [10, 20, 5, 30, 15]

print("Second largest number:", second_largest(numbers))


'''12.Guessing Game
Generate a random number between 1 and 10.
Keep asking the user to guess until they get it right.
Use a loop,conditionals, and functions.'''

import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Congratulations! You guessed it right.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guessing_game()


'''13.Write a function grade(marks)that:
Returns "A" for marks>=90
Returns "B" for marks>=80
Returns "C" for marks>=70
Returns "D" for marks>=60
Otherwise returns "F".'''

def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "F"     
        
marks=89
print("Grade:",grade(marks))        


