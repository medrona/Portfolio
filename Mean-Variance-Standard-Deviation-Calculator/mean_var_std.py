import numpy as np

def calculate(list):

    if len(list)==9:
    
        #get list and create a numpy array
        nparray = np.array(list)

        #reshape numpy array into a 3x3 matrix
        matrix = nparray.reshape((3,3))

        #calculating mean along axes 0,1 and "flat"
        mean0 = np.mean(matrix, axis=0).tolist()
        mean1 = np.mean(matrix, axis=1).tolist()
        mean_flat = np.mean(matrix)

        #calculating mean along axes 0,1 and "flat"
        var0 = np.var(matrix, axis=0).tolist()
        var1 = np.var(matrix, axis=1).tolist()
        var_flat = np.var(matrix).tolist()

        #calculating standard deviation along axes 0,1 and "flat"
        std0 = np.std(matrix, axis=0).tolist()
        std1 = np.std(matrix, axis=1).tolist()
        std_flat = np.std(matrix).tolist()
        
        #calculating max along axes 0,1 and "flat"
        max0 = np.max(matrix, axis=0).tolist()
        max1 = np.max(matrix, axis=1).tolist()
        max_flat = np.max(matrix).tolist()

        #calculating min along axes 0,1 and "flat"
        min0 = np.min(matrix, axis=0).tolist()
        min1 = np.min(matrix, axis=1).tolist()
        min_flat = np.min(matrix).tolist()

        #calculating min along axes 0,1 and "flat"
        sum0 = np.sum(matrix, axis=0).tolist()
        sum1 = np.sum(matrix, axis=1).tolist()
        sum_flat = np.sum(matrix).tolist()
    
    else:
        raise ValueError("List must contain nine numbers.")

    return {
        'mean' : [mean0, mean1, mean_flat],
        'variance' : [var0, var1, var_flat],
        'standard deviation' : [std0, std1, std_flat],
        'max' : [max0, max1, max_flat],
        'min' : [min0, min1, min_flat],
        'sum' : [sum0, sum1, sum_flat]
            }
    #calculations
