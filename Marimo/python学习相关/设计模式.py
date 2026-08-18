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
    # 单例模式
    """)
    return


@app.cell
def _():
    class _Earth:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            self.flags = 12345

    def _connect():
        e_1 = _Earth()
        e_2 = _Earth()

        print(e_1 is e_2)

    _connect()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 工厂模式
    """)
    return


@app.cell
def _(DataConnection):
    class _DatabaseConnection:
        def __init__(self, host, port, username, password):
            self.host = host
            self.port = port
            self.username = username
            self.password = password

        def connect(self):
            return f"Connecting to database at {self.host}:{self.port} with {self.username}"

    def _client():
        # 难以维护，而且一直出现重复代码
        main_db = _DatabseConnection("127.0.0.1", 3306, "root", "123456")
        analytics_db = _DatabaseConnection("192.168.1.1", 3307, "admin", "123456")
        cache_db = _DatabaseConnection("10.0.0.1", 23410, "cacheuser", "123456")
        print(main_db.connect())
        print(analytics_db.connect())
        print(cache_db.connect())

    def _connection_factory(db_type: str) -> DataConnection | None:
        # 这里更合适的是抽成一个配置文件
        db_configs = {
            "main": {
                "host": "127.0.0.1",
                "port": 3306,
                "username": "root",
                "password": "123456",
            },
            "analytics": {
                "host": "192.168.1.1",
                "port": 3307,
                "username": "admin",
                "password": "123456",
            },
            "cache": {
                "host": "10.0.0.1",
                "port": 23410,
                "username": "cacheuser",
                "password": "123456",
            },
        }
        return _DatabaseConnection(**db_configs[db_type])

    _connection_factory("cache").connect()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 建造者模式(Builder)
    """)
    return


@app.cell
def _():
    class _DatabaseConnection:
        def __init__(self, host, port, username, password,
                     max_connections=None, timeout=None,
                     enable_ssl=False,
                     ssl_cert=None, connection_pool=None,
                     retry_attempts=None,
                     compression=False, read_preference=None):
            self.host = host
            self.port = port
            self.username = username
            self.password = password
            self.max_connections = max_connections
            # validate timeout
            # 这里违反了单一责任原则
            if timeout is not None and timeout <= 0:
                raise ValueError("Connect timeout must be positive")
            self.timeout = timeout
            self.enable_ssl = enable_ssl
            self.ssl_cert = ssl_cert
            self.connection_pool = connection_pool
            self.retry_attempts = retry_attempts
            self.compression = compression
            self.read_preference = read_preference

        def connect(self):
            return f"Connecting to database at {self.host}:{self.port} with username '{self.username}'"

    def _connect():
        connect = _DatabaseConnection(
            "127.0.0.1", 
            3306, 
            "root", 
            "123456",
            max_connections=100, 
            timeout=30, 
            enable_ssl=True, 
            ssl_cert="/path/to/cert",
            connection_pool=20,
            retry_attempts=3, 
            compression=True,
            read_preference="secondary"
        )
        # 太麻烦
        print(connect.connect())

    class _DatabaseConnectionBuilder:
        def __init__(self, host, port, username, password):
            self._config = {
                "host": host,
                "port": port,
                "username": username,
                "password": password,
            }

        def set_max_connection(self, max_connection: int):
            self._config["max_connection"] = max_connection
            return self

        def set_timeout(self, timeout: int):
            if timeout < 0:
                raise ValueError("timeout cannot be negative.")
            self._config["timeout"] = timeout
            return self

        def enable_ssl(self, ssl_cert=None):
            self._config['enable_ssl'] = True
            self._config['ssl_cert'] = ssl_cert
            return self

        def set_connection_pool(self, pool_size):
            self._config['connection_pool'] = pool_size
            return self

        def set_retry_attempts(self, attempts):
            self._config['retry_attempts'] = attempts
            return self

        def enable_compression(self):
            self._config['compression'] = True
            return self

        def set_read_preference(self, preference):
            self._config['read_preference'] = preference
            return self

        def build(self):
            return _DatabaseConnection(**self._config)

    _main_db = _DatabaseConnectionBuilder("127.0.0.1", 3306, "root", "123456").enable_ssl().build()

    _main_db.connect()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 适配器模式

    现在有这样一个场景，一个老式项目中有一个`OldLogger`类，但是很不好用，我们引入第三方库的`NewLogger`进行优化，但是二者的接口不一致，这时为了解决这个问题，我们引入适配器`LoggerAdapter`
    """)
    return


app._unparsable_cell(
    r"""
    class _Logger:
    
        def debug()
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
