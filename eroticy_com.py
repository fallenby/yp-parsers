import sys
import msvcrt
import os.path
import json

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
            d = ':' if (((':' in line) and (';' not in line)) or ((':' in line) and (';' in line))) else ';'
            print(BreachItem(line.split(d)[0].lower(), line.split(d)[1]).toJSON())

    return 0

class BreachItem:
    def __init__(self, email, password):
        self.alias = email.split('@')[0]
        self.domain = email.split('@')[1]
        self.password = password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())