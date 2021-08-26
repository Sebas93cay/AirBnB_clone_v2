#!/usr/bin/python3
"""
generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""


from datetime import datetime
import os
import os.path
import tarfile
from fabric.api import local


def do_pack():
    """
    generates a .tgz archive from the contents
    of the web_static folder
    """
    time = datetime.now()
    name = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
                                                         time.month,
                                                         time.day,
                                                         time.hour,
                                                         time.minute,
                                                         time.second)
    source = "web_static"
    try:
        os.mkdir('versions')
    except FileExistsError:
        pass
    # local("tar -czvf {} {}".format(name, source))

    try:
        with tarfile.open(name, "w:gz") as tar:
            tar.add(source, arcname=os.path.basename(source))
    except FileNotFoundError:
        return None
