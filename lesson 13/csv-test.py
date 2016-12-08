import csv

data = ['2,True', '3,True', '12,False', '13,True']
data1 = [[2,True], [3,True], [12,False], [13,True]]
csv_writer = csv.writer(open('testCsv', 'w'))

if __name__ == '__main__':

    # print dir(csv_writer)

    csv_writer.writerows(data1)
    # with open('testCsv', 'r') as input_file:
    #     # print (input_file.read())
    #     csv_reader = csv.reader(input_file)
    #     for line in csv_reader:
    #         # print(line)
    #         user, password, is_valid = line
    #         print user, password, is_valid


    # csv_reader = csv.reader(open('testCsv', 'r'))
    # print csv_reader
    # print csv_reader.line_num
    # print csv_reader.dialect
    # print csv_reader.dialect.__dict__

    # for attribute in dir(csv.dialect):
    #     if not attribute.startswith('__'):
    #         print attribute, csv.dialect.__getattr__(attribute)

