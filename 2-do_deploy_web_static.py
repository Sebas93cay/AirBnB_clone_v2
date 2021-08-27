#!/usr/bin/python3
"""
generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""


from datetime import datetime
import os
import os.path
from fabric.api import run, put, env

env.hosts = ['34.138.21.162', '3.82.20.191']

def do_display(archive_path):
    """
    distributes an archive to your web servers, using the function do_deploy
    """
    try:
        namefile = archive_path.split('/')[-1]
        put(archive_path, '/tmp/'+namefile, use_sudo=True)
        uncompressFolder = "/data/web_static/releases/{}/".format(namefile.split(".")[0])
        run("sudo rm -rf {}".format(uncompressFolder))
        run("sudo mkdir -p {}".format(uncompressFolder))
        run("sudo tar -xzvf /tmp/{} -C {}".format(namefile, uncompressFolder))
        run("sudo mv {}web_static/* {}".format(uncompressFolder, uncompressFolder))
        run("sudo rm -rf {}web_static".format(uncompressFolder))
        run("sudo rm /tmp/"+namefile)
        run("sudo rm -f /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(uncompressFolder))
        return True
    except Exception:
        return False
