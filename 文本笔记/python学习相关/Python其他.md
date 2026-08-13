# 魔术方法

## 基础方法

### `__init__` 和 `__new__`

[[init和new.py]]

### `__del__`

这个方法可以看作这个对象的析构函数，很不可控，只有当对象的引用计数为 0 时才会被调用，理论上可以在任意时刻发生

> [!WARNING]
> `__del__()`与 `del` 关键字没有任何关系

### `__repr__` 和 `__str__`

都是返回这个对象的字符串的字符串表达，但是，后者更强调人类可读，前者需要有更多信息。

对象传入 `print` 函数时，如果类定义了`__str__`，会优先调用`__str__`，没有的时候会调用`__repr__`。

而当两个函数不需要做很多区分时，只重写 `__rper__` 即可。

### `__format__`

[[format.py]]

### `__bytes__`

返回这个对象的自定义二进制数据

[[bytes.py]]

## 比较方法

六个方法：

| 比较符号 | 方法       |
| ---- | -------- |
| `==` | `__eq__` |
| `!=` | `__ne__` |
| `>`  | `__gt__` |
| `<`  | `__lt__` |
| `>=` | `__ge__` |
| `<=` | `__le__` |

如没有定义 `__eq__`方法，对两个对象使用`a == b` 时，等价于`a is b`。

如果没有定义 `__ne__`方法，但是定义了`__eq__`方法，会调用`__eq__`并取反，也就是一般只用定义`__eq__` 即可。

`__gt__`和 `__lt__` 也是上面的规则，但是这仅仅对于比较的都是同一个类的两个对象。

当 `a == b`和`a < b`而且`b.__class__`是`a.__class__`的子类时，会分别调用`b.__eq__(a)` 和`b.__gt__(a)`。

### `__hash__`

原本所有的类都会默认实现一个 `hash`方法，用于存储到`dict`或`set` 时调用。

如果定义了 `__eq__` 函数，系统就不会自动生成这个函数了。

这个函数有若干要求，首先，该函数的返回结果必须是整数，并且 `__eq__`相等的两个对象，`__hash__` 的结果必须相同。

官方建议，使用 `hash()` 函数并将类的重要参数组成元组作为参数获得 hash 值，并返回。

比如：

```python
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return False
		else:
			return self.name == other.name and self.age == other.age
	
	def __hash__(self):
		return hash((self.name, self.age))
```

> [!NOTE]
> 注意，当一个 hashable 作为键传入字典等容器时，不可以再将它当作 mutable 的对象，因为这违反了 hashtable 的工作原理

### `__bool__`

当一个类没有实现这个方法时，它的对象传入 `if` 时，会被默认当作`true`。

而实现了这个方法的类的对象，则会调用这个方法。

## 属性方法

[[属性相关魔术方法.py]]

### `__getattr__`

当访问类中不存在的显式定义的 attr 时，会调用这个函数。

### `__getattribute__`

当访问类对象的任何 `attr` 时，都会调用这个函数。

> [!WARNING]
> 小心，当想要使用 `__getattribute__` 默认行为时，需要使用`super().__getattribute__(name)`，不能使用`getattr(self, name)`，这会产生无限递归。
>
> ```python
> class A:
> 	def __init__(self, data):
> 		self.data = data
> 		self.counter = 0
> 		
> 	def __getattribute__(self, name):
> 		self.counter += 1  # 这里又无限递归了
> 		return super().__getattribute__(name)
> ```

### `__setattr__`

这个函数和 `__getattr__`不同，在任何时候设置属性时，都会调用这个函数，包括`__init__` 内的赋值。

需要使用 `super().__setattr__(name, val)` 调用默认的设置函数。

### `__delattr__`

他和 `__del__` 没有关系，甚至在对象的整个生命周期里都不会被调用。

只有显式地调用 `del o.attr` 时才会被调用。

### `__dir__`

在使用 `dir(o)` 时，会调用`o.__dir__()`。

得到这个对象所有可以访问到的属性和方法。

> [!NOTE] `__slots__`
> 它并非一个方法，而是一个标记，规定了某个类里可以有哪些自定义的属性。
> ```python
> class A:
> 	__slots__ = ["a", "b"]
> ```

## 类构建方法

### `__init_subclass__`

当这个类成为另一个类的基类时，衍生类创建时会调用这个函数。

### `__set_name__`

更多用在描述器，在类构建一个带有 `__set_name__` 的描述器的某个实例时会调用。

### `__class_getitem__`

区别于 `__getitem__`，这个是在对 class 做切片时调用的；而后者是在对象做切片时使用的。

这个函数也是 `List[int]` 等的 type hint 的实现原理。

### `__mro_entries__`

> If an object that is not a class object appears in the tuple of bases of a class definition, then method `__mro_entries__` is searched on it. If found, it is called with the original tuple of bases as an argument. The result of the call must be a tuple, that is unpacked in the base classes in place of this object. (If the tuple is empty, this means that the original bases is simply discarded.) If there are more than one object with `__mro_entries__`, then all of them are called with the same original tuple of bases. This step happens first in the process of creation of a class, all other steps, including checks for duplicate bases and MRO calculation, happen normally with the updated bases.
> Using the method API instead of just an attribute is necessary to avoid inconsistent MRO errors, and perform other manipulations that are currently done by `GenericMeta.__new__`. The original bases are stored as `__orig_bases__` in the class namespace (currently this is also done by the metaclass). For example:
> ```python
> class GenericAlias:
>    def __init__(self, origin, item):
>        self.origin = origin
>        self.item = item
>    def __mro_entries__(self, bases):
>        return (self.origin,)
> class NewList:
>    def __class_getitem__(cls, item):
>        return GenericAlias(cls, item)
> class Tokens(NewList[int]):
>    …
> assert Tokens.__bases__ == (NewList,)
> assert Tokens.__orig_bases__ == (NewList[int],)
> assert Tokens.__mro__ == (Tokens, NewList, object)
> ```
> Resolution using `__mro_entries__` happens _only_ in bases of a class definition statement. In all other situations where a class object is expected, no such resolution will happen, this includes `isinstance` and `issubclass` built-in functions.
> NOTE: These two method names are reserved for use by the `typing` module and the generic types machinery, and any other use is discouraged. The reference implementation (with tests) can be found in [[4]](https://peps.python.org/pep-0560/#id10), and the proposal was originally posted and discussed on the `typing` tracker, see [[5]](https://peps.python.org/pep-0560/#id11).

### `__prepare__`

这个方法在写的时候需要手动加上 `@classmethod`

用来准备构建 class 的命名空间的。

### `__instancecheck__`和`__subclasscheck__`

在使用`isinstance(o, base)`和`issubclass(o, base)`时调用。

## 运算相关

### 二元运算

|         符号         |                 函数                  |                      备注                      |
| :----------------: | :---------------------------------: | :------------------------------------------: |
|         +          |              `__add__`              |                                              |
|         -          |              `__sub__`              |                                              |
|         *          |              `__mul__`              |                 另：`__rmul__`                 |
|         /          |            `__truediv__`            |                                              |
|         @          |            `__matmul__`             |                     矩阵乘法                     |
|         //         |           `__floordiv__`            |                      整除                      |
|         %          |              `__mod__`              |                      取余                      |
| `divmod(o_1, o_2)` |            `__divmod__`             |                  既得到商，又拿到余数                  |
|         **         | `__pow__(self, other, modulo=None)` | 乘方，加上`modulo`就是`(self ** other) % modulo`的结果 |
|         <<         |            `__lshift__`             |                      左移                      |
|         >>         |            `__rshift__`             |                      右移                      |
|         &          |              `__and__`              |                      与                       |
|         ^          |              `__xor__`              |                      异或                      |
|         \|         |              `__or__`               |                      或                       |

> [!NOTE] `__rmul__`
> 想象一下向量的数乘，当有一个自定义类`Vector`时。
> ```python
> class Vector:
> 	def __init__(self, x, y):
> 		self.x = x
> 		self.y = y
> 	def __mul__(self, other):
> 		if isinstance(other, int):
> 			return Vector(self.x * other, self.y * other)
> ```
> 
> 这时`Vector(1, 2) * 3` <==> `Vector(1, 2).__mul__(3)`
> 而 `3 * Vector(1, 2)` 则无法使用，这时，可以定义一个`__rmul__`，调用时`int`没有关于`Vector`乘法，会查找后者的`__rmul__`进行运算。
> 其他的所有函数也都有他们的`r`版本。
> 还有一种`i`版本，对应的是`+=`，`-=`...

### 一元运算

|     符号      |      方法       |        备注        |
| :---------: | :-----------: | :--------------: |
|      -      |   `__neg__`   |                  |
|      +      |   `__pos__`   |                  |
|   `abs()`   |   `__abs__`   |                  |
|      ~      | `__invert__`  |                  |
|   `int()`   |   `__int__`   |   需要返回int的数据结构   |
|  `float()`  |  `__float__`  |  需要返回float的数据结构  |
| `complex()` | `__complex__` | 需要返回complex的数据结构 |
|     []      |  `__index__`  |                  |


> [!NOTE] `__index__`
> ```python
> class Vector:
> 	def __init__(self, x, y):
> 		self.x = x
> 		self.y = y
> 	def __index__(self):
> 		return int(self.x)
> v = Vector(1.2, 5)
> list = [1, 2, 3, 4]
> list[v] # list[1] = 2
> ```
> 而且当`__index__`被定义之后，会被`__int__`、`__float__`和`__complex__`默认使用，除非你手动定义。


### 取整运算



