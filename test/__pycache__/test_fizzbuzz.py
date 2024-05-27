from fizzbuzz import fizzbuzz


def test_pass_div_3():
    assert fizzbuzz(3) == "Fizz"

def test_pass_div_5():
    assert fizzbuzz(5) == "Buzz"

def test_pass_div_5_3():
    assert fizzbuzz(15) == "FizzBuzz"

def test_pass_othe_case():
    assert fizzbuzz(8) == 8       
  
