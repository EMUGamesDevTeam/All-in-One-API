import subprocess, configparser, time, os
from getpass import getpass as paswd
config = configparser.ConfigParser()
clear = lambda: os.system('clear')

clear()

with open("extras/art.txt", "r") as f:
    print(f.read())

print("Generating config file...")
try:
   time.sleep(0.5)
except KeyboardInterrupt:
    exit()

if not os.path.exists("config.ini"):
    os.mknod("config.ini")
else:
    print("File already exists, deleting...")

try:
   time.sleep(2)
except KeyboardInterrupt:
    exit()

try:
    pythonver  = input("Enter your Python command (e.g. \"python3.7\", leave blank for 3.7): ")
    tdbport    = input("Enter TitleDB port (defaults to 6543): ")
    tdbsqlname = input("Enter TitleDB MySQL database user name (defaults to \"titledb\"): ")
    tdbsqlpass = paswd("Enter TitleDB MySQL database user password (not echoed): ")
    tdbauthsec = paswd("Enter TitleDB auth secret (not echoed): ")
    sqlhost    = input("Enter MySQL host (valid for both Wii Shop and TitleDB, defaults to localhost): ")
    tdbsqldb   = input("Enter TitleDB MySQL database (defaults to \"titledb\"): ")
    wscport    = input("Enter Wii Shop Channel API port (defaults to 9871): ")
    wscsitetc  = input("Enter Wii Shop Channel website name (defaults to \"wiishop\"): ")
    wscsqlname = input("Enter Wii Shop Channel MySQL database user name (defaults to \"wiisoap\"): ")
    wscsqlpass = paswd("Enter Wii Shop Channel MySQL database user password (not echoed): ")
    wscsqldb   = input("Enter Wii Shop Channrl MySQL database (defaults to \"wiisoap\"): ")
except KeyboardInterrupt:
    exit()

if wscsqlname == "":
    wscsqlname == "wiisoap"

if wscsqldb == "":
    wscsqldb = "wiisoap"

if wscsitetc == "":
    wscsitetc = "wiishop"

if wscport == "":
    wscport = "9871"

if pythonver == "":
    pythonver = "python3.7"

if sqlhost == "":
    tdbsqlhost = "localhost"

if tdbsqldb == "":
    tdbsqldb = "titledb"

if tdbsqlpass == "" or wscsqlpass == "" or tdbauthsec == "":
    print("You must give a password!")
    time.sleep(0.2)
    print("Aborting!")
    exit(1)
if tdbsqlname == "":
    tdbsqlname = "titledb"

if tdbport == "":
    tdbport = "6543"

config["TitleDB"] = {"address": "127.0.0.1", "port": tdbport, "mysqlname": tdbsqlname, "mysqlpass": tdbsqlpass, "mysqlhost": tdbsqlhost, "mysqldb": tdbsqldb}
config["WiiShop"] = {"address": "127.0.0.1", "port": wscport, "sitename": wscsitetc, "mysqlname": wscsqlname, "mysqlpass": wscsqlpass, "mysqldb": wscsqldb}
try:
   with open("config.ini", "w") as configfile:
        print("Writing configuration to config.ini file...")
        time.sleep(0.2)
        config.write(configfile)
except KeyboardInterrupt:
    exit()
