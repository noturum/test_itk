from requests import post


files = {"file": open("./example.xlsx", "rb")}

r = post(url="http://127.0.0.1:8000/upload/", files=files)
r.text
