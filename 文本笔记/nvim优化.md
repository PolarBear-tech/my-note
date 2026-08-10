# img-clip.nvim

`img-clip.nvim` 是一个在 Neovim 中**粘贴/嵌入图片**的插件，支持从剪贴板粘贴、拖放、URL 下载，并自动生成对应标记语言的图片语法。

---

## 一、安装

### 系统依赖

| 系统                  | 需要安装                                 |
| ------------------- | ------------------------------------ |
| **Linux (X11)**     | `xclip`                              |
| **Linux (Wayland)** | `wl-clipboard`                       |
| **macOS**           | `pngpaste` (`brew install pngpaste`) |
| **Windows**         | 无需额外依赖                               |

安装后运行 `:checkhealth img-clip` 验证依赖是否满足。

### lazy.nvim

```lua
{
    "HakonHarnes/img-clip.nvim",
    event = "VeryLazy",
    opts = {
        -- 空对象使用默认配置，或在这里自定义
    },
    keys = {
        { "<leader>p", "<cmd>PasteImage<cr>", desc = "Paste image from clipboard" },
    },
}
```

---

## 二、核心用法

### 命令

| 命令 | 作用 |
|---|---|
| `:PasteImage` | 从系统剪贴板粘贴图片 |
| `:ImgClipDebug` | 打印调试日志 |
| `:ImgClipConfig` | 查看当前配置 |

### Lua API

```lua
require("img-clip").paste_image(opts?, input?)
```

- `opts`：临时覆盖配置选项
- `input`：可选，指定文件路径或 URL（不指定则从剪贴板读取）

```lua
-- 从剪贴板粘贴，临时覆盖文件名
require("img-clip").paste_image({ file_name = "screenshot.png" })

-- 从指定文件粘贴
require("img-clip").paste_image({}, "/path/to/image.png")

-- 从 URL 下载并嵌入
require("img-clip").paste_image({}, "https://example.com/image.png")
```

---

## 三、配置详解

### 默认配置结构

```lua
{
    default = {
        -- 文件路径
        dir_path = "assets",              -- 图片保存目录
        extension = "png",                -- 默认扩展名
        file_name = "%Y-%m-%d-%H-%M-%S",  -- 文件名格式（时间戳）
        use_absolute_path = false,        -- 是否使用绝对路径
        relative_to_current_file = false, -- 路径是否相对于当前文件

        -- 模板
        template = "$FILE_PATH",          -- 插入的文本模板
        url_encode_path = false,          -- 是否 URL 编码路径
        relative_template_path = true,    -- 模板路径是否相对
        use_cursor_in_template = true,    -- 模板中是否包含光标位置
        insert_mode_after_paste = true,   -- 粘贴后是否进入插入模式
        insert_template_after_cursor = true, -- 模板插入到光标后

        -- 交互
        prompt_for_file_name = true,      -- 是否提示输入文件名
        show_dir_path_in_prompt = false,  -- 提示时是否显示目录路径

        -- Base64
        embed_image_as_base64 = false,    -- 是否以 base64 嵌入
        max_base64_size = 10,             -- base64 最大大小(MB)

        -- 图片处理
        process_cmd = "",                 -- 图片处理命令（如 ImageMagick）
        copy_images = false,              -- 是否复制图片
        download_images = true,           -- 是否自动下载网络图片
        formats = { "jpeg", "jpg", "png" }, -- 支持的格式

        -- 拖放
        drag_and_drop = {
            enabled = true,               -- 启用拖放
            insert_mode = false,          -- 是否在插入模式也启用
        },
    },

    -- 按文件类型定制
    filetypes = {
        markdown = {
            url_encode_path = true,
            template = "![$CURSOR]($FILE_PATH)",
            download_images = false,
        },
        html = {
            template = '<img src="$FILE_PATH" alt="$CURSOR">',
        },
        tex = {
            relative_template_path = false,
            template = [[
\begin{figure}[h]
  \centering
  \includegraphics[width=0.8\textwidth]{$FILE_PATH}
  \caption{$CURSOR}
  \label{fig:$LABEL}
\end{figure}
            ]],
            formats = { "jpeg", "jpg", "png", "pdf" },
        },
        typst = {
            template = [[
#figure(
  image("$FILE_PATH", width: 80%),
  caption: [$CURSOR],
) <fig-$LABEL>
            ]],
        },
        org = { ... },
        rst = { ... },
        asciidoc = { ... },
    },

    -- 按文件/目录/自定义条件定制
    files = {},
    dirs = {},
    custom = {},
}
```

### 模板占位符

| 占位符 | 说明 |
|---|---|
| `$FILE_PATH` | 图片文件路径 |
| `$CURSOR` | 光标位置（粘贴后光标会定位到这里） |
| `$LABEL` | 图片标签（用于 LaTeX 等） |

---

## 四、实用配置示例

### 示例 1：Markdown 笔记工作流

把截图自动保存到当前文件同级 `assets` 目录，并转换为 webp 压缩：

```lua
{
    "HakonHarnes/img-clip.nvim",
    event = "VeryLazy",
    opts = {
        default = {
            dir_path = "assets",
            extension = "webp",
            file_name = "%Y-%m-%d-%H-%M-%S",
            process_cmd = "convert - -quality 75 webp:-", -- ImageMagick 压缩
        },
        filetypes = {
            markdown = {
                url_encode_path = true,
                template = "![$CURSOR]($FILE_PATH)",
                download_images = false,
            },
        },
    },
    keys = {
        { "<leader>p", "<cmd>PasteImage<cr>", desc = "Paste image" },
    },
}
```

### 示例 2：为自定义文件类型添加支持

比如 Quarto (`.qmd`) 文件，让它和 Markdown 行为一致：

```lua
opts = {
    filetypes = {
        quarto = {
            url_encode_path = true,
            template = "![$CURSOR]($FILE_PATH)",
            download_images = false,
        },
    },
}
```

### 示例 3：拖放时自动嵌入（不提示文件名）

```lua
opts = {
    default = {
        prompt_for_file_name = false,  -- 不提示，直接用时间戳命名
        drag_and_drop = {
            enabled = true,
            insert_mode = true,  -- 插入模式也支持拖放
        },
    },
}
```

---

## 五、与其他插件集成

### 1. Telescope 选择本地图片插入

```lua
local function embed_with_telescope()
    local telescope = require("telescope.builtin")
    local actions = require("telescope.actions")
    local action_state = require("telescope.actions.state")

    telescope.find_files({
        attach_mappings = function(_, map)
            local function embed_image(prompt_bufnr)
                local entry = action_state.get_selected_entry()
                actions.close(prompt_bufnr)
                require("img-clip").paste_image({}, entry[1])
            end
            map("i", "<CR>", embed_image)
            map("n", "<CR>", embed_image)
            return true
        end,
    })
end

vim.keymap.set("n", "<leader>pi", embed_with_telescope, { desc = "Insert image from telescope" })
```

### 2. Snacks.picker 集成

```lua
local function embed_with_snacks()
    Snacks.picker.files({
        ft = { "jpg", "jpeg", "png", "webp" },
        confirm = function(self, item, _)
            self:close()
            require("img-clip").paste_image({}, "./" .. item.file)
        end,
    })
end
```

### 3. Oil.nvim 集成

```lua
-- 在 oil 中按 <leader>p 插入当前选中的图片
require("oil").setup({
    keymaps = {
        ["<leader>p"] = function()
            local oil = require("oil")
            local filename = oil.get_cursor_entry().name
            local dir = oil.get_current_dir()
            oil.close()
            require("img-clip").paste_image({}, dir .. filename)
        end,
    },
})
```

---

## 六、拖放支持情况

不同终端模拟器对拖放的支持：

| 终端 | X11 文件 | X11 URL | Wayland 文件 | Wayland URL | macOS 文件 | macOS URL | Windows 文件 | Windows URL |
|---|---|---|---|---|---|---|---|---|
| **Kitty** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **WezTerm** | ❌ | ❌ | ❌ | ❌ | ❓ | ❓ | ❓ | ❓ |
| **Alacritty** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Foot** | ➖ | ➖ | ➖ | ➖ | ✅ | ✅ | ✅ | ✅ |

> 拖放功能通过覆盖 `vim.paste()` 实现，要求终端以 bracketed paste 模式插入文本。

---

## 七、常见问题

1. **粘贴后只显示路径，没有生成图片语法？**
   - 检查当前文件类型是否在 `filetypes` 中配置了模板
   - 自定义文件类型需要手动添加配置

2. **图片处理命令不生效？**
   - 确保已安装 ImageMagick（`convert` 或 `magick` 命令可用）
   - 检查 `process_cmd` 语法是否正确

3. **macOS 上无法从剪贴板粘贴？**
   - 安装 `pngpaste`：`brew install pngpaste`
   - 运行 `:checkhealth img-clip` 确认

4. **Windows 上拖放有问题？**
   - 尝试将默认 shell 改为 `powershell` 或 `pwsh`


# weztrerm.nvim

有关wezterm:
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