# scripts to run at first start

import os

# backup nvim folder and install optional plugins
def firstStart():
    # if Windows
    optionalPlugins = ['fd', 'ripgrep', 'lazygit']
    pkgInstallCmd = ""

    print('Backing up nvim folder...')
    if os.name == 'nt':
        # Move nvim folder to backup
        os.system('move $env:LOCALAPPDATA\\nvim $env:LOCALAPPDATA\\nvim.bak')
        os.system('move $env:LOCALAPPDATA\\nvim-data $env:LOCALAPPDATA\\nvim-data.bak')

        pkgInstallCmd = 'scoop install '
    else:
        # Move nvim folder to backup
        os.system('mv ~/.config/nvim ~/.config/nvim.bak')
        os.system('mv ~/.local/share/nvim ~/.local/share/nvim.bak')
        os.system('mv ~/.local/state/nvim ~/.local/state/nvim.bak')
        os.system('mv ~/.cache/nvim ~/.cache/nvim.bak')

        # if Arch Linux, yay; else if Debian, apt
        if os.path.exists('/usr/bin/yay'):
            pkgInstallCmd = 'yay -S '
        elif os.path.exists('/usr/bin/apt'):
            pkgInstallCmd = 'sudo apt install '
    
    print('Installing optional plugins...')
    
    # Install optional plugins
    os.system(pkgInstallCmd + ' '.join(optionalPlugins))

if __name__ == '__main__':
    firstStart()
