""" Write a function that receives a list of student records,where
each record contains a student's name and a list of marks. In one
pass through the records, determine the student with the highest average,
count how many students passed every subject, and calculate the class-wide average of all
individuls marks. Handle empty reords and students with no marks without crashing."""

def students_reports(students):
    highest_avg = 0
    topper = None
    passed_count = 0
    total_marks = 0
    total_subjects = 0
    
    for student in students:
        name = student["name"]
        marks = student["marks"]
        
        if len(marks) == 0:
            continue
        avg = sum(marks)/len(marks)
        
        if topper is none or avg > highest_avg:
            highest_avg = avg
            topper = name
            
        if min(marks) >= 40:
            passed_count += 1
            
        total_marks += sum(marks)
        total_subjects += len(marks)
        
    if total_subjects > 0:
        class_avg = total_marks/total_subjects
    else:
        class_avg = 0
        
    print("Topper",topper)
    print("Highest average",highest_avg)
    print("students passed all subjects",passed_count)
    print("Class average",class_avg)
    
    students = [
    {"name": "Pratyush", "marks": [80, 90, 85]},
    {"name": "Maitrik", "marks": [70, 35, 60]},
    {"name": "Shubham", "marks": [95, 90, 98]},
    {"name": "Reeya", "marks": []}
]

student_report(students)