import sys
import os.path
import json
import re

# emailpassword
# Shitty breach to parse

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

            email = re.search("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}", line)
            if email is not None:
                split = line.split(email.group(0))
                print(BreachItem(email.group(0).lower(), split[1]).toJSON())
            else:
                print(BreachItem('', split[1]).toJSON())

    return 0

class BreachItem:
    def __init__(self, email, password):
        self.alias = email.split('@')[0] if '@' in email else ''
        self.domain = email.split('@')[1] if '@' in email else ''
        self.password = password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())