# Place code below to do the munging part of this assignment.

import os

def munge():
    # You must write the code using plain Python.
    # Issues your program must address:
    # read the data directly from the file 66/data/GLB.Ts+dSST.txt
    platform_agnostic_file_path = os.path.join('data', 'GLB.Ts+dSST.txt')
    with open(platform_agnostic_file_path) as f:
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
        data[i] = data[i].split(',')[:-1]


    d_last_ = data[-1]
    t = [int(x) for x in data[-2]]
    t_m = int(sum(t[1:13])/12)
    # J-D D-N    DJF  MAM  JJA  SON
    d_last = [int(x) for x in d_last_]
    for i in range(1,13):
        if d_last[i]==0:
            d_last[i] = t_m

    if d_last[13] == 0:
        d_last[13] = int(sum(d_last[1:13]) /12)

    if d_last[14]==0:
        d_last[14] =  int(sum(d_last[1:12]) /11)

    if d_last[15]==0:
        a = d_last[1:3]
        a.append(int(data[-2][12]))
        d_last[15] =int(sum(a) /3)
    if d_last[16] == 0:
        d_last[16] = int(sum(d_last[3:6]) /3)
    if d_last[17] == 0:
        d_last[17] = int(sum(d_last[6:9]) /3)
    if d_last[18] == 0:
        d_last[18] = int(sum(d_last[9:12]) / 3)


    data[-1] = [str(x) for x in d_last]
    # data.pop(-1)

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

    platform_agnostic_file_path = os.path.join('data', 'clean_data.csv')
    with open(platform_agnostic_file_path, 'w') as f:
        for e in data:
            f.write(','.join(e) + '\n')



munge()






