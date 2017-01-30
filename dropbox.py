import sys
import os.path
import json
import codecs

# email:password_hash

def main():
    if len(sys.argv) <= 1:
        print("Not enough arguments; please specify the file you want to parse.")
        return 1

    filename = sys.argv[1]
    
    if not os.path.isfile(filename):
        print ("The file you provided does not exist.")
        return 1

    hash_type = 'bcrypt' if 'bf_' in filename else 'sha1' 
    d = ':'

    with codecs.open(filename, "r") as f:
        for line in f:
            line = line.strip()
            
            if len(line) == 0:
                continue

            try:
                print(BreachItem(line.split(d)[0].lower(), line.split(d)[1], hash_type).toJSON())
            except:
                print(line, file=sys.stderr)
                quit()

    return 0

class BreachItem:
    def __init__(self, email, password_hash, password_hash_type):
        self.alias = email.split('@')[0] if '@' in email else email
        self.domain = email.split('@')[1] if '@' in email else ''
        self.password_hash = password_hash
        self.password_hash_type = password_hash_type

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())