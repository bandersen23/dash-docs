
## DOKKU_SCALE

`DOKKU_SCALE` is an optional text file used to increase the number of containers 
created for the process types defined in your app's `Procfile` . By default Dash Enterprise runs a single web container.

You will need `DOKKU_SCALE` if your `Procfile` includes 
processes other than **web** and **release**. Without `DOKKU_SCALE` you will  only be able to scale the available containers through the **App Manager** UI.

If you are running other processes, then **we recommend scaling up those
containers to 1** as well. For example:

```
web=1
worker-default=1
worker-beat=1

```

Containers are stateless, so you can scale them up as long as your server
or Kubernetes cluster have enough processing and memory resources available:

```
web=4
worker-default=1
worker-beat=1

```

We recommend scaling your Dash app by enabling the gunicorn **--worker**
and **--preload** flags before using a `DOKKU_FILE`.

Scaling this way consumes significantly less processing and  memory resources.

''',
