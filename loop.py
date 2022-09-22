from sre_constants import CHCODES


a=[1,2,3,4,5]
user ={
    'name': 'jonh',
    'age': 20,
    'class' : True
}

for key ,value  in user.items(): # item trả về tuple (key,value) dùng unpacking list (destructuring)  để lấy giá trị
    print(key,value)

for item in user.values():
    print('>>> Check value() :',item)

for item in user:
    print('>>> Check key():',item)



# Lấy index trong list range,enumerate

# Hàm range () trả về một chuỗi số, bắt đầu(start) từ 0 theo mặc định và tăng lên 1 (step)(theo mặc định), và dừng trước một số được chỉ định.
# range(start, stop, step)

# C1 :
names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'>>> enumerate : {index}: {value}')

# C2 :
for index in range(len(names)):
    print(f'>>> range : {index}: {names[index]}')



# output: 
# 0: Bob
# 1: Alice
# 2: Guido


# VD : check trùng lăp trong list 
# C1 : 
# Lấy ra phần tử  trùng lặp 
my_list = ['a','b','c','a','d','d','e']
checked= []
for item in my_list:
    if (my_list.count(item)>1):
        if item not in checked:
            checked.append(item)
print('>>> check dulicate: ',checked)

# C2 : sử dụng comprehension

# Lấy ra phần tử  trùng lặp 
new_list = list(set([item for item in my_list if my_list.count(item)>1 ]))
print('>>> check dulicate with comprehension: ',new_list) # ->  ['d', 'a']

# Bonus: Lấy ra phần tử không trùng lặp 
# new_list = [item for item in my_list if my_list.count(item)==1] # ->  ['b', 'c', 'e']