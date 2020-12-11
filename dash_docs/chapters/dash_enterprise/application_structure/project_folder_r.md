## Project Folder

To deploy a Dash R app with Dash Enterprise, three additional files are needed:

1. A `init.R` file to describe your app's dependencies
2. A `Procfile` to declare what commands & processes should be run to run the Dash 
    app and any other background processes 
3. An R `buildpack` to transfer your app's code into the Docker image that is later
    run on the Dash Enterprise Server or Kubernetes cluster

A minimal project structure might look like this:

```
|-- app.R
|-- Procfile
|-- init.R
|-- .buildpacks
```

You may also include optional files such as a `runtime.txt` file if you want to 
specify your R version, an `apt-packages` file if your app requires additional 
system-level packages like database drivers, an `app.json` file if you want to call 
scripts when deploying changes, or a `CHECKS` file if you want to customize 
pre-release health checks. See [Files Reference](#optional-files) section
below for more details.

A more complex project structure might look like this:

```
|-- app.R
|-- CHECKS
|-- Procfile
|-- init.R
|-- runtime.txt
|-- .buildpacks
|-- apt-packages
|-- app.json
```
