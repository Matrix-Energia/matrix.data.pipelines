from app import main

def test_capital_case():
    assert main.capital_case('semaphore') == 'Semaphore'