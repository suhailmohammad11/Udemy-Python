#In this Program we are unpacking tuples.
#We have a list of tuples and we find Employee with highest Work hours.



def BestEmployee(Work_hours):
    max_hours=0
    employee_of_the_month=""
    
    for employee,hours in Work_hours:
        if hours>max_hours:
            max_hours=hours
            employee_of_the_month=employee
            
        
    return (employee_of_the_month,max_hours)

Work_hours=[("Abubakar", 1000),("Suhail",200), ("Hameed",150),("Umaer", 450)]
result= BestEmployee(Work_hours)
print(result)