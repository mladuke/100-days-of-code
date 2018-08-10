##From https://www.reddit.com/r/dailyprogrammer/
##[2018-04-23] Challenge #358 [Easy] Decipher The Seven Segments
##
##Description
##
##Today's challenge will be to create a program to decipher a seven segment display, commonly seen on many older electronic devices.
##
##Input Description
##
##For this challenge, you will receive 3 lines of input, with each line being 27 characters long (representing 9 total numbers), with the digits spread across the 3 lines.
##Your job is to return the represented digits. You don't need to account for odd spacing or missing segments.
##
##Output Description
##
##Your program should print the numbers contained in the display.
##
##Challenge Inputs
##    _  _     _  _  _  _  _ 
##  | _| _||_||_ |_   ||_||_|
##  ||_  _|  | _||_|  ||_| _|
##
##    _  _  _  _  _  _  _  _ 
##|_| _| _||_|| ||_ |_| _||_ 
##  | _| _||_||_| _||_||_  _|
##
## _  _  _  _  _  _  _  _  _ 
##|_  _||_ |_| _|  ||_ | ||_|
## _||_ |_||_| _|  ||_||_||_|
##
## _  _        _  _  _  _  _ 
##|_||_ |_|  || ||_ |_ |_| _|
## _| _|  |  ||_| _| _| _||_ 
##
##
##Challenge Outputs
##123456789
##433805825
##526837608
##954105592

line = [[0 for i in range(27)] for j in range(3)]

##line[0] ="    _  _     _  _  _  _  _ " 
##line[1] ="  | _| _||_||_ |_   ||_||_|"
##line[2] ="  ||_  _|  | _||_|  ||_| _|"

##line[0] ="    _  _  _  _  _  _  _  _ "
##line[1] ="|_| _| _||_|| ||_ |_| _||_ "
##line[2] ="  | _| _||_||_| _||_||_  _|"

##line[0]=" _  _  _  _  _  _  _  _  _ " 
##line[1]="|_  _||_ |_| _|  ||_ | ||_|"
##line[2]=" _||_ |_||_| _|  ||_||_||_|"

line[0]=" _  _        _  _  _  _  _ "
line[1]="|_||_ |_|  || ||_ |_ |_| _|"
line[2]=" _| _|  |  ||_| _| _| _||_ "

for i in range(9):
    if line[0][i*3] == ' ' and line[0][(i*3)+1] == ' ' and line[0][(i*3)+2] == ' ':
        if line[1][i*3] == ' ':
            print ("1",end='')
        else:
            print ("4",end='')
    if line[0][i*3] == ' ' and line[0][(i*3)+1] == '_' and line[0][(i*3)+2] == ' ':
        if line[1][i*3] == ' ' and line[1][(i*3)+1] == '_' and line[1][(i*3)+2] == '|':
            if line[2][i*3] == '|':
                print ("2",end='')
            else:
                print ("3",end='')
        elif line[1][i*3] == '|' and line[1][(i*3)+1] == '_' and line[1][(i*3)+2] == ' ':
            if line[2][i*3] == ' ':
                print ("5",end='')
            else:
                print ("6",end='')
        elif line[1][i*3] == '|' and line[1][(i*3)+1] == '_' and line[1][(i*3)+2] == '|':
            if line[2][i*3] == '|':
                print ("8",end='')
            else:
                print ("9",end='')
        elif line[1][i*3] == ' ' and line[1][(i*3)+1] == ' ' and line[1][(i*3)+2] == '|':
            print ("7",end='')
        elif line[1][i*3] == '|' and line[1][(i*3)+1] == ' ' and line[1][(i*3)+2] == '|':
            print ("0",end='')
print("")
