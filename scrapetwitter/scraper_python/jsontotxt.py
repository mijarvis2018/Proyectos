#Unfinished code!!!

import os
import re
import csv
import sys
import json
import decimal
import datetime

texto_tweets = 'default'
texto_pantalla = ''
filename = 'extra.log'
# delimiter = "\t"
delimiter = '\n'
quotechar= '"'
i = 0

print ('\nInit ok...loading file... ')
try:
    with open(filename, 'r',newline='') as fp:
        print ('\n...File loaded on Read mode... ')
        reader = csv.reader(fp, delimiter=delimiter, quotechar=quotechar)

#Is SHOWing THE RESULSTS!!!!

        for row in reader:
            texto_tweets = str(row)

            print ('\nROW\n')
            numtext = len(str(row))
#            print('" '.join(row))
            print('Numtext= %d' % numtext)
            print(reader.line_num)
            print('\n End of rows')

        for i in range(numtext):

            if texto_tweets[i] == '"':
                print('\n')
                print(texto_pantalla)
                texto_pantalla = ''
            else:
                texto_pantalla += texto_tweets[i]





    print ('Exit loop')
except FileNotFoundError:
    with open(filename, 'rU') as fp:
        print ('\n...File loaded on Read mode + U... ')
        reader = csv.DictReader(fp, delimiter=delimiter, quotechar=quotechar)
        for i, record in enumerate(reader):
            fields = reader.fieldnames
            print ('\nFields: %s' % fields )
            for i, field in enumerate(fields):
                value = record[field]
                print ('\nValues: %s' % value )
