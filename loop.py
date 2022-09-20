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


# Hàm range () trả về một chuỗi số, bắt đầu(start) từ 0 theo mặc định và tăng lên 1 (step)(theo mặc định), và dừng trước một số được chỉ định.
# range(start, stop, step)


names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'{index}: {value}')

# output: 
# 0: Bob
# 1: Alice
# 2: Guido


# VD : check trùng lăp trong list 
my_list = ['a','b','c','a','d','d','e']
checked= []
for item in my_list:
    if (my_list.count(item)>1):
        if item not in checked:
            checked.append(item)
print('>>> check dulicate: ',checked)