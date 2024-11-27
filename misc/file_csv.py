import csv
#import pandas

data = '''Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8
'''

print(data)

filename = "/tmp/employee.csv"
with open(filename, mode='w') as csv_file:
    csv_file.write(data)

employee_dicts = []
try:
    with open(filename, mode='r') as csv_file:
        rows = ( row.rstrip().split(',') for row in csv_file )
        cols = next(rows)
        print('cols:', cols)
        employee_dicts += [ dict(zip(cols, fields)) for fields in rows if len(fields) > 1 ]
except:
    pass

print("Employees", employee_dicts)

filename_backup = "/tmp/employee2.csv"
with open(filename_backup, mode='w') as csv_file:
    fieldnames = employee_dicts[0].keys()
    print("field names: ", fieldnames)
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()
    for employee in employee_dicts:
        csv_writer.writerow(employee)

print("test csv.DictReader")
with open(filename, mode='r') as csv_file:
    employee_dicts = list(csv.DictReader(csv_file))
    print("employee dicts: ", employee_dicts)        


