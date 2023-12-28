# Character classes:
# We can use character classes to search a group of characters
# 1. [abc]===>Either a or b or c
# 2. [^abc] ===>Except a and b and c
# 3. [a-z]==>Any Lower case alphabet symbol
# 4. [A-Z]===>Any upper case alphabet symbol
# 5. [a-zA-Z]==>Any alphabet symbol
# 6. [0-9] Any digit from 0 to 9
# 7. [a-zA-Z0-9]==>Any alphanumeric character
# 8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)
#
# Pre defined Character classes:
# \s  Space character
# \S  Any character except space character
# \d  Any digit from 0 to 9
# \D  Any character except digit
# \w  Any word character [a-zA-Z0-9]
# \W  Any character except word character (Special Characters)
# .  Any character including special characters
#
# Qunatifiers:
# We can use quantifiers to specify the number of occurrences to match.
# a  Exactly one 'a'
# a+  Atleast one 'a'
# a*  Any number of a's including zero number
# a?  Atmost one 'a' ie either zero number or one number
# a{m}  Exactly m number of a's
# a{m,n}  Minimum m number of a's and Maximum n number of a's

# Notes
# 1. re.compile method is used to the object to regexobject
# 2. .match always check for first letter match else it will fail.


# 1.  write a pgm for valid mobile number
# import re
#
# lis = "9827776686"
# pattern="[7-9][0-9]{9}"
# result = re.fullmatch(pattern,lis)
# if result:
#     print("Valid mobile number")
# else:
#     print("not valid mobile number")
#
#
# st = "service is deployed and deployed version is 6@904"
#
# pattern1 = r"service is deployed"
# result1 = re.search(pattern1,st)
# print(result1)
# if result1:
#     print("service is deployed successfully")
# else:
#     print("not deployed successfully")
# pattern2 = r"\d+"
# result2 = re.findall(pattern2,st)
# version = ''.join(result2)
# print(result2)
# print(version)


# import re
#
# s = "hello my name 46is 65saksham"
#
# # st = "".join(s.split())
# # print(st)
# pt = r"[a]+"
# d = re.findall(pt,s)
# # print(d.group(0))
# print(d)

import re

# name = input("Enter the name which you want to search: ")
st = "my name is Saksham and house number is 509/11"

s = re.finditer("9{4}",st)
data = []
for i in s:
    print(i.group())
    data.append(i.group())
# for i in s:
#     if i.lower() == "{}".format(name.lower()):
#         data.append(i)
#         print("data found")
#
print(data)
# print(data)
# print(s.group(0),s.start(),s.end(),s)
print(s)
