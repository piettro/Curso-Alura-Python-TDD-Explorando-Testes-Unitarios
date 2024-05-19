from package.bytebank import Employee
import pytest
from pytest import mark

class TestClass:

    @mark.age
    def test_when_age_receive_13_03_2000_must_return_24(self):
        entry = '13/03/2000'
        expected = 24

        employee_test = Employee('Test', entry, 1111)
        result = employee_test.age()

        assert result == expected

    @mark.last_name
    def test_when_last_name_receive_lucas_carvalho_must_return_carvalho(self):
        entry = 'Lucas Carvalho'
        expected = 'Carvalho'

        employee_test = Employee(entry, '13/03/2000', 1111)
        result = employee_test.last_name()

        assert result == expected
    
    @mark.decrease_salary
    def test_when_decrease_salary_receive_100000_must_return_90000(self):
        entry = 100000
        entry_name = 'Piettro Rodrigues'
        expected = 90000

        employee_test = Employee(entry_name, '13/03/2000', entry)
        employee_test.decrease_salary()
        result = employee_test._salary

        assert result == expected

    @mark.bonus_calculate
    def test_when_bonus_calculate_receive_1000_must_return_100(self):
        entry = 1000
        expected = 100

        employee_test = Employee('Test', '13/03/2000', entry)
        result = employee_test.bonus_calculate()

        assert result == expected

    @mark.bonus_calculate
    def test_when_bonus_calculate_receive_1000000_must_return_exception(self):
        with pytest.raises(Exception):
            entry = 1000000
            employee_test = Employee('Test', '13/03/2000', entry)
            result = employee_test.bonus_calculate()

            assert result

    def test_return_str(self):
        name, birth_date, salary  = 'Test', '13/03/2000', 1000
        expected = f'Funcionario({name}, {birth_date}, {salary})'

        employee_test = Employee('Test', '13/03/2000', 1000)
        result = employee_test.__str__()

        assert result == expected