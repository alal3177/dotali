#!/bin/zsh

BACKUP_DIR=$HOME/dotali_backup
FILES_ARRAY=(zshrc vimrc screenrc)
GIT_PATH=`which git 2>/dev/null`

# if git is not installed, abort
[ ! -x $GIT_PATH ] && echo "git is not installed .." && exit 1

# if already instlled, abort
[ -d $HOME/dotali ] && echo "dotali already installed" && exit 1

# create backup folder
[ ! -d $BACKUP_DIR ] && mkdir $BACKUP_DIR

# clone git repo
git clone --recursive https://github.com/alal3177/dotali $HOME/dotali/ &>/dev/null
[ $? != 0 ] && echo "could not clone repo" && exit 1

# loop over all our files, back it up, remve it, create symlink
for afile in $FILES_ARRAY
do
    [ -f $HOME/.$afile ] && cp $HOME/.$afile $BACKUP_DIR/ && rm $HOME/.$afile
    ln -s $HOME/dotali/rc/$afile $HOME/.$afile
done


