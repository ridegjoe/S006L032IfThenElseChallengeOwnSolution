# TIM BUCHALKA'S COMPLETE PYTHON MASTERCLASS
#
# START OF CHALLENGE FOR PROGRAM FLOW IN PYTHON                                                                                                                                                       # plus all additionals, each showing the addition name, and addition price, and a grand/final total for the
# Write a small program to ask for name and age
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday
# (they must be over 18 and under 31)
# If they are, welcome them to the holiday,
# otherwise print a (polite) message refusing them entry.
# END OF CHALLENGE FOR PROGRAM FLOW IN PYTHON
#
#      link to the Complete Python Masterclass of Tim Buchalka at udemy.com:
#      https://www.udemy.com/python-the-complete-python-developer-course/
#

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
if 18 < age < 31:
    print("Welcome to the holiday!")
else:
    print("Unfortunately you are not eligible for this holiday!")
