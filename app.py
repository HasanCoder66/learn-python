# print("hello world", "thanks buddy for using python!")


# there are 4 primitives data types in python
# string , integer, bool, float


# name = "hasan";
# age = 23
# isAdmin = True
# floatingNumber = 55.4

# print("type of floatingNumber -->",type(floatingNumber))

# print("hello" +  " " + name);
# print("my age is", age);
# print("admin is :", isAdmin)



# input

# name = input("enter your name")

# print("hello", name);
# num = input("enter your number")

# new_num = float(num)
# print(new_num + 1);



name = "jani";

# print(name.upper());
# print(name);
# print(name.find("ni"))
# print(name.replace("jani", "hello janiii"))




# print("I" in name)


# p1 = int(input("enter a price"))
# p2 = int(input("enter a price"))
# p3 = int(input("enter a price"))



# print("products sum:", p1 + p2 + p3)



# super_hero = input("enter your name");

# start_with_s = print(super_hero.lower().startswith("s"));

# print(start_with_s)


# a = 3 > 5
# b = 5 >= 5


# print(a and b)
# print(not True)


# print( 3 + 3)
# print( 3 - 3)
# print( 3 * 3)
# print( 3 ** 3)
# print( 3 / 3)
# print( 3 // 3)
# print( 3 % 3)



# print((2  + 5)  * 5)

# if 2 > 2 :
#     print("three two sai baraa haii..")
# elif 2 < 3 :
#     print("else if true hai..")
# else :
#     print("else chl giya..")     



# calculator


# a = int(input("enter a value"));
# b = int(input("enter b value"));
# operator = input("enter a operator  + - / * e.g;")



# if operator == "+":
#     print(a + b);
# elif operator == "-" :   
#     print(a - b)
# elif operator == "*"  :  
#     print(a * b)
# elif operator == "/":    
#     print(a / b)
# else : 
#     print("invalid operation")



# logical operators in python

# name = "hasan"
# admin = False
# age = 22



# if name == "hasan" and admin == True and age >= 23:
#     print("you are valid user for this platform!")
# else:
#     print("invalid user!")


# if name == "hasan" or admin == True or age >= 23:
#     print("you are valid user for this platform!")
# else:
#     print("invalid user!")


# lottery = 4443;


# if lottery != 4444:
#     print("try again")
# else:
#     print("you win")


# range

# nums = range(1,101, 2)

# print(nums)



# i = 1
# while i <= 5:
#     print(i * "hello")
#     i += 1
    

# print("end of code!")




# for loop

# nums = range(0, 5001);


# for i in nums:
#     print("hello world", i)



# for i in range(0, 21):
#     if i % 2 == 0:
#         print("even num", i)
#     elif i % 3 == 0:
#         print("odd num", i)


# for i in range(2, 11, 2):
#     print(i)


# break & continue in python


# for i in range(1, 11):
#     if i == 5:
#         print("5 milgaya or loop break kerdia..")
#         break
#     if i % 2 == 0:
#         print("even number found", i)



# for i in range(1, 11):
#     if i == 6:
#         print("6 milgaya or skip bi kerdia..")
#         continue
#     if i % 2 == 0:
#         print("even number found", i)





# print the table of 57

# tableOf57 = 57

# for i in range(1,11):
#     print(tableOf57 , "x" , i , "=" , i * tableOf57)



# print all multiples 3 from 1 to 50 and skip 15

# for i in range(1, 51):

#     if i == 15 :
#         continue
#     if i % 3 == 0:
#         print("multiply by 3 -->",i)


# a = int(input("enter first number"));
# b = int(input("enter second number"));

# found  = False
# for i in range (1, 1001):
#     if i % a == 0 and i % b == 0:
#        print(f"The first number divisible by both is: {i}")



# if not found:
#     print("No number between 1 and 1000 is divisible by both.")



a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

found = False

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(f"The first number divisible by both is: {i}")
        found = True
        break

if not found:
    print("No number between 1 and 1000 is divisible by both.")