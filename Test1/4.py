# -*- coding: utf-8 -*-


def delete_extra_spaces(string):
    while '  ' in string:
        string = string.replace('  ', ' ')
    return string


if __name__ == '__main__':
    delete_extra_spaces('jsahfd   iasdfh jasdhfue audhf8ew iahdsf8we   oadsfuoi   oidsauf8 huy8ya  p  ')
