'''
Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
40
20
25
Sample Output:
L1

'''
Sample Input:
6
8
Sample Output:
6 less than 8
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Compare the two numbers and print the appropriate message
if a == b:
    print(f"{a} and {b} are equal.")
elif a > b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{a} is less than {b}.")
  
