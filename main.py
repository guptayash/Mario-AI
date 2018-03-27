from getkeys import key_check
from grabscreen import grab_screen
from directkeys import PressKey, ReleaseKey,Comma,Dot,Left_Arrow,Right_Arrow
import pyautogui
import cv2
import numpy as np
import os
import time

def keys_to_output(keys):
    output=[0,0,0,0]
    if 'A' in keys:
        output[0]=1
    elif 'D' in keys:
        output[1]=1
    elif 'M' in keys:
        output[2]=1
    elif 'N' in keys:
        output[3]=1
    #[A,D,M,N]md
    return output

##file_name='training_data.npy'
##
##if os.path.isfile(file_name):
##    print('File already exists, loading previous data')
##    training_data=list(np.load(file_name))
##else:
##    print('New training file created')
##    training_data=[]
starting_value = 25

while True:
    file_name = 'training_data-{}.npy'.format(starting_value)

    if os.path.isfile('training_data.npy'):
        print('File exists, moving along',starting_value)
        training_data=list(np.load(training_data.npy))
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        training_data=[]
        
        break
    
def main(file_name,starting_value):
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    file_name = file_name
    starting_value = starting_value
    training_data = []
    last_time=time.time()
    while True:
        screen=grab_screen(region=(0,60,575,500))
        screen=cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen=cv2.resize(screen,(80,60))
        keys=key_check()
        output=keys_to_output(keys)
        training_data.append([screen,output])
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time=time.time()
        if len(training_data)%500==0:
            print(len(training_data))
            np.save(file_name,training_data)
            print('SAVED')
            training_data = []
            starting_value += 1
            file_name = 'training_data-{}.npy'.format(starting_value)
##        cv2.imshow('screen',screen)
##        cv2.waitKey(0)
