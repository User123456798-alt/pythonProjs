r1 ={
    "math":{
        "a":96,
        "b":84,
        "c":60,
    },
    "history":{
        "a":40,
        "b":35,
        "c":50,
    },
    "english":{
        "a":20,
        "b":60,
        "c":47,
        "d":100
    },
    "science":{
        "a":45,
        "b":35,
        "c":70,
        "d":100
    },
}
r2 ={
    "math":{
        "a":94,
        "b":95,
        "c":63,
        "d":46
    },
    "history":{
        "a":84,
        "b":85,
        "c":73,
        "d":90
    },
    "english":{
        "a":88,
        "b":83,
        "c":90,
        "d":73
    },
    "science":{
        "a":99,
        "b":74,
        "c":56,
        "d":70
    },
}
r3 = {
    "maths" : {
        "sai" : 100,
        "ravi" : 98,
        "kumar" : 95,
        "suresh" : 98
    },
    "science" : {
        "sai" : 91,
        "ravi" : 97,
        "kumar" : 60,
    },
    "english" : {
        "ravi" : 79,
        "kumar" : 86,
        "suresh" : 95
    },
    "Telugu" : {
        "sai" : 97,
        "ravi" : 90,
        "kumar" : 93,
        "suresh" : 65
    },
    "Hindi" : {
        "sai" : 88,
        "ravi" : 98,
        "kumar" : 90,
        "suresh" : 96
    }
}

def assignGrade(grade:float):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
def findEligbleStudents(report:dict):
    students = set()
    for k,v in report.items():
        students = students|set(v.keys())
    for k,v in report.items():
        currStudents = []
        for i,j in v.items():
            currStudents.append(i)
        for s in list(students):
            if s not in currStudents:
                students.discard(s)
    return students

# print(findEligbleStudents(r3))
# print(findEligbleStudents(r1))

def studentAnylisis(report:dict):
    students = {}
    ilegableStudents = []
    classes = 0
    for i,v in report.items():
        classes+=1
        for j,k in report[i].items():
            if j not in students:
                students[j] = k
            else:
                students[j] = students[j] + k
    for i,v in report.items():
        for j,k in students.items():
            if j not in v:
                ilegableStudents.append(j)
    first = ""
    second = ""
    for i,v in students.items():
        if v in ilegableStudents:
            break
        grade = students[i] / classes
        students[i] = grade
        if (second == "" or grade > students[second]):
            if first == "" or grade > students[first]:
                second = first
                first = i
            else:
                second = i
        print(i+" : Average = "+str(grade)+", Grade = "+assignGrade(grade))

    if first != "":
        print ("Class First : "+first+"("+str(students[first])+")")
    if second != "":
        print ("Class Second : "+second+"("+str(students[second])+")")

# studentAnylisis(r1)
#studentAnylisis(r3)

def subejctAnylisis(report:dict):
    eligableStudents = findEligbleStudents(report)
    for i,v in report.items():
        total = 0
        students = 0
        for j,k in v.items():
            if j in eligableStudents:
                students+=1
                total += k
        ave = total / students
        print(i+" : Average = "+str(ave)+", Grade = "+assignGrade(ave))

# subejctAnylisis(r1)
# subejctAnylisis(r3)

def highScorers(report:dict,subject:str):
    eligableStudents = findEligbleStudents(report)
    for i,v in report.items():
        if i == subject:
            for j,k in v.items():
                if k > 90 and j in eligableStudents:
                    print(j+" : "+str(k))
            break

# highScorers(r2,"math")
# highScorers(r3,"maths")

def reportCard(report:dict,student:str):
    for i,v in report.items():
        subjectsCovered = False
        for j,k in v.items():
            if j == student:
                subjectsCovered = True
                grade = k
                print(i+" : "+str(grade)+"("+assignGrade(grade)+")")
                break
        if not subjectsCovered:
            print(i+" : 0(F)")

    

# reportCard(r1,"a")    
# reportCard(r3,"sai")    