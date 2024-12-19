'''
You have been given two data files in CSV format, each of which contains specific statistics about various dinosaurs.
Using this formula to calculate the speeds of the dinosaurs found in the two files:
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * 9.8)


... write a program that will:


Take the paths of the two files as inputs
Parse the files
Calculate the speeds of the dinosaurs
Print only the names of the bipedal dinosaurs, ordered from fastest to slowest
The data files that you are given appear as follows:


$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore


$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
'''

csv_data1 ="""NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore
"""

filename1 = "/tmp/dataset1.csv"
with open(filename1, mode = 'w') as csv_file:
    csv_file.write(csv_data1)


csv_data2 ="""NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
"""

filename2 = "/tmp/dataset2.csv"
with open(filename2, mode = 'w') as csv_file:
    csv_file.write(csv_data2)    

import csv
import math

try:
    data1 = []
    with open(filename1, mode = 'r') as csv_file:
        data1 = list(csv.DictReader(csv_file))

    data2 = []
    with open(filename2, mode = 'r') as csv_file:
        data2 = list(csv.DictReader(csv_file))

    dinosaurs = {}
    speed_data = []

    for dinosaur in data2:
        name = dinosaur.get('NAME')
        stride_length = dinosaur.get('STRIDE_LENGTH')
        stance = dinosaur.get('STANCE')
        if name and stride_length and stance and stance == 'bipedal':
            dinosaurs[name] = {}
            dinosaurs[name]['STRIDE_LENGTH'] = stride_length

    for dinosaur in data1:
        name = dinosaur.get('NAME')
        leg_length = dinosaur.get('LEG_LENGTH')
        if name and name in dinosaurs and leg_length:
            stride_length = float(dinosaurs[name]['STRIDE_LENGTH'])
            leg_length = float(leg_length)
            speed = ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)
            speed_data += [ (name, speed) ]

    print(dinosaurs)
    print(speed_data)
    if speed_data:
        for name, _ in sorted(speed_data, key=lambda x: x[1], reverse=True):
            print(name)

except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"Error: {e}")



