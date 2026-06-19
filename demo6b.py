import requests


# url = "http://127.0.0.1:8000/students/hello"
# response = requests.get(url)
# print(response.json())

# url = "http://127.0.0.1:8000/students/students"
# response = requests.post(url,json={"id":9,"name":"wef","marks":90})
# print(response.json())

print(requests.get("http://127.0.0.1:8000/calulator/add?x=2&y=3").json())


