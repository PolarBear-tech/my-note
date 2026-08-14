---
source: "https://zhuanlan.zhihu.com/p/555359585"
created: 2026-08-13
---

有人可能在平时看代码的时候，会看到类似这样的标识 `@dataclass` 。 `@` 众所周知，简单易得，是 python 当中修饰符的意思（狗头）。那么 `@dataclass` 是做什么的呢？

### 开始

首先我们可以看这么一段代码：

```python
class Car():
    def __init__(self, brand:str, price:float, color:str):
        self.brand = brand
        self.price = price
        self.color = color 

    def __repr__(self):
        return f"{self.brand}, {self.price}, {self.color}"

    def __eq__(self, other):
        return (self.brand, self.price, self.color) == (other.brand, other.price, other.color)
```

在这段代码中，我们定义了一个类 `Car` ，并且实现了它的三个函数：初始化、输出属性的值, 以及判断两个 Car 实例是否相等。

然后我们可以看一下结果。

```python
>> bmw = Car("bmw", 500000, "red")
>> tesla = Car("tesla", 30000, "gray")
>> print(bmw)
bmw, 500000, red
>> print(tesla)
tesla, 30000, gray
>> bmw == tesla
False
```

OK,可以看到，我们非常成功的实现了我们想要实现的功能，太牛逼了。 但是等一等。如果我们再回头重新看我们的这段代码的话，发现其实并不是那么的优雅： 1、有的代码写的简单无趣，只是把一段代码重复了 N 个变量遍而已； 2、如果我想要新加一个变量，那么我就要修改这三个函数，这三个函数的修改其实也是简单无趣的重复而已。

于是，bang！ `dataclass` 类，诞生了！烦恼就解决了！让我们看下 `dataclass` 该怎么用

```python
from dataclasses import dataclass

@dataclass(order=True)
class Car():
    brand : str
    price : float 
    color : str
```

Over, that's all.

是不是非常简单？我们确认下他是不是真的实现了我们的功能：

```python
>> bmw = Car("bmw", 500000, "red")
>> tesla = Car("tesla", 30000, "gray")
>> print(bmw)
bmw, 500000, red
>> print(tesla)
tesla, 30000, gray
>> bmw == tesla
False
```

太牛逼了！ Double 牛逼！

其实牛逼不止于此。除了这三个函数之外， `dataclass` 还它实现了其他的一些函数，具体的函数名可以参考 [3. Data model — Python 3.14.7 documentation](https://docs.python.org/3/reference/datamodel.html#specialnames) ，可以看下哪些这是你需要的。如果没有的话，那就需要你自己写了, good luck。

### 默认初始化

接下来让我们再深入的思考一下。在上面使用 `dataclass` 进行定义的时候，我们只是用了 `name:type` 就进行了初始化，那么如果我们想要使用默认值进行初始化呢，比如实现这个例子

```python
class Car():
    def __init__(self, brand:str, price:float, color:str = ‘red'):
        self.brand = brand
        self.price = price
        self.color = color
```

那么我们可以写为

```python
from dataclasses import dataclass

@dataclass()
class Car():
    brand : str
    price : float 
    color : str = "red"
```

这个也是很直观的，比较容易理解。 那么我们再来一个，如果我想初始化一个 `list` 呢，比如新加一个 `order_list`

```python
class Car():
    def __init__(self, brand:str, price:float, color:str = ‘red'
                    order_list=[]):
        self.brand = brand
        self.price = price
        self.color = color 
        self.order_list = []
```

那么我们可以写成下面这样吗

```python
from dataclasses import dataclass

@dataclass(order=True)
class Car():
    brand : str
    price : float 
    color : str = "red"
    order_list : list = []
```

执行一下就可以发现，实际上是报错的。那我们应该怎么初始化呢？ 实际上，我们需要这么写： `order_list : list[int] = field(default_factory = list)`

在 python 的 class 里面，每个变量可以称之为一个 field。那么在使用 `dataclass` 之后， `dataclass` 觉得原先的 `field` 可能不太够用，于是也定义了一个 `field` 函数。在 `field` 函数中，有一个变量叫 `default_factory` 。你可以用它来定义一个 初始化函数 。这也就意味着，不仅仅可以简单的 list 初始化，也可以进行复杂一点的初始化了，比如

```python
import random 

def random_color():
    color_list = ['red','gray', 'black']
    return random.choice(color_list)

from dataclasses import dataclass
from dataclasses import field

@dataclass
class Car():
    brand : str 
    price : float = 0.0
    color : str = field(default_factory=random_color)

>> bmw = Car('bmw', '500000')
>> tesla = Car("tesla", "300000", 'gray')
>> print(bmw, tesla)

Car(brand='bmw', price='500000', color='black') Car(brand='tesla', price='300000', color='gray')
```

可以看到，bmw 随机的初始化了一个颜色 `black`. 但是要注意一点，这个初始化函数是不支持传参数的。那么，如果你就是需要初始化一个东西，而且必须要参数，这个该怎么办呢？ 这是时候，你自己定义一个 `__post__init__` 函数就可以了。他会在 [init函数](https://zhida.zhihu.com/search?content_id=211546098&content_type=Article&match_order=1&q=init%E5%87%BD%E6%95%B0&zhida_source=entity) 之后自动的去执行。

### field 是嘛啊

因为可以用 field 函数替代原生的 field(),那么其实意味着我们可以这么写

```python
from dataclasses import dataclass

@dataclass(order=True)
class Car():
    brand : str = field(default = "None")
    price : float = field(default = '0.0')
    color : str = field(default ="red")
    order_list : list[int] = field(default_factory = list)
```

所有的变量都用 `field` 函数来代替，并且设置了 `default` 值。 那么用这个 `field` 来控制变量有什么好处呢？它可以让我们更好的来掌控`dataclass`所提供给我们的功能。我们可以列出 `field` 的参数来看下他所能实现的功能，但是在此之前，我们先来思考一下：

> 尽管 dataclass 帮我们做了这么多事情，但是有些东西我们想要再来点 [个性化定制](https://zhida.zhihu.com/search?content_id=211546098&content_type=Article&match_order=1&q=%E4%B8%AA%E6%80%A7%E5%8C%96%E5%AE%9A%E5%88%B6&zhida_source=entity) ，而不是 dataclass 一手包办的？

我们看下 filed 的参数就明白了

```python
dataclasses.field(*, default=MISSING, default_factory=MISSING, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=MISSING)
```

`default` 就是默认值 `default_factory` 也说过了，可以用来进行初始化函数。 `init` 就是会让该字段不再进行初始化 `repr` 就是让字段不会再放入到 repr 里面去。 比如我们试下：

```python
from dataclasses import dataclass
from dataclasses import field

@dataclass
class Car():
    brand : str 
    price : field(repr=False, default = 0.0)
    color : str = field(default_factory=random_color)
```

然后我们打印看下：

```python
>> bmw = Car("bmw", 500000, "red")
>> print(bmw)

bmw, red
```

可以看到， price 的值就不会再打印出来了。

### 你挺好的，但是谢谢了

介绍完了 dataclass 帮我们实现的这些函数之后，相信你会不由得竖起大拇指为他点赞。但是有的同学就未必愿意了：

> 你实现的挺好的，但是不必了。

比如，你帮我实现 init 函数挺好的，但是不用了，我自己来就好了。那么该怎么办呢？很简单，你就直接自己实现一个就好了，你自己实现的函数会覆盖你 dataclass 所定义的函数。

那如果我就是头铁，我不想实现，但是你也别帮我实现，那么该怎么办呢？ 其实看下 dataclass 类的参数就知道了 `dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False)` 这里面 init, reper, eq, order 对应的就是 初始化，打印，以及判断相等的 flag。使用这个的 true/false 就可以控制了。 除了这个几个参数之外，还有一个参数可能会常用到 `frozen` 。 `frozen` 来表明实例是否可以被重新赋值，例如：

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Car():
    brand : str
    price : float 
    color : str = "red"
>> bmw = Car('bmw', '500000')
>> bmw.color = 'black'

FrozenInstanceError                       
Traceback (most recent call last)
/Users/yang.liu/Documents/github/test/dataclass.ipynb Cell 13 in <cell line: 1>()
----> 1 bmw.color = 'black'

File <string>:4, in __setattr__(self, name, value)

FrozenInstanceError: cannot assign to field 'color'
```

可以看到直接报错了。这个方法在你实例化你的数据后，不想让人修改非常有用。 其他的几个参数用的相对来说要少一些，当然也挺有用，感兴趣话可以去这里参考看下。