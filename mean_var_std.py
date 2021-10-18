import numpy as np

def calculate(list):
    ### List[int]-> Dict{'string': List[List[np.float64]], ... 'string': List[List[int]}
    ### Input list of nine numbers. Convert list to 3x3 numPy array
    ### Calculate mean, variance, standard deviation, max, min and sum of each axis, and the flattened matrix
    ### Output a dict of lists for each calculation
    ### Raise ValueError for lists < 9 numbers
    
    
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
