'''
Given 2 CSV files data1.csv and data2.csv, such as

Dinosaur      , Pedal         , Feet length
Dilophosaurus , Bipedal       , 3.0        
Troodon       , quadrupedal   , 4.2        
Sauropoda     , Bipedal       , 4.1        
Archaeopteryx , quadrupedal   , 2.5      

Dinosaur      , Stride Length , Max Age    
Archaeopteryx , 13.0          , 15         
Sauropoda     , 12.2          , 22         
Dilophosaurus , 14.1          , 37         
Troodon       , 12.5          , 71     
and Given following formula for computing speed,

Speed = ((Feet length * Stride Length)/ (Pedal) ) * g
I had to print out the names of Dinosaurs in increasing order of their speed.

I solved the question but did two minor mistakes.

'''

import csv

data1 = '''Dinosaur      , Pedal         , Feet length
Dilophosaurus , Bipedal       , 3.0        
Troodon       , quadrupedal   , 4.2        
Sauropoda     , Bipedal       , 4.1        
Archaeopteryx , quadrupedal   , 2.5
'''

data2 = '''Dinosaur      , Stride Length , Max Age    
Archaeopteryx , 13.0          , 15         
Sauropoda     , 12.2          , 22         
Dilophosaurus , 14.1          , 37         
Troodon       , 12.5          , 71     
'''

class Solution1:
    def __init__(self):
        self.get_data()

    def get_data(self):
        filename1 = "/tmp/data1.csv"
        with open(filename1, mode = 'w') as csv_file:
            for line in data1.split('\n'):
                if not line:
                    continue
                line = ','.join(list(map(str.strip, line.split(',')))) + "\n"
                print("line: ", line)
                csv_file.write(line)

        filename2 = "/tmp/data2.csv"
        with open(filename2, mode = 'w') as csv_file:
            for line in data2.split('\n'):
                if not line:
                    continue
                line = ','.join(list(map(str.strip, line.split(',')))) + "\n"
                print("line: ", line)
                csv_file.write(line)

        with open(filename1, mode = 'r') as csv_file:
            self.data1 = list(csv.DictReader(csv_file))
            print("data1: ", self.data1)

        with open(filename2, mode = 'r') as csv_file:
            self.data2 = list(csv.DictReader(csv_file))
            print("data2: ", self.data2)

    def get_fast_dinosaurs(self):
        dinosaurs = {}

        try:
            for dinosaur in self.data2:
                if not dinosaur:
                    continue

                name = dinosaur.get('Dinosaur')
                stride_length = dinosaur.get('Stride Length')
                if name and stride_length:
                    dinosaurs[name] = {}
                    dinosaurs[name]['Stride Length'] = float(stride_length)

            for dinosaur in self.data1:
                if not dinosaur:
                    continue
                
                name = dinosaur.get('Dinosaur')
                pedal = dinosaur.get('Pedal')
                feet_length = dinosaur.get('Feet length')

                if not name or name not in dinosaurs or not feet_length:
                    continue

                pedals = 1
                if pedal == 'Bipedal':
                    pedals = 2
                elif pedal == 'quadrupedal':
                    pedals = 4
                
                stride_length = dinosaurs[name]['Stride Length']                
                dinosaurs[name]['Speed'] = (float(feet_length) * stride_length) / pedals

            print(dinosaurs)
            for name, _ in sorted(dinosaurs.items(), key=lambda x: x[1]['Speed'], reverse=True):
                print(name)

        except:
            pass
        
class Solution2:
    def __init__(self):
        self.dinosaurs = {}

    def get_fast_dinosaurs(self):
        filename1 = "/tmp/data1.csv"
        with open(filename1, mode = 'w') as csv_file:
            csv_file.write(data1)

        filename2 = "/tmp/data2.csv"
        with open(filename2, mode = 'w') as csv_file:
            csv_file.write(data2)
        
        dinosaurs = {}
        with open(filename2, mode = 'r') as csv_file:
            headers = None
            for line in csv_file:
                fields = list(map(str.strip, line.strip().split(',')))
                print('data1: ', fields)
                if not headers:
                    headers = fields
                else:
                    data = dict(zip(headers, fields))
                    print(data)
                    name = data.get('Dinosaur')
                    stride_length = data.get('Stride Length')
                    if name and stride_length:
                        dinosaurs[name] = {}
                        dinosaurs[name]['Stride Length'] = float(stride_length)                 

        with open(filename1, mode = 'r') as csv_file:
            headers = None
            for line in csv_file:
                fields = list(map(str.strip, line.strip().split(',')))
                if not headers:
                    headers = fields
                else:
                    data = dict(zip(headers, fields))
                    name = data.get('Dinosaur')
                    pedal = data.get('Pedal')
                    feet_length = data.get('Feet length')

                    pedal_number = 1
                    if pedal == 'Bipedal':
                        pedal_number = 2
                    elif pedal == 'quadrupedal':
                        pedal_number = 4

                    if name and pedal and feet_length and name in dinosaurs:
                        stride_length = dinosaurs[name]['Stride Length']
                        dinosaurs[name]['Speed'] = (float(feet_length) * stride_length) / pedal_number

        print(dinosaurs)
        for name, _ in sorted(dinosaurs.items(), key=lambda x: x[1]['Speed'], reverse=True):
            print(name)




solution1 = Solution1()
solution1.get_fast_dinosaurs()

solution2 = Solution2()
solution2.get_fast_dinosaurs()