import sys
import msvcrt
import os.path
import json

# userid-|--|-email-|-hash-|-hint-|--

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
            d = '-|-'
            print(BreachItem(line.split(d)[0], line.split(d)[2].lower(), line.split(d)[3], line.split(d)[4]).toJSON())

    return 0

class BreachItem:
    def __init__(self, user_id, email, password_encrypted, hint):
        self.alias = email.split('@')[0]
        self.domain = email.split('@')[1]
        self.password_encrypted = password_encrypted
        self.hint = hint
        self.user_id = user_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())