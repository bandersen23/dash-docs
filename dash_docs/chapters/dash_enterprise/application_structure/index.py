import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
import os

content = tools.load_markdown_files(__file__)

content['requirements.md'] = content['requirements.md'].format(
    url=(
        'something' if 'DASH_DOCS_URL_PREFIX' in os.environ
        else 'another thing'
    )
)

PAGE_CONTENT = rc.Markdown('''
{requirements}
***
{runtime}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}))

PYTHON_TAB = html.Div([
    PAGE_CONTENT,

    rc.Markdown(content['requirements.md'].format(
        url=(
            'something' if 'DASH_DOCS_URL_PREFIX' in os.environ
            else 'another thing'
        )
    )),

    html.Hr(),

    rc.Markdown(content['runtime.md']),
])


layout = html.Div([
    html.H1('Application Structure'),
    html.Div('Subtitle...'),

    dcc.Tabs([
        dcc.Tab(label='Python', children=PYTHON_TAB)
    ])
])
