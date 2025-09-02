class A:
    def method(self):
        print('froma A')

class B(A):
    def method(self):
        print('froma B')

class C(A):
    def method(self):
        print('froma C')

class D(C, B):
    pass

d = D()

print(D.mro())

d.method()