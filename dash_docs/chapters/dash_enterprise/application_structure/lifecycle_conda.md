
## Lifecycle

When you run `git push plotly master`, Dash Enterprise will do the following:

1. Mount app source code
2. Detect which buildpack to use based off of files present in app root folder. 
This Python & `conda` buildpack is detected if `conda-requirements.txt` and `requirements.txt`
files are found
3. Detect  `conda-runtime.txt`, which specifies the version of `conda` in the form 
    of `Miniconda<2-or-3>-<conda-version >= 3.18.3>`, e.g. `Miniconda3-4.5.12` to install.
    Note that with Dash Enterprise in Airgapped (offline) mode, the only `Miniconda3-4.5.12` and `Miniconda2-4.5.12` are supported.
4. Install version of  `conda` specified in `conda-runtime.txt` 
5. Install custom APT or DKPG packages if an `apt-packages` or `dkpg-package` file is provided (optional)
6. Install Python app dependencies specified in `conda-requirement.txt` file with `miniconda`
7. Install Python app dependencies specified in `requirements.txt` file with `pip`  
8. Run a build script if an `app.json` file is included with a `"predeploy"` 
field (optional). Changes made by this script will be committed to the Docker 
image.
9. At this point, the Docker images have been created. In Dash Enterprise 
Kubernetes, these images are pushed to the container registry.
10. Run the `release` command in the image if specified in the `Procfile` (optional)
11. Create Docker containers from the Docker image on the host (Dash Enterprise 
    Single Server) or in the Kubernetes cluster (Dash Enterprise Kubernetes). 
    The number of containers created for each process type can be configured with 
    the `DOKKU_SCALE` file (optional) or in the App Manager.
12. Run the `postdeploy` script in each container if the `app.json` file is 
    included (optional)
13. Run the commands as specified in `Procfile` in each container.
14. Run the app health checks. If the health checks fail, abort the deployment and 
    keep the previous containers running. Override the default health checks with 
    the `CHECKS` file (Dash Enterprise Single Server) or the `readiness` field in 
    the `app.json` file (Dash Enterprise Kubernetes)
15. Release: Open app to web traffic
16. Remove the old containers & images
17. Run periodic `liveness` checks on Dash Enterprise Kubernetes to ensure that 
    the app is still up and to restart it if not (not available on Dash Enterprise 
    Single Server)
18. Restart the deployment process every 24 hours on Dash Enterprise Kubernetes to 
    prevent long-running apps from going down (not available on Dash Enterprise Single Server).

> Steps 1-7 are used to create the Docker image for a Dash Enterprise Workspace and the 
> remaining steps to deploy the container are skipped.
