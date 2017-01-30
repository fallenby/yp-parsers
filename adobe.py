import sys
import os.path
import json
import traceback

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

            # Some lines are empty, and some don't have proper formatting, so skip those
            if (len(line) == 0) or (d not in line):
                continue

            # Some lines are split over two lines for some reason, so we'll check
            # if the line ends with the terminating string, and if it doesn't,
            # grab the next line and concat it to the current one
            if not line.endswith('|--'):
                line += next(f).strip()

            try:
                print(BreachItem(line.split(d)[0], line.split(d)[2].lower(), line.split(d)[3], line.split(d)[4]).toJSON())
            except StopIteration:
                print("We seem to have reached the end of the file", file=sys.stderr)
                print(traceback.format_exc())
                quit()
            except Exception as e:
                print(traceback.format_exc())
                print(line, file=sys.stderr)
                quit()

    return 0

class BreachItem:
    def __init__(self, user_id, email, password_encrypted_base64, hint):
        self.username = email if '@' not in email else '' 
        self.alias = email.split('@')[0] if '@' in email else ''
        self.domain = email.split('@')[1] if '@' in email else ''
        self.password_encrypted_base64 = password_encrypted_base64
        self.hint = hint
        self.user_id = user_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


if __name__ == "__main__":
    sys.exit(main())