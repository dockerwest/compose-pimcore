"""
Read .env file, basically taken from docker-compose for simplicity and modified
for our usecase
"""

import os
import contextlib
import codecs
import re
from distutils.spawn import find_executable


def split_env(env):
    if '=' in env:
        return env.split('=', 1)
    else:
        return env, None


def env_vars_from_file(filename):
    """
    Read in a line delimited file of environment variables.
    """
    if not os.path.exists(filename):
        raise Exception("Env file does not exist: %s" % filename)
    elif not os.path.isfile(filename):
        raise Exception("%s is not a file." % (filename))
    env = {}
    with contextlib.closing(codecs.open(filename, 'r', 'utf-8')) as fileobj:
        for line in fileobj:
            line = line.strip()
            if line and not line.startswith('#'):
                k, v = split_env(line)
                env[k] = v
    return env


class Environment:

    required_keys = [
        'BASEHOST', 'APPLICATION', 'WINDOW_MANAGER'
    ]

    def __init__(self, envfile):
        self.environment = env_vars_from_file(envfile)
        self.__check_environment()

    def __check_environment(self):
        for requiredkey in self.required_keys:
            if requiredkey not in self.environment:
                raise ValueError("Env does not contain %s" % requiredkey)

    def get_compose_filename(self):
        dingyexec = find_executable('dinghy')
        if None is not dingyexec:
            return 'docker-compose-dinghy.yml'
        return 'docker-compose.yml'

    def get_project_name(self):
        regex = re.compile('\\W+')
        basehost = self.get('BASEHOST')
        projectname = regex.sub('', basehost)
        return projectname

    def get(self, key):
        if key not in self.environment:
            return None
        return self.environment[key]
