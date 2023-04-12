class Employee:
    all = []
    
    def __init__(self, employee_name, salary, manager_name):
        self.employee_name = employee_name
        self.salary = salary
        self.manager_name = manager_name
        Employee.all.append(self)
        
    @classmethod    
    def get_all_employees(cls):
        return cls.all
    
    @classmethod
    def paid_over(cls, salary):
        return [employee for employee in cls.all if employee.salary > salary]

    @classmethod
    def find_by_department(cls, department):
        from .manager import Manager
        all_departments = Manager.get_all_managers()
        manager_department = [manager for manager in all_departments if manager.department == department]
        return manager_department[0].employees()[0].__dict__