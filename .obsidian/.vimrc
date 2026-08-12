imap jk <Esc>
imap jj <Esc>

" 将数字上的 j 和 k 改为视觉
nmap j gj
nmap k gk


" HJKL 实现更大范围的 hjkl
nmap H ^
nmap L $
nmap J 6gj
nmap K 6gk

" 访问系统剪切板
set clipboard=unnamed

" 移动到下一段落
nmap [ {
nmap ] }

" 复制整行
nmap Y y$

" 实现括号的surrend功能 
exmap surround_wiki surround [[ ]]
exmap surround_double_quotes surround " "
exmap surround_single_quotes surround ' '
exmap surround_backticks surround ` `
exmap surround_brackets surround ( )
exmap surround_square_brackets surround [ ]
exmap surround_curly_brackets surround { }
exmap surround_italic surround * *
exmap surround_bold surround ** **
exmap surround_delete surround ~~ ~~
exmap surround_mark surround == ==
exmap surround_math surround $ $

" 必须使用 'map'
map [[ :surround_wiki
nunmap s
vunmap s
map s" :surround_double_quotes<CR>
map s' :surround_single_quotes<CR>
map s` :surround_backticks<CR>
map sb :surround_brackets<CR>
map s( :surround_brackets<CR>
map s) :surround_brackets<CR>
map s[ :surround_square_brackets<CR>
map s] :surround_square_brackets<CR>
map s{ :surround_curly_brackets<CR>
map s} :surround_curly_brackets<CR>
map si :surround_italic<CR>
map sb :surround_bold<CR>
map sd :surround_delete<CR>
map sm :surround_mark<CR>
map s$ :surround_math<CR>



" 关闭工作区
exmap q obcommand workspace:close

