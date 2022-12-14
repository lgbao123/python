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


# global keyword : Sử dụng để truy cập global (tham chiếu)
# nonlocal keyword : Sử dụng để truy cập biến parent local (tham chiếu) 


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


# Sắp xếp tuple 
list1 = [['a','a1'],['b','b1'],['c','c1']]
list2 = [1,2,3]
list3 = list(zip(list1,list2))
list3.sort(reverse=True,key=lambda x : x[1])
def test(item):
    return item[1]
list4 = list(map(test,list3)) 
print(list3) # -> [(['c', 'c1'], 3), (['b', 'b1'], 2), (['a', 'a1'], 1)]
print(list4) #  -> [3, 2, 1]


# Max key ,value  in dict

square = {'a': 4, 'b': 9, 'c': 1, 'd': 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # d
# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])
print("The key with the largest value:", key2)    # b
# getting the largest value
print("The largest value:", square[key2])    # 9


