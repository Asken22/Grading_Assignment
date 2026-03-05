students = {
"Arun": [80, 90, 85],
"Bala": [70, 75, 72],
"Charan": [95, 92, 96]
}

#intialsing all the variables
N_dictionary={}
grade={}
reportCard={}
Pass=0
Fail=0

#function for average
def average(students):
    for key in students:
        Average=sum(students[key])/len(students[key])
        N_dictionary[key]=round(Average,2)
    return N_dictionary

#function for  grading
def classify_grades(N_dictionary):
    A=90
    B=75
    C=60
    for key in N_dictionary:
        if N_dictionary[key]>=A:
            grade[key]=N_dictionary[key],"A"
        elif N_dictionary[key]>=B:
            grade[key]=N_dictionary[key],"B"
        elif N_dictionary[key]>=C:
            grade[key]=N_dictionary[key],"C"
        else:
            grade[key]=N_dictionary[key],"F"
    return grade

#function for pass status
def report(grade,passinggrades=70):
    for key in grade:
        global Pass,Fail
        if int(grade[key][0])>=70:
            reportCard[key]=grade[key][0],grade[key][1],"Pass"
            Pass+=1
        else:
            reportCard[key]=grade[key][0],grade[key][1],"Fail"
            Fail+=1
    return reportCard,Pass,Fail

#function for printing
def Print_result(reportCard):
    T_student=len(reportCard)
    global Pass,Fail
    print("====Student Grade Report====")
    for key in reportCard:
        print(f"{key} | Avg:{reportCard[key][0]} | Grade:{reportCard[key][1]} | Status={reportCard[key][2]} ")
    print("===========================")
    print(f"Total Students:{T_student}")
    print(f"Passed: {Pass}")
    print(f"Failed: {Fail}")

#calling all the functions 
average(students)
classify_grades(N_dictionary)
report(grade,71)
Print_result(reportCard)



        
    

    
    
