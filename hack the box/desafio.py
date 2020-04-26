#!-*-coding: utf8-*-
import requests
from bs4 import BeautifulSoup
import hashlib

# requisição 
sess = requests.session()
url = 'http://docker.hackthebox.eu:30571'
page = sess.get(url)
print(page)

# Beautifoul
soup = BeautifulSoup(page.text,'html.parser')
print(soup.prettify())
hash_to_md5 = soup.find_all('h3')[0].get_text()
print("To Encrypt hash = " + hash_to_md5)

# md5
md5 = hashlib.md5(hash_to_md5.encode())
md5_result = md5.hexdigest()
print("hash MD5 =" + md5_result)

result_final = sess.post(url, data = {'hash': md5_result})
print(result_final.text)
