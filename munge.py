# Place code below to do the munging part of this assignment.
import re

def munge():
    # You must write the code using plain Python.
    # Issues your program must address:
    # read the data directly from the file 66/data/GLB.Ts+dSST.txt
    #

    with open('data/GLB.Ts+dSST.txt') as f:
        data = f.readlines()

    
    data = data[7:-6]
    
    data = [x for x in data if x.strip() != '']

    # the column headings are repeated on multiple lines throughout the file -
    # remove all but the first line of column headings.
    for i, e in enumerate(data):
        if e.startswith('Year') and i != 0:
            
            data.pop(i)

    # there is missing data indicated with *** figure out how to handle missing data so that your analyses are correct.
    
    for i, e in enumerate(data):
        
        data[i] = (',').join(e.split())
        data[i] = data[i].replace('****', '0').replace('***', '0')
        data[i] = data[i].split(',')[:-2]

    data.pop(-1)


    # the temperature anomalies in this data are given in 0.01 degrees Celsius.
    # Convert temperature anomalies to Farenheit, the US standard unit of temperature:
    # the formula to do this can be found within the data set
    # format the results so that there's one decimal place (use format with .1f as the second argument)
    # since this data is in fixed-width column format,
    # there are inconsistent numbers of spaces separating the numeric values
    for i, e in enumerate(data[1:]):
        for j, e1 in enumerate(e[1:]):
            data[i+1][j+1 ] = float(e1) * 0.01 * 9 / 5
            data[i+1][j+1 ]= format(data[i+1][j+1 ], '.1f')

    
    with open('data/clean_data.csv', 'w') as f:
        for e in data:
            f.write(','.join(e) + '\n') 








munge()
