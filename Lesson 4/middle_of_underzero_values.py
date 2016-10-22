def middle_value(given_list):
    list_of_underzero = []
    for i in range(len(given_list)):
        if given_list[i] < 0:
            list_of_underzero.append(given_list[i])
    return sum(list_of_underzero)/len(list_of_underzero)

if __name__ == '__main__':
    input_list = input()
    print(middle_value(input_list))
