# import copy


# listX =["x"]
# listX.append("t")
# listY =["y"]
# listX += listY
# dictX = {"a":1,"c":4}
# dictY = {"a":2,"b":2}
# # dictX.update(dictY)
# # updatedDict = dictX|dictY
# updatedDict = {**dictX,**dictY}
# # print(updatedDict)
# def higherMerge(d1:dict,d2:dict):
#     dictNew = copy.deepcopy(d2)
#     for k,v in d1.items():
#         if k in dictNew:
#             if dictNew[k] < v:
#                 dictNew[k] = v
#         else:
#            dictNew[k] = v
#     return dictNew

# # print(higherMerge(dictX,dictY))
# # print(dictY)

# a = set()
# a = {1,2}
# a.add(1)
# b = set()
# b = {3,2,4}
# # print(a.union(b))
# # print(a|b)
# # a.update(b)
# # print(a)
# # print(b)

# l = [4,3,2,3,2,3,4,3,3,4]

# def unique(l:list):
#     return list(set(l))

# print(unique(l))
x = "name:8-digit-id,English:grade,Mathematics:grade,Science:grade,Social Studies:grade,Computers:grade"
studentData =x.split(",")
print(studentData)
def extractData(string:str,index:int = 0):
    return string.split(":")[index]
print(studentData[0])
print(extractData(studentData[1],1))
x= [ "a:28493020,English:70,Mathematics:64,Science:34,Social Studies:94,Computers:30", 
"b:47392043,English:98,Mathematics:83,Science:85,Social Studies:96,Computers:83"]