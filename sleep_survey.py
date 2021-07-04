carry_on = "y"
total_hours = 0
number_of_students = 0

while carry_on == "y":
    try:
        hours = int(input("How many hours do you sleep each night? "))
        total_hours += hours
        number_of_students += 1
        average = total_hours / number_of_students
        print("Average number of hours per night: ", average)
        carry_on = str(input("Do you want to carry on with the survey? y/n "))
        print("total of Students in the survey: ", number_of_students)
    except ValueError:
        print("Invaild in input. enter a number.")
        carry_on = "y"
