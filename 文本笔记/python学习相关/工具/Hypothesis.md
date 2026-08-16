Python 生态最主流**基于属性的测试库（Property‑Based Testing）**。

## 和普通单元测试区别

- 普通单元测试：**你手动写几组输入 + 预期输出**，只能测你想到的案例。
- Hypothesis：你描述**函数永远应该成立的性质（不变量 property）**，库自动生成成百上千组输入（包含空、边界、极端值、乱码、重复元素等你想不到的 case），去寻找破坏这条性质的反例。

> 发现 bug 后，它会自动**收缩（shrink）**，把失败案例化简成最小复现输入，方便调试 PyPI。

## 简单示例（配合 pytest）

```python
from hypothesis import given, strategies as st

def my_sort(lst):
    # 有bug：用set会丢失重复元素
    return sorted(set(lst))

# 性质：排序前后，列表元素完全一致
@given(st.lists(st.integers()))
def test_sort_property(xs):
    ys = my_sort(xs)
    assert len(xs) == len(ys)
```

运行会直接报出最小失败样例：`ls=[0,0]`，重复元素被错误删掉了 PyPI。

## 核心概念

1. **`@given`**：装饰器，声明要自动生成参数
2. **strategies（策略 st.xxx）**：定义生成什么数据

    - `st.integers()` 整数
    - `st.text()` 任意字符串（含 unicode、空串）
    - `st.lists(st.integers())` 整数列表
    - 支持组合、嵌套、自定义复杂结构体

3. **shrink 收缩**：出现失败，自动把巨大输入缩减到最小失败用例，这是它最强的特性。