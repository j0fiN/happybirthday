import requests as req
import os
url = "http://127.0.0.1:5001/jobin"

r = req.request("GET", url, headers = {'key': 'notildore#2020'})
ans = r.text
print(ans)