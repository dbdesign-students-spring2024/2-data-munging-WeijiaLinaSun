
import csv
import os

def analyze():

    # opens up your cleaned up data file, data/clean_data.csv and imports it using Python's csv module.
    # outputs the average temperature anomaly in degrees Farenheit for each decade since 1880.
    # For example, output the average temperature anomaly for the decades:
    # 1880 to 1889
    # 1890 to 1899
    # 1900 to 1909
    # ...and so on.
    average_temperature = []
    platform_agnostic_file_path = os.path.join('data', 'clean_data.csv')
    with open(platform_agnostic_file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            t = 0
            for i in range(1,13):
                t += float(row[i+1])
            average_temperature.append(t/12)

    count = 0
    m = 0
    for i in range(0, len(average_temperature)):

        m += average_temperature[i]
        count +=1
        if count % 10 == 0:
            m /= 10
            print(f'{1870 + count} to {1879 + count}: {format(m, ".1f")}')
            m = 0

        if 1880 + count == 2020:

            for j in range(i+1, len(average_temperature)):

                m += average_temperature[j]
            m /= (len(average_temperature) - count)

            print(f'{1880 + count} to {1880 +len(average_temperature)-1 }: {format(m, ".1f")}')

analyze()