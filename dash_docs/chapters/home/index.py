# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash_docs.chapter_index import URLS, URL_TO_CONTENT_MAP, DASH_ENTERPRISE_URLS

from dash_docs.convert_to_html import convert_to_html
from dash_docs.reusable_components import TOC, WorkspaceBlurb
from dash_docs.tools import merge, relpath

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Dash open-source', children=[
            html.H1('Dash User Guide'),

            dcc.Markdown(
                '''
                > This user guide is for the Python implementation of Dash Open Source.
                > Dash Open Source is also available in R and Julia.
                > View the [Dash for R User Guide & Documentation](https://dashr.plotly.com)
                > and the [Dash for Julia User Guide & Documentation](https://dash-julia.plotly.com)
                ''', style={'fontSize': 14}
            ),

            WorkspaceBlurb,

            TOC(URLS)
        ]),

        dcc.Tab(label='Dash Enterprise', children=[
            html.Div(TOC([DASH_ENTERPRISE_URLS])),
            html.Img(
                src=relpath('/assets/images/dds/app-architecture.jpg'),
                alt='Dash App Architecture Diagram'
            )
        ])

    ])
])


# Ugly side effect:
# home isn't in chapter_index because it's created dynamically in this file
# from the URLS: importing it into chapter_index would be a circular import.
# Since it's not in chapter_index, it's also not in the server-side rendering
# dict.
# So, we add it here as a side effect from importing.
URL_TO_CONTENT_MAP['/'] = layout
