" gVim {{{
if has("gui_running") && !has("gui_vimr")
    " au GUIEnter * simalt ~x " 窗口启动时自动最大化
    set guioptions-=m " 隐藏菜单栏
    set guioptions-=T " 隐藏工具栏
    set guioptions-=L " 隐藏左侧滚动条
    set guioptions-=r " 隐藏右侧滚动条
    set guioptions-=b " 隐藏底部滚动条
    if has("mac")
        set lines=28
        set columns=90
    else
        set lines=36
        set columns=110
    endif
    winpos 440 200
    source $VIMRUNTIME/delmenu.vim
    source $VIMRUNTIME/menu.vim
    if has("win32")
        command Wsl :ter C:\Windows\Sysnative\wsl.exe
    endif
endif
" }}}

