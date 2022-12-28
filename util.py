import csv

path = 'E:/Work/Michelin/'
data_file = 'michelin_data.csv'
full_f_name = path + data_file
full_tmp_name = path + 'tmp.csv'


def sell():
    print('Sell')

def top():
    print('Top')

def latest():
    print('Latest')

def region():
    """Calculate the number of sales by each region"""
    tmp_num = input('Сколько регионов выводить? [5]: ')
    if tmp_num == '':
        tmp_num = 5
    else:
        tmp_num = int(tmp_num)

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


def main():
    print('Worked!')


if __name__ == '__main__':
    region()