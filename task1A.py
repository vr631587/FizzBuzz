import csv


with open("Trails.csv","r") as f:
    dict1={}
    
    data=csv.reader(f)
    for elements in data:
        if "CONDITION" == "GOOD"
