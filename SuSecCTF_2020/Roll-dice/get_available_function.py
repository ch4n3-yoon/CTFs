#!/usr/bin/python3
# coding: utf-8

functions = dir(__builtins__)
filters = set(['7', 'o', '(', '6', 'a', '4', 'n', '1', ',', 'i', '-', '+', 's', '0', 'g', 'd', '3', 'e', '5', 'l', 'v', '2', 't', '*', 'r', ')', '8', '9'])

def main():
    for function in functions:
        available = True
        for c in function:
            if c not in filters:
                available = False
        if available is True:
            print(function)

if __name__ == '__main__':
    main()

