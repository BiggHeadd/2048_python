# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:56:54 2018

@author: 佛山
"""

import random


def print_array(array):
    for i in range(4):
        print(array[i])

def up2down(array):
    new_array = [[array[3-i][j] for j in range(4)] for i in range(4)]
    #print_array(new_array)
    return new_array    

def left2right(array):
    new_array = [[array[i][3-j] for j in range(4)] for i in range(4)]
    return new_array

def slide_up(array):
    flag = False
    for j in range(4):
        flag = False
        for i in range(4):
            """
            if flag == True and i+1<4:
                array[i][j] = array[i+1][j]
            if i == 3 and flag == True:
                array[i][j] = 0
            if i+1 < 4 and array[i][j] == array[i+1][j] and flag == False:
                array[i][j] *= 2
                flag = True
            
            """
            if array[i][j] == 0:
                for down in range(i,4):
                    if down+1 < 4:
                        array[down][j] = array[down+1][j]
                    if down == 3:
                        array[down][j] = 0
            
            if i-1>=0 and array[i-1][j] == 0:
                for down in range(i,4):
                    array[down-1][j] = array[down][j]
            
            
            if flag == True and i+1<4:
                array[i][j] = array[i+1][j]
            if i == 3 and flag == True:
                array[i][j] = 0
            if i+1 < 4 and array[i][j] == array[i+1][j] and flag == False:
                array[i][j] *= 2
                flag = True 
    return array

def slide_down(array):
    array = up2down(array)
    flag = False
    for j in range(4):
        flag = False
        for i in range(4):
            """
            if flag == True and i+1<4:
                array[i][j] = array[i+1][j]
            if i == 3 and flag == True:
                array[i][j] = 0
            if i+1 < 4 and array[i][j] == array[i+1][j] and flag == False:
                array[i][j] *= 2
                flag = True
            
            """
            if array[i][j] == 0:
                for down in range(i,4):
                    if down+1 < 4:
                        array[down][j] = array[down+1][j]
                    if down == 3:
                        array[down][j] = 0
            
            if i-1>=0 and array[i-1][j] == 0:
                for down in range(i,4):
                    array[down-1][j] = array[down][j]
            
            
            if flag == True and i+1<4:
                array[i][j] = array[i+1][j]
            if i == 3 and flag == True:
                array[i][j] = 0
            if i+1 < 4 and array[i][j] == array[i+1][j] and flag == False:
                array[i][j] *= 2
                flag = True 
    array = up2down(array)
    return array

def slide_left(array):
    for i in range(4):
        flag = False
        for j in range(4):
            """
            if flag == True and i+1<4:
                array[i][j] = array[i+1][j]
            if i == 3 and flag == True:
                array[i][j] = 0
            if i+1 < 4 and array[i][j] == array[i+1][j] and flag == False:
                array[i][j] *= 2
                flag = True
            
            """
            if array[i][j] == 0:
                for down in range(j,4):
                    if down+1 < 4:
                        array[i][down] = array[i][down+1]
                    if down == 3:
                        array[i][down] = 0
            
            if j-1>=0 and array[i][j-1] == 0:
                for down in range(j,4):
                    array[i][down-1] = array[i][down]
            
            
            if flag == True and j+1<4:
                array[i][j] = array[i][j+1]
            if j == 3 and flag == True:
                array[i][j] = 0
            if j+1 < 4 and array[i][j] == array[i][j+1] and flag == False:
                array[i][j] *= 2
                flag = True 
    return array

def slide_right(array):
    array = left2right(array)
    for i in range(4):
        flag = False
        for j in range(4):
            """
            if flag == True and i+1<4:
                array[i][j] = array[i+1][j]
            if i == 3 and flag == True:
                array[i][j] = 0
            if i+1 < 4 and array[i][j] == array[i+1][j] and flag == False:
                array[i][j] *= 2
                flag = True
            
            """
            if array[i][j] == 0:
                for down in range(j,4):
                    if down+1 < 4:
                        array[i][down] = array[i][down+1]
                    if down == 3:
                        array[i][down] = 0
            
            if j-1>=0 and array[i][j-1] == 0:
                for down in range(j,4):
                    array[i][down-1] = array[i][down]
            
            
            if flag == True and j+1<4:
                array[i][j] = array[i][j+1]
            if j == 3 and flag == True:
                array[i][j] = 0
            if j+1 < 4 and array[i][j] == array[i][j+1] and flag == False:
                array[i][j] *= 2
                flag = True 
    array = left2right(array)
    return array


array = [[random.randint(0,2) for i in range(4)] for j in range(4)]
#print(array)
for i in range(4):
    print(array[i])


while(1):
    choice = input()
    if choice == 'w':
        array = slide_up(array)
        print("slide up:")
        print_array(array)
        print('\n')
    elif choice == 's':
        array = slide_down(array)
        print("slide down:")
        print_array(array)
        print('\n')
    elif choice == 'a':
        array = slide_left(array)
        print("slide left:")
        print_array(array)
        print('\n')
    elif choice == 'd':
        array = slide_right(array)
        print("slide right")
        print_array(array)
        print('\n')
    else:
        print("end")
        break

print_array(array)
