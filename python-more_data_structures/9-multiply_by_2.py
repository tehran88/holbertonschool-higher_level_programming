#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary.keys():
        new_dictionary[i] = a_dictionary[i]*2
    return new_dictionary
