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

def init_array():
    array = [[0 for i in range(4)] for j in range(4)]
    #print(array)
    for i in range(0,3):
        row = random.randint(0,3)
        colum = random.randint(0,3)
        array[row][colum] = random.randint(0,2)*2
    return array

def copy(source):
    target = [[source[row][colum] for row in range(len(source))] for colum in range(len(source[0]))]
    return target

def equal(target, source):
    for row in range(len(target)):
        for colum in range(len(source)):
            if target[row][colum] != source[row][colum]:
                return True
    return False

def run(array):
    array_pre = list()
    while(1):
        print_array(array)
        print('\n')
        choice = input()
        if choice == 'w':
            array = slide_up(array)
            print("slide up:")
        elif choice == 's':
            array = slide_down(array)
            print("slide down:")
        elif choice == 'a':
            array = slide_left(array)
            print("slide left:")
        elif choice == 'd':
            array = slide_right(array)
            print("slide right")
        else:
            print("end")
            break
        index = random.randint(1,2)
        count = 0
        if len(array_pre) == 0 or equal(array_pre, array):
            for i in range(0,index):
                row = random.randint(0,3)
                colum = random.randint(0,3)
                if(array[row][colum] == 0):
                    array[row][colum] = random.randint(1,2) * 2
                else:
                    i-=1
                    count+=1
                if count == 5:
                    break
        array_pre = copy(array)
    return array


if __name__ == "__main__":
    array = init_array()
    array = run(array)
    print_array(array)
