'''
Given a file containing switch names, ports, Incoming BPS, Outgoing BPS, need to find out the top talking switches


cat machine.csv
SWITCH, PORTS, IBPS,OBPS
ARIS, ge-0/1, 5800000000, 5800000000
CISCO, ge-0/2, 1000000000, 5700027720
JUNIPER, ge-0/3, 2000000000,3000000000
HPE, ge-0/4,3000000000,4000000000


in this case machine name ARIS should be returned

if OBPS is greater but IBPS is lesser or vice-versa return machine name when either of them is greater.

'''

csv_data = '''SWITCH,PORTS,IBPS,OBPS
ARIS, ge-0/1, 5800000000, 5800000000
CISCO, ge-0/2, 1000000000, 5700027720
JUNIPER, ge-0/3, 2000000000,3000000000
HPE, ge-0/4,3000000000,4000000000
'''
import csv
import math

def write_data(file_path):
    with open(file_path, mode = 'w') as csv_file:
        csv_file.write(csv_data)

def get_greater_talking_machine(file_path):
    try:
        machines = []

        with open(file_path, mode = 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row)
                name = row['SWITCH']
                ibps = int(row['IBPS'])
                obps = int(row['OBPS'])
                machines += [ (name,  max(ibps, obps)) ]
        print(machines)
        machines.sort(key=lambda x: x[1], reverse=True)
        if machines:
            print(machines[0][0])
    except Exception as e:
        print(f"Error: {e}")

    return

file_path = "/tmp/switches_data.csv"
write_data(file_path)
get_greater_talking_machine(file_path)

