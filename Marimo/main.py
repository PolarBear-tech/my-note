import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import dis

    return (dis,)


@app.cell
def _():
    class _A:
        """
        _A
        """
        name = "_A"
        def __init__(self, age: int):
            self.age = age


    print(_A.__dict__)
    _o = _A(10)
    print(_o.__dict__)
    return


@app.cell
def _(dis):
    class _A:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def func(cls):
            print(1)

    dis.dis(_A)
    return


@app.cell
def _():
    class _SayMetaClass(type):
        def __new__(cls, name, bases, attrs):
            attrs["say_" + name.lower()] = lambda self, value, saying=name: print(f"{value}: {saying}!")
            return type.__new__(cls, name, bases, attrs)

    class _Hello(metaclass=_SayMetaClass):
        pass

    _hello = _Hello()
    print(_hello.__dict__)
    # _hello.say__hello("world")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
