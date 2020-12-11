
## Lifecycle

When you run `git push plotly master`, Dash Enterprise will do the following:

1. Mount app source code

2. Detect which Buildpack to use based off of files present in app root folder. 
This Python & `pip` buildpack is detected by discovering the `requirements.txt` 
file. Dash Enterprise buildpacks get updated with every Dash Enterprise release.
3. Install Python 3.6.10 — override the version with a `runtime.txt` file. 
    For Dash Enterprise in Airgapped (offline) mode, only Python-3.6.5 is supported.
4. Install custom APT packages if an `apt-packages` file is provided (optional)
5. Install Python app dependencies specified in `requirement.txt` file
6. Run a build script if an `app.json` file is included with a `"predeploy"` 
field (optional). Changes made by this script will be committed to the Docker 
image.
7. At this point, the Docker images have been created. In Dash Enterprise 
Kubernetes, these images are pushed to the container registry.
8. Run the `release` command in the image if specified in the `Procfile` (optional)
9. Create Docker containers from the Docker image on the host (Dash Enterprise 
Single Server) or in the Kubernetes cluster (Dash Enterprise Kubernetes). 
The number of containers created for each process type can be configured with 
the `DOKKU_SCALE` file (optional) or in the App Manager.
10. Run the `postdeploy` script in each container if the `app.json` file is 
    included (optional)
11. Run the commands as specified in `Procfile` in each container.
12. Run the app health checks. If the health checks fail, abort the deployment and 
    keep the previous containers running. Override the default health checks with 
    the `CHECKS` file (Dash Enterprise Single Server) or the `readiness` field in 
    the `app.json` file (Dash Enterprise Kubernetes)
13. Release: Open app to web traffic
14. Remove the old containers & images
15. Run periodic `liveness` checks on Dash Enterprise Kubernetes to ensure that 
    the app is still up and to restart it if not (not available on Dash Enterprise 
    Single Server)
16. Dash Enterprise will detect which files have any changes. If they have been 
    changed Dash Enterprise will rerun the steps if not it will use the previous version.
17. Restart the deployment process every 24 hours on Dash Enterprise Kubernetes to 
    prevent long-running apps from going down (not available on Dash Enterprise Single Server).

{url}

> Steps 1-7 are used to create the Docker image for a Dash Enterprise Workspace and the 
> remaining steps to deploy the container are skipped.
