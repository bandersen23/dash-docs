
## Procfile

`Procfile` is a required text file that declares which commands are run by your Dash app on
startup like starting your app's web server, scheduling jobs and running background processes.

This file is always named `Procfile` — with no file extension. It must be placed in your app's root
directory and uses the following format:

```
<process type>: <command>

```

Process type names are arbitrary, however there are 
two special process types:

1. `web`
2. `release`


A simple Dash app `Procfile` will resemble the following:

```
web: gunicorn app:server --workers 4
```

A Dash app running  a background task queue will have `Procfile` similar to this:

```
web: gunicorn app:server --workers 4
worker: celery -A app:celery_instance worker
```

A Dash app periodically generating report with the Snapshot Engine might have 
`Procfile` like this:

```
web: gunicorn index:server --workers 4
worker: celery -A index:celery_instance worker --concurrency=2
scheduler: celery -A index:celery_instance beat
```
Note that `worker` and `scheduler` process names are arbitrary. 
We recommend using descriptive names as they will appear in all logs and in the 
app manager.

**Web Process**

`web` is the only process type that can receive external HTTP traffic. Use this
to run your Dash app with `gunicorn`, your Dash app's web server. In the following 
example we are declaring `gunicorn` as our web server with `web: gunicorn`:

```
web: gunicorn app:server --workers 4

```

These commands are [standard `gunicorn` commands](https://docs.gunicorn.org/en/latest/run.html).

`gunicorn` accepts a [wide variety of settings](https://docs.gunicorn.org/en/latest/settings.html). 
Here are a few common flags:


1. `--workers` specifies the number worker processes that are being used to run the Dash app. 
This is typically between 2 and 8. Adding workers will enable your application to serve more 
users at once but will increase the CPU & memory usage. 

See [Gunicorn Docs on Workers](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) 
for more details.

```
web: gunicorn app:server --workers 4

```

2. `--timeout` allows you to modify the default amount of time available for your workers to complete
a task. 

See [Gunicorn Docs on Timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout) for
details.

```
web: gunicorn app:server --workers 4 --timeout 240

```

3. Use the `--preload` flag to reduce your application's memory and speed up boot time.  

Avoid the `--preload` flag if you are using shared database connection pools
see [Database Connections](/dash-enterprise/database-connections).

See [Gunicorn Docs on Preloading](https://docs.gunicorn.org/en/latest/settings.html#preload-app) 
for more details.

```
web: gunicorn app:server --workers 4 --preload

``` 

**Release Process**

`release` is a process type only used to run commands during your app's release
phase and is rarely required for Dash apps.

In following example, the `release-task.sh` would be run. This script might be priming or
invalidating cache stores, running database schema migrations, or 
sending datasets, CSS, JS or other assets from your app’s image to a CDN or S3 bucket.

```
release: ./release-tasks.sh
web: gunicorn app:server --workers 4

```

**Other Processes**

You can also run other background processes in their own containers.
For example, you may run a background job queue to periodically 
update your application's data, generate snapshots, or process long-running tasks:

```
web: gunicorn app:server --workers 4
worker: celery -A app:celery_instance worker

```

Note that the name `worker` is arbitrary. However, we recommend using descriptive 
names as they will appear in logs and in the App Manager. `web` & `release` are the 
only reserved names.

Note that a `DOKKU_SCALE` should be added to your app's root directory if you 
use processes other than `web` and `release` in your `Procfile`.

Without a `DOKKU_SCALE` file, the containers corresponding to these other processes 
will not be scaled automatically. Instead, they would need to be scaled in the App 
Manager's **Resources** page.
