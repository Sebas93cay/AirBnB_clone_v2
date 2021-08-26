#!/usr/bin/python3
"""
generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""


from datetime import date, datetime
import tarfile
import os
import os.path


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
    source = "web_staticdr"
    try:
        os.mkdir('versions')
    except FileExistsError:
        pass
    try:
        with tarfile.open(name, "w:gz") as tar:
            tar.add(source, arcname=os.path.basename(source))
    except FileNotFoundError:
        return None


do_pack()
