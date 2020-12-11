
## APT files

APT files can be used to install system-level packages via the `apt` package manager.
Supported APT files include the following:

```
apt-packages
dpkg-packages
apt-conf
apt-env
apt-keys
apt-preferences
apt-sources-list
apt-repositories
apt-debconf
```

***

**apt-packages**

`apt-packages` is an optional text file required when apt packages need to be 
installed on a per app basis. For example, data base drivers.

This file should contain APT packages to install. It accepts multiple packages per 
line, and multiple lines.

If this file is included, an `apt-get update` is triggered beforehand during app 
deployment.

In the following example we are installing `vim`, `unixodbc` and `unixodbc-dev`: 

```shell
vim
unixodbc
unixodbc-dev
```

***

**dpkg-packages**

`dpkg-packages` is an optional directory holding .deb packages to be installed 
automatically after apt-packages, apt-repositories and apt-debconf. Allows the 
installation of custom packages inside the container.

Packages are installed in lexicographical order. As such, if any packages depend 
upon one another, that dependency tree should be figured out beforehand.

```shell
$ ls dpkg-packages/
your-package-0_0.0.1.deb
```

***

**apt-conf**

`apt-conf` is an optional config file for `APT`. This is moved to the folder 
/etc/apt/apt.conf.d/99dokku-apt, and can override any apt.conf files that come 
before it in lexicographical order. See [apt.conf Linux man page](https://linux.die.net/man/5/apt.conf) entry for more details.

```
Acquire::http::Proxy "http://user:password@proxy.example.com:8888/";
```

***

**apt-env**

`apt-env` is an optional text file that can contain environment variables. 
Note that this is sourced, and should not contain arbitrary code.

```
export ACCEPT_EULA=y
```

***

**apt-keys**

`apt-keys` is an optional text file that can contain a list of urls for apt 
repository keys. Each one is installed via `curl "$KEY_URL" | apt-key add -`. 
Redirects are not followed. The `sha256sum` of the key contents will be displayed 
to allow for key verification.

```
https://packages.example.com/keys/example.asc
```

***

**apt-preferences**

A file that contains [APT Preferences](https://wiki.debian.org/AptConfiguration?action=show&redirect=AptPreferences. This file is not validated for correctness, and is installed to 
`/etc/apt/preferences.d/90customizations`.

```json
APT {{
Install-Recommends "false";
}}
```

**apt-sources-list**

`apt-sources-list` is an optional text file that overrides the /etc/apt/sources.list
    file. An empty file may be provided in order to remove upstream packages.

```
deb http://archive.ubuntu.com/ubuntu/ bionic main universe
deb http://archive.ubuntu.com/ubuntu/ bionic-security main universe
deb http://archive.ubuntu.com/ubuntu/ bionic-updates main universe
deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main
```

**apt-repositories**

`apt-repositories` is an optional text file that should contain additional APT 
repositories to configure to find packages.

If this file is included, an apt-get update is triggered, and the packages 
`software-properties-common` and `apt-transport-https` are installed. Both these 
actions happen before any repositories are added.

Requires an empty line at end of file.

```shell
ppa:nginx/stable
deb http://archive.ubuntu.com/ubuntu quantal multiverse

```

***

**apt-debconf**

`apt-debconf`is an optional text file allowing to configure package installation. 
Use case is mainly for EULA (like ttf-mscorefonts-installer). Requires an empty 
line at end of file.

```shell
ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true
```
