#!/usr/bin/env python

import urllib2
import os
import pwd

KEYS_ARRAY = ['http://ali.cs.colorado.edu/ssh_public_keys/current']


def get_key_from_url(url):
    try:
        response = urllib2.urlopen(url)
        key = response.read()
        return key.strip(), 
    except urllib2.URLError as exception :
        return False, exception

def get_process_user_info():
    proc_uid = os.getuid()
    try:
        return pwd.getpwuid(proc_uid)
    except KeyError as exception:
        return False

def is_writeable(apath):
    return os.access(apath, os.W_OK)

def is_readable(apath):
    return os.access(apath, os.W_OK)

def path_exists(apath):
    return os.path.exists(apath)

def create_ssh_folder():
    user_info = get_process_user_info()
    if is_writeable(user_info.pw_dir):
        ssh_folder = os.path.join(user_info.pw_dir, ".ssh")
        if not path_exists(ssh_folder):
            os.mkdir(ssh_folder)
            return True
        else:
            return is_writeable(ssh_folder)
    else:
        return False

def create_auth_keys_file():
    user_info = get_process_user_info()
    if is_writeable(user_info.pw_dir):
        auth_keys_file = os.path.join(user_info.pw_dir, ".ssh/authorized_keys")
        if not path_exists(auth_keys_file):
            with open(auth_keys_file, 'w') as file_obj:
                file_obj.write("")
            return True
        else:
            return is_writeable(auth_keys_file)
    else:
        return False

def setup_ssh_folder():
    return create_ssh_folder() and create_auth_keys_file()

def add_key(key_text):
    user_info = get_process_user_info()
    auth_keys_file = os.path.join(user_info.pw_dir, ".ssh/authorized_keys")
    try:
        with open(auth_keys_file,'r') as file_obj:
            lines = file_obj.readlines()
        
        if len(lines) > 0:
            if not lines[-1].endswith("\n"):
                key_text = "\n%s\n" % (key_text)
            else:
                key_text = "%s\n" % (key_text)
        with open(auth_keys_file,'a') as file_obj:
            file_obj.write(key_text)

        return True
    except:

        return False

def key_exists(key):
    try:
        user_info = get_process_user_info()
        auth_keys_file = os.path.join(user_info.pw_dir, ".ssh/authorized_keys")
        with open(auth_keys_file) as file_obj:
            for line in file_obj.readlines():
                if key.strip() == line.strip():
                    return True
        return False
    except:
        return False

def set_permission():
    user_info = get_process_user_info()
    ssh_folder = os.path.join(user_info.pw_dir, ".ssh")
    auth_keys_file = os.path.join(ssh_folder, "authorized_keys")
    try:
        os.chmod(ssh_folder, 0700)
        os.chmod(auth_keys_file, 0600)
        return True
    except:
        return False

def main():
    for key_loc in KEYS_ARRAY:
        key_info = get_key_from_url(key_loc)
        if key_info[0]:
            if not key_exists(key_info[0]):
                if setup_ssh_folder():
                    if add_key(key_info[0]):
                        set_permission()
                        print "key added successfully"
                    else:
                        print "failed to add the key" 
                else:
                    print "failed to setup ssh folder"
            else:
                print "key is already authorized"
        else:
            print "failed to get the key : %s" % key_info[1]

if __name__== "__main__":
    main()
