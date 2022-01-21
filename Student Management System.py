import getpass
import sys


def add_students(id, name, cls, m1="", m2=""):
    s = open("student_db", "a")
    s.write(",".join(map(str, [id, name, cls, m1, m2])))
    s.write("\n")
    s.close()


def add_teacher(id, name, cls, subject):
    t = open("teacher_db", "a")
    t.write(",".join(map(str, [id, name, subject, cls, subject])))
    t.write("\n")
    t.close()


def search_student(id):
    s = open("student_db")
    for i in s:
        if (str(id) in i):
            print(i)
            s.close()
            return ("Id Found")
    s.close()
    return ("Id not found")


def search_teacher(id):
    t = open("teacher_db")
    for i in t:
        if (str(id) in i):
            print(i)
            t.close()
            return ("Id Found")
    t.close()
    return ("Id not found")


def delete_record(file_name, id):
    try:
        file_obj = open(file_name, "r")
        obj_lst = [i.strip().split(",") for i in file_obj.readlines()]
        obj_w = open(file_name, "w")
        for ele in obj_lst:
            if (ele[0] != str(id)):
                temp = ",".join(map(str, ele)) + "\n"
                obj_w.write(temp)
    finally:
        obj_w.close()
        file_obj.close()


def update_record(file_name, id, name, cls, m1="", m2=""):
    try:
        file_obj = open(file_name, "r")
        obj_lst = [i.strip().split(",") for i in file_obj.readlines()]
        obj_w = open(file_name, "w")
        for ele in obj_lst:
            if (ele[0] != str(id)):
                temp = ",".join(map(str, ele)) + "\n"
                obj_w.write(temp)
            if (ele[0] == str(id)):
                if (file_name == "student_db"):
                    temp = ",".join(map(str, [id, name, cls, m1, m2])) + "\n"
                else:
                    temp = ",".join(map(str, [id, name, cls, sub]))

                obj_w.write(temp)
    finally:
        obj_w.close()
        file_obj.close()


def Student_menu():
    print("************************************")
    print("Welcome Student")
    print("************************************")
    print("Hit 1 for student details:")
    choice = int(input("Enter your choice:"))
    if (choice == 1):
        id = int(input("Enter your id:"))
        search_student(id)
    else:
        print("........................................")
        print("Thank You")
        print("........................................")
        exit


def Teacher_menu():
    print("***********************************")
    print("Welcome Teacher!!")
    print("***********************************")
    print("Hit 1 to search a student ")
    print("Hit 2 to update student's mark")
    choice = int(input("Enter your choice"))
    if (choice == 1):
        a = input("Enter student id")
        search_student(a)
    elif (choice == 2):
        a = int(input("Enter student id:-"))
        b = input("Enter student name:-")
        c = input("Enter student class:-")
        d = int(input("Enter student marks1:-"))
        e = int(input("Enter student marks2:-"))
        update_record("student_db", a, b, c, m1=d, m2=e)

    else:
        print("..........................................")
        print("Thank You")
        print("..........................................")
        exit


def add_logindetail_S(id, password, default, user):
    try:
        obj = open("login_db", "w")
        obj.write(",".join(map(str, [id, password, default, "S"])))
        obj.write("\n")
    finally:
        obj.close()


def add_logindetail_T(id, password, default, user):
    try:
        obj = open("login_db", "w")
        obj.write(",".join(map(str, [id, password, default, "T"])))
        obj.write("\n")
    finally:
        obj.close()


def validpassword(password):
    specialcharacter = "@#$%&!*"
    flag = True
    if (len(password) < 6 and len(password) > 12):
        print("INVALID  PASSWORD LENGTH")
        flag = False
    if not any(char.isdigit() for char in password):
        print("Password should contain at least 1 number between 0-9")
        flag = False
    if not any(char.isupper() for char in password):
        print("Password should contain at least 1 letter in upper case[A-Z]")
        flag = False
    if not any(char.islower() for char in password):
        print("Password should contain at least 1 letter in lower case[a-z]")
        flag = False
    if not any(char in specialcharacter for char in password):
        print("Password should contain at least 1 special character")
        flag = False
    if flag:
        return flag


def main():
    Login = input("enter login id:")
    password = getpass.getpass()
    choice = None
    if (Login == "Admin" and password == "Admin"):
        print(" Welcome Admin!!!")
        print("************************************")
        print("Welcome to Student Management System")
        print("************************************")
        print("1. Add New Student")
        print("2. Remove student")
        print("3. Add teacher")
        print("4. Remove teacher")
        print("q. Quit")

        while (choice != "q"):
            choice = input("Enter your choice: ")
            if (choice == "1"):
                id = int(input("Enter the id:-"))
                name = input("Enter the name of student:-")
                cls = input("Enter the class:-")
                add_students(id, name, cls, m1='', m2='')
                add_logindetail_S(id, "password", "D", "S")
            if (choice == "2"):
                id = int(input("Enter student's id to be removed:"))
                delete_record("student_db", id)
                delete_record("login_db", id)
            if (choice == "3"):
                id = int(input("Enter the teacher's id:"))
                name = input("Enter the teacher's name:")
                cls = input("Enter the class in which the teacher teaches:")
                add_teacher(id, name, cls, subject='')
                add_logindetail_T(id, "password", "D", "T")
            if (choice == "4"):
                id = int(input("Enter the teacher's id to be removed:"))
                delete_record("student_db", id)
                delete_record("teacher_db", id)
    else:
        try:
            objr = open("login_db", "r")
            login_list = [i.strip().split(",") for i in objr.readlines()]
            objw = open("login_db", "w")
            for login in login_list:
                if (login[0] == str(Login)):
                    if (login[1] == password):
                        if (login[2] == "D"):
                            print("enter a new password:")
                            password = getpass.getpass()
                            if (validpassword(password)):
                                delete_record("login_db", login[0])
                                add_logindetail_S(login[0], password, "Y", login[3])
                                add_logindetail_T(login[0], password, "Y", login[3])
                                print("password changed successfully !! please Relogin")
                        if (login[3] == "S"):
                            print("welcome student")
                            print("call function for student functionality")
                            Student_menu()
                        else:
                            if (login[3] == "T"):
                                Teacher_menu()
                    else:
                        print("id and password are incorrect")

        finally:
            objw.close()
            objr.close()


main()
