from fabric.api import *

env.hosts=['10.160.0.161','10.160.0.162','10.160.0.163','10.160.0.167','10.160.0.112','10.160.0.152']

env.roledefs = {
    'api':['10.160.0.161','10.160.0.162','10.160.0.163','10.160.0.167','10.160.0.112','10.160.0.152'],
    'web':['10.160.0.161','10.160.0.162','10.160.0.163','10.160.0.167','10.160.0.112','10.160.0.152']
}

env.user = "hungdq11"
env.key_filename = "/home/hungdq11/.ssh/id_rsa"

#@roles('api')
def upcode_apiplay():
    with cd('/webapps/PlayApi/PlayApi'):
        sudo('svn up && supervisorctl restart api.fptplay.net.vn')

#@roles('web')
def upcode_webplay():
    with cd('/webapps/fptplay2/fptplay'):
        sudo('svn up && supervisorctl restart play.fpt.vn')
