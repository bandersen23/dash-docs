# Dash Application Structure

---

## Required Files

### requirements.txt

### conda-requirements.txt (conda)

Dash App Templates including `conda-requirements.txt`:

- [Sample RAPIDS Application](https://dash-playground.plotly.host/Docs/templates/rapids-sample)
- [Managing Dependencies with Conda](https://dash-playground.plotly.host/Docs/templates/conda)
- [Managing Dependencies with Conda-Airgapped](https://dash-playground.plotly.host/Docs/templates/conda-airgapped)

### setup py

### Pipfile

The `Pipfile` is the dedicated file used by the `Pipenv` virtual environment to manage project dependencies.

### Procfile

The `Procfile` specifies the commands that are executed by the app on startup. **All** deployed Dash app require a `Procfile`. You can use a Procfile to declare a variety of process types, including:

- Your app’s web server
- Multiple types of worker processes
- A singleton process, such as a clock
- Tasks to run before a new release is deployed


```shell
web: gunicorn app:server --workers 4
worker-default: celery -A tasks worker --loglevel=INFO --concurrency=2
worker-beat: celery -A tasks beat --loglevel=INFO
```
A typical `Procfile` should be similar to what you see above. Other commands include:

- --workers
- --timeout
- --preload

(link to doc expanding on use)

---

## Optional Files

### CHECKS

Custom checks defined by a `CHECKS` file only apply to the web process type.

Dash App Templates including `CHECKS`:

- [Sample Vaex Application](https://dash-playground.plotly.host/Docs/templates/vaex-sample)

### runtime.txt

This optional file specifies python runtime. For example, its contents would be python-2.7.15 or python-3.6.6. If omitted, Python 3.6.7 will be installed.

### conda-runtime.txt

Dash App Templates including `conda-runtime.txt`:

- [Sample RAPIDS Application](https://dash-playground.plotly.host/Docs/templates/rapids-sample)
- [Managing Dependencies with Conda](https://dash-playground.plotly.host/Docs/templates/conda)
- [Managing Dependencies with Conda-Airgapped](https://dash-playground.plotly.host/Docs/templates/conda-airgapped)
  
### .condarc

### ./assets

An optional folder that contains CSS stylesheets, images, or custom JavaScript files. [Learn more about assets](https://dash.plotly.com/external-resources).

### app.json

Optional

Sometimes you need to run a command on at deployment time, but before an app is completely deployed. Common use cases include:

- Checking a database is initialized
- Running database migrations
- Any commands required to set up the server (e.g. something like a Django collectstatic)
- Signalling the completion of your app deployment

```json
{
    "scripts": {
        "dokku": {
            "predeploy": "python predeploy.py"
        "postdeploy": "curl https://some.external.api.service.com/deployment?state=success"
        }
    }
}
```

Dash App Templates including `app.json`:

- [Internal Repository Manager](https://dash-playground.plotly.host/Docs/templates/airgapped-repo)
- [Refresh Data Periodically via the built-in Redis Database](https://dash-playground.plotly.host/Docs/templates/celery-periodic-task)
- [MS SQL Server Sample App](https://dash-playground.plotly.host/Docs/templates/mssql-pyodbc-sample-app)
- [Oracle Sample App](https://dash-playground.plotly.host/Docs/templates/oracle-sample-app)
- [Platform Analytics App](https://dash-playground.plotly.host/Docs/templates/platform-analytics)
- [pyodbc Sample App](https://dash-playground.plotly.host/Docs/templates/pyodbc-sample-app)

### DOKKU_SCALE

`DOKKU_SCALE` is a formation file used for manual process and container management. It must be located in your app's root directory. While present, using `ps:scale` for scaling will be disabled.

```shell
web=1
worker-default=1
worker-beat=1
```

`web` process and other processes either before or after the initial deploy.

Dash App Templates including `DOKKU_SCALE`:

- [Platform Analytics App](https://dash-playground.plotly.host/Docs/templates/platform-analytics)
- [Refresh Data Periodically via the built-in Redis Database](https://dash-playground.plotly.host/Docs/templates/celery-periodic-task)
- [Background Task Queue](https://dash-playground.plotly.host/Docs/templates/snapshots-single-page)
- [Generating PDF Reports from an App View](https://dash-playground.plotly.host/Docs/templates/snapshots-web-and-pdf)
- [Share Data Between Multiple Pages](https://dash-playground.plotly.host/Docs/templates/multi-page-data-sharing)
- [Dash Notes - Saving Notes & Comments with Redis](https://dash-playground.plotly.host/Docs/templates/redis-notes-persistence)
- [Scheduled PDFs and Alerts](https://dash-playground.plotly.host/Docs/templates/snapshots-scheduled-reports)
- [Refresh Data Periodically via the built-in Postgres Database](https://dash-playground.plotly.host/Docs/templates/celery-periodic-task-postgres)
- [Generating PDF Reports from Background Task](https://dash-playground.plotly.host/Docs/templates/snapshots-generate-pdf-report)
- [Snapshots-Enabled Clinical Trial App & Report](https://dash-playground.plotly.host/Docs/templates/snapshots-clinical-trial-dashboard)
- [Dash Embedded with Snapshots Engine](https://dash-playground.plotly.host/Docs/templates/dash-embedded-snapshots-example)
- [Background Task Queue and Viewing Previous Results](https://dash-playground.plotly.host/Docs/templates/snapshots-results-on-same-page-with-archive)


### APT files

APT files are used to extend the base image in the build process.

- apt-conf
- apt-env
- apt-keys
- apt-preferences
- apt-sources-list
- apt-repositories
- apt-debconf
- apt-packages
- dpkg-packages

#### `apt-conf`

A config file for apt, as documented [here](https://linux.die.net/man/5/apt.conf). This is moved to the folder /etc/apt/apt.conf.d/99dokku-apt, and can override any apt.conf files that come before it in lexicographical order.

Example:

```shell
Acquire::http::Proxy "http://user:password@proxy.example.com:8888/";
```

#### `apt-env`

A file that can contain environment variables. Note that this is sourced, and should not contain arbitrary code.

Example:

```shell
export ACCEPT_EULA=y
```

#### `apt-keys`

A file that can contain a list of urls for apt repository keys. Each one is installed via `curl "$KEY_URL" | apt-key add -`. Redirects are not followed. The `sha256sum` of the key contents will be displayed to allow for key verification.

Example:

```shell
https://packages.microsoft.com/keys/microsoft.asc
```

#### `apt-preferences`
A file that contains [APT Preferences](https://wiki.debian.org/AptConfiguration?action=show&redirect=AptPreferences). This file is not validated for correctness, and is installed to `/etc/apt/preferences.d/90customizations`.

Example:

```json
APT {
  Install-Recommends "false";
}
```

#### `apt-sources-list`
Overrides the /etc/apt/sources.list file. An empty file may be provided in order to remove upstream packages.

Example:

```shell
deb http://archive.ubuntu.com/ubuntu/ bionic main universe
deb http://archive.ubuntu.com/ubuntu/ bionic-security main universe
deb http://archive.ubuntu.com/ubuntu/ bionic-updates main universe
deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main
```

Dash App Templates including `apt-source-list`:

- [Internal Repository Manager](https://dash-playground.plotly.host/Docs/templates/airgapped-repo)

#### `apt-packages`

The `apt-packages` file is required when apt packages need to be installed on a per app basis. For example, data base drivers. 

This file should contain apt packages to install. It accepts multiple packages per line, and multiple lines.

If this file is included, an `apt-get update` is triggered beforehand.

Example:

```shell
nginx
unifont
```

Dash App Templates including `apt-packages`:

- [Internal Repository Manager](https://dash-playground.plotly.host/Docs/templates/airgapped-repo)
- [Oracle Sample App](https://dash-playground.plotly.host/Docs/templates/oracle-sample-app)
- [pyodbc Sample App](https://dash-playground.plotly.host/Docs/templates/pyodbc-sample-app)
- [MS SQL Server Sample App](https://dash-playground.plotly.host/Docs/templates/mssql-pyodbc-sample-app)
- [Databricks-connect dash application](https://dash-playground.plotly.host/Docs/templates/databricks-connect)

#### `apt-repositories`

Optional file that should contain additional APT repositories to configure to find packages.

If this file is included, an apt-get update is triggered, and the packages `software-properties-common` and `apt-transport-https` are installed. Both these actions happen before any repositories are added.

Requires an empty line at end of file.

Example:

```shell
ppa:nginx/stable
deb http://archive.ubuntu.com/ubuntu quantal multiverse
```

#### `apt-debconf`

Optional file allowing to configure package installation. Use case is mainly for EULA (like ttf-mscorefonts-installer). Requires an empty line at end of file.

Example:

```shell
ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true
```

#### `dpkg-packages`

Optional directory holding .deb packages to be installed automatically after apt-packages, apt-repositories and apt-debconf. Allows the installation of custom packages inside the container.

Packages are installed in lexicographical order. As such, if any packages depend upon one another, that dependency tree should be figured out beforehand.

Example:

```shell
$ ls dpkg-packages/
your-package-0_0.0.1.deb
```

---

### Sample Apps

[Sample App (Python)](https://dash-playground.plotly.host/Docs/templates/sample-app)

[Sample App (R)](https://dash-playground.plotly.host/Docs/templates/dash-for-r)

[Deploying From a Jupyter Notebook](https://dash-playground.plotly.host/Docs/templates/jupyter-dash-sample)

[Screen Fit](https://dash-playground.plotly.host/Docs/templates/screen-fit)

[Graph with Controls](https://dash-playground.plotly.host/Docs/templates/controls-graph-header)

[Multiple Graphs with Controls 1](https://dash-playground.plotly.host/Docs/templates/controls-multiple-graphs-header)
[Multiple Graphs with Controls 2](https://dash-playground.plotly.host/Docs/templates/controls-sidebar-multiple-graphs-header)
[Graphs with Horizontal Controls](https://dash-playground.plotly.host/Docs/templates/horizontal-controls-graph-header)

[Graphs with Horizontal Controls & Dropdown in Cards](https://dash-playground.plotly.host/Docs/templates/horizontal-controls-graph-header-card-controls)

[2x2 Grid of Graphs](https://dash-playground.plotly.host/Docs/templates/horizontal-controls-graph-2x2-header)

[Graphs with Horizontal Controls & Data Cards](https://dash-playground.plotly.host/Docs/templates/horizontal-controls-graph-header-card-controls)

[Text in Cards](https://dash-playground.plotly.host/Docs/templates/controls-multiple-graphs-header-data-cards-text)

[Text above Controls](https://dash-playground.plotly.host/Docs/templates/controls-multiple-graphs-header-data-cards-text-2)

[Multiple Graphs with Controls and Sidebar](https://dash-playground.plotly.host/Docs/templates/controls-multiple-graphs-sidebar)

[Graph with Controls and Sidebar](https://dash-playground.plotly.host/Docs/templates/controls-graph-sidebar)
[Fitting Content in the Window - No vertical Scroll](https://dash-playground.plotly.host/Docs/templates/screen-fit)

[No vertical Scroll - 3 Rows](https://dash-playground.plotly.host/Docs/templates/screen-fit-3-rows)

[Create an App with Multiple Tabs](https://dash-playground.plotly.host/Docs/templates/multi-tab-sample-app)

[Report 1](https://dash-playground.plotly.host/Docs/templates/report-template-portrait-1)

[Report 2](https://dash-playground.plotly.host/Docs/templates/report-template-portrait-2)

[Presentation 1](https://dash-playground.plotly.host/Docs/templates/report-template-landscape-1)

[Presentation 2](https://dash-playground.plotly.host/Docs/templates/report-template-landscape-2)

[Databricks-connect dash application](https://dash-playground.plotly.host/Docs/templates/databricks-connect)

[Sample Vaex Application](https://dash-playground.plotly.host/Docs/templates/vaex-sample)

[Sample Dask Application](https://dash-playground.plotly.host/Docs/templates/dask-sample)

[Sample RAPIDS Application](https://dash-playground.plotly.host/Docs/templates/rapids-sample)

[Snapshotting the State of an App](https://dash-playground.plotly.host/Docs/templates/snapshots-saving-inputs-and-outputs)

[Snapshotting the Outputs of an App](https://dash-playground.plotly.host/Docs/templates/snapshots-saving-outputs)

[Background Task Queue](https://dash-playground.plotly.host/Docs/templates/snapshots-single-page)

[Background Task Queue and Viewing Previous Results](https://dash-playground.plotly.host/Docs/templates/snapshots-results-on-same-page-with-archive)

[Generating PDF Reports from an App View](https://dash-playground.plotly.host/Docs/templates/snapshots-web-and-pdf)

[Generating PDF Reports from Background Task](https://dash-playground.plotly.host/Docs/templates/snapshots-generate-pdf-report)

[Scheduled PDFs and Alerts](https://dash-playground.plotly.host/Docs/templates/snapshots-scheduled-reports)

[Snapshot Engine & Dash Notes - Saving Notes & Comments alongside the Snapshot](https://dash-playground.plotly.host/Docs/templates/snapshots-notes-persistence)

[Oracle Sample App](https://dash-playground.plotly.host/Docs/templates/oracle-sample-app)

[pyodbc Sample App](https://dash-playground.plotly.host/Docs/templates/pyodbc-sample-app)

[MS SQL Server Sample App](https://dash-playground.plotly.host/Docs/templates/mssql-pyodbc-sample-app)

[MySQL Sample App](https://dash-playground.plotly.host/Docs/templates/pymysql-sample-app)

[PostgreSQL Sample App](https://dash-playground.plotly.host/Docs/templates/postgresql-sample-app)

[Connect to S3 using credentials saved in Environment Variables](https://dash-playground.plotly.host/Docs/templates/s3-credentials-as-envvars)

[Refresh Data Periodically via the built-in Redis Database](https://dash-playground.plotly.host/Docs/templates/celery-periodic-task)

[Refresh Data Periodically via the built-in Postgres Database](https://dash-playground.plotly.host/Docs/templates/celery-periodic-task-postgres)

[Multi-Page Dash App with a Header](https://dash-playground.plotly.host/Docs/templates/multi-page-sample-app)

[Multi-Page Dash App with Dash for R](https://dash-playground.plotly.host/Docs/templates/dashr-multi-page-sample-app)

[Multi-Page Dash App with a Sidebar](https://dash-playground.plotly.host/Docs/templates/multi-page-sample-app-sidebar)

[Share Data Between Multiple Pages](https://dash-playground.plotly.host/Docs/templates/multi-page-data-sharing)

[Dash Notes - Saving Notes & Comments with Redis](https://dash-playground.plotly.host/Docs/templates/redis-notes-persistence)

[Platform Analytics App](https://dash-playground.plotly.host/Docs/templates/platform-analytics)

[Dash App User Analytics](https://dash-playground.plotly.host/Docs/templates/dash-app-user-analytics)

[JavaScript Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-javascript-example)

[Vue JS Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-vue-example)

[Angular JS Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-angular-example)

[JWT Authentication Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-react-jwt-example)

[Create React App Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-react-example)

[React + Webpack Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-react-webpack-example)

[Pass Parameter with dcc.Location](https://dash-playground.plotly.host/Docs/templates/dash-embedded-dcc-location-example)

[Dash Embedded with Snapshots Engine](https://dash-playground.plotly.host/Docs/templates/dash-embedded-snapshots-example)

[Workspaces Ready Embeddable Dash App](https://dash-playground.plotly.host/Docs/templates/dash-embedded-workspaces-dash)

[Workspaces Ready Javascript Host App](https://dash-playground.plotly.host/Docs/templates/dash-embedded-workspaces-host)

[Salesforce Example](https://dash-playground.plotly.host/Docs/templates/dash-embedded-salesforce)

[Managing Dependencies with Conda](https://dash-playground.plotly.host/Docs/templates/conda)

[Accessing the Viewer's Username](https://dash-playground.plotly.host/Docs/templates/dash-enterprise-auth)

[Deploying a Flask API](https://dash-playground.plotly.host/Docs/templates/flask)

[Download a large CSV](https://dash-playground.plotly.host/Docs/templates/flask-api-download)

[Internal PyPI Server](https://dash-playground.plotly.host/Docs/templates/airgapped-pypi)

[Managing Dependencies with Conda with a Custom Conda Channel](https://dash-playground.plotly.host/Docs/templates/conda-airgapped)

[Internal Repository Manager](https://dash-playground.plotly.host/Docs/templates/airgapped-repo)

[Real Time Web Traffic Analytics](https://dash-playground.plotly.host/Docs/templates/usa-gov-analytics)

[Snapshots-Enabled Clinical Trial App & Report](https://dash-playground.plotly.host/Docs/templates/snapshots-clinical-trial-dashboard)
