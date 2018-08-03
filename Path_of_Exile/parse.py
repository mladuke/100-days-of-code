max_number_of_items = 50
items = []
for i in range(max_number_of_items):
    items.append([])
itemMap = {}
resistance =[]
life =[]
armour= []
att = []
i=1
printing = False
start = False
with open("Jugg_81.xml") as f:
     for line_of_text in f:
         if '<Item id' in line_of_text:
             start = True
             items[i].append(line_of_text.strip())
             printing= True
             continue
         elif '</Item>' in line_of_text:
            printing = False
            i=i+1
            continue
         elif '<Socket ' in line_of_text:
            temp = line_of_text.split('"')
            #print (temp)
            temp1 = temp[1]
            temp2 = temp[3]
            #print (temp1,temp2)
            if int(temp2) > 0: 
                itemMap[temp2] = temp1        
         elif '<Slot' in line_of_text:
             start = False
             temp = line_of_text.split('"')
             #print (temp)
             temp1 = temp[1]
             temp2 = temp[3]
             #print (temp1,temp2)
             if int(temp2) > 0: 
                 itemMap[temp2] = temp1         
         if start == True:             
             if 'Resistance' in line_of_text:
                 #print (i, line_of_text)
                 resistance.append([i,line_of_text])
             if 'Life' in line_of_text:
                 #print (i, line_of_text)
                 life.append([i,line_of_text])
             if 'Armour' in line_of_text:
                 #print (i, line_of_text)
                 armour.append([i,line_of_text])
             if ("all Attributes" in line_of_text or "Strength" in line_of_text or "Dexterity" in line_of_text or "Intelligence" in line_of_text):
                 #print (i, line_of_text)
                 att.append([i,line_of_text])
             if printing and 'Unique ID' not in line_of_text:
                items[i].append(line_of_text.strip())
print ()
print (itemMap)
list2 = [x for x in items if x != []]

list3 = []
list3=list2

for i in range(len(list2)):
    list3[i] =' \n * '.join(list2[i])

import csv
res = list3
csvfile = "Jugg_81.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        writer.writerow([val]) 
print ()
for i in range(len(resistance)):
    resistance[i][0] = itemMap[str(resistance[i][0])]
    print (resistance[i])
print ()
for i in range(len(life)):
    life[i][0] = itemMap[str(life[i][0])]
    print (life[i]) 
print ()
for i in range(len(armour)):
    armour[i][0] = itemMap[str(armour[i][0])]
    print (armour[i])
print ()
for i in range(len(att)):
    att[i][0] = itemMap[str(att[i][0])]
    print (att[i])
print ()
print ("File Saved")
