from grabscreen import grab_screen
import cv2
import numpy as np
import os
import time
from alexnet import alexnet
from directkeys import PressKey, ReleaseKey, A, D, M, N
from getkeys import key_check
WIDTH =80
HEIGHT=60
LR=1e-3
EPOCHS=8
MODEL_NAME='mario-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)

model=alexnet (WIDTH,HEIGHT,LR)
#model.load(MODEL_NAME)
model.load("J:\\Machine_Learning_Project\\version2\\final.model", weights_only=True)
def A_fun():
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(M)
    ReleaseKey(N)
def D_fun():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(M)
    ReleaseKey(N)
def M_fun():
    PressKey(M)
    ReleaseKey(D)
    ReleaseKey(A)
    ReleaseKey(N)
    time.sleep(1)
    ReleaseKey(M)
def N_fun():
    PressKey(N)
    ReleaseKey(D)
    ReleaseKey(M)
    ReleaseKey(A)
        
def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    
    last_time=time.time()
    paused=False
    while True:
        screen=grab_screen(region=(0,60,575,500))
        screen=cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen=cv2.resize(screen,(80,60))
        
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time=time.time()
        prediction=model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
        moves=list(np.around(prediction))
        print(moves,prediction)
        if moves ==[0, 0, 1, 0]:
            print("M should be pressed")
            M_fun()
        elif moves ==[0, 1, 0, 0]:
            print("D should be pressed")
            D_fun()
        elif moves ==[1, 0, 0, 0]:
            print("A should be pressed")
            A_fun()
        elif moves ==[0, 0, 0, 1]:
            print("N should be pressed")
            N_fun()
        else:
            pass
        keys=key_check()

        if 'T' in keys:
            if paused:
                paused=False
                time.sleep(1)
            else:
                paused=True
                ReleaseKey(A)
                ReleaseKey(M)
                ReleaseKey(N)
                ReleaseKey(D)
