message_1 = '''
Welcome to University Eligibility Checker for Pec University.
Input the necessary details below to ascertain your eligibility for
admission
'''
message_2 = '''
Thank you for using this product, hope you gained admission 
and We look forward to welcoming you to our Institution.
'''
department = '''
1. Computer Science
2. Mass Communication
'''
print(message_1)
full_name = input("What is your name: ")
school = input("What is your Secondary School: ")
print(department)
choose_department = input("Which department do you want to apply for: ")

admitted = []
not_admitted = []

if choose_department is "Computer Science" or "1":
    print("Eligibility checker for Computer Science")
    jamb_score = int(input("What is your JAMB score: "))
    maths_grade = input("What was your grade in Mathematics: ")
    english_grade = input("What is your grade in English Language: ")
    biology_grade = input("What is your grade in Biology: ")
    chemistry_grade = input("What is your grade in Chemistry: ")
    physics_grade = input("What is your grade in Physics: ")
    passed_interview = input("Did you pass the interview: ")
    
    if jamb_score >= 250 and maths_grade is "C" or "B" or "A" and english_grade is "C" or "B" or "A" and biology_grade is "C" or "B" or "A" and chemistry_grade is "C" or "B" or "A" and physics_grade is "C" or "B" or "A" and passed_interview is "Yes":
        admitted.append(full_name)
        print(f"Dear {full_name}, you are eligible for admission to Computer Science")
    else:
        not_admitted.append(full_name)
        print(f"Dear {full_name}, you are not eligible for admission to Computer Science")
        
   
if choose_department is "Computer Science" or "1":
    print("Eligibility checker for Computer Science")
    jamb_score = int(input("What is your JAMB score: "))
    maths_grade = input("What was your grade in Mathematics: ")
    english_grade = input("What is your grade in English Language: ")
    literature_grade = input("What is your grade in Literature: ")
    history_grade = input("What is your grade in History: ")
    government_grade = input("What is your grade in Government: ")
    passed_interview = input("Did you pass the interview:")
    
    if jamb_score >= 250 and maths_grade is "C" or "B" or "A" and english_grade is "C" or "B" or "A" and literature_grade is "C" or "B" or "A" and history_grade is "C" or "B" or "A" and government_grade is "C" or "B" or "A" and passed_interview is "Yes":
        admitted.append(full_name)
        print(f"Dear {full_name}, you are eligible for admission to Computer Science")
    else:
        not_admitted.append(full_name)
        print(f"Dear {full_name}, you are not eligible for admission to Computer Science")    

print(message_2)