import requests
from bs4 import BeautifulSoup
import certifi
import urllib3

# use mint API from github - mimic for webscraping using click() from selenium(?)
# https://github.com/mrooney/mintapi/blob/master/mintapi/api.py
def main():
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    url = 'https://verified.capitalone.com/sic-ui/#/esignin'
    http.request('GET', url)
    response = requests.get(url, auth=('user','pw'), verify = True)
    page = BeautifulSoup(response.text, "lxml")
    print(page)
'''
payload = {
    'barcode': 'your user name/login',
    'telephone_primary': 'your password',
    'persistent': '1'  # remember me
}

session = requests.session()
r = requests.post(URL, data=payload)
print r.cookies'''



main()
