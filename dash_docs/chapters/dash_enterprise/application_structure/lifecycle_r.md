## Lifecycle

When you run `git push plotly master`, Dash Enterprise will do the following:

1. Create a new Docker container from builder image
2. Mount app source code
3. Detect which Buildpack to use based off of files present in app root folder
4. Install Conda runtime environment — override with a `runtime.txt` file
5. Install APT packages: provided with `apt-packages` file
6. Install R and app's R dependencies with `init.R` files
7.  Run pre-deployment script specified in `app.json`
8.  Scale containers for each process as specified in `DOKKU_SCALE`
9.  Run commands in each container as specified in `Procfile`
10. Run pre-release app health checks with `CHECKS` file
11. Release: Open app to web traffic
12. Run post-deployment script specified in `app.json`

{url}
