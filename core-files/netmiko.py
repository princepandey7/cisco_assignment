from netmiko import ConnectHandler
from getpass import getpass


# dictionary lists
cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_881)

#print(net_connect.find_prompt())
#output = net_connect.send_command('show ip int brief')
#print(output)

with open("conf.txt", "r") as f, open("cmdoutput.txt", "w") as nf:
    for line in f:
        output = net_connect.send_command(line)
        nf.write(output)
net_connect.disconnect()