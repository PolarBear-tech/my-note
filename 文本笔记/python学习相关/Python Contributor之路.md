## RoadMap

- [x] C 语言学习
- [ ] 阅读源码

## 资源

- [中国大学MOOC](https://www.icourse163.org/)
- [Python Developer’s Guide](https://devguide.python.org/)

## 关于源码

按「对读 CPython 源码的直接帮助」**排序，给你一份务实的书单。不需要全读，每本标了**重点章节。

---

### 🔥 最优先：直接帮你读 CPython 的书

这两本比教科书更值钱，因为它们就是**对着 CPython 源码讲的**。

#### 1. 《Python 源码剖析》— 陈儒

- **基于 Python 2.5，但核心机制完全适用到今天**
- **重点读**：第 2 章（对象模型）、第 3 章（整数/字符串/list/dict 的实现）、第 4 章（解释器与字节码）
- 中文世界最好的 CPython 源码导读，翁恺的课学完后读它刚刚好
- 缺点：GC 部分较老，GIL 部分需要结合新版源码看

#### 2. *CPython Internals* — Anthony Shaw

- **基于 Python 3.9，非常新**
- 从编译管线、对象模型、内存管理到 C-API 都有覆盖
- 有纸质书和 PDF，作者还配了调试环境的 Docker 镜像
- 如果你英文可以，**这是目前最好的入门书**

---

### 📐 编译原理（补「代码怎么变成字节码」）

#### 3. 《编译原理（第 3 版）》（龙书）— Aho 等

- **你只需要读前 3 章**（词法分析、语法分析、语法制导翻译）
- 目的不是让你写编译器，而是让你看到 CPython 的 `tokenizer.c`、`parser.c`、`ast.c` 时，知道它们在流水线的哪一环
- 机械工业出版社，中文版很成熟

> 💡 替代方案：如果龙书太枯燥，可以直接看 CPython 官方 Dev Guide 的 [Compiler](https://devguide.python.org/internals/compiler/) 章节，配合龙书查概念。

---

### 🖥️ 操作系统 / 内存管理（补「运行时怎么管内存」）

#### 4. 《操作系统导论》（*Operating Systems: Three Easy Pieces*）— Arpaci-Dusseau

- **强烈推荐，现代、免费、写得极好**
- 重点读「虚拟化内存」**部分（第 12–22 章左右）：虚拟地址空间、分页、malloc 底层、垃圾回收
- 读完你会理解为什么 CPython 要自己造 `obmalloc`（pymalloc）而不是直接用系统 malloc
- 有中文版，也有 [免费英文版官网](http://pages.cs.wisc.edu/~remzi/OSTEP/)

#### 5. 《深入理解计算机系统（第 3 版）》（CSAPP）— Bryant & O'Hallaron

- **只读第 9 章：虚拟内存**。这是整本书最精华的章节之一
- 配合实验（malloc lab）最好，能让你真正理解堆管理和内存对齐
- 机械工业出版社，中文版极佳

#### 6. 《程序员的自我修养—链接、装载与库》— 俞甲子等

- **非常被低估的中文好书**
- 重点读第 1–6 章：目标文件格式、静态/动态链接、装载、内存布局
- 对理解 CPython 怎么加载 `.so` / `.pyd` 模块、C 扩展的符号解析特别有帮助

---

### 📋 阅读路线图（建议顺序）

| 阶段        | 读什么                         | 目的                              |
| --------- | --------------------------- | ------------------------------- |
| **现在**    | 《Python 源码剖析》第 2–3 章        | 建立 CPython 对象模型的直觉              |
| **同时**    | CSAPP 第 9 章（虚拟内存）           | 理解 `PyObject_Malloc` 和引用计数      |
| **1 个月后** | 龙书前 3 章 + CPython Dev Guide | 看懂 `compile.c` 和 `ceval.c` 的流水线 |
| **穿插**    | 《操作系统导论》内存部分                | 理解 GC 和内存池的设计动机                 |
| **进阶**    | *CPython Internals* 全书      | 把碎片知识串成体系                       |

---

### ⚠️ 不要做的事

- **不要从头到尾读龙书**：对读 CPython 来说，第 4 章以后的代码优化、目标代码生成基本用不上
- **不要从头到尾读 CSAPP**：除非你有半年时间，否则只挑虚拟内存和链接两章
- **不要纠结 Python 2 vs 3 的差异**：《Python 源码剖析》虽然基于 2.x，但**对象模型和解释器循环的核心机制几乎没变**，先建立直觉，再用新版源码校正细节

---

#### 一句话总结

> **《Python 源码剖析》+ CSAPP 第 9 章 + 龙书前 3 章**，这三样啃完，再打开 CPython 源码，你会感觉从「看天书」变成「查字典」。

## 工具链

### bear

生成 complie_

```bash
sudo apt install bear
```

## pkg-config

## pkg‑config 是什么

`pkg‑config` 是 Linux/Unix 下的**库元数据工具**，不是编译器，也不是开发库本身。

简单一句话：**帮编译脚本自动查询第三方库的头文件路径、编译参数、链接参数**。

### 它干什么活

当你编译软件（比如 CPython）需要依赖系统库：`openssl`、`libffi`、`readline`。

这些库安装后分散在系统各处：

- 头文件：`/usr/include/xxx.h`
- 库文件：`/usr/lib/x86_64‑linux‑gnu/libxxx.so`

手写 `-I/usr/include -L/usr/lib -lxxx` 很麻烦，不同系统路径还不一样。

`pkg‑config` 读取 `.pc` 文件（存于 `/usr/lib/pkgconfig/`），里面记录该库的编译、链接参数。

举个例子终端直接执行：

```bash
pkg-config --cflags libffi
pkg-config --libs libffi
```

输出该库需要的 `-I` 头文件路径、`‑l` 链接参数。

### 和 CPython 的关系

CPython 的 `configure` 脚本会调用 `pkg‑config`：

```
checking for libffi … via pkg‑config
```
1. 如果有 pkg‑config：自动拿到 libffi、openssl、readline 的编译参数，开启对应的扩展模块（`_ctypes`、`ssl`）。
2. **缺少 pkg‑config（就是你刚才看到的警告）**
    configure 不会直接报错崩溃，但**无法用.pc 文件探测库**，会降级尝试猜路径。
    - 猜成功：模块正常编译
    - 猜失败：直接跳过该扩展，编译出来的 Python 就没有这个模块。

> ⚠️重点区分：
> - `pkg‑config`：查询工具
> - `libffi‑dev / libssl‑dev`：真正的库源码/头文件
> 就算装了 pkg‑config，没装 `‑dev` 开发包，照样检测不到库。

### 对你当前场景的影响

1. **Cpython 内核源码阅读（ceval.c / PyObject）：不受影响**
clangd、`gen_compile_commands.py`、解释器核心编译，**完全不需要 pkg‑config**。
2. 只影响**第三方扩展模块**：ssl、ctypes、readline 等是否被编译进你本地编译出来的 python。

如果你只是看解释器内核源码，这个警告可以无视；如果你要本地编译一个功能完整的 Python，建议安装。

### 实操小例子

```bash
# 安装
sudo apt install pkg-config

# 查看系统有哪些pc文件
ls /usr/lib/x86_64-linux-gnu/pkgconfig/

# 查询libffi
pkg-config --cflags --libs libffi
```

### 类比理解

`pkg‑config` ≈ 一个**库信息查询手册**。

configure（CPython 配置脚本）就是查手册的人。

手册丢了（没装 pkg‑config），人只能靠记忆瞎猜库在哪，有可能猜对，有可能猜错漏掉功能。

> Windows MSVC 生态没有 pkg‑config，Windows 用 vcpkg 的方式实现类似能力。

#### 总结

- 它不是编译器，不是库；是查询工具。
- 警告≠报错，核心解释器依旧可以编译。
- 读 CPython 内核源码可以忽略警告；要完整 Python 二进制建议装上。