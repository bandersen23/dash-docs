## conda-runtime.txt

`conda-runtime.txt` is a required text files that specifies Conda's runtime. It must be placed in
your app's root directory. It should contain the version of conda to install, in the 
form of Miniconda<2-or-3>-<conda-version>, e.g. Miniconda3-4.5.12.

```
Miniconda3-4.5.12

```

The supported runtimes are the ones in this [list](https://repo.anaconda.com/miniconda/) and >= 3.18.3.

> **Dash Enterprise in Airgapped (offline) mode** only
> supports `Miniconda3-4.5.12` or `Miniconda2-4.5.12`


>Python 2 will soon be deprecated. Dash Enterprise will no longer support 
>Miniconda2 and Python 2 as of January 1, 2021.

---
