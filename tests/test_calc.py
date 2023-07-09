from app.calculator import Calculator

# Позитивный тест для метода adding()
def test_adding():
    # Создаем экземпляр класса Calculator
    calc = Calculator()
    # Проверяем, что 2 + 2 = 4
    assert calc.adding(2, 2) == 4

# Позитивный тест для метода subtracting()
def test_subtracting():
    # Создаем экземпляр класса Calculator
    calc = Calculator()
    # Проверяем, что 5 - 3 = 2
    assert calc.subtraction(5, 3) == 2

# Позитивный тест для метода multiplying()
def test_multiplying():
    # Создаем экземпляр класса Calculator
    calc = Calculator()
    # Проверяем, что 3 * 4 = 12
    assert calc.multiply(3, 4) == 12

# Позитивный тест для метода dividing()
def test_dividing():
    # Создаем экземпляр класса Calculator
    calc = Calculator()
    # Проверяем, что 10 / 2 = 5
    assert calc.division(10, 2) == 5