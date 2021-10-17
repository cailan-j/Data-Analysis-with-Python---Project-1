import numpy as np

def calculate(list):
    # try main body of function
    try: 
    #create 3 x 3 matrix from list
        larray = np.asarray(list).reshape((3,3)) 
    
    #calculate statistics for axis1, axis2 and flat array, store as list
        means = [np.mean(larray, axis = 0).tolist(),
                 np.mean(larray, axis = 1).tolist(),
                 np.mean(larray).tolist()]
    
        variances = [np.var(larray, axis = 0).tolist(),
                     np.var(larray, axis = 1).tolist(),
                     np.var(larray).tolist()]
    
        stdevs = [np.std(larray, axis = 0).tolist(),
                  np.std(larray, axis = 1).tolist(),
                  np.std(larray).tolist()]
    
        maxs = [np.max(larray, axis = 0).tolist(),
                np.max(larray, axis = 1).tolist(),
                np.max(larray).tolist()]
    
        mins = [np.min(larray, axis = 0).tolist(),
                np.min(larray, axis = 1).tolist(),
                np.min(larray).tolist()]
    
        sums = [np.sum(larray, axis = 0).tolist(),
                np.sum(larray, axis = 1).tolist(),
                np.sum(larray).tolist()]
    
        #make dictionary 
        calculations = {'mean' : means,
                        'variance' : variances, 
                        'standard deviation' : stdevs,
                        'max' : maxs,
                        'min' : mins,
                        'sum' : sums}
    
        return calculations 
    
    #ValueError Exception Message
    except ValueError:
         raise ValueError("List must contain nine numbers.")
