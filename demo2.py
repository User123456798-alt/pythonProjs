# #logical operator and or not
listEligable = ["greg","richard","micheal"]
listNotEligable = ["sam","richard","frank"]


# def eligable(name:str,age:int):
#     if age>=18 and name in listEligable and name not in listNotEligable:
#         return"eligable"
#     return "not eligable"
    
# print(eligable("greg",32))
# print(eligable("sam",32))
# print(eligable("richard",32))
# print("richard".upper())
# print("AveDFEFSDee".lower())

# for i in range(5):
#     print(i)
# for i in range(1,5):
# #     print(i)   
# for i in range(1,5,2):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)
# for i in listEligable:
#     print (i)
# for i in "mathew":
#     if i == "m":
#         continue
#     elif i == "t":
#         break
#     print(i)
# for index,i in enumerate(listEligable):
# # #     print(index,i)
# # for i in range(3):
# #     for j in range(3):
# #         print(i,j)

# def factorial(n:int):
#     total = 1
#     for i in range(1,n+1):
#         total = total*i
#     return total
# print(factorial(1))
# print(factorial(4))

# def factorialW(n:int):
#     total = 1
#     i = 1
#     while i <n+1:
#         total = total*i
#         i+=1
# #     return total
# # print(factorialW(1))
# # print(factorialW(4))
# p3 = {1:40,2:80}
# for k,v in p3.items():
#     print(k,v)
# def squareList(nums:list):
#     squares = []
#     for i in nums:
#         squares.append(i**2)
#     return squares
# print(squareList([2,5,1]))
# def squareListE(nums:list):
#     squares = []
#     for i in nums:
#         if i%2 == 0:
#             squares.append(i**2)
#     return squares
# print(squareListE([2,5,1]))
# a= " "
# b = a.split(" ")
# print(b)
# def vowels(string:str):
#     total = 0
#     a = string.lower()
#     v= ["a","e","i","o","u"]
#     for i in a:
#         if i in v:
#             total += 1
#     return total
# print(vowels("mathew"))
# print(vowels("mthth"))
# def secondLargest(nums:list):
#     max = 0
#     max2 = 0
#     if len(nums) <=1:
#         return -1
#     elif nums[0] > nums [1]:
#         max = nums[0]
#         max2 = nums[1]
#     else:
#         max = nums[1]
#         max2 = nums[0]
#     for i in nums[2:]:
#         if i > max2 and not i == max:
#             if i > max:
#                 max2 = max
#                 max = i
#             else:
#                 max2 = i
#     return max2
# print(secondLargest([2,3,4]))
# print(secondLargest([3,4,2]))
# print(secondLargest([2,2,2]))
# print(secondLargest([3]))
# # print(secondLargest([10,12,16, 18, 20,20, 1, 9]))
# def reverse(string:str):
#     fin =""
#     for i in range (len(string)-1,-1,-1):
#         fin = fin+string[i]
#     return fin
# print(reverse("mathew"))
# print(reverse("m"))
def amount(string:str):
    amountUp = 0
    amountLw = 0
    for i in string:
        if i.isupper():
            amountUp += 1
        else:
            amountLw += 1
    return amountUp,amountLw
print(amount("SDedSe"))
print(amount("eeeee"))
def palindrome(string:str):
    half = 1
    for i in range(0,len(string)//2,1):
        if not string[i] == string[len(string)-half]:
            return False
        half+=1
    return True
print(palindrome("theht"))
print(palindrome("theeht"))
print(palindrome("theeht"))
print(palindrome("theaht"))
def occur(string:str,char:str):
    total = 0
    for i in string:
        if i == char:
            total+=1
    return total
print(occur("thhesh","h"))
print(occur("tes","h"))
def sum(nums:list):
    total = 0
    for i in nums:
        total+=i
    return total
print (sum([2,4,1]))
print (sum([0,0,0]))
def triangle(n:int):
    prev = ""
    for i in range(1,n+1):
        prev = prev + str(i)
        print(prev)
triangle(5)
triangle(1)
def multiChar(string:str):
    chars = []
    multi = ""
    for i in string:
        if i in chars and not i in multi:
            multi = multi + i
        else:
            chars.append(i)
    return multi
print(multiChar("ddsdadwa"))
print(multiChar("dseg"))
def anagram(s1:str,s2:str):
    for i in s1:
        if i in s2:
            char = i
            newS2 =""
            for i in range(0,len(s2)):
                if s2[i] == char:
                    newS2 = newS2 + s2[i+1:] 
                    break
                else:
                    newS2 = newS2 + s2[i]
            s2=newS2
        else:
            return False
    return True
print(anagram("are","era"))
print(anagram("are","ere"))
def fizzBuzz(n:int,a:int,b:int):
    for i in range(1,n+1):
        if i % a == 0 and i % b == 0:
            print("FIZZBUZZ")
        elif i % a == 0:
            print("FIZZ")
        elif i % b == 0:
            print("BUZZ")
        else:
            print(i)
fizzBuzz(4,2,4)
fizzBuzz(10,2,3)
def adj(nums:list):
    fin = -1
    prev = 0
    for i in nums:
        if i - prev > 1:
            fin = i-1
            prev = i
        else:
            prev = i
    print(fin)
adj([1,2,4,5])
adj([1,2,3])
def pyramid(n:int):
    for i in range(n):
        for j in range(n- i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print("\n")
pyramid(3)
pyramid(10)
def removeVowels(string:str):
    v = ["a","e","i","o","u"]
    return [i for i in string if i not in v]
print(removeVowels("ecvres"))
print(removeVowels("oiuae"))

