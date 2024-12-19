import re

logs = """[2024-12-14T03:37:47.467672-0800] INFO: isautil.py: test 1
[2024-12-14T03:37:47.467749-0800] DEBUG: isautil.py:3997 :  Retry 0
"""
# Example log line: [2024-12-14 14:30:21] INFO: User login successful for user123
log_pattern = r'\[(?P<timestamp>.+?)\]\s+(?P<level>INFO|ERROR|DEBUG):\s+(?P<message>.+)'


def save_log_file(file_path):
    with open(file_path, mode = 'w') as file:
        file.write(logs)

def parse_log_file(file_path):
    try:
        with open(file_path, mode = 'r') as file:
            for line in file:
                match = re.match(log_pattern, line)
                if match:
                    print(match.groupdict())
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error: {e}")

# Parse the log file
file_path = "/tmp/application.log"
save_log_file(file_path)
parse_log_file(file_path)