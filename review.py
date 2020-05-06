# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:48:25 2020

@author: NeoSixMan
"""

import numpy as np
import pandas as pd

wishList = pd.read_csv("wish_list.csv") #example data
review_column = ['user_id','product_id']
review = pd.DataFrame(columns=review_column)

command = ''

while(command != 'q'):
        command = input('add (a), see (s), remove (r), exit (q) :')        
        if command == 'a':
            name = str(input('Enter product name:'))
            '''
            row = insurance.loc[insurance['names'] == name]
            check = wishList.isin({'names': [name]})
            if check['names'].any(axis=None) == False:
                wishList = wishList.append(row)
            else:
                print('already add')
            '''
        elif command == 's':
            print(wishList)
        elif command == 'r':
            name = str(input('Enter remove name:'))
            wishList = wishList[wishList.names != name]
        else:
            print('...')
