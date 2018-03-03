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
filename = 'extra.json'
output_filename = 'tweets.txt'

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
            numtext = len(str(row))
            print('Total caracteres= %d' % numtext)
        for i in range(numtext):
            if texto_tweets[i] == '"':
#                print('\n')
#                print(texto_pantalla)
                try:
                    with open(output_filename, 'a', newline='') as tweeteo:
                        tweeteo.write('\n %s' % str(texto_pantalla))
                        tweeteo.close()
                except FileNotFoundError:
                    with open(output_filename, 'w', newline='') as tweeteo:
                        tweeteo.write('\n %s' % str(texto_pantalla))
                        tweeteo.close()
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
