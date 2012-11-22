#!/bin/zsh

[ `id -u` != 0 ] && echo "please run using sudo" && exit 1

# Battery
defaults write com.apple.menuextra.battery ShowPercent -string "YES"

#ScreenSave
defaults write com.apple.screensaver askForPassword -int 1
defaults write com.apple.screensaver askForPasswordDelay -int 0

#Trackpad/keyboard/mouse ( I like it fast )
defaults write NSGlobalDomain com.apple.trackpad.scaling -int 3
defaults write NSGlobalDomain com.apple.swipescrolldirection -int 0
defaults write NSGlobalDomain com.apple.keyboard.fnState -int 0 
defaults write NSGlobalDomain com.apple.mouse.scaling -int 3 
defaults write NSGlobalDomain com.apple.springing.delay -float 0.5 
defaults write NSGlobalDomain com.apple.springing.enabled -int 1 

# Terminal
open "$HOME/dotali/misc/AlisZsh.terminal"
sleep 1
defaults write com.apple.terminal "Default Window Settings" -string "AlisZsh"
defaults write com.apple.terminal "Startup Window Settings" -string "AlisZsh"

# misc
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
