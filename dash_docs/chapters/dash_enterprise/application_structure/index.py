# -*- coding: utf-8 -*-
import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
import os

content = tools.load_markdown_files(__file__)

PAGE_CONTENT_PY = rc.Markdown('''

{buildpack}
{project_folder_py}
{lifecycle_py}

{app_py}
{requirements_py}
{procfile_py}

{checks}
{dokku_scale}            
{gitignore}
{runtime_py}
{apt_files}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
    kubernetes = (
'See [Kubernetes](/Docs/kubernetes) Chapter for more details.' 
if 'DASH_DOCS_URL_PREFIX' in os.environ else '''
>To view the Kubernetes Docs, visit: https://<your-dash-enterprise-hostname\>/Docs/Kubernetes, 
>replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
>Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
''')
))

PAGE_CONTENT_CONDA = rc.Markdown('''

{buildpack}
{project_folder_conda}
{lifecycle_conda}

{app_py}
{requirements_conda}
{procfile_py}

{checks}
{dokku_scale}            
{gitignore}
{runtime_conda}
{apt_files}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
    kubernetes = (
'See [Kubernetes](/Docs/kubernetes) Chapter for more details.' 
if 'DASH_DOCS_URL_PREFIX' in os.environ else '''
>To view the Kubernetes Docs, visit: https://<your-dash-enterprise-hostname\>/Docs/Kubernetes, 
>replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
>Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
''')
))

PAGE_CONTENT_R = rc.Markdown('''

{buildpack}
{project_folder_r}
{lifecycle_r}

{app_r}
{init_r}
{procfile_r}

{checks_r}
{dokku_scale}
{gitignore}
{runtime_conda}
{apt_files}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
    kubernetes = (
'See [Kubernetes](/Docs/kubernetes) Chapter for more details.' 
if 'DASH_DOCS_URL_PREFIX' in os.environ else '''
>To view the Kubernetes Docs, visit: https://<your-dash-enterprise-hostname\>/Docs/Kubernetes, 
>replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
>Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
''')
))

PYTHON_TAB = html.Div([
    PAGE_CONTENT_PY
])

CONDA_TAB = html.Div([
    PAGE_CONTENT_CONDA
])

R_TAB = html.Div([
    PAGE_CONTENT_R
])

layout = html.Div([
    html.H1('Application Structure'),
    html.Div(''),

    dcc.Tabs([
        dcc.Tab(label = 'Python', children = PYTHON_TAB),
        dcc.Tab(label = 'Conda', children = CONDA_TAB),
        dcc.Tab(label = 'R', children = R_TAB)
    ])
])


