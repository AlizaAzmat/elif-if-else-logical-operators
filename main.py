# Take name and fee input and check if name is “atif” and fee is equal to 1000 than
# print “Valid Record” otherwise Print “Invalid Record”.

# Ex 1
# String & Number

# name = input("Please enter your name: ")
# fee = int(input("Please enter your fee: "))

# if name == "atif" and  fee == 1000:
#   print("Valid Record")
# else:
#   print("Invalid Record")

# Take course and age input and check if course is “DOT NET” and age is greater than
# or equal 15 then print “You Can Enroll” otherwise Print “You Can‟t Enroll”.

# Ex 2
# String & Number

# course = input("Please enter your course: ")
# age = int(input("Please enter your age: "))
# if course == "DOT NET" and age >= 15:
#   print("You Can Enroll")
# else:
#   print("You Can‟t Enroll")

# Take a character input and check if character is „d‟ or „D‟ then print “DOT NET”
# otherwise Print “Invalid Character”.

# Ex 3
# Character

# ch = input("Please enter a character: ")
# if ch == "d" or ch == "D":
#   print("DOT NET")
# else:
#   print("Invalid Chaacter")

# 7. Take a number input and check if number is 1 or 3 then prints
# “Starting Positive Two ODD Numbers “otherwise Print “Unknown Numbers”.

# Ex 4

# num = int(input("Please enter a number:"))
# if num == 1 or num == 3:
#   print("Starting Positive Two ODD Numbers")
# else:
#   print("Unknown Numbers")

# 11. Take a number input and check if number is 1, 3, 5 or 7 then print “Odd Number
# “otherwise print “Unknown Numbers”.

# Ex 5
# Number

# check_num = int(input("Please enter a number:"))
# if check_num % 2 == 1:
#   print("Odd Number")
# else:
#   print("Unknown Numbers")

# 12. Take name, course, age input and check if name is “asif”, course is “C#” and age is
# greater than or equal 15 then print “Valid Record” otherwise Print “Invalid Record”.

# Ex 6
# String & number

# name = input("Please enter your name :")
# course = input("Please enter your course :")
# age = int(input("Please enter your age "))

# if name == "asif" and course == "C#" and age >= 15:
#   print("Valid Record")
# else:
#   print("Invalid Record")

# 14.  Take course and fee input and check if course is “C#” and fee is 4000 or 5000 then
# print “Valid Record” otherwise Print “Invalid Record”.

# Ex 7
# String & number

# course = input("Please enter a course :")
# fee = int(input("Please enter a fee :"))
# if course == "C#" and fee == 4000 or fee == 5000:
#   print("Valid Record")
# else:
#   print("Invalid Record")

# 15.  Take username and password input and check if username is “admin” or “Admin”
# and password is “admin” then print “WelCome” otherwise print “Sorry”.

# Ex 8
# String

# user_name = input("Please enter a username :")
# password = input("Please enter a password :")
# if user_name == "admin" or user_name == "Admin" and password == "admin":
#   print("WelCome")
# else:
#   print("Sorry")

# =======================================Exercise 6 ====================================

# Write a program to check whether a person is eligible for free shipping based on
# two conditions: if their total order amount is over $50 or if they are a premium member
# Write a program to  check their eligibility and provide an appropriate message based on
# the conditions met.

# Ex 1
# string and number

# order = int(input("Please enter your order amount :"))
# premium_member = bool(input("Are you a premium member"))
# if order >= 50 or premium_member == True:
#   print("You are eligible for free shipping")
# else:
#   print("You are not eligible for free shipping")

# Create a program that checks whether a given character is a vowel
# (one of 'a', 'e', 'i', 'o', 'u') or a  special character.

# Ex 2
#Character

# char = input("Please enter a character :")
# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#   print("Vowel")
# else:
#   print("Not a Vowel")

# Write program to determine if a person is eligible for early retirement if
# they have either reached the age of 55 or have worked for 30 or more years.
# Ask for the person's age and years worked.

# Ex  3

# age_retire = int(input("Please enter your age :"))
# work_retire = int(input("Please enter your years worked :"))
# if age_retire >= 55 or work_retire >= 30:
#   print("You are eligible for early retirement. ")
# else:
#   print("You are not eligible for early retirement. ")

# Write a program to check if a student has passed the course if their exam score
# is either above 60% or they have a teacher's recommendation. Ask for the
# student's exam score and if they have a recommendation.

# Ex 4

# exam_score = int(input("Please enter your exam score :"))
# recommendation = bool(input("Do you have a teacher's recommendation?"))
# if exam_score >= 60 and recommendation  == True:
#   print("You have passed the course. ")
# else:
#   print("You have failed the course. "")

# Write a Program to check if a product is available for purchase if it is either
# in stock or on pre order. Ask the user for the availability status.

# Ex 5

# in_stock = input("Is the product in stock? (Yes / No)").lower() == "yes"
# on_pre_order = input("Is the product on pre-order? (yes/no): ").lower() == "yes"

# if in_stock or on_pre_order:
#   print("The product is available for purchase.")
# else:
#   print("The product is not available for purchase.")

# Write a program to Determine if a person is eligible for a discount if they are
# either a senior citizen (60 or older) or a student with a valid ID. Ask for the
# person's age and student status.

# Ex 6

# citizen_age = int(input("Please enter your age :"))
# std_id = bool(input("Do you have a student ID? (Yes / No)"))
# if citizen_age >= 60 or std_id == True:
#   print("You are eligible for a discount.")
# else:
#   print("You are not eligible for a discount.")

#====================================Exercise 5======================================

# Create a  program that checks if a person's age is between 25 and 40 (inclusive) and
# if they are employed. If the age falls within the specified range and they are employed,
# display "Person is in the prime working age and employed," otherwise, print
# "Person is not in the prime working age and/or not employed."

# Ex 1

# person_age = int(input("Please enter your age :"))
# employed = input("Are you employed? (Yes / No)").lower() == "yes"
# if person_age >=25 and person_age <= 40 and employed:
#   print("Person is in the prime working age and employed.")
# else:
#   print("Person is not in the prime working age and/or not employed")

# Write a program that checks if a given temperature is both above freezing (above 0°C)
# below boiling (below 100°C). If it meets both conditions, print "The water is in a
#liquid state,"  otherwise, print "The water is not in a liquid state."

# Ex 2

# temp = int(input("Please enter a temperature :"))
# if temp > 0 and temp <= 100:
#   print("The water is in a liquid state.")
# else:
#   print("The water is not in a liquid state.")

# Write a  program to determine whether a number is positive and even or negative & odd.
# If it is positive and even, or negative and odd, print "Number is either positive and
# even or negative and odd," otherwise, print "Number is not in the specified categories

# Ex 3

# number= int(input("Please enter a number"))
# if number > 0 and number % 2 == 0:
#   print("Number is either positive and even or negative and odd")
# else:
#   print("Number is not in the specified categories")

# Create a program that determines whether a student passed an exam.To pass, the student
# must score at least 50 marks in both the written and practical parts of the exam.
# If they meet both conditions, print "Pass," otherwise, print "Fail."

# Ex  4

# written_exam = int(input("Please enter your written exam score :"))
# practical_exam = int(input("Please enter your practical exam score :"))
# if written_exam >= 50 and practical_exam >= 50:
#   print("Pass")
# else:
#   print("Fail")

#====================================Exercise 4======================================

# Write a program to check whether a given integer is both positive and even. If the number
# meets both criteria, display a message stating that it's positive and even. Otherwis
# indicate that it's not.

# Ex 1

# given_int = int(input("Please enter any integer"))
# if given_int > 0 and given_int % 2 == 0:
#   print("The number is positive and even")
# else:
#   print(f" {given_int}  is not  a positive or even number.")

# Write a program that converts temperatures between Celsius and Fahrenheit.
# Ask the user for a temperature value and its unit (Celsius or Fahrenheit) and
# then convert it to the other unit.

# Ex 2

# temp = int(input("Please enter a temperature :"))
# unit = input("Please enter a unit (Celsius / Fahrenheit) :").lower()
# if unit == "celsius":
#   print(f"The {temp} in {unit} is {(temp * 9/5) + 32}")
# elif unit == "fahrenheit":
#   print(f"The {temp} in {unit} is {(temp - 32) * 5/9}")
# else:
#   print("Invalid unit")

# Write a program that takes units and calculates the electricity bill as per the below
# given criteria.

#  1-100 unit - 5/=
#  101-200 unit - 7/=
#  201-300 unit - 10/=
#  Above 300 - 15/=

# Ex 3

# unit = int(input("Please enter a unit"))
# bill = 0
# if unit <=100:
#   bill = unit * 5
# elif unit <=200:
#   bill = 100 * 5 + (unit - 100) * 7
# elif unit <=300:
#   bill = 100 * 5 + 100 * 7 + (unit - 200) * 10
# elif unit >=300:
#   bill = 100 * 5 + 100 * 7 + 100 * 10 + (unit - 300) * 15

# print(f"The bill is {bill}")


