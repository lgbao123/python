# Dictionary : giống object , mutable
user ={
    'name' : "john",
    'age'  : 20,
}
print(user['name']) # nếu không tìm thấy key có thể bị lỗi nên sử dụng phương thức get 

# get(key,[default]) : get key của dict nếu không có sẽ lấy giá trị default 
print(user.get('age',1)) # -> 20  
print(user.get('class','A')) # -> A
# https://devera.vn/blog/our-blog-1/post/11-dictionary-methods-nen-biet-trong-python-77