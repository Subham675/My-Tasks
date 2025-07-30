# a=float(input("please enter the first number : " ))
# b=float(input("please enter the second number: " ))
# c=float(input("please enter the third number : " ))
# d=float(input("please enter the fourth number : " ))
# print()
# sum=lambda a,b,c,d:(a+b+c+d)
# substraction=lambda a,b,c,d:((a+b)-(c+d))
# multiplication=lambda a,b,c,d:(a*b*c*d)
# divition=lambda a,b,c,d:((a+b)/(c+d)) if c+d!=0 else "not divisible by zero"
# avg=lambda a,b,c,d:(a+b+c+d)/4
# percentage=lambda a,b,c,d:(a+b+c+d)*100/400

# print("sum is :",sum(a,b,c,d))
# print("substraction is :",substraction(a,b,c,d))
# print("multiplication is :", multiplication(a,b,c,d))
# print("divition is :",divition(a,b,c,d))
# print("avg is :",avg(a,b,c,d))
# print("percentage is :",percentage(a,b,c,d))
# print()


import phonenumbers
from phonenumbers import geocoder, carrier

# Replace this with the phone number you want to check
phone_number = phonenumbers.parse("+14155552671")  # US number example

# Get the region (location)
location = geocoder.description_for_number(phone_number, "en")
print("Location:", location)

# Get the carrier (network provider)
service_provider = carrier.name_for_number(phone_number, "en")
print("Carrier:", service_provider)