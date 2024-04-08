# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1956399
# Date: 2022/12/01 
p_count=mt_count=mr_count=e_count=pass_mark=defer_mark=fail_mark=0
markslist = []
idlist = []
def input_credits():
    global pass_mark
    global defer_mark
    global fail_mark
    while True:
        while True:
            try:
                pass_mark = int(input("Enter your credit at PASS: "))
                if pass_mark not in range(0,121,20):
                    print("Out of range\n")
                    continue
            except ValueError:
                print("Integer required\n")
                continue
            break
        while True:
            try:
                defer_mark = int(input("Enter your credit at DEFER: "))
                if defer_mark not in range(0,121,20):
                    print("Out of range""\n")
                    continue
            except ValueError:
                print("Integer required\n")
                continue
            break
        while True:
            try:
                fail_mark = int(input("Enter your credit at Fail: "))
                if fail_mark not in range(0,121,20):
                    print("Out of range\n")
                    continue
            except ValueError:
                print("Integer required\n")
                continue
            break
        total = pass_mark+defer_mark+fail_mark
        if total != 120:
            print("Total incorrect\n")
            continue
        decide_marks()
        break
        
def decide_marks():
    global p_count
    global mt_count
    global mr_count
    global e_count
    if (pass_mark == 120):
        print("Progress")
        p_marks = 'Progress - '+ str(pass_mark)+', '+str(defer_mark)+', '+str(fail_mark)
        markslist.append(p_marks)
        id_no = student_id
        idlist.append(id_no)
        p_count=p_count+1
        print()
    elif (pass_mark >= 100) and (pass_mark < 120):
        print("Progress (module trailer)")
        mt_marks = 'Progress (module trailer) - '+ str(pass_mark)+', '+str(defer_mark)+', '+str(fail_mark)
        markslist.append(mt_marks)
        id_no = student_id
        idlist.append(id_no)
        mt_count=mt_count+1
        print()
    elif (fail_mark >= 80):
        print("Exclude")
        e_marks = 'Exclude - '+ str(pass_mark)+', '+str(defer_mark)+', '+str(fail_mark)
        markslist.append(e_marks)
        id_no = student_id
        idlist.append(id_no)
        e_count=e_count+1
        print()
    else:
        print("Module retriever")
        mr_marks = 'Module retriever - '+ str(pass_mark)+', '+str(defer_mark)+', '+str(fail_mark)
        markslist.append(mr_marks)
        id_no = student_id
        idlist.append(id_no)
        mr_count=mr_count+1
        print()
    histogram()

def histogram():
    if occupation == 'staff':
        print("Would you like to enter another set of data?")
        choice = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
        if choice == 'q':
            print()
            print('-'*60)
            print('Histogram')
            print('Progress', p_count,'  :', '*'*p_count)
            print('Trailer', mt_count,'   :', '*'*mt_count)
            print('Retriever', mr_count,' :', '*'*mr_count)
            print('Exclude', e_count,'   :', '*'*e_count)
            print()
            print((p_count+mt_count+mr_count+e_count),'outcomes in total')
            print('-'*60)
            marks_list()
            textfile_save()
            dictionary()
        elif choice == 'y':
            get_student_id()
        else:
            print("Invalid option\n")
            histogram()
    else:
        exit

def marks_list():
    print("Part 2:")
    for i in range(len(markslist)):
        print(markslist[i])

def textfile_save():
    f=open('scores.txt', 'w')
    for i in range(len(markslist)):
        progress_entry = str(markslist[i])
        f.write(progress_entry + '\n')
    f.close()
    print("\nPart 3:")
    f=open('scores.txt','r')
    data = f.read()
    f.close()
    print(data)

def dictionary():
    print("Part 4:")
    d={}
    for i in range(len(markslist)):
        d[idlist[i]]= markslist[i]
    for (k,v) in d.items():
        print(k,':',v,end=' ')

def student_or_staff():
    global occupation
    occupation = input("State your occupation ('student' or 'staff'): ")
    if occupation == 'student' or occupation == 'staff':
        get_student_id()
    else:
        print("Invalid option (Try 'student' or 'staff')\n")
        student_or_staff()
       
def get_student_id():
    global student_id
    student_id = input("\nEnter your student ID: ")
    if (len(student_id)) == 8:
        if student_id in idlist:
            print("Student ID has already entered")
            get_student_id()
        else:
            input_credits()
    else:
        print("Invalid Student ID (Should be in 'wXXXXXXX' format)")
        get_student_id()
   
student_or_staff()
