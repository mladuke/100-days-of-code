max_number_of_items = 50
items = []
for i in range(max_number_of_items):
    items.append([])    

i=0
printing = False
with open("lvl98_Jugg.xml") as f:
     for line_of_text in f:
         if '<Item id' in line_of_text:
             items[i].append(line_of_text.strip())
             printing= True
             continue
         elif '</Item>' in line_of_text:
            printing = False
            i=i+1
            continue
         if printing and 'Unique ID' not in line_of_text:
            items[i].append(line_of_text.strip())

list2 = [x for x in items if x != []]

list3 = []
list3=list2

for i in range(len(list2)):
    list3[i] =' \n * '.join(list2[i])

import csv
res = list3
csvfile = "lvl98_Jugg.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        writer.writerow([val]) 
        
print ("File Saved")
