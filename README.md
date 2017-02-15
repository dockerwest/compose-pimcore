PHP basic developer environment
===============================

Basic developer environment for Pimcore apps.

Usage
-----

For your convenience the developer environment has some helpers which take away
some difficulties you could experience using docker containers.

If you want this easy helpers to be readily available for you you can use
`environment` before you start. `environment` allows you to start your
environment with an updated `PATH` and allows you to choose between `tmux` or
`screen`

tmux environment

~~~ sh
$ ./environment tmux
~~~

screen environment

~~~ sh
$ ./environment screen
~~~

When you are running in this environment all helpers are available in your path.

You are not required to use the environent, but then you have to call the
helpers with their full path.

To make use of the helpers you should use the `run` wrapper for `docker-compose`.

~~~ sh
$ run up
~~~

Configuration
-------------

There is a sample configuration `.env-sample` which contains the defaults used
in this environment.

If you want to change some of these values, copy `.env-sample` to `.env` and
start editing.

default `.env-sample`

~~~
C_UID=1000
C_GID=1000
PHPVERSION=7.1
NGINXVERSION=stable
BASEHOST=pimcore.dev
MYSQL_ROOT_PASSWORD=toor
PIMCORE=../pimcore
DEVELOPMENT=noprofile
~~~

### C_UID / C_GID

Configure what UID and GID your PHP container must use. This usually should
match your Hosts UID and GID. To find your local UID you can run `id -u` and to
find your local GID you can run `id -g`.

### PHPVERSION

Choose your PHP version. To see which versions are available
[here](https://github.com/BlackIkeEagle/docker-php-pimcore).

### NGINXVERSION

Choose what version of Nginx you want. To see which versions are available see
[here](https://github.com/BlackIkeEagle/docker-nginx-pimcore)

### BASEHOST

This setting defines what the hostname will be you can browse your pimcore app.
The example configuration will be give you `http://pimcore.dev`.

### MYSQL_ROOT_PASSWORD

Choose whatever you want to use as default root password.

### PIMCORE

A relative or absolute path to your pimcore code. this can be a checkout of
  [pimcore](https://github.com/pimcore/pimcore).

### DEVELOPMENT

Set the development flag. Default we use noprofile which will allow us to use
xdebug. When `DEVELOPMENT=1` you also have tideways enabled which gives you
profiling output of you application.

To visualize your profiling output see
[docker-compose-xhgui](https://github.com/BlackIkeEagle/docker-compose-xhgui)

Helpers
-------

`TODO explain what the helpers do`

### composer

### create_db

### mysql

### mysqldump

### mysqlimport

### node

### npm

### php

### redis-cli

### run

Tricks
------

### macOS

For this environment to work properly you should install gnu coreutils

using homebrew:

~~~ sh
$ brew install coreutils
~~~

On macOS you could just install docker from the docker site and run like this.
But our experience is that the native docker install is fairly slow to use. We
would suggest you to install [dinghy](https://github.com/codekitchen/dinghy).

[install dinghy](https://github.com/codekitchen/dinghy#install) and install the
VM technology you want to use. If you want native xhyve support you can
additionally install 
[xhyve driver for docker machine](https://github.com/zchee/docker-machine-driver-xhyve).

If you have dinghy installed this environment will try to use it.

Currently there is an annoying limitation when we are using dinghy and that is
that the hostnames used must end with `docker`.

### oh-my-zsh users

[oh-my-zsh](http://ohmyz.sh/) users should check if there is no fixed setting
for `$PATH` in their `~/.zshrc`. If that is the case you can safely comment it
out. If somewhere in your shell startup `$PATH` is forced you lose the features
the `./environment` script brings to you.

License
-------

MIT License (MIT). See [License File](LICENSE.md) for more information.
