import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    print("{}".format(15))
    print("{:b}".format(15))
    print("{:x}".format(15))
    return


@app.cell
def _():
    class _A:
        def __format__(self, spec):
            if spec == "x":
                return "0xA"
            return "<A>"

    print(f"{_A()}")
    print(f"{_A():x}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
