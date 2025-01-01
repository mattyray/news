# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set the default theme, if using oh-my-zsh (optional)
ZSH_THEME="robbyrussell"  # You can replace this with any theme you prefer.

# Enable the plugins below, if installed manually or through Homebrew
# Load zsh-autosuggestions
if [ -f /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
    source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh
elif [ -f ~/zsh-plugins/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
    source ~/zsh-plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
fi

# Load zsh-syntax-highlighting
if [ -f /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
    source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
elif [ -f ~/zsh-plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
    source ~/zsh-plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
fi

# History settings for command suggestions
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=1000

# Make history suggestions work
setopt HIST_IGNORE_DUPS  # Ignore duplicate commands
setopt HIST_IGNORE_SPACE # Ignore commands with leading spaces
setopt HIST_FIND_NO_DUPS # Don't show duplicates in suggestions

# Alias examples (add your own as needed)
alias ll="ls -la"
alias gs="git status"

# Export any other variables you want to set globally
export PATH="$HOME/bin:/usr/local/bin:$PATH"

# Source any other settings files you may have
if [ -f ~/.zshrc.local ]; then
    source ~/.zshrc.local
fi

export PATH=$PATH:$HOME/.fly/bin
