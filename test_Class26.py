import pytest
from Class26 import add, get_customer

@pytest.mark.addfunctionality
@pytest.mark.smoke
@pytest.mark.Regression
def test_add():
    result = add(3, 4)
    assert result == 7

@pytest.mark.addfunctionality
@pytest.mark.Regression
def test_add_negative():
    result = add(-3, 4)
    assert result == 1

@pytest.mark.addfunctionality
@pytest.mark.Regression
def test_add_negative_multiple():
    result = add(-3, -4)
    assert result == -7

@pytest.mark.addfunctionality
@pytest.mark.Regression
def test_add_float():
    result = add(3.4, 2.3)
    assert round(result) == 6

@pytest.mark.addfunctionality
@pytest.mark.Regression
def test_add_invalid():
    is_error_occured = False
    try:
        add('abc', 4)
    except:
        is_error_occured = True

    assert is_error_occured

@pytest.mark.bank
@pytest.mark.smoke
@pytest.mark.Regression
def test_bank_customer():
    result = get_customer(87666)
    assert result is not None
    assert result["name"] == "Veeresh"
    assert result["Account"] == 9865335
    assert result["bank"] == "HDFC"

@pytest.mark.bank
@pytest.mark.Regression
def test_bank_invalid():
    result = get_customer(1234)
    assert result == "No details found"

@pytest.mark.bank
@pytest.mark.Regression
def test_bank_invalid_empty():
    result = get_customer("")
    assert result == "No details found"

@pytest.mark.parametrize("input1,input2,output",[(1,2,3),(3,4,7),(5,6,11),(-1,-2,-3),(-4,1,-3)])
def test_add_multiple_input(input1,input2,output):
    result = add(input1,input2)
    assert result == output



