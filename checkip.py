import os
from netmiko import ConnectHandler

user = os.environ["USER"]
password = os.environ["PASSWORD"]
enable_password = os.environ["ENABLE_PASSWORD"]
ios_device = {
    "device_type": "cisco_ios",
    "ip": "10.10.20.171",
    "username": "vishnu",
    "password": "vishnu",
    "secret": "cisco",
}
net_connect = ConnectHandler(**ios_device)
output = net_connect.send_command("show ip int brief")
print(output)
