import requests

NOIP_USERNAME = 'your_noip_username'
NOIP_PASSWORD = 'your_noip_password'
NOIP_HOSTNAME = 'your_noip_hostname'

NOIP_UPDATE_URL = f'https://dynupdate.no-ip.com/nic/update?hostname={NOIP_HOSTNAME}'

def get_current_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def update_noip(ip):
    response = requests.get(NOIP_UPDATE_URL, auth=(NOIP_USERNAME, NOIP_PASSWORD), params={'myip': ip})
    return response.text

if __name__ == '__main__':
    current_ip = get_current_ip()
    result = update_noip(current_ip)
    print(result)
