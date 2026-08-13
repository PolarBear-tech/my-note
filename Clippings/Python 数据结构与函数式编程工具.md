---
source: "https://zhuanlan.zhihu.com/p/1943980148157318981"
created: 2026-08-13
---
在写 Python 的过程中，你可能经常遇到这样的痛点：

- 想用 `dict` 计数，但每次写 `if key in dict` 太麻烦？
- 想实现一个带过期缓存的函数？
- 想优雅地处理迭代器，但链式操作却让代码臃肿？

别急，Python 早就为你准备好了三大“内置工具库”：

- **`collections`** —— 数据结构增强版
- **`functools`** —— 高阶函数和装饰器工具
- **`itertools`** —— 高效迭代器工具

它们的共同点是： **轻量级、内置、不依赖第三方库，却能极大提升代码的优雅度与性能。**

## 1\. collections：更强的数据结构

Python 自带的 `list` 、 `dict` 、 `set` 、 `tuple` 已经覆盖了大多数需求，但在某些场景下，写起来还是会有点“笨重”。  
`collections` 模块则像是一把“瑞士军刀”，提供了一系列 **更高效、更专业的数据结构** ，大大简化了代码。

### 1.1 Counter —— 计数神器

`Counter` 是一个专门用来做计数的字典子类，最常见的用途就是 **频率统计** 。

```python
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)

print(count)            # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(count.most_common(1))  # [('apple', 3)]
```

**应用场景** ：

- 词频分析（文本处理 / NLP）
- 投票计数（选举/问卷调查）
- 日志分析（统计 IP 出现次数）

还能做 [集合运算](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E9%9B%86%E5%90%88%E8%BF%90%E7%AE%97&zhida_source=entity) ：

```python
c1 = Counter("hello")
c2 = Counter("world")
print(c1 + c2)   # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
```

### 1.2 defaultdict —— 自动初始化字典

普通字典如果访问不存在的 key 会报错，而 `defaultdict` 会自动给它一个默认值。

```python
from collections import defaultdict

scores = defaultdict(int)  # 默认值是 0
scores["Alice"] += 10
scores["Bob"] += 5
print(scores)  # defaultdict(<class 'int'>, {'Alice': 10, 'Bob': 5})
```

**应用场景** ：

**分组统计：**

```python
groups = defaultdict(list)
for name, dept in [("Alice","HR"), ("Bob","IT"), ("Cathy","IT")]:
    groups[dept].append(name)

print(groups)  
# defaultdict(<class 'list'>, {'HR': ['Alice'], 'IT': ['Bob', 'Cathy']})
```
- 自动计数、自动建表，不需要反复写 `if key not in dict:` 这种样板代码。

### 1.3 deque —— 双端队列

`deque` （double-ended queue）支持 **两端高效插入和删除** ，性能远超 `list` 。

```python
from collections import deque

q = deque([1, 2, 3])
q.appendleft(0)   # 左侧插入
q.append(4)       # 右侧插入
print(q)          # deque([0, 1, 2, 3, 4])
```

**应用场景** ：

- **队列/栈实现** （先进先出 / 后进先出）
- **[滑动窗口](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3&zhida_source=entity)** （例如： [实时计算](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%AE%9E%E6%97%B6%E8%AE%A1%E7%AE%97&zhida_source=entity) 最近 N 条数据的均值）
- **回溯/撤销功能** （浏览器历史记录）

还能用 `maxlen` 实现 **固定长度队列** ，自动丢弃旧数据：

```python
dq = deque(maxlen=3)
for i in range(5):
    dq.append(i)
    print(dq)  
# deque([0], maxlen=3)
# deque([0,1], maxlen=3)
# deque([0,1,2], maxlen=3)
# deque([1,2,3], maxlen=3)
# deque([2,3,4], maxlen=3)
```

### 1.4 namedtuple —— 可读性更好的元组

`tuple` 虽然轻量，但用索引取值不直观。  
`namedtuple` 让你既能享受 `tuple` 的性能，又能用 **字段名** 访问数据。

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x, p.y)   # 10 20
```

**应用场景** ：

- **[数据建模](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%95%B0%E6%8D%AE%E5%BB%BA%E6%A8%A1&zhida_source=entity)** （轻量版类，用来替代 [小数据](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%B0%8F%E6%95%B0%E6%8D%AE&zhida_source=entity) 对象）
- **返回多个值时更清晰** （函数返回 `(x,y)` → 可读性提升）
- **不可变数据结构** （和 tuple 一样是不可变的，更安全）

还能和解包结合：

```python
x, y = p
print(x, y)  # 10 20
```

### 1.5 OrderedDict —— 有序字典

Python3.7+ 之后，普通字典 `dict` 默认就是 **插入有序** 的，  
所以 `OrderedDict` 出场的机会少了，但它仍有一些特别用途：

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(list(od.keys()))  # ['a', 'b', 'c']
```

**应用场景** ：

- 实现 **LRU 缓存** （最近最少使用策略）
- 在某些需要兼容旧版本 Python 的项目中保证有序性
- 保证 [序列化](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%BA%8F%E5%88%97%E5%8C%96&zhida_source=entity) （JSON / YAML）时字段顺序固定

### 1.6 小结

- `Counter` → 快速计数
- `defaultdict` → 自动分组、自动计数
- `deque` → 高效队列 / 滑动窗口
- `namedtuple` → 轻量级 [数据模型](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%95%B0%E6%8D%AE%E6%A8%A1%E5%9E%8B&zhida_source=entity)
- `OrderedDict` → [有序字典](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=2&q=%E6%9C%89%E5%BA%8F%E5%AD%97%E5%85%B8&zhida_source=entity) ，缓存实现

一句话： `collections` 就是 Python 内置数据结构的“超级加强版”，能让你的代码 **更简洁、更高效、更 Pythonic** 。

## 2\. functools：函数式编程工具

在 Python 里，函数是 **一等公民** ：可以作为 [参数传递](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%8F%82%E6%95%B0%E4%BC%A0%E9%80%92&zhida_source=entity) 、作为返回值输出，还能动态生成新的函数。  
`functools` 模块就是一套“函数黑科技工具包”，帮助你更优雅地处理函数逻辑。

### 2.1lru\_cache —— 自动缓存结果

如果一个函数多次被调用，且输入参数相同，那么结果也一定相同。 `lru_cache` 可以自动帮你做 **结果缓存** ，避免重复计算。

```python
from functools import lru_cache

@lru_cache(maxsize=128)   # 最近最少使用缓存
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # 832040，计算飞快！
```

**应用场景** ：

- [递归](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E9%80%92%E5%BD%92&zhida_source=entity) & 动态规划（斐波那契、 [背包问题](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98&zhida_source=entity) ）
- 接口调用结果缓存（节省请求次数）
- 计算型函数（避免重复计算，提高性能）

还能查看缓存状态：

```python
print(fib.cache_info())  
# CacheInfo(hits=28, misses=31, maxsize=128, currsize=31)
```

### 2.2 partial —— 偏函数

有些函数参数很多，而我们经常只改其中一部分。  
用 `partial` 可以“预先绑定”一些参数，生成新的函数。

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)   # 固定 exp=2
cube = partial(power, exp=3)     # 固定 exp=3

print(square(5))  # 25
print(cube(2))    # 8
```

**应用场景** ：

- 固定部分参数，生成更简洁的 API
- 配合 [回调函数](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%9B%9E%E8%B0%83%E5%87%BD%E6%95%B0&zhida_source=entity) （GUI、并发）
- 提高代码可读性

小技巧： `partial` 常常用在 **并发库 concurrent.futures** 或 **GUI [事件绑定](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E4%BA%8B%E4%BB%B6%E7%BB%91%E5%AE%9A&zhida_source=entity)** 中。

### 2.3 reduce —— 累积计算

`reduce` 是一个经典的函数式工具，它把一个序列 **两两合并** ，直到得到一个结果。

```python
from functools import reduce

nums = [1, 2, 3, 4]
s = reduce(lambda x, y: x + y, nums)
print(s)  # 10
```

虽然 Python 更推荐直接用 `sum(nums)` 、 `min(nums)` 等 [内置函数](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%86%85%E7%BD%AE%E5%87%BD%E6%95%B0&zhida_source=entity) ，  
但在某些 **复杂聚合** 场景， `reduce` 仍然很有用。

例如计算 [阶乘](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E9%98%B6%E4%B9%98&zhida_source=entity) ：

```python
fact = reduce(lambda x, y: x * y, range(1, 6))
print(fact)  # 120
```

**应用场景** ：

- 自定义聚合（比方说链式合并字典/集合）
- [数据流](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%95%B0%E6%8D%AE%E6%B5%81&zhida_source=entity) 处理
- 某些函数式编程风格的代码

### 2.4 wraps —— 写装饰器必备

如果你写过装饰器，可能遇到过这样的问题：

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def hello():
    print("Hello!")

print(hello.__name__)  # wrapper（丢失原函数信息）
```

这就会导致调试、文档生成、反射时很不方便。  
解决方案就是 `functools.wraps` ：

```python
from functools import wraps

def log(func):
    @wraps(func)   # 关键！
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def hello():
    print("Hello!")

hello()
print(hello.__name__)  # hello ✅ 保留原函数名
```

**应用场景** ：

- 自定义装饰器
- 保留函数的 **元信息** （函数名、文档、注解）
- 避免调试时“一头雾水”

### 2.5 小结

- `lru_cache` → 自动缓存结果，提升性能
- `partial` → 固定部分参数，生成新函数
- `reduce` → 累积计算，适合复杂聚合
- `wraps` → 装饰器必备，保留函数元信息

一句话： `functools` 让函数不仅能“被调用”，还能“被改造”，是写高阶函数和装饰器的必修课。

## 3\. itertools：高效迭代器工具

如果你喜欢 **函数式风格** ，那 `itertools` 一定是最好的伙伴。  
它提供了很多 **[惰性计算](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%83%B0%E6%80%A7%E8%AE%A1%E7%AE%97&zhida_source=entity)** （lazy evaluation）的迭代器：不会一次性生成完整结果，而是按需计算，既省内存，又高效。  
避免了写一大堆 `for` 循环，让代码更简洁优雅。

### 3.1 无限迭代器

`itertools` 提供了几种“无限流式”迭代器：

```python
import itertools

for i in itertools.count(10, 2):  # 从 10 开始，每次 +2
    if i > 20:
        break
    print(i)  
# 10, 12, 14, 16, 18, 20
```

其他无限迭代器：

- `cycle([1, 2, 3])` → 无限循环 `[1, 2, 3]`
- `repeat("A", 5)` → 重复 `"A"` 5 次（可指定次数，否则无限）

**应用场景** ：

- 数据流生成器
- 模拟 [无限序列](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%97%A0%E9%99%90%E5%BA%8F%E5%88%97&zhida_source=entity)
- 与 `zip` / `map` 搭配实现对齐填充

### 3.2 组合与排列

排列和组合是 [算法](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E7%AE%97%E6%B3%95&zhida_source=entity) 常见场景， `itertools` 提供了现成函数。

```python
from itertools import permutations, combinations

letters = ["A", "B", "C"]
print(list(permutations(letters, 2)))  
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

print(list(combinations(letters, 2)))  
# [('A','B'), ('A','C'), ('B','C')]
```

区别：

- `permutations` → 有顺序（AB ≠ BA）
- `combinations` → 无顺序（AB = BA）

**应用场景** ：

- 密码/验证码穷举
- 排班、座位安排
- [组合优化](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96&zhida_source=entity) 问题

### 3.3 链式拼接

常见需求：把多个 [序列拼接](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E5%BA%8F%E5%88%97%E6%8B%BC%E6%8E%A5&zhida_source=entity) 在一起。  
用 `+` 拼接效率不高，还需要额外拷贝； `chain` 可以做到 **惰性拼接** 。

```python
from itertools import chain

a = [1, 2]
b = [3, 4]
print(list(chain(a, b)))  
# [1, 2, 3, 4]
```

相当于 `a + b` ，但不会提前创建新列表。  
如果数据量巨大，性能优势明显。

### 3.4 分组

`groupby` 是一个隐藏的神器，但需要注意 **数据必须先排序** ，否则结果可能出乎意料。

```python
from itertools import groupby

data = [("apple", 1), ("apple", 2), ("banana", 3), ("banana", 4)]

for k, g in groupby(data, key=lambda x: x[0]):
    print(k, list(g))
```

输出：

```python
apple [(apple,1),(apple,2)]
banana [(banana,3),(banana,4)]
```

**应用场景** ：

- 数据分组（日志按用户分组、销售数据按日期分组）
- 替代 `pandas.groupby` 的轻量方案

### 3.5 其他常用函数（速查表）

除了上面介绍的， `itertools` 还有不少常用工具：

- `islice(iterable, start, stop, step)` → 类似切片，但对 [迭代器](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=8&q=%E8%BF%AD%E4%BB%A3%E5%99%A8&zhida_source=entity) 有效
- `zip_longest(a, b, fillvalue=None)` → 对齐两个序列，缺失用 `fillvalue` 填补
- `product([1,2], ["A","B"])` → [笛卡尔积](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E7%AC%9B%E5%8D%A1%E5%B0%94%E7%A7%AF&zhida_source=entity) ，常用于参数组合
```python
from itertools import product

print(list(product([1, 2], ["A", "B"])))
# [(1,'A'), (1,'B'), (2,'A'), (2,'B')]
```

### 3.6 小结

- **无限迭代器** → 无限生成数据流（ `count`, `cycle`, `repeat` ）
- **组合/排列** → 枚举可能性（ `permutations`, `combinations`, `product` ）
- **链式拼接** → 高效合并序列（ `chain` ）
- **分组** → 数据按键分组（ `groupby` ）

一句话： `itertools` 就像 Python 的“乐高积木”，让你用最简洁的代码，拼出最复杂的迭代逻辑。

## 4\. 综合案例：日志分析

假设我们有一份 **Web 访问日志** ，想要快速得到以下结果：

- 访问量最多的 IP（可能是恶意爬虫？）
- 访问量前 10 的页面（热门页面统计）
- 分析某个 IP 是否频繁访问 `/index` （缓存优化查询）

用 `collections + functools + itertools` ，代码可以写得简洁优雅：

```python
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import chain

# 模拟日志数据 (IP, 页面)
logs = [
    ("192.168.0.1", "/index"),
    ("192.168.0.2", "/about"),
    ("192.168.0.1", "/index"),
    ("192.168.0.3", "/index"),
    ("192.168.0.2", "/about"),
]

# --- 1. 统计访问量 ---
ips = Counter(ip for ip, _ in logs)
pages = Counter(page for _, page in logs)

print("Top IP:", ips.most_common(1))
print("Top Pages:", pages.most_common(2))
# Top IP: [('192.168.0.1', 2)]
# Top Pages: [('/index', 3), ('/about', 2)]

# --- 2. 分组：按 IP 聚合访问的页面 ---
user_pages = defaultdict(list)
for ip, page in logs:
    user_pages[ip].append(page)
print(user_pages)
# defaultdict(list, {'192.168.0.1': ['/index','/index'], ...})

# --- 3. 缓存：查询某 IP 是否频繁访问首页 ---
@lru_cache(maxsize=None)
def is_frequent(ip):
    return user_pages[ip].count("/index") > 1

print(is_frequent("192.168.0.1"))  # True
print(is_frequent("192.168.0.3"))  # False
```

**这里的亮点：**

1. **`Counter`** → 秒算访问量排名，不用手写循环计数。
2. **`defaultdict`** → 自动初始化列表，轻松实现“IP → 页面列表”的映射。
3. **`lru_cache`** → 对热点查询做缓存，避免重复统计，提升性能。
4. **`itertools`** → 可以进一步用于合并多份 [日志文件](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6&zhida_source=entity) ，或做复杂组合过滤。

比如：

```python
# 假设我们有两份日志，可以用 chain 无缝拼接
more_logs = [
    ("192.168.0.4", "/contact"),
    ("192.168.0.1", "/index"),
]

all_logs = chain(logs, more_logs)
print(list(all_logs))
```

输出：

```python
[('192.168.0.1','/index'), ('192.168.0.2','/about'), ..., ('192.168.0.1','/index')]
```

这样无需额外创建大列表，直接迭代，内存友好。

## 5\. 总结

- **`collections`** → 提供更强大的数据结构：  
	`Counter` （统计）、 `defaultdict` （自动初始化）、 `deque` （高效队列）、 `namedtuple` （可读性更好的元组）。
- **`functools`** → 高阶函数 & 装饰器利器：  
	`lru_cache` （缓存）、 `partial` （偏函数）、 `wraps` （保持函数元信息）。
- **`itertools`** → 迭代器乐高积木：  
	`count` （无限迭代）、 `chain` （拼接序列）、 `permutations` （排列组合）、 `groupby` （分组）。

✨ 虽然它们只是 **“标准库里的小工具”** ，但却能让 Python 在 **[数据处理](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86&zhida_source=entity) / 脚本开发 / 算法实现** 中更简洁、更高效、更优雅。

下次当你觉得 Python 内置工具“不够用”时，先翻翻这三个模块，也许答案早已内置！

## 下一篇预告

**第7篇： `json / pickle / shelve` —— 数据序列化与 [持久化](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E6%8C%81%E4%B9%85%E5%8C%96&zhida_source=entity) 。**

写代码时，我们常常需要把数据保存下来，下次程序再运行时还能继续使用。那该选 **`json` 、 `pickle` 还是 `shelve`** 呢？

下一篇，我们就来聊聊 Python 里的三种常见“数据打包与存档”方式：

- `json` ：最常用、 [跨语言](https://zhida.zhihu.com/search?content_id=262300873&content_type=Article&match_order=1&q=%E8%B7%A8%E8%AF%AD%E8%A8%80&zhida_source=entity) 通用的序列化格式
- `pickle` ：Python 专属，几乎能保存任何对象
- `shelve` ：像“迷你数据库”，简单键值存取

让数据不只是存在内存里，而是能 **随时保存、随时加载** 。

## Tips：

本篇和本系列都只是完整教程中的一篇，完整内容索引见总览页：

[![](https://picx.zhimg.com/v2-f6941403b71427fe1eaef5bc73ac5a5b.jpg?source=7e7ef6e2&needBackground=1)](https://zhuanlan.zhihu.com/p/1932065916251791958)

如果你觉得内容有帮助，欢迎点赞 + 收藏 + 评论 + 关注 + 订阅 —— 你的支持，是我持续创作最重要的动力！

还没有人送礼物，鼓励一下作者吧

编辑于 2025-09-02 17:47・北京[程序员0基础入门大模型的学习路线！](https://zhuanlan.zhihu.com/p/31864213680)

[

0基础入门大模型，transformer、bert这些是要学的，但是 你的第一口不一定从这里咬下去。真的没有必要一上来就把时间精力全部投入到复杂的理论、各种晦涩的数学公式还有编程语言上，...

](https://zhuanlan.zhihu.com/p/31864213680)

赞同 18