# *args **kwargs 
def super_func(*args ,**kwargs):
    '''
        This function to test  *args **kwargs
    '''
    print('>>> check kwargs :',kwargs)
    print('>>> check args :',args)
    return sum(args)
print(super_func.__doc__) # use .__doc__ to print comment in function 
print(super_func(1,2,3,4,5, a=10,b=15))