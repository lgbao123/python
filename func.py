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


# global keyword : Sử dụng để truy cập global 
# nonlocal keyword : Sử dụng để truy cập biến parent local 


def outer():
    x = 'local'
    def inner():
        nonlocal x 
        x = 'nonlocal'
        print('inner : ',x)
    inner()
    print('outer : ',x)
outer()

# Scope 
# 1.start with local 
# 2.Parent local 
# 3.Global 