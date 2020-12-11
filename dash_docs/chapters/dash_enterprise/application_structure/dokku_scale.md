
## DOKKU_SCALE

`DOKKU_SCALE` is an optional text file used to specify the number of containers 
created for each process type. 
Note that a DOKKU_SCALE should must be added to your app's root directory if you use 
processes other than web and release in your `Procfile`.

Without a `DOKKU_SCALE` file, the containers corresponding to these other processes 
will not be scaled automatically. Instead, they would need to be scaled in your app's
"Resources" page in the App Manager.

By default, Dash Enterprise runs a single web container:
web=1
If you are running other processes, then we recommend scaling up those
containers to 1 as well. For example:

```
web=1
worker-default=1
worker-beat=1

```

These containers are stateless so you can scale them up as long as your server
or Kubernetes cluster has enough memory and CPU:

```
web=4
worker-default=1
worker-beat=1

```

However, we recommend scaling up your Dash app using the gunicorn --worker
and --preload flag before scaling up your containers.
Scaling with --workers and --preload will be consume less memory than scaling
up by containers.
''',
