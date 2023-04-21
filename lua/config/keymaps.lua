-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local function map(mode, lhs, rhs, opts)
  local keys = require("lazy.core.handler").handlers.keys
  ---@cast keys LazyKeysHandler
  -- do not create the keymap if a lazy keys handler exists
  if not keys.active[keys.parse({ lhs, mode = mode }).id] then
    opts = opts or {}
    opts.silent = opts.silent ~= false
    vim.keymap.set(mode, lhs, rhs, opts)
  end
end

-- Base keymap
map("n", ";", ":", { silent = true })
map("n", "Q", "<cmd>q<cr>", { silent = true })
map("n", "S", "<cmd>w<cr>", { silent = true })
map("n", "s", "nop", { silent = true })

-- Exit insert mode
map("i", "jj", "<esc>", { desc = "Exit insert mode" })
map("t", "jj", "<c-\\><c-n>", { desc = "Exit terminal mode" })


