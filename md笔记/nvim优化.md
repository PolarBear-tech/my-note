# img-clip.nvim

# weztrerm.nvim

`willothy/wezterm.nvim` 的核心定位是：**在 Neovim 里通过 Lua 调用 `wezterm` CLI，从而控制外部的 WezTerm 终端**。它不需要你在 WezTerm 侧做任何配置，纯 nvim 插件。

---

## 一、安装

要求 **Neovim >= 0.10**。

```lua
-- lazy.nvim
{
    'willothy/wezterm.nvim',
    config = true,
}
```

### 配置选项

```lua
{
    'willothy/wezterm.nvim',
    opts = {
        -- 默认会注册 :WeztermSpawn 命令
        -- 如果你不需要这个命令，设为 false
        create_commands = true,
    },
}
```

---

## 二、核心 API

插件暴露的模块是 `require('wezterm')`，主要分两类：**标签/窗格切换** 和 **任务执行**。

### 1. 切换标签页（switch_tab）

```lua
local wezterm = require('wezterm')

-- 按索引切换到指定标签页
-- 不传参数时，自动读取 vim.v.count（即 3<leader>wt 会跳到第 3 个标签）
vim.keymap.set("n", "<leader>wt", wezterm.switch_tab.index)

-- 也可以显式传索引
vim.keymap.set("n", "<leader>w1", function() wezterm.switch_tab.index(1) end)
vim.keymap.set("n", "<leader>w2", function() wezterm.switch_tab.index(2) end)

-- 相对切换（下一个/上一个）
vim.keymap.set("n", "<leader>wn", wezterm.switch_tab.relative)
vim.keymap.set("n", "<leader>wp", function() wezterm.switch_tab.relative(-1) end)
```

> 规律：**所有接收数值参数的函数，如果没传参，会自动检查 `vim.v.count`**。

### 2. 切换窗格（switch_pane）

在 `flatten.nvim` 的源码中可以看到实际用法：

```lua
-- 切换到指定 pane id（通常从环境变量获取当前 pane）
vim.keymap.set("n", "<leader>wf", function()
    local pane_id = tonumber(os.getenv("WEZTERM_PANE"))
    if pane_id then
        require('wezterm').switch_pane.id(pane_id)
    end
end)
```

### 3. 执行任务（spawn）

#### 方式 A：命令 `:WeztermSpawn`

安装后默认会注册一个用户命令：

```vim
:WeztermSpawn cargo build
:WeztermSpawn npm run dev
:WeztermSpawn python script.py
```

这会在 **WezTerm 的新标签页** 中执行命令。

#### 方式 B：Lua API（如果文档中有暴露）

完整的 API 列表建议直接在 nvim 中查看插件自带的文档：

```vim
:h wezterm.nvim
```

或打开插件目录下的 `doc/wezterm.nvim.txt`。

---

## 三、典型使用场景

### 场景 1：快速跳转到 WezTerm 的某个标签

```lua
-- 1-9 数字直接跳转
for i = 1, 9 do
    vim.keymap.set("n", "<leader>" .. i, function()
        require('wezterm').switch_tab.index(i)
    end)
end
```

### 场景 2：配合 flatten.nvim 使用

这是最常见的组合。`flatten.nvim` 负责把外部命令打开的文件"扁平化"到当前 nvim 实例，而 `wezterm.nvim` 负责在操作完成后把焦点切回正确的 WezTerm pane：

```lua
-- flatten.nvim 配置片段
post_open = function(bufnr, winnr, ft, is_blocking)
    -- 文件打开后，把 WezTerm 的焦点切到当前 pane
    require("wezterm").switch_pane.id(
        tonumber(os.getenv("WEZTERM_PANE"))
    )
end
```

### 场景 3：在 nvim 里启动后台任务

```lua
vim.keymap.set("n", "<leader>rr", function()
    vim.cmd("WeztermSpawn cargo run")
end)

vim.keymap.set("n", "<leader>rt", function()
    vim.cmd("WeztermSpawn npm test")
end)
```

---

## 四、注意事项

1. **依赖 `wezterm` CLI**：确保 `wezterm` 命令在系统 PATH 中可用。
2. **只对当前 WezTerm 实例生效**：插件通过环境变量（如 `WEZTERM_PANE`）识别当前所在的 WezTerm 会话。
3. **与 pane 导航插件不冲突**：这个插件是"nvim 控制 WezTerm"，而 `smart-splits.nvim` / `wezterm-mux.nvim` 是"在 nvim split 和 WezTerm pane 之间导航"，两者可以共存。

如果你需要完整的函数签名和更多 API，最权威的方式是在 nvim 里执行 `:h wezterm.nvim`。