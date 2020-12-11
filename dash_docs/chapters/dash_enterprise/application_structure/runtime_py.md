
## runtime.txt

`runtime.txt` is an optional text file that specifies your Dash app's Python runtime 
environment. It must be placed in your app's root directory. The contents are case 
sensitive and must contain include major and minor release, and patch numbers. 

```
python-3.7.4

```

The python runtime used by deployed apps on Dash Enterprise is different from the runtime available on Workspaces.
Dash Enterprise 4.0.1 uses `python-3.6.10` by default. Workspaces uses `python-3.7.4` and cannot be configured with changes to `runtime.txt`. 
Dash Enterprise in Airgapped (offline) mode is only compatible with `python-3.6.5`.

As of 4.0.1, the following Python versions are supported below. The available Python 
runtimes get updated whenever a version of Dash Enterprise is released.

```
python-2.7.10 (deprecated)
python-2.7.11 (deprecated)
python-2.7.12 (deprecated)
python-2.7.13 (deprecated)
python-2.7.14 (deprecated)
python-2.7.15 (deprecated)
python-2.7.16 (deprecated)
python-2.7.9 (deprecated)
python-3.6.0
python-3.6.1
python-3.6.10
python-3.6.2
python-3.6.3
python-3.6.4
python-3.6.5
python-3.6.6
python-3.6.7
python-3.6.8
python-3.6.9
python-3.7.0
python-3.7.1
python-3.7.2
python-3.7.3
python-3.7.4
python-3.7.5
python-3.7.6
python-3.8.0
python-3.8.1
python-3.8.2

```

Dash Enterprise will automatically update the Python version to 
get the latest security releases if a `runtime.txt` file is omitted.

>**Note:** Python 2 will soon be deprecated. Dash Enterprise will no longer support 
>Python 2 as of January 1, 2021.
