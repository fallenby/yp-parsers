import sys
import os.path
import json

# XStrikeX:2b385def1fad60118a69456234fdb788:ahaia@live.dea:173.245.51.208
# username:password_hash:email:ip_address

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
            split = fix_split(line.split(':'))

            print(BreachItem(split[0], split[1], split[2].lower(), split[3]).toJSON())

    return 0

def fix_split(split_line):
    # I could clean this if up but it would be fucking messy and take time so fuck it

    for i in range(0, len(split_line)):
        if ((len(split_line[i]) == 32) and ('@' in split_line[i + 1]) and (split_line[i + 2].count('.') == 3))\
            or (len(split_line[i]) == 32) and ('@' not in split_line[i + 1]) and (split_line[i + 2].count('.') == 3):
                if i > 1:
                    return [':'.join(split_line[:i])] + split_line[i:]
                else:
                    return [''.join(split_line[:i])] + split_line[i:]
        elif '@' in split_line[i]:
            # Line with empty password hash
            if i > 2:
                return [':'.join(split_line[:i])] + [''] + split_line[i:]
            else:
                return [''.join(split_line[:i])] + [''] + split_line[i:]

    return [':'.join(split_line)[:-3], '', '', '']

class BreachItem:
    def __init__(self, username, password_hash, email, ip_address):
        self.username = username if (username is not None) else ''
        self.alias = email.split('@')[0] if ('@' in email) else ''
        self.domain = email.split('@')[1] if ('@' in email) else ''
        self.password_hash = password_hash if (password_hash is not None) else ''
        self.ip_address = ip_address if (ip_address is not None) else ''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())