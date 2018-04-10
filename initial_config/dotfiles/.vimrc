" Vundle
set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
" Folding
Plugin 'tmhedberg/SimpylFold'
" Is this even necessary if i use youcompleteme? TODO:
Plugin 'davidhalter/jedi-vim'
" Indents for python
Plugin 'vim-scripts/indentpython.vim'
" Vim LaTeX support
Plugin 'lervag/vimtex'
" Colors
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'

" This two can cause too long writes, turn off if this happens
Plugin 'vim-syntastic/syntastic'
Plugin 'nvie/vim-flake8'

" Pretty status bar TODO: does not work at the moment!
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'Valloric/YouCompleteMe'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" End of Vundle

if v:progname =~? "evim"
  finish
endif

" Get the defaults that most users want.
source $VIMRUNTIME/defaults.vim

if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file (restore to previous version)
  if has('persistent_undo')
    set undofile	" keep an undo file (undo changes after closing)
  endif
endif

if &t_Co > 2 || has("gui_running")
  " Switch on highlighting the last used search pattern.
  set hlsearch
endif

" Only do this part when compiled with support for autocommands.
if has("autocmd")

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
  autocmd FileType text setlocal textwidth=78

  augroup END

else

  set autoindent		" always set autoindenting on

endif " has("autocmd")

" Add optional packages.
"
" The matchit plugin makes the % command work better, but it is not backwards
" compatible.
" The ! means the package won't be loaded right away but when plugins are
" loaded during initialization.
if has('syntax') && has('eval')
  packadd! matchit
endif

" Add tab = 4 spaces (for ALL, some overwrites later)
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Enable folding
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za
" Docstring for folded code
let g:SimpylFold_docstring_preview=1

" Disable python autocomplete on dot vim-jedi
let g:jedi#popup_on_dot = 0
" Disable vim-jedi for YouCompleteMe

" YouCompleteMe configuration
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" TODO: You will probably want to disable YCM always-on and use it with
" shortcut

" set showcmd
let mapleader = " "

let g:jedi#completions_enabled = 0
" Python PEP8 standards
au BufNewFile,BufRead *.py set tabstop=4
au BufNewFile,BufRead *.py set softtabstop=4
au BufNewFile,BufRead *.py set shiftwidth=4
au BufNewFile,BufRead *.py set textwidth=79
au BufNewFile,BufRead *.py set expandtab
au BufNewFile,BufRead *.py set autoindent
au BufNewFile,BufRead *.py set fileformat=unix

" Define BadWhitespace and mark as darkred in py files
highlight BadWhitespace ctermbg=red guibg=darkred
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
" Red line at 79-th line in .py files
au BufNewFile,BufRead *.py set colorcolumn=79

" Similar but for webdev
au BufNewFile,BufRead *.js, *.html, *.css set tabstop=2
au BufNewFile,BufRead *.js, *.html, *.css set softtabstop=2
au BufNewFile,BufRead *.js, *.html, *.css set shiftwidth=2

" VirtualEnv support for python
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF

" Syntax Python
let python_highlight_all=1
syntax on

" ColorSchemes
if has('gui_running')
  set background=dark
  colorscheme solarized
else
  colorscheme zenburn
endif
" Lines numbering
set nu
" TODO: Indentation plugin, how to use it?
" Latex live preview default pdf opener -> zathura
let g:vimtex_view_general_viewer = 'zathura'
