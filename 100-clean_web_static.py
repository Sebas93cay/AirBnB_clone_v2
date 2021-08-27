#!/usr/bin/python3
"""
This script deletes out-of-date archives, using the function do_clean
"""


from datetime import datetime
import os
import os.path
from fabric.api import local, run, env, put, cd
env.hosts = ['34.138.21.162', '3.82.20.191']


def delete_locals(n):
    """
    delete local versions
    """
    folder = "versions/"
    files = next(os.walk(folder))[2]
    files_to_delete = sorted(files, reverse=True)[int(n):]
    for file in files_to_delete:
        os.remove(folder + file)


def delete_remotes(n):
    """
    delete remote versions
    """
    folder = "/data/web_static/releases/"
    # run("find {} | tail -n +2 | sort | head -n -{}".format(folder, n))
    run('sudo rm -rf $(find {} -maxdepth 1 | tail -n +2 | sort | head -n -{})\
            '.format(folder, n))


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    number = int(number)
    if number is 0:
        number = 1
    delete_locals(number)
    delete_remotes(number)
