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
    # 工厂模式
    """)
    return


@app.cell
def _():
    class DataConnection:
        def __init__(self, host, port, username, password):
            self.host = host
            self.port = port
            self.username = username
            self.password = password

        def connect(self):
            return f"Connecting to database at {self.host}:{self.port} with {self.username}"


    def client():
        # 难以维护，而且一直出现重复代码
        main_db = DataConnection("127.0.0.1", 3306, "root", "123456")
        analytics_db = DataConnection("192.168.1.1", 3307, "admin", "123456")
        cache_db = DataConnection("10.0.0.1", 23410, "cacheuser", "123456")
        print(main_db.connect())
        print(analytics_db.connect())
        print(cache_db.connect())

    client()
    return (DataConnection,)


@app.cell
def _(DataConnection):
    def connection_factory(db_type: str) -> DataConnection | None:
        # 这里更合适的是抽成一个配置文件
        db_configs = {
            "main":{
                "host": "127.0.0.1",
                "port": 3306,
                "username": "root",
                "password": "123456"
            },
            "analytics":{
                "host": "192.168.1.1",
                "port": 3307,
                "username": "admin",
                "password": "123456"
            },
            "cache": {
                "host": "10.0.0.1",
                "port": 23410,
                "username": "cacheuser",
                "password": "123456"
            }
        }
        return DataConnection(**db_configs[db_type])

    return (connection_factory,)


@app.cell
def _(connection_factory):
    connection_factory("cache")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
