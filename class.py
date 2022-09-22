# https://cafedev.vn/tong-hop-toan-bo-tai-lieu-hoc-huong-doi-tuong-va-bai-tap-full-huong-dan-tren-python/

#  @classmethod and @staticmethod : truy cập dược method mà không cần khởi tạo instance
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        print( 'class method called :', cls) # có thể thêm đối số là class hiện tại 

    @staticmethod
    def staticmethod():
        print( 'static method called') # Ko thể thêm đối số là class hiện tại 

# MyClass.classmethod()
# MyClass.staticmethod()


class User:
    __a = 1 
    def __init__(self,a) :
        self.__a =a 
user1 =User('123')
