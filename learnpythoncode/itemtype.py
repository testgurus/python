#Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'python', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print("Type of ",item, " is ", type(item))