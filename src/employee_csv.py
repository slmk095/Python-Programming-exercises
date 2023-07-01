elif selection == 2:
    write_handle = open("salary_employee.csv", "w")

    for i in salary_employees:
        employee_info = [i.id, i.name, i.monthly_salary]
        write_handle.write(my_join(employee_info, ","))
        write_handle.write("\n")
    write_handle.close()
    print(len(salary_employees), " employee(s) added to salary_employee.csv")

elif selection == 3:
    salary_employees = []
    read_handle = open("salary_employee.csv", "r")
    for i in read_handle:
        employee_attributes = my_split(i.rstrip(), ",")
        salary_employees.append(SalaryEmployee(employee_attributes[0], employee_attributes[1], employee_attributes[2]))
    write_handle.close()
    print(len(salary_employees), " employee(s) read from salary_employee.csv")
