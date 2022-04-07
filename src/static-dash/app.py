"""
"""
import pathlib

import dash

# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html


external_scripts = [
    # 'https://www.google-analytics.com/analytics.js',
    # {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    # {
    #     'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
    #     'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
    #     'crossorigin': 'anonymous'
    # }
]

external_stylesheets = [
    "style.css",
    # 'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # {
    #     'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
    #     'rel': 'stylesheet',
    #     'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
    #     'crossorigin': 'anonymous'
    # }
]

app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
)

markdown_text = pathlib.Path("content.md").read_text()

app.layout = html.Div([dcc.Markdown(children=markdown_text)])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=8000)
