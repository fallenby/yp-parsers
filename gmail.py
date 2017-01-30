import sys
import os.path
import json
import codecs

# tobi.lehman@gmail.com:m
# email:password

def main():
    if len(sys.argv) <= 1:
        print("Not enough arguments; please specify the file you want to parse.")
        return 1

    filename = sys.argv[1]
    
    if not os.path.isfile(filename):
        print ("The file you provided does not exist.")
        return 1

    with codecs.open(filename, "r", encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            d = ':'

            if len(line) == 0:
                continue 
            elif (':' not in line) and ('@' in line):
                # Only e-mail address
                print(BreachItem(line.split(d)[0].lower()).toJSON())
                quit()
            elif (':' not in line) and ('@' not in line):
                # Only password
                print(BreachItem('', line.split(d)[0]).toJSON())
            else:
                # Password and e-mail address
                print(BreachItem(line.split(d)[0].lower(), line.split(d)[1]).toJSON())

    return 0

class BreachItem:
    def __init__(self, email, password = ''):
        self.alias = email.split('@')[0] if '@' in email else ''
        self.domain = email.split('@')[1] if '@' in email else ''
        self.password = password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())