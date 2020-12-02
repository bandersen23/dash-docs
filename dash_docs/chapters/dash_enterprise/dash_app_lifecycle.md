## Deployment & Release Lifecycle

In this chapter we will discuss how to configure your project folder to deploy apps on Dash Enterprise.

Hello World
App Deployment
Scaling your Dash App
Best practices

## Deployment

When you run `git push plotly master`, Dash Enterprise will do the following:

    1. Create a new Docker container from builder image
    2. Mount app source code
    3. Detect which Buildpack to use based off of files present in app root folder
    4. Install Python runtime environment — override with a `runtime.txt` file
    5. Install APT packages: provided with `apt-packages` file 
    6. Install Python and app's Python dependencies with `requirement.txt` files (required)
    7.  Run pre-deployment script specified in `app.json` 
    8.  Scale containers for each process as specified in `DOKKU_SCALE` 
    9.  Run commands in each container as specified in `Procfile` (required)
    10. Run pre-release app health checks with `CHECKS` file 
    11. Release: Open app to web traffic
    12. Run post-deployment script specified in `app.json` 

Your app's lifecycle begins when changes are pushed to your Dash Enterprise server. A new Docker image is then created from a builder image and a Buildpack detect script will be run. You have the option to modify how Dash Enterprise builds, deploys and release your apps by including special files in your project folder.

To deploy an app only two files are needed: a `requirements.txt` file to describe your app's dependencies, and a `Procfile`, to declare what commands are run by the app's containers.

You may also include a `runtime.txt` file if you want to specify your Python version, an `apt-packages` file if your app requires additional system-level packages like database drivers, an `app.json` file if you want to call scripts when deploying changes, or a `CHECKS` file if you want to customize pre-release health checks.
