## Lifecycle

When you run `git push plotly master`, Dash Enterprise will do the following:

1. Mount app source code
2. Detect which buildpack to use based off of files present in app root folder. 
This Python & `conda` buildpack is detected by discovering `conda-requirements.txt` and `requirements.txt` files

> **Workspaces do not support `conda` buildpacks.** You cannot preview apps that use
> `conda` in Workspaces. This does not affect your ability to deploy these apps from workspaces.

3. Detect  `conda-runtime.txt`, which specifies the version of `conda` to install

> **Dash Enterprise in Airgapped (offline) mode** only
> supports `Miniconda3-4.5.12` or `Miniconda2-4.5.12`

4. Install version of  `conda` specified in `conda-runtime.txt` 
5. Install custom APT packages if an `apt-packages` is provided and custom `.deb` if a `dkpg-package` file is provided (optional)
6. Install Python app dependencies specified in `conda-requirement.txt` and `requirements.txt` files
7. Run a build script if an `app.json` file is included with a `"predeploy"` 
field (optional). Changes made by this script will be committed to the Docker 
image.
8. At this point, the Docker images have been created. In Dash Enterprise {kubernetes}
these images are pushed to the container registry
9. Run the `release` command in the image if specified in the `Procfile` (optional)
10. Create Docker containers from the Docker image on the host (Dash Enterprise 
Single Server) or in the Kubernetes cluster ({kubernetes}).
The number of containers created for each process type can be configured with 
the `DOKKU_SCALE` file (optional) or in the App Manager
11. Run the `postdeploy` script in each container if the `app.json` file is included (optional)
12. Run the commands as specified in `Procfile` in each container
13. Run the app health checks. If the health checks fail, abort the deployment and 
keep the previous containers running. Override the default health checks with 
the `CHECKS` file (Dash Enterprise Single Server) or the `readiness` field in 
the `app.json` file ({kubernetes})
14. Release: Open app to web traffic
15. Remove the old containers & images
16. Run periodic `liveness` checks on {kubernetes} to ensure that the app is still up and to restart it if not (not available on Dash Enterprise Single Server)
17. Restart the deployment process every 24 hours on {kubernetes} to prevent long-running apps from going down (not available on Dash Enterprise Single Server.


> On **subsequent deploys**, Dash Enterprise will detect which files have changed. If the file has
> changed Dash Enterprise will rerun the step. If not it will use the artifacts of that step from the previous image.
> For example, if `conda-requirements.txt` or `requirements.txt` have not
> hanged then the packages won't be reinstalled (or upgraded!) on subsequent deploys.


> In **Dash Enterprise Workspaces**, steps 1-7 are used to create the Docker image that 
> resembles the Dash app image.  The remaining steps to deploy the container are skipped.


{kubernetes_notes}

---
