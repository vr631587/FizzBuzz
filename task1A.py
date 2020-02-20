import csv


with open("Trails.csv","r") as f:
    list1=[]
    
    data=csv.reader(f)
    for elements in data:
        list1.append((str(elements[9]),str(elements[1])))
    print(list1)

