import requests


def test_hello():

    url = "http://127.0.0.1:5000/hello"

    res_response = requests.get(url=url)

    assert res_response.text == "Hello, Glowbyte!"


def test_calc():

    url = "http://127.0.0.1:5000/calc"
    a, b = 5, "sgsg"

    res_response = requests.get(url=url, params={"a": a, "b": b})

    assert res_response.status_code == 200
