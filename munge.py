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

    for i, d in enumerate(data[1:]):
       data[i+1] = [int(x) for x in d]

    t_m = []  #  Annual average from January to December
    for i in range(1,13):
        _t = 0
        for j in range(1,len(data)-1):
            _t += data[j][i]
        _t = int( _t / (len(data)-2))
        t_m.append(_t)


    # first line  D-N    DJF
    d_first = data[1]
    a = d_first[1:12]
    a.append(t_m[-1])
    d_first[14] = int(sum(a)/12)
    a = d_first[1:3]
    a.append(t_m[-1])
    d_first[15] = int(sum(a)/3)
    data[1] = d_first


    # 2024 last line  J-D  D-N    DJF  MAM  JJA  SON

    d_last = data[-1]
    index_y = data[-1].index(0)
    if index_y <= 12:
        for i in range(index_y,13):
            d_last[i] = t_m[i-1]  # instead of mean of all year of mounth

    d_last[13] = int(sum(d_last[1:13]) /12)

    a = d_last[1:12]
    a.append(data[-2][12])
    d_last[14] = int(sum(a) /12)

    a = d_last[1:3]
    a.append(int(data[-2][12]))
    d_last[15] =int(sum(a) /3)

    d_last[16] = int(sum(d_last[3:6]) /3)

    d_last[17] = int(sum(d_last[6:9]) /3)

    d_last[18] = int(sum(d_last[9:12]) / 3)


    data[-1] = d_last

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
    with open(platform_agnostic_file_path, 'w') as csvfile:
        for index, num in enumerate(data):

            line = [str(x) for x in num]
            line = ','.join(line)

            if index != len(data) - 1:
                csvfile.write(line + '\n')
            else:
                csvfile.write(line)


munge()