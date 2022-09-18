# List : mutable

#  List slicing list[start : stop : step]
amazon =['notebook','pen','toys','a','b','c']
# Nếu muốn copy mảng thì dùng slicing chứ không được gán new_amazon = amzone 
# new_amazon = amazon # ( kiểu này là tham chiếu)
new_amazon = amazon[:]
new_amazon[0]= 'laptop'
# print('>>> Check new',new_amazon)
# print('>>> Check old',amazon[0:2])


# List method
basket = [1,2,3,4,5]
# 1. adding 
# - append : thêm phần tử vào cuối list
basket.append(100) # -> [1, 2, 3, 4, 5, 100]

# - insert : thêm phần tử vào vị trí chỉ định 
basket.insert(2,500) # -> [1, 2, 500, 3, 4, 5, 100]

# -extend :  adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
basket.extend([8,9,10]) # -> [1, 2, 500, 3, 4, 5, 100, 8, 9, 10]

# 2. Removing
basket = [1,2,3,4,4,5,6,7]
#  - pop : xoá phần tử cưối list nếu không truyền index vào ( trả về phần tử đã xoá)
basket.pop() # -> [1, 2, 3, 4, 4, 5, 6]
basket.pop(1) # -> [1, 3, 4, 4, 5, 6]

# - remove : xoá phần tử theo giá trị , nếu tìm thấy nhiều giá trị giống nhau thì chỉ xoá đầu tiên
basket.remove(4) # -> [1, 3, 4, 5, 6]
print(basket)

# 3.index(value,[start],[end]) : tìm index của value từ start tới end 
basket.index(6) #-> 4 
# Lưu ý : nếu không tìm ra sẽ lỗi , để tránh lỗi có thể kiểm tra trước
if ( 66 in basket):
    basket.index(66)

# 4. count(value)  : đếm số lần xuất hiện value
print(basket.count(5)) # -> 1

basket = [1,5,2,3,8,8,4]
#5. sort : sắp xếp mảng 
basket.sort() #-> [1, 2, 3, 4, 5, 8, 8]

#6. reverse() : đảo ngược list
basket.reverse() # -> [8, 8, 5, 4, 3, 2, 1]
print(basket)

# Nối các phần tử list thành string
sentences = "-".join(['my','name','is','Tes']) # -> my-name-is-Tes

# List unpacking ( giống Destructuring trong JS )
number = [1,2,3,4,5,6]
a,b,*orther,d = number
# a -> 1 
# b -> 2
# orther -> [3, 4, 5]
# d -> 6
