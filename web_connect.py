import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://verified.capitalone.com/sic-ui/#/esignin'
    response = requests.get(url, auth=('user','pw'), verify = False)
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
