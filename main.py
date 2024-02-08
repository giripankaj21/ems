class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class EmployeeManagementSystem:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_employee(self, employee):
        with open(self.file_name, 'a') as file:
            file.write(f"{employee.emp_id},{employee.name},{employee.position},{employee.salary}\n")

    def view_employees(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                emp_id, name, position, salary = line.strip().split(',')
                employee = Employee(emp_id, name, position, salary)
                print(employee)

    def search_employee(self, emp_id):
        with open(self.file_name, 'r') as file:
            for line in file:
                emp_data = line.strip().split(',')
                if emp_data[0] == emp_id:
                    return Employee(emp_data[0], emp_data[1], emp_data[2], emp_data[3])
        return None


def main():
    system = EmployeeManagementSystem("employees.txt")

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            new_employee = Employee(emp_id, name, position, salary)
            system.add_employee(new_employee)
            print("Employee added successfully.")

        elif choice == '2':
            print("\nEmployee List:")
            system.view_employees()

        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            employee = system.search_employee(emp_id)
            if employee:
                print("Employee found:")
                print(employee)
            else:
                print("Employee not found.")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
