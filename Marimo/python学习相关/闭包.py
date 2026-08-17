import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # 闭包

    就是当一个函数`func`返回其内部的另一个函数`gunc`时，而且`gunc`内使用了`func`内的变量（比如`a`），当调用了`func`得到了`gunc`后，理应`a`已经被释放了，但是为了保证`gunc`的正常运行，会给`gunc`一个闭包，相当于`gunc`的运行环境，保证`gunc`的正常运行。
    """)
    return


@app.cell
def _():
    def _func():
        a = 1
        def gunc():
            nonlocal a # 只有当gunc()内部给存在对a赋值的操作时，才会使用到这个nonlocal
            a += 1
            return a
        a += 1
        return gunc

    _gunc = _func()
    print(_gunc())
    return


@app.cell
def _():
    # 这是错误的写法
    def _func():
        l = []
        for i in range(10):
            def gunc():
                print(i)
            l.append(gunc)
        return l

    _l = _func()
    for _gunc in _l:
        _gunc()
    return


@app.cell
def _():
    # 应该这样写
    def _func():
        l = []
        for i in range(10):
            def gunc(i_):
                # 这一步把i这个unbound var 存进了闭包，持久化不会受到for循环的影响
                def inner():
                    print(i_)
                return inner
            l.append(gunc(i))
        return l

    _l = _func()
    for _gunc in _l:
        _gunc()
    return


if __name__ == "__main__":
    app.run()
