import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data=list(np.load('J:\\Machine_Learning_Project\\Data files\\training_data.npy'))

df=pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))
##lefts=[]
##rights=[]
##m=[]
##n=[]
##kuch_nahi=[]
##shuffle(train_data)
##
##for data in train_data:
##    img=data[0]
##    choice=data[1]
##    if choice ==[1,0,0,0]:
##        lefts.append([img,choice])
##    elif choice ==[0,1,0,0]:
##        rights.append([img,choice])
##    elif choice ==[0,0,1,0]:
##        m.append([img,choice])
##    elif choice ==[0,0,0,1]:
##        n.append([img,choice])
##    elif choice ==[0,0,0,0]:
##        kuch_nahi.append([img,choice])
##    else:
##        print("No matching data")
##rights=rights[:len(m)][:len(n)]
##lefts=lefts[:len(lefts)]
##kuch_nahi=kuch_nahi[:len(lefts)]
##final_data=rights + lefts + kuch_nahi + m + n
##shuffle(final_data)
##print(len(final_data))
##np.save('training_data_v2.npy', final_data)
##for data in train_data:
##    img =data[0]
##    choice=data[1]
##    cv2.imshow('img',img)
##    print(choice)
##    if cv2.waitKey(25) & 0xFF ==ord('q'):
##        cv2.destroyAllWindows()
##        break
