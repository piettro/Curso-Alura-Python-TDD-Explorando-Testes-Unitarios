from bytebank import Employee

def test_age():
    employee_test = Employee('Test', '13/03/2000', 1111)
    print(f'Teste = {employee_test.age()}')

    employee_test_2 = Employee('Test', '13/03/1999', 1111)
    print(f'Teste = {employee_test_2.age()}')

    employee_test_3 = Employee('Test', '01/12/1999', 1111)
    print(f'Teste = {employee_test_3.age()}')

test_age()