#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy
"""


from datetime import datetime
import os
import os.path
from fabric.api import local, run, env, put
env.hosts = ['34.138.21.162', '3.82.20.191']


def do_pack():
    """
    generates a .tgz archive from the contents
    of the web_static folder
    """
    time = datetime.now()
    name = "versions/web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    source = "web_static"
    try:
        os.mkdir('versions')
    except FileExistsError:
        pass
    try:
        local("tar -czvf {} {}".format(name, source))
        return name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers, using the function do_deploy
    """
    try:
        namefile = archive_path.split('/')[-1]
        put(archive_path, '/tmp/'+namefile, use_sudo=True)
        uncompressFolder = "/data/web_static/releases/{}/".format(
            namefile.split(".")[0])
        run("sudo rm -rf {}".format(uncompressFolder))
        run("sudo mkdir -p {}".format(uncompressFolder))
        run("sudo tar -xzvf /tmp/{} -C {}".format(namefile, uncompressFolder))
        run("sudo mv {}web_static/* {}".format(uncompressFolder,
            uncompressFolder))
        run("sudo rm -rf {}web_static".format(uncompressFolder))
        run("sudo rm /tmp/"+namefile)
        run("sudo rm -f /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(uncompressFolder))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """
    creates and distributes an archive to your web servers,
    using the function deploy
    """
    name = do_pack()
    if name is None:
        return False
    return do_deploy(name)
