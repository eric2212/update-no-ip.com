import requests
import socket

# Thay đổi các thông tin sau cho phù hợp với tài khoản No-IP của bạn
NOIP_USERNAME = 'your_noip_username'
NOIP_PASSWORD = 'your_noip_password'
NOIP_HOSTNAME = 'your_noip_hostname'
# URL để cập nhật IP
NOIP_UPDATE_URL = f'https://dynupdate.no-ip.com/nic/update?hostname={NOIP_HOSTNAME}'

def get_private_ip():
    # Lấy địa chỉ IP của thiết bị từ tất cả các giao diện mạng
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))  # Kết nối đến Google DNS
        ip_address = s.getsockname()[0]
    except Exception as e:
        ip_address = 'Could not determine IP'
    finally:
        s.close()
    return ip_address

def update_noip(ip):
    # Cập nhật IP riêng lên No-IP
    response = requests.get(NOIP_UPDATE_URL, auth=(NOIP_USERNAME, NOIP_PASSWORD), params={'myip': ip})
    return response.text

if __name__ == '__main__':
    # Lấy IP riêng
    private_ip = get_private_ip()
    print(f'Private IP Address: {private_ip}')
    
    # Cập nhật IP riêng lên No-IP
    update_result = update_noip(private_ip)
    print(f'Update Result: {update_result}')
