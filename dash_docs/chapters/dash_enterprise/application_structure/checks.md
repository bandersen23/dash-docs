
## CHECKS

`CHECKS` is an optional text file that allows you to precisely modify Dash 
Enterprise's app health diagnostic checks. 

> `CHECKS` is only available on Dash Enterprise Single Server. Similar functionality 
> for Dash Enterprise Kubernetes is available via the `app.json` file. 

By default, Dash Enterprise will wait 10 seconds after starting each container 
before assuming it is up and proceeding with the deployment. Once this happens for 
all of the containers associated with the deployed Dash app, web traffic will then 
be directed to the new containers. Dash Enterprise will then wait an additional 60 
seconds to give time for old containers with longer running connections 
a chance to terminate. The checks are compared to the detected `web` process in your 
`Procfile`.

We recommend that you include a `CHECKS` file in your app's root directory if your 
Dash app needs more time to boot or load data into memory so as to verify if it 
can serve traffic. 

There are three settings you can modify in your `CHECKS` file:

1. `WAIT` corresponds to the allocated time before the checks are performed
2. `TIMEOUT` corresponds to the time allowed for checks to be carried out
3. `ATTEMPTS`, corresponds to the number of allowed check attempts

The default `CHECKS` file values used by Dash Enterprise are the following:

```
WAIT=15
TIMEOUT=10
ATTEMPTS=3
```

In the simple example above, Dash Enterprise will wait 15 seconds before performing 
the check and will allow up to 10 seconds for a response from the app, and attempt the 
check 3 times before marking it as a failure. 

Note that omitting `CHECKS` file instructions will result in Dash Enterprise skipping
those checks. 

```
WAIT=15
# TIMEOUT=10
ATTEMPTS=3
```

You may also include instructions that are specified in the format of a relative 
link, followed by content that Dash Enterprise should find in the response. 
The expected content can be omitted if text content is not relevant. 
(e.g if you want to check whether an image can be served). The example below checks 
that `dash-logo.png` is being served to the app.


```
WAIT=15
TIMEOUT=10
ATTEMPTS=3

/<your-dash-app>/assets/images/dash-logo.png
```

Another use case for `CHECKS` might be to verify that an app that takes
a few minutes to load pass checks.  

```python
import dash
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
import time

# simulate long loading time
time.sleep(120)

app = dash.Dash(__name__)
server = app.server
app.layout = ddk.App([
    html.H1('hello world')
])

if __name__ == '__main__':
    app.run_server(debug=False)
```

In this example, we are simulating an app with a two-minute loading time with
`time.sleep(120)`. Deploying this example without a `CHECKS` file will result in 
Dash Enterprise running an app health check with its default values.
Dash Enterprise will then be serving an app that has not yet loaded and prompting a 
`[CRITICAL] WORKER TIMEOUT` error.

The inclusion of the following `CHECKS` file resolves this issue by delaying web 
traffic long enough for the app to fully load:

```
WAIT=15
TIMEOUT=130
ATTEMPTS=2
```

You can also create your own health check by writing a custom Flask endpoint that will return
a value of your choosing. In the following example, we include  `@app.server.route('/status')` 
that returns `OK'.

```python
import dash
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server
app.layout = ddk.App([
    html.H1('hello world'),
])

# Custom status file for the deployment CHECKS
@app.server.route('/status')
def update_status():
    return 'OK'
if __name__ == '__main__':
    app.run_server(debug=False)

```

The example app's `CHECKSFILE` will then resemble:

```
WAIT=15
TIMEOUT=130
ATTEMPTS=2

<your-dash-app>/status OK

```
