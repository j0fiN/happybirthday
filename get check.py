import requests as req

url = "http://127.0.0.1:5001/franklin"

r = req.request("GET", url, headers = {'key':"1234"})
ans = r.text
print(ans)