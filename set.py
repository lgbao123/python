# Một Set gồm các yếu tố sau:

# - Được giới hạn bởi cặp ngoặc {}
# - Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
# - Set không chứa nhiều hơn 1 phần tử trùng lặp
# - Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.

new_list = [1,2,3,4,5,5,5,5]
new_set = set(new_list)  
print(new_set) # -> {1, 2, 3, 4, 5}

A = {1,2,3,4,5}
B ={4,5,6,7,8,9,10}

# Chọn ra những phần tử thuộc A nhưng ko thuộc B 
print(A.difference(B)) # -> {1, 2, 3}

# intersection : chọn ra phần tử A giao B 
print(A.intersection(B)) # -> {4, 5}
print(A & B ) # -> {4, 5}

# isdisjoint : kiểm tra không có điểm chung (ko giao nhau)
print(A.isdisjoint(B)) # -> false

#  difference_update giống difference nhưng sữa trực tiếp vào biến A 
A.difference_update(B)
print(A) # -> {1,2,3} 

# union : hợp tập A với B
print(A.union(B)) # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(A | B)   # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 

A= {1,2,3}
B={1,2,3,4,5}
C={1,2,3,4,5,6,7}

# Kiểm tra A là tập con B 
A.issubset(B) # -> true

# Kiểm tra tất cả A là tập cha B 
print(A.issuperset(B)) # -> false
print(B.issuperset(B)) # -> true
print(C.issuperset(B)) # -> true

# Xoá phần tử 
A.discard(2)
print(A) # -> {1, 3}
