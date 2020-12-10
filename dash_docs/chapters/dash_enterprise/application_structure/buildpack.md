## Buildpack Detection

By including special files in your project folder, you can modify how Dash Enterprise builds,
deploys and releases your apps.

These special files depend which **buildpack** is detected or configured during deployment.
Buildpacks are the technology responsible for transforming deployed code into the Docker image
that is then run as a container on the Dash Enterprise server or the Kubernetes cluster.
It's a higher-level abstraction of a Dockerfile.

Dash Enterprise is shipped with custom buildpacks for Python, Conda and R.
