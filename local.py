import requests

res = requests.post('http://127.0.0.1:3000/api/courses/2', json={"name": "Golang", "videos": 5})

print(res.json())
