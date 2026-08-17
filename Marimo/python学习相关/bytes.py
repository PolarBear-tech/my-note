import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    class _A:
        def __bytes__(self):
            print("_A.__bytes__ called")
            return bytes([0, 1])

    print(bytes(_A()))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
