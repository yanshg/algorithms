'''
read a file and count how many times an email address is found. 

It uses regular expressions to identify email patterns in the file:
'''

import re

data ='''
test emails:  a.b@c.com   a@c    1223@qq.com   1234@1234.com @c.net a@c.dom 
Invalid emails: b@.com b#c.com
good emails:   a@b.com
'''

pattern = r"[a-zA-Z0-9][a-zA-Z0-9.]*@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}"

def write_file(file_path):
    with open(file_path, mode = 'w') as file:
        file.write(data)


def count_email_addresses(file_path):
    # edge cases
    if not file_path:
        return 0
    
    count = 0

    try:
        with open(file_path, mode = 'r') as file:
            for line in file:
                # find email addresses in the line
                emails = re.findall(pattern, line)
                count += len(emails)
                print(line, "emails: ", emails)
    except FileNotFoundError:
        print(f"Error: file {file_path} not find")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

    return count


file_path = '/tmp/emails.txt'
write_file(file_path)
print(count_email_addresses(file_path))