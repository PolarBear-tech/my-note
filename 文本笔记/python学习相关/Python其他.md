# 魔术方法

## `__init__` 和 `__new__`

[[init和new.py]]

## `__del__`

这个方法可以看作这个对象的析构函数，很不可控，只有当对象的引用计数为 0 时才会被调用，理论上可以在任意时刻发生

> [!WARNING]
> `__del__()`与 `del` 关键字没有任何关系

## `__repr__` 和 `__str__`

都是返回这个对象的字符串的字符串表达，但是，后者更强调人类可读，前者需要有更多信息。

对象传入 `print` 函数时，如果类定义了`__str__`，会优先调用`__str__`，没有的时候会调用`__repr__`。

而当两个函数不需要做很多区分时，只重写 `__rper__` 即可。

## `__format__`

[[format.py]]

## `__bytes__`

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

如没有定义`__eq__`方法，对两个对象使用`a == b`时，等价于`a is b`。
如果没有定义`__ne__`方法，但是定义了`__eq__`方法，会调用`__eq__`并取反，也就是一般只用定义`__eq__`即可。
`__gt__`和`__lt__`也是上面的规则，但是这仅仅对于比较的都是同一个类的两个对象。

当`a == b`和`a < b`而且`b.__class__`是`a.__class__`的子类时，会分别调用`b.__eq__(a)`和`b.__gt__(a)`。

## `__hash__`

原本所有的类都会默认实现一个`hash`方法，用于存储到`dict`或`set`时调用。

如果定义了`__eq__`函数，系统就不会自动生成这个函数了。

这个函数有若干要求，首先，该函数的返回结果必须是整数，并且`__eq__`相等的两个对象，`__hash__`的结果必须相同。

官方建议，使用`hash()`函数并将类的重要参数组成元组作为参数获得hash值，并返回。

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
> 注意，当一个hashable作为键传入字典等容器时，不可以再将它当作mutable的对象，因为这违反了hashtable的工作原理


