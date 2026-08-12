import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 描述器

    定义：从描述器的创建来说，一个类中定义了 `__get__` 、 `__set__` 、 `__delete__` 中的一个或几个，这个类的实例就可以叫做一个描述器。

    创建一个描述器的类，它的实例就是一个描述器，这个类要有__get__  __set__ 这样的方法，这种类是当做工具使用的，不单独使用。
    """)
    return


@app.cell
def _():
    class _M:
        def __init__(self, x=1):
            self.x = x
        
        def __get__(self, instance, owner):
            return self.x
    
        def __set__(self, instance, value):
            self.x = value
        

    class _A:
        m = _M() 
    
    _o = _A()
    print(_o.m)
    _o.m = 2
    print(_o.m) 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## _o.m的访问顺序

    - 程序会先查找 `_o.__dict__['m']` 是否存在
    - 不存在再到 `type(_A).__dict__['m']` 中查找
    - 然后找 `type(_A)` 的父类

    ## 描述器的分类

    - 同时定义了 `__get__` 和 `__set__` 方法的描述器称为 **资料描述器**
    - 只定义了 `__get__` 的描述器称为 **非资料描述器**

    二者的区别是：当属性名和描述器名相同时，在访问这个同名属性时，如果是资料描述器就会先访问描述器，如果是非资料描述器就会先访问属性
    """)
    return


@app.cell
def _():
    # 既有__get__又有__set__，是一个资料描述器
    class _M:
        def __init__(self):
            self.x = 1
        
        def __get__(self, instance, owner):
            print('get m here') 
            return self.x
    
        def __set__(self, instance, value):
            print('set m here') 
            self.x = value + 1 

    # 只有__get__是一个非资料描述器
    class _N:
        def __init__(self):
            self.x = 1
        
        def __get__(self, instance, owner):
            print('get n here') 
            return self.x
        
    # 调用描述器的类
    class _A:
        m = _M() # m就是一个描述器
        n = _N()
    
        def __init__(self, m, n):
            self.m = m # 属性m和描述器m名字相同，调用时发生一些冲突
            self.n = n # 非资料描述器的情况，与m对比
    
    _o = _A(2,5)
    print(_o.__dict__) # 只有n没有m, 因为资料描述器同名时，不会访问到属性，会直接访问描述器，所以属性里就查不到m这个属性了
    print(_A.__dict__) # m和n都有
    print(_o.n) # 5, 非资料描述器同名时调用的是属性，为传入的5
    print(_A.n) # 1, 如果是类来访问，就调用的是描述器，返回self.x的值

    print(_o.m) # 3, 其实在_o = _A(2,5)创建实例时，进行了属性赋值，其中相当于进行了_o.m=2
    # 但是_o调用m时却不是常规地调用属性m，而是资料描述器m
    # 所以定义实例_o时，其实触发了m的__set__方法，将2传给value，self.x变成3
    # _o.m调用时也访问的是描述器，返回self.x即3的结果
    # 其实看打印信息也能看出什么时候调用了__get__和__set__

    _o.m = 6 # 另外对属性赋值也是调用了m的__set__方法
    print(_o.m) # 7，调用__get__方法

    print('-'*20)
    # 在代码中显式调用__get__方法
    print(_A.__dict__['n'].__get__(None, _A)) # 1
    print(_A.__dict__['n'].__get__(_o, _A)) # 1
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
