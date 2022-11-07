from login_page import login_page

def test_login_valid():
     result  = login_page("standard_user","secret_sauce")
     assert result == "https://www.saucedemo.com/inventory.html"


def test_login_invalid_username():
    result = login_page("standard_user1", "secret_sauce")
    assert result == "https://www.saucedemo.com/"

def test_login_invalid_password():
    result = login_page("standard_user", "12333")
    assert result == "https://www.saucedemo.com/"