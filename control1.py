# code to interprete
num1 = int(input("input your first number"))
num2 = int(input("input your second number"))
#
#operator = input("choose the operator")
if num1 >= num2:
   #the condition on line 7 should be true for the print to run
   print("Error:First should be less than the second number.")
   #in python if writing a if condition,the next line should be indented with four spaces after the full colon e.g(line 11,8)
if num1 % num2 == 0:
      print(f"{num1}is divisible by {num2}")
   #  a block of code arerelated to one another and uses is not(!) 
if num1 != 0:   
   num2 += num1
   print(num2)
   
