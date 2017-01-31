import sys
import os.path
import json

# username:email:ip:password

def main():
    if len(sys.argv) <= 1:
        print("Not enough arguments; please specify the file you want to parse.")
        return 1

    filename = sys.argv[1]
    
    if not os.path.isfile(filename):
        print ("The file you provided does not exist.")
        return 1

    with open(filename) as f:
        for line in f:
            line = line.strip()
            d = ':'

            if d not in line:
                continue

            split = line.split(d)

            try:
                print(BreachItem(split[0], split[1].lower(), split[2], split[3] if len(split) == 4 else '').toJSON())
            except:
                continue

    return 0

class BreachItem:
    def __init__(self, username, email, ip_address, password = ''):
        self.alias = email.split('@')[0] if '@' in email else ''
        self.domain = email.split('@')[1] if '@' in email else ''
        self.password = password
        self.username = username
        self.ip_address = ip_address

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())