import csv
import json
import os.path
import datetime

path = 'E:/Work/Michelin/'
data_file = 'michelin_data.csv'
full_f_name = path + data_file
full_tmp_name = path + 'tmp.csv'
path_cache = path + 'cache/'


def sell():
    """Add sale record to file"""
    regions = ['Georgia', 'Russia', 'Germany', 'Spain', 'USA', 'India', 'China']

    print('Select region for sale record: ')
    for i in range(len(regions)):
        print(f'{i}. {regions[i]}')

    tmp_region = input('Your choice of region? [1]: ')
    if tmp_region == '':
        tmp_region = regions[1]
    else:
        tmp_region = regions[int(tmp_region)]

    tmp_cai = int(input('Input cai: '))
    tmp_diameter = int(input('Input diameter: '))
    tmp_s = int(input('Input tire width: '))
    tmp_price = float(input('Input sell price: '))

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    tmp_date = str(year) + '-' + str(month) + str(day)

    print(tmp_diameter, tmp_s, tmp_cai, tmp_region, tmp_date, tmp_price)

    # fp = open(full_tmp_name, 'r', encoding='UTF-8')
    # line_reader = csv.reader(fp)
    # header = next(line_reader)
    # init_cntr = 0
    #
    # for i in line_reader:



def top():
    """Output the top of sales by regions"""
    tmp_num = input('Number of records to output? [15]: ')
    if tmp_num == '':
        tmp_num = 15
    else:
        tmp_num = int(tmp_num)

    # Check cache
    cache_file_name = path_cache + 'top' + str(tmp_num) + '.json'

    if os.path.isfile(cache_file_name):

        tmp_input = input('For this request cache file exist. Recalculate? Y/[N]: ')

        if tmp_input != 'Y' or tmp_input != 'y':
            fp = open(cache_file_name, 'r', encoding='UTF-8')
            data = json.load(fp)
            fp.close()

            for i in range(len(data)):
                print(data[i])

            return

    top_sales = []

    fp = open(full_f_name, 'r', encoding='UTF-8')
    line_reader = csv.reader(fp)
    header = next(line_reader)
    init_cntr = 0

    for i in line_reader:
        if init_cntr < tmp_num:  # Filling top_sales list
            top_sales.append(i)

        elif init_cntr == tmp_num:  # Top_sales filled and sorted
            top_sales.sort(key=lambda x: x[5], reverse=True)
            if i[5] > top_sales[-1][5]:  # One of sale greater the smallest top_sales
                top_sales.pop()  # Update and resort top_sales
                top_sales.append(i)
                top_sales.sort(key=lambda x: x[5], reverse=True)


        elif init_cntr > tmp_num:
            if i[5] > top_sales[-1][5]:  # One of sale greater the smallest top_sales
                top_sales.pop()  # Update and resort top_sales
                top_sales.append(i)
                top_sales.sort(key=lambda x: x[5], reverse=True)

        init_cntr += 1
        if init_cntr % 100000 == 0:
            print(i[3], init_cntr / 100000)

    fp.close()

    for sale in top_sales:
        print(sale)

    fp = open(cache_file_name, 'w', encoding='UTF-8')
    json.dump(top_sales, fp)
    fp.close()


def latest():
    """Output the latest sales by regions"""
    tmp_num = input('Number of records to output? [15]: ')
    if tmp_num == '':
        tmp_num = 15
    else:
        tmp_num = int(tmp_num)

    # Check cache
    cache_file_name = path_cache + 'latest' + str(tmp_num) + '.json'

    if os.path.isfile(cache_file_name):

        tmp_input = input('For this request cache file exist. Recalculate? Y/[N]: ')

        if tmp_input != 'Y' or tmp_input != 'y':
            fp = open(cache_file_name, 'r', encoding='UTF-8')
            data = json.load(fp)
            fp.close()

            for i in range(len(data)):
                print(data[i])

            return

    latest_sales = []

    fp = open(full_f_name, 'r', encoding='UTF-8')
    line_reader = csv.reader(fp)
    header = next(line_reader)
    init_cntr = 0

    for i in line_reader:
        if init_cntr < tmp_num:  # Filling latest sales list
            latest_sales.append(i)

        elif init_cntr == tmp_num:  # Latest sales filled and sorted
            latest_sales.sort(key=lambda x: x[4], reverse=True)
            if i[4] > latest_sales[-1][4]:  # One of sale later latest sales
                latest_sales.pop()  # Update and resort latest sales
                latest_sales.append(i)
                latest_sales.sort(key=lambda x: x[4], reverse=True)


        elif init_cntr > tmp_num:
            if i[4] > latest_sales[-1][4]:  # One of sale later latest sales
                latest_sales.pop()  # Update and resort latest sales
                latest_sales.append(i)
                latest_sales.sort(key=lambda x: x[4], reverse=True)

        init_cntr += 1
        if init_cntr % 100000 == 0:
            print(i[3], init_cntr / 100000)

    fp.close()

    for sale in latest_sales:
        print(sale)

    fp = open(cache_file_name, 'w', encoding='UTF-8')
    json.dump(latest_sales, fp)
    fp.close()



def region():
    """Calculate the number of sales by each region"""
    tmp_num = input('Number of regions to output? [5]: ')
    if tmp_num == '':
        tmp_num = 5
    else:
        tmp_num = int(tmp_num)

    # Check cache
    cache_file_name = path_cache + str(tmp_num) + '.json'

    if os.path.isfile(cache_file_name):

        tmp_input = input('For this request cache file exist. Recalculate? Y/[N]: ')

        if tmp_input != 'Y' or tmp_input != 'y':
            fp = open(cache_file_name, 'r', encoding='UTF-8')
            data = json.load(fp)
            fp.close()

            cntr = 0
            for i in range(len(data)):
                cntr += 1
                print(data[i])
                if cntr >= tmp_num:
                    return

            return

    regions = {}
    tmp_sum = 0
    tmp_region = ''
    progress_bar = 0

    fp = open(full_f_name, 'r', encoding='UTF-8')
    line_reader = csv.reader(fp)
    header = next(line_reader)

    for i in line_reader:
        if i[3] != tmp_region:
            if tmp_region == '':
                tmp_region = i[3]
            else:
                regions.update({tmp_region: tmp_sum})
                tmp_sum = 0
                tmp_region = i[3]
                progress_bar = 0

        tmp_sum += float(i[5])
        progress_bar += 1
        if progress_bar % 100000 == 0:
            print(tmp_region, progress_bar / 100000)

    fp.close()

    # Не могу я ладу дать с этим sorted, проще своё написать
    #    sorted(regions, key=lambda x: x[1], reverse=True)

    cntr = len(tmp_region)
    region_sorted = []

    while cntr >= 0:
        cntr -= 1
        tmp_sum = 0
        for k in regions.keys():
            if regions[k] > tmp_sum:
                tmp_k = k
                tmp_sum = regions[k]

        region_sorted.append({tmp_k: tmp_sum})
        del regions[tmp_k]

    cntr = 0
    for i in range(len(region_sorted)):
        cntr += 1
        print(region_sorted[i])
        if cntr >= tmp_num:
            break

    fp = open(cache_file_name, 'w', encoding='UTF-8')
    json.dump(region_sorted, fp)
    fp.close()


def main():
    print('Worked!')


if __name__ == '__main__':
    sell()
