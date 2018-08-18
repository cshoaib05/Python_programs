class Test:                                                     #### class class_name:
    foo=[2,3]                                       
t1=Test()                                                       #### OBJECT   ::::::   VAR=class_name()
t2=Test()
print(t1)
t1.foo.append(23)
print(t1.foo)

class Test2:
    def __init__(self):                                         ####   __init__(ss(var)):                ___init___(object_name):      __init__  predefine
        self.foo=[2,3]                                          ####            ss(var).var                      object_name.var            doesn't need to call it call auto
    def add(sd,a):                                              ####  Class_name.fun_name(object_name)            call as classname
        sd.c=32+a
t1=Test2()                                                       #####  var=class(var)   for __init__     
t2=Test2()                                                     
t1.foo.append(23)
print(t1.foo)
t2.add(4)
print(t2.c)

class LIST:
    @classmethod                                                #### @classmethod takes only 1 method   cand call with class_name.var
    def ADD(s,l):
        sum=0
        for i in range(0,len(l)):
            sum=sum+l[i]
        return sum
    @classmethod
    def MULTI(q,l):
        sum=1
        for i in l:
            sum=sum*i
        return sum
l=[1,2,3,4,5]
o=LIST()
print(o.ADD(l))
print(LIST.MULTI(l))



class TEST3:
    @staticmethod                                                   #### static no need any self var
    def Add(n,o):
        b=o+n
        return b
print(TEST3.Add(55,4))

class TEST4(TEST3):                                                 #### inheritance                child_class(parent_class)
                                                                    ####  multi inheritance          child_class(parent_class1,parent_class2)
    
    


