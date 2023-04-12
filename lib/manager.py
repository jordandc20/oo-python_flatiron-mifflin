from lib.employee import Employee

class Manager:
    all = []
    
    def __init__(self, manager_name, department, age):
        self.manager_name = manager_name
        self.department = department
        self.age = age
        Manager.all.append(self)
    
    def hire_employee(employee_name, salary, self):
        Employee(employee_name, salary, self.manager_name)
    
    # Manager.hire_employee('jane', 1000, m1)
    
    # @property
    # def employees(self):
    #     return self._employees
    
    # @employees.setter
    def employees(self):
        # if not hasattr(self, 'employees'):
        return [employee for employee in Employee.get_all_employees() if employee.manager_name == self.manager_name]
    
    @classmethod        
    def all_departments(cls):
        return [manager.department for manager in cls.all]
    
    @classmethod
    def average_age(cls):
        num_manager = len(cls.all)
        age_list = sum([manager.age for manager in cls.all])
        return age_list / num_manager
    
    @classmethod
    def get_all_managers(cls):
        return cls.all