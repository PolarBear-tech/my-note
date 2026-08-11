import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import dis

    return (dis,)


@app.cell
def _(dis):
    def _f():
        print("1", "2")

    dis.dis(_f)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
