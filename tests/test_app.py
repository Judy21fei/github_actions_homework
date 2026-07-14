from myapp.app import add, subtract

def test_add():
    """Тест для функції додавання."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Тест для функції віднімання."""
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4