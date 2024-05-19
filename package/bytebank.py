from datetime import date

class Employee:
    def __init__(self, name, birth_date, salary):
        self._name = name
        self._birth_date = birth_date
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def age(self):
        birth_year = self._birth_date.split('/')[-1]
        actual_year = date.today().year
        
        return actual_year - int(birth_year)

    def bonus_calculate(self):
        value = self._salary * 0.1
        if value > 1000:
            value = 0

        return value

    def last_name(self):
        full_name = self._name.strip()
        split_full_name = full_name.split(' ')
        
        return split_full_name[-1] 

    def __str__(self):
        return f'Funcionario({self._name}, {self._birth_date}, {self._salary})'
    
