# print("hello world")
# print("hello world")
# # print("hello world")
# """uyfyfiu
# print("hello world")
# ydyifuoihoh"""
# print("hello world")
# x = 5
# print(x)
# x= 'demo'
# print(x)
# #tuple
# x = (1,2)
# print(x)
# #list
# x = [1,2]
# print(x)
# x.append(3)
# print(x)
# #dictionary
# x = {"max":24,"sam":{"age":34}}
# print(x)
# print(x["max"])
# print(x["sam"]["age"])

def addition(a:int,b:int):
    print(a+b)
    return a+b
c = addition(2,4)
print(c)
def slicer(a:str,b:int,c:int):
    return a[:c]
print(slicer("mathew",3,6))
x = "some string"
print(x[:30])
a=5
b=4
if (a==b):
    print("equal")
else:
    print("not equal")

def oldest(people:dict,a:str,b:str):
    if a not in people and b not in people:
        print("invalid keys")
    elif(people.get(a,0)>people.get(b,0)):
        print(a + " is older")
    elif(people.get(a,0)<people.get(b,0)):
        print(b + " is older")
    else:
        print("they are the same age")

p1 = {"sam":24,"jake":23,"max":25,"greg":15}

oldest(p1,"sam","jake")
oldest(p1,"max","frank")
oldest(p1,"sam","max")
oldest(p1,"frank","dave")

def substrings(string:str,n:int,k:int):
    if (n+k > len(string)):
        return string
    else:
        first = string[:n]
        last = string[k*-1:]
        return first + last
    
print(substrings("company",2,3))
print(substrings("company",5,4))

def eligable(pepole:dict,a:str):
    if a not in pepole:
        print("invalid key")
    elif(pepole[a] >= 18):
        print("eligable")

eligable(p1,"greg")
eligable(p1,"sam")

def mask(a:str):
    return "xxxxxx" + a[-4:]

print(mask("1111111111"))
print(mask("1111112324"))

def removal(a:str,b:str):
    aLen = len(a)
    bLen = len(b)
    if(aLen>bLen):
        return a[:bLen]
    elif(bLen>aLen):
        return b[:aLen]
    else:
        return "same length"

print(removal("arc","company"))
print(removal("arc","art"))

def snake(a:str):
    if(a[0]==a[-1]):
        print("same")
    else:
        print("diffrent")

snake("arnfejwokfneoia")
snake("art")

def years(name:str,a:dict,b:dict):
    if name not in a or a[name] not in b:
        return "invalid input"
    return b[a[name]]

p2 = {"chris":1,"tyler":2}
p3 = {1:40,2:80}

print(years("chris",p2,p3))
print(years("tyler",p2,p3))

def fullName(f:str,l:str):
    return f +" "+l

print(fullName("mathew","abraham"))
print(fullName("tyler","blevins"))

def rec(l:int,w:int):
    perim = 2*l + 2*w
    area = l*w
    print("perimeter: "+str(perim)+" area: "+str(area))

rec(2,3)
rec(0,3)

def polarity(x:int):
    if(x>0):
        return "positive"
    elif(x<0):
        return "negative"
    else:
        return "zero"
    
print(polarity(1))
print(polarity(-1))
print(polarity(0))
    
def email(first:str,last:str,comp:str):
    return first+"."+last+"@"+comp+".com"

print(email("mathew","abraham","ubisoft"))
print(email("tyler","blevins","fortnight"))

def divisable(num:int,k:int):
    if(num%k==0):
        return"divisable"
    else:
        return "not divisable"
    
print(divisable(30,15))
print(divisable(15,2))

def swap(s:str):
    if(len(s)>1):
        f = s[0]
        l= s[-1]
        return l + s[1:len(s)-1]+f
    else:
        return s

print(swap("python"))
print(swap("a"))

def cut(s:str,n:int):
    return s[::n]

print(cut("five",2))
print(cut("exelsior",4))
