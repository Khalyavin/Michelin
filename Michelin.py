import util
import csv
import os


def main():
    """Course test work with big data file"""
    path = 'E:/Work/Michelin/'
    data_file = 'michelin_data.csv'
    full_f_name = path + data_file
    full_tmp_name = path + 'tmp.csv'

    while True:
        print('В программе возможны следующие вызовы:')
        print('1. sell')
        print('2. top N записей')
        print('3. latest N записей')
        print('4. region N ')
        print('[0]. Выход')
        tmp = input('Ваш выбор: ')

        if tmp == '':
            break

        try:
            tmp = int(tmp)
        except:
            print('Введите ЧИСЛО от 0 до 4')

        if tmp == 1:
            util.sell()
        elif tmp == 2:
            util.top()
        elif tmp == 3:
            util.latest()
        elif tmp == 4:
            util.region()
        else:
            break


    # fp_from = open(full_f_name, 'r', encoding='utf-8')
    # from_reader = csv.reader(fp_from)
    # header = next(from_reader)
    #
    # fp_to = open(full_tmp_name, 'w', encoding='utf-8', newline='')
    # to_reader = csv.writer(fp_to)
    # to_reader.writerow(header)
    #
    # cntr = 0
    # for line in from_reader:
    #     cntr += 1
    #     to_reader.writerow(line)
    #     if cntr >= 100000:
    #         break
    #
    # fp_from.close()
    # fp_to.close()


if __name__ == '__main__':
    main()