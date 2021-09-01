def create_result(x):
    result = np.where(x==0, 0.5,
                      np.where(x==1, 0.4,
                               np.where(x==2, 0.2,
                                        np.where(x==3, 0.7,
                                                 np.where(x==4,1,0.5)))))
                      
    return result
