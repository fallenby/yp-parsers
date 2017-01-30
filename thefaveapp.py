import sys
import os.path
import json
import codecs

# "",821647340c712ecc53e09a1a75d1a4df9cafb45a,7506b9db5e199660fcd10f7280bfbe1df6063509,wppro@comcast.net
# name,password,salt,email

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
            d = ','
            print(BreachItem(line.split(d)[0] if line.split(d)[0] != '""' else '', line.split(d)[1], line.split(d)[2], line.split(d)[3].lower()).toJSON())

    return 0

class BreachItem:
    def __init__(self, name, password_hash, password_salt, email):
        self.alias = email.split('@')[0] if '@' in email else ''
        self.domain = email.split('@')[1] if '@' in email else ''
        self.name = name
        self.password_hash = password_hash
        self.password_salt = password_salt

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())