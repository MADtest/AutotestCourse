def middle_value(given_list):
    list_of_underzero = []
    for j in range(len(given_list)):
        for i in range(len(given_list[j])):
            if given_list[j][i] < 0:
                list_of_underzero.append(given_list[j][i])
    return sum(list_of_underzero)/len(list_of_underzero)

if __name__ == '__main__':
    input_list = input()
    print(middle_value(input_list))
    # print middle_value([[1, 5, -7], [-5, 7, -8], [-9, -2, 8]])
