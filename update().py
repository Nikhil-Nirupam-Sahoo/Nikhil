import pickle
import os
def writedata():
    f1=open("students.dat", "wb")
    n=int(input("Enter number of students: "))
    for i in range(n):
        s=eval(input("Enter student details in the form of a tuple: "))
        pickle.dump(s, f1)
    f1.close()

def update():
    fr=open("students.dat", "rb")
    fw=open("temp.dat", "wb")
    try:
        while True:
            s1=pickle.load(fr)
            if s1['mark']>=33:
                pickle.dump(s1, fw)
                print(s1)
    except EOFError:
        pass
    fr.close()
    fw.close()
    os.remove("students.dat")
    os.rename("temp.dat", "students.dat")

#main
writedata()
update()