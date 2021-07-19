set tabstop=2
set shiftwidth=2
set expandtab
set number

call plug#begin()
  Plug 'preservim/nerdtree'
  Plug 'https://github.com/Xuyuanp/nerdtree-git-plugin'
  Plug 'https://github.com/ryanoasis/vim-devicons'
  Plug 'https://github.com/tiagofumo/vim-nerdtree-syntax-highlight'
  Plug 'https://github.com/PhilRunninger/nerdtree-buffer-ops'
call plug#end()

nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
