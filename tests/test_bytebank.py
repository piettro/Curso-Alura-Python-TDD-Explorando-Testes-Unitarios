from package.bytebank import Employee

class TestClass:
    def test_when_age_receive_13_03_2000_must_return_24(self):
        entry = '13/03/2000'
        expected = 24

        employee_test = Employee('Test', entry, 1111)
        result = employee_test.age()

        assert result == expected

    def test_when_last_name_receive_lucas_carvalho_must_return_carvalho(self):
        entry = 'Lucas Carvalho'
        expected = 'Carvalho'

        employee_test = Employee(entry, '13/03/2000', 1111)
        result = employee_test.last_name()

        assert result == expected