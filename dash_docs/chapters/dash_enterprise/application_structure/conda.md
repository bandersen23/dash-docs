The Conda buildpack is similar to the Python buildpack except it includes `Miniconda` 
and allows you to install packages with `miniconda` via the `conda-requirements.txt` file.

## Conda

Conda is a cross-platform packaging manager that can be used to handle your app's 
Python dependencies. We suggest that Conda should be used if mandated by your organization or if your you apps requires packages that cannot be installed with pip like `cupy` or `cuda`.  

We recommend using Pip instead of Conda, because it allows for faster app deployments. Conda includes a dependency check used to verify that all installed package requirements are met. This additional check considerably increases the time it takes to deploy an app. This is relevant during development and when deploying larger apps.

{rapids_template}

Initial deployment (conda):

```
git push plotly master  0.09s user 0.08s system 0% cpu 13:51.63 total

```

Subsequent deployment (conda):

```
git push plotly master  0.05s user 0.07s system 0% cpu 16:00.79 total
```

---

{conda_template}

Initial deployment (conda):

```
git push plotly master  0.08s user 0.06s system 0% cpu 10:08.98 total

```

Subsequent deployment (conda):

```
git push plotly master  0.06s user 0.03s system 0% cpu 5:59.89 total

```

Initial deployment (pip):

```
git push plotly master  0.05s user 0.04s system 0% cpu 3:35.17 total

```

Subsequent deployment (pip):

```
git push plotly master  0.05s user 0.03s system 0% cpu 3:07.01 total

```
