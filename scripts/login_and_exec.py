from tapo_plug import tapoPlugApi
import json
import argparse

parser = argparse.ArgumentParser(description='Login to a TP-Link Tapo device and execute a command.')
#parser.add_argument('ip', help='IP address of the device')
parser.add_argument('config', help='JSON file containing the device IP and credentials')
parser.add_argument('command', help='Command to execute in JSON format')
args = vars(parser.parse_args())


#json/config.json
f_login = open(args['config'])
device = json.load(f_login)
print(tapoPlugApi.getDeviceInfo(device))
f_login.close()
print("Login successful")
f_command = open(args['command'])
command = json.load(f_command)
print(tapoPlugApi.send(command, device))
f_command.close()
print("Command sent")