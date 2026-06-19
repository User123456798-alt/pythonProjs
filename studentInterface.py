
def printAllStudents(lines:list):
    for line in lines:
        print(line,end="")
    print("\n")

def addStudent(file:str):
    with open(file , "a+")as f:
        ids = []
        for line in f.readlines():
            Id = ""
            for ch in line:
                if ch.isdigit:
                    Id = Id+ch
                elif ch == ",":
                    break
            ids.append(int(Id))
        f.seek(0,2)
        line = ""
        if f.tell() != 0:
            line = "\n"+line
        line = line + input("Enter student name: ")
        Id = int(input("Enter student Id: "))
        if Id in ids:
            print("id already in system")
            return
        line = line + ":"+str(Id)+","
        line = line + "English:"+input("Enter grade in English: ")+","
        line = line + "Math:"+input("Enter grade in Math: ")+","
        line = line + "Science:"+input("Enter grade in Science: ")+","
        line = line + "Social Studies:"+input("Enter grade in Social Studies: ")+","
        line = line + "Computers:"+input("Enter grade in Computers: ")
        f.seek(0,2)
        f.write(line)

def findStudent(lines:list):
    mode = int(input("Search by 1.Name or 2.Id: "))
    if mode == 1:
        name = input("Enter Name: ")
        for line in lines:
            curName = ""
            for ch in line:
                if ch == ":":
                    break
                else:
                    curName = curName + ch
            if name == curName:
                print(line)
                break
    elif mode == 2:
        Id = input("Enter Id: ")
        if len(Id) != 8:
            print("invaid id")
            return
        for line in lines:
            curId = ""
            for ch in line:
                if ch.isdigit():
                    curId = curId + ch
                elif ch == ",":
                    break
            if Id == curId:
                print(line)
                break
    else:
        print("invalid input")

def removeStudent(file:str):
    with open(file, "r") as f:
        lines  = f.readlines()    
        mode = int(input("Search by 1.Name or 2.Id: "))
        f.seek(0,0)
    newLines = []
    if mode == 1:
        name = input("Enter Name: ")
        for line in lines:
            data = extractData(line)
            if data[0].split(":")[0] == name:
                continue
            newLines.append(line)
        if newLines[-1][:0] == "\n":
            newLines[-1] = newLines[-1][:-1]
        with open(file,"w") as f:
            f.writelines(newLines)
    elif mode == 2:
        Id = input("Enter Id: ")
        if len(Id) != 8:
            print("invaid id")
            return
        for line in lines:
            data = extractData(line)
            if data[0].split(":")[1] == Id:
                continue
            newLines.append(line)
            if newLines[-1][:0] == "\n":
                newLines[-1] = newLines[-1][:-1]
        with open(file,"w") as f:
            f.writelines(newLines)
    else:
        print("invalid input")

def main():
    try:
        file = input("Enter file name: ")
        lines = ""
        cmd = 0
        with open(file,"r") as f:
            f.seek(0)
            while cmd != 5:
                lines = f.readlines()
                cmd = int(input("Enter desired comand\n" \
                "1.Distplay all student records\n" \
                "2.add a student record\n" \
                "3.find a student record\n" \
                "4.remove a student\n" \
                "5.Quit\n"))
                match cmd:
                    case 1:
                        printAllStudents(lines)
                    case 2:
                        addStudent(file)
                    case 3:
                        findStudent(lines)
                    case 4:
                        removeStudent(file)
                    case 5:
                        print("Ending program")
                    case _:
                        print("invalid cmd")

    
    except Exception as e:
        print(e)

def extractData(line:str):
    return line.split(",")

main()