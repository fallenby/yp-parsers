import sys
import os.path
import json
import re

# email:password

def main():
    if len(sys.argv) <= 1:
        print("Not enough arguments; please specify the file you want to parse.")
        return 1

    filename = sys.argv[1]
    
    if not os.path.isfile(filename):
        print ("The file you provided does not exist.")
        return 1

    d = ':'

    with open(filename) as f:
        for line in f:
            if d not in line:
                continue

            line = line.strip()
            split = line.split(d)

            print(BreachItem(split[0].lower(), split[1]).toJSON())

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