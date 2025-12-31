'''
You have been given two data files in CSV format, each of which contains specific statistics about various dinosaurs.
Using this formula to calculate the speeds of the dinosaurs found in the two files:
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * 9.8)


write a program that will:


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

def calculate_speed(stride_length: float, leg_length: float) -> float:
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)

def main():
    try:
        speeds = []

        leg_lengths = {}
        with open(filename1, mode = 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                leg_lengths[row['NAME']] = float(row['LEG_LENGTH'])

        with open(filename2, mode = 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row['NAME']
                stance = row['STANCE']
                stride_length = float(row['STRIDE_LENGTH'])
                if stance == 'bipedal' and name in leg_lengths:
                    leg_length = leg_lengths[name]
                    speed = calculate_speed(stride_length, leg_length)
                    speeds.append( (name, speed) )

        speeds.sort(key=lambda x: x[1], reverse=True)
        for name, _ in speeds:
            print(name)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()