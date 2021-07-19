##the prurpose of history_finder() is to find the previous trial history
##of an animal in the Steinmetz et al. 2019 dataset. 

import numpy as np

#shift things by however much
def shift1(arr, num, fill_value=np.nan):
    arr = np.roll(arr,num)
    if num < 0:
        arr[num:] = fill_value
    elif num > 0:
        arr[:num] = fill_value
    return arr

#we will need to get the appropriate session indeces
def history_finder(alldat, session_idx):
    previousReward = np.zeros_like(alldat[session_idx])
    for i in range(len(session_idx[:])):
        dat = alldat[session_idx[i]]
        previousReward[i] = shift1(dat["feedback_type"], 1, fill_value=np.nan)       
        ###-1 is negative feedback, +1 is positive feedback
        ##xyz other variables of interest here
    return previousReward
