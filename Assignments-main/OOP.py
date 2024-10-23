"""
#class constructor
class person:
    def __init__(self,pe,va,uy):
        self.n = pe
        self.a = va
        self.h = uy
"""

'''
#class methods
class person:
    def __init__(self,pe,va,uy):
        self.n = pe
        self.a = va
        self.h = uy
    def beings(self):
        print("name ; " +self.n)
        print("age ; " + str(self.a))
        print("height : " + str(self.h))

#object = person('mani',25,135)
#object.beings()
'''
'''

#import a as a


class clas_alpha:
    a=10
    def func(self):
        for missing in range(1,11):
            print('finish')
ob=clas_alpha()
ob.func()
value = ob.a
print('total valuse is :',value)

'''

'''POLYMORPHISM'''

'''Method overloading'''

# class Method_overloading:
#     def func(self, *args):
#         sum = 0
#         for missing in args:
#             sum += missing
#         print('the sum is : ', sum)
#
#
# quiz = Method_overloading()
# quiz.func(10, 20, 1)
# quiz.func(100000000000,21)
# quiz.func(1,2,4,5,2,3)


'''OPERATOR OVERLOADING'''

# # __add__
# # __sub__
# # __mul__
# # __div__
# # These are all operator overloading
#
# class Operator_Overloading:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         return self.a + other.a
#
#
# quiz = Operator_Overloading(222)
# obj1 = Operator_Overloading(2)
#
# print(quiz + obj1)

'''METHOD OVERRIDING'''

# class student:
#     def project(self):
#         print('one')
# class teacher(student):
#     def project(self):
#         super().project()
#         print('two')
# class princi(teacher):
#     def project(self):
#         super().project()
#         print('three')
#
# ob = princi()
# ob.project()

'''FUNCTION DECORATOR'''
# def UpperString(ref):
#     def process():
#         data = ref()
#         return data.upper()
#
#     return process
#
#
# @UpperString
# def MyFunction():
#     return "welcome  to    python "
#
#
# # result=UpperString(MyFunction)
# # print(result())
# print(MyFunction())


"""class decorator """


class MyDecorator:
    def __init__(self, ref):
        self.ref = ref

    def __call__(self, *args):
        return self.ref(*args).upper()


@MyDecorator
def Myfunction(str1, str2):
    return f'this is {str1}  {str2}'


print(Myfunction("class", "decorator"))
