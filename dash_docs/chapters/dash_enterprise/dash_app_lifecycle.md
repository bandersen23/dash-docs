# Dash App Lifecycle

    1. Push changes to Dash Enterprise server: `git push <remote> master`
    2. Create new Docker container from builder image
    3. Mount app source code
    4. Buildpack detect scripts are run (Python)
       1. Check for `requirement.txt`
       2. Check for `setup.py`
       3. Check for `Pipfile`
    5. `runtime.txt` (optional)
    6. `apt-packages` (optional)
    7. `app.json` (optional)
    8. Check `Procfile`
    9. Install Python and app's Python dependencies
    10. Pre-deployment `CHECKS` (optional)
    11. Deploy app
    12. Post-deployment `CHECKS` (optional)

Your app's lifecycle begins when changes are pushed to your Dash Enterprise server. A new Docker image is then created from a builder image and Buildpack detect scripts will be run. You will need a `requirements.txt` or `setup.py` or `Pipfile` file to describe your app's dependencies, and a `Procfile` to declare what commands are run by the app's containers.

Optionally, you may also include a `runtime.txt` file if you want to specify your runtime environment, an `apt-packages` file if your app requires additional system-level packages, an `app.json` file if you want to call scripts when deploying changes, or a `CHECKS` file if you want to customize health checks performed on your app.

In this chapter we will be going over Dash app structure and configuration. All of these files must be placed in your app's root directory.
