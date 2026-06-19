import pythonProjs.grading as grading

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
        "suresh" : 91
    },
    "english" : {
        "sai" : 98,
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

def totalReport(report:dict):
    grading.subejctAnylisis(report)
    grading.studentAnylisis(report)
    for k,v in report.items():
        grading.highScorers(report,k)
        passing = 0
        students = 0
        for i,j in v.items():
            students += 1
            if j >= 60:
                passing += 1
        print(k + " : "+str(passing/students*100)+"% passing")

totalReport(r3)