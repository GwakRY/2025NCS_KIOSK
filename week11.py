import requests

#url = f"https://wttr.in/incheon?format=%c+%t"
url = f"https://wttr.in/incheon?&n&O"

response= requests.get(url)
print(response.status_code)
print(response.text)


if response.status_code == 200:
    print(response.text.strip())
else:
    print(f"상태 코드 : {response.status_code}")