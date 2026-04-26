"""inp = int(input("Enter an integer: "))
if inp == 0:
  print('Enter an integer higher than 0')
if inp % 2 == 0: 
  print('Even')
else:
  print('Odd')
""" 
"""nums = [2, 5, 7, 8, 9, 5]
x = list(set(nums))
print(x)"""

"""
vowels = ['a', 'e', 'i', 'o', 'u']
def count_vowels(s):
    count = 0
    for i in s:
        if i in vowels:
          count = count +  1
    return count        
       
s = input('Enter a String:')
val = count_vowels(s)
print(val)    """      

"""str = "man"
rev = ""
for i in reversed(str):
    rev = rev + i
print(rev)"""    

"""num = [1, 100, 5, 6, 9, 100,101, 20, 30]
num = list(set(num))
num.sort()
print(num[-1])"""

"""str = "madam"
check = str[::-1]
if str == check:
    print("Is a Palindrome")
else:
    print("Not a Palindrome")"""
        
"""nums = [1, 2, 3, 4]
out =[]
count = 1
for i in range(len(nums)):
    for j in range(len(nums)):
       if  i != j :
           count = count * nums[j]
       else:
           continue 
       if j ==len(nums) - 1 :
           out.append(count)
           count = 1
print(out)  """     
   
"""str = 'Anirudh Sai'
ans = {}
for i in str:
    ans[i] = str.count(i)
print(ans)   """ 

"""num = [1, 100, 5, 6, 9, 100, 101, 20, 30]
num = list(set(num))
num.sort()
print(num)
print(num[-2])"""

"""num1 = [1, 100, 5, 6, 8]
num2 = [9, 100, 101, 20, 30]
num1.sort()
num2.sort()
num3 = num1 + num2
num3.sort()
print(num3)"""

"""nums = [2, 7, 11, 15]
target = 22
for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)"""
 
"""str = "anirudh sai"
count = 0
for char in str:
    count = str.count(char)
    if count == 1:
        print(char)
        break    """
        
"""str ="anirudh sai"
length = 0 
for char in str:
    length = length + 1
print(length)  """  

"""
newlist = [1, [2, 3], [4, [5, 6]]]
a, b, c = newlist
emptylist =[]
emptylist.append(a)
d = int(str(b))
emptylist.append(d)
print(emptylist)"""

"""str1 = "length"
str2 = "htg lea"
count = 0
for char in str1:
    if char in str2:
        count = count + 1
if count == len(str2) - 1:
    print("It is an Anagram")
else:
    print("Not an Anagram")             
        """
"""def calc():
    print("welcome to my calculator")
    x = float(input("Enter a number: "))
    print("Operations: + | - | * | /")
    func = (input("Enter the operation you want to perform: "))
    y = float(input("Enter another number: "))
    match func:
        case "+":
            print("Answer: ", x + y)
        case "-":
           print("Answer: ", x - y)
        case "*":
            print("Answer: ", x * y)
        case "/":
            if y == 0:
                print("Cannot divide by zero")
            else:
                print("Answer: ", x / y)        
        case _:
            print("Invalid Operation, Try Again")
    return None        
            
cont = input("To continue Using the calculator, press 1: ")
while cont == "1":
    calc()
    cont = input("To continue Using the calculator, press 1: ")"""
  
"""import random  
import string
def play_game():
    choices = ["rock","paper", "scissors"]
    print("Rock, Paper or Scissors? Play with a computer!")
    userval = input("Enter your choice:")
    userval = userval.lower()
    Compval = random.choice(choices)
    print("Computer's choice:", Compval)
    if userval == Compval:
        print("It's a tie!")
    elif userval == "rock":
        if Compval =="scissors":
            print("You win! Computer Loses!")
        elif Compval == "paper":
            print("Computer wins! You Lose!")
    elif userval =="paper":
        if Compval == "rock":
            print("You win! Computer Loses!")
        elif Compval == "scissors":
            print("Computer wins! You Lose!")
    elif userval == "scissors":
        if Compval == "paper":
            print("You win! Computer Loses!")
        elif Compval == "rock":
            print("Computer wins! You Lose!")        
            
cont = input("To play the game, press 1:")       
while cont =="1":
    play_game()
    cont = input("To play the game, press 1:")      """       

str = input("Enter your string: \n")
print(len(str.split()))
  
    
    
  
                       
            
        
        
            

        

