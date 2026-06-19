# try:
#     num = int(input("Enter a number: "))
#     print(100 / num)
#     [2,1][5]

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("only integers acepted")

# # except Exception as e:
# #     print(e)

# def divide(x:int,y:int):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         print("user entered a zero for the second input")
#     except Exception as e:
#         print(e)
#     finally:
#         print("divide fin")

# print(divide(2,0))
# print(divide(2,2))

# class InvaidAgeError(Exception):
#     pass

# try:
#     age = -1 
#     if age < 0:
#         raise InvaidAgeError("age entered was less that 0")
# except InvaidAgeError:
#     print("age should be above 0")
# file = open("r.txt", "r")


# print(file.read())

# file.close()
# file = open("sample.txt", "r")

# for line in file:
# 	print(line)

# file.close()


# content = file.read()
# for line in file:
# lines = file.readlines()
# print(lines)

# file.close()
# with open("sample.txt", "r") as file:
#     content = file.read()

# print(content)
# file = open("sample.txt", "w")
# file.write("Hello World")
# # file.close()
# file = open("sample.txt", "a")

# file.write("New Line\n")

# file.close()

# try:
#     inFile = input("enter file: ")
#     with open(inFile,"r") as file:
#         content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("invalid file")
# with open("sample.txt", "r+") as f:
#     lines = f.readlines()
#     f.seek(0)
#     lines = lines[:4] + ["abc\n"] + lines[4:]
#     f.writelines(lines)
# f.seek(offset, whence)

# f.seek(0, 2)
# f.seek(-5, 1)   
with open("sample.txt", "rb") as f:
    f.seek(-15,2)
    content = f.read()
    print(content)