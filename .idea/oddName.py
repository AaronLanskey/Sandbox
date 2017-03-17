""" Aaron Lanskey"""
userName = input("Please give your name:\t")
while userName == "":
    userName = input("Please give your name:\t")
for x in range(0,len(userName),2):
    print(userName[x])