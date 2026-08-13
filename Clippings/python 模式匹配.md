---
source: "https://zhuanlan.zhihu.com/p/706263499"
created: 2026-08-13
---

# 基本语法

使用 match 语句和 case 子句来实现模式匹配。

match 语句会逐个检查 case 子句，直到找到一个匹配的 case 子句。

```python
match subject:
   case pattern1:
       action1
   case pattern2:
       action2
   ...
   case _:
       default_action
```

# 简单值匹配

```python
def describe_type(item):
    match item:
        case 0:
            return "It's a zero"
        case 1:
            return "It's a one"
        case str():
            return "It's a string"
        case list():
            return "It's a list"
        case _:
            return "It's something else"

print(describe_type(0))  # It's a zero
print(describe_type(1))  # It's a one
print(describe_type("hello"))  # It's a string
print(describe_type([1, 2, 3]))  # It's a list
```

# 结构匹配

```python
def describe_structure(data):
    match data:
        case []:
            return "It's an empty list"
        case [x]:
            return f"It's a list with one item: {x}"
        case [x, y]:
            return f"It's a list with two items: {x} and {y}"
        case [a, *rest]:
            return f"It's a list starting with {a} and the rest is {rest}"

print(describe_structure([]))  # It's an empty list
print(describe_structure([1]))  # It's a list with one item: 1
print(describe_structure([1, 2]))  # It's a list with two items: 1 and 2
print(describe_structure([1, 2, 3, 4]))  # It's a list starting with 1 and the rest is [2, 3, 4]
```

# 对象匹配

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point: Point):
    match point:
        case Point(x = 0, y =0):
            return "It's the origin"
        case Point(x = 0, y = y):
            return f"It's on the y-axis at {y}"
        case Point(x = x, y = 0):
            return f"It's on the x-axis at {x}"
        case Point():
            return f"It's at ({point.x}, {point.y})"
        case _:
            return "It's somewhere else"

print(describe_point(Point(0, 0)))  # It's the origin
print(describe_point(Point(0, 5)))  # It's on the y-axis at 5
print(describe_point(Point(3, 0)))  # It's on the x-axis at 3
print(describe_point(Point(3, 5)))  # It's at (3, 5)
```

# 条件匹配（守卫）

```python
def categorize_num(item: int):
    match item:
        case n if n < 0:
            return "negative"
        case 0:
            return "zero"
        case n if n % 2 == 0:
            return "positive even"
        case _:
            return "positive odd"

print(categorize_num(-1))  # negative
print(categorize_num(0))  # zero
print(categorize_num(2))  # positive even
print(categorize_num(3))  # positive odd
```

# OR 模式

```python
def describe_or_type(item):
    match item:
        case str() | list():
            return "It's a string or a list"
        case int() | float():
            return "It's a number"
        case _:
            return "It's something else"

print(describe_or_type("hello"))  # It's a string or a list
print(describe_or_type([1, 2, 3]))  # It's a string or a list
print(describe_or_type(3))  # It's a number
print(describe_or_type(3.5))  # It's a number
print(describe_or_type(Point(3, 5)))  # It's something else
```

# 变量捕获

```python
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Quitting the program"
        case ["hello", name]:
            return f"Hello, {name}"
        case ["add", *number]:
            return f"The sum is {sum(map(int, number))}"
        case _:
            return "Invalid command"

print(process_command("quit"))  # Quitting the program
print(process_command("hello world"))  # Hello, world
print(process_command("add 1 2 3"))  # The sum is 6
print(process_command("sub 1 2 3"))  # Invalid command
```