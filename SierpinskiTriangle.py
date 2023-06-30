#Sierpinski's Triangle is a modified version of The Pascal's Triangle 
#The odd numbers of the Pascal's triangle is written as *** and the even numbers are just blank spaces and this triangle is created

from math import factorial

n = int(input("Enter Number of Rows: "))

def start():
    for i in range(n+1):
        for j in range((n - i + 1)):
            print(end= "  ") #print empty spaces before the triangle
        for k in range(i+ 1):
            if (factorial(i)/(factorial(k)* (factorial(i-k))))% 2 != 0.0: #odd numbers of the pascals triangle
                print("***", end=" ")
            else:
                print("   ", end=" ")#empty spaces for even numbers
        print()
start()

#works best with 2^n numbers
