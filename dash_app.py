import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import base64
import glob
import numpy as np
import random
import os
import subprocess

selected = 2


def latest_results(resultdir="results/"):
    results = [fn.split("/")[-1] for fn in glob.glob(resultdir + "*")]
    numbers = [int(direc[:5]) for direc in results]
    most_recent = np.array(numbers).argmax()
    return (
        [
            img
            for img in os.listdir(resultdir + results[most_recent])
            if img.endswith("png")
        ],
        resultdir + results[most_recent],
    )


def generate_random_seeds(n=100):
    return ",".join(
        [
            str(round(random.SystemRandom().random() * (2 ** 32) - 100))
            for i in list(range(n))
        ]
    )


def select_random_pickle(selected_value):
    if selected_value == 1:
        return random.choice(
            [
                "/content/network-snapshot-000480.pkl",
                "/content/network-snapshot-000492.pkl",
            ]
        )
    else:
        return random.choice(
            [
                "/content/network-snapshot-000612.pkl",
                "/content/network-snapshot-000624.pkl",
                "/content/network-snapshot-000636.pkl",
            ]
        )


img_no = 50

app = JupyterDash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Github Repo",
                href="https://github.com/mphirke/fire-emblem-fake-portaits-GBA",
                target="_blank",
                style={"font-weight": "bold"},
            )
        ),
    ],
    style={"margin-bottom": "20px", "padding": "5px"},
    brand="Fire Emblem Fake GBA Portraits Generator",
    brand_href="#",
    color="primary",
    dark=True,
)

radioitems = dbc.FormGroup(
    [
        dbc.RadioItems(
            options=[
                {"label": "From Vanilla FE Portraits", "value": 1},
                {"label": "Everything included", "value": 2},
            ],
            value=2,
            id="radioitems-input",
        ),
    ]
)

app.layout = html.Div(
    children=[
        navbar,
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        [
                            "Generate",
                            dbc.Badge(
                                "50", color="light",
                                id="mybadge", className="ml-1"
                            ),
                        ],
                        color="primary",
                        id="Generate_images",
                        block=True,
                    ),
                    width={"size": 4, "offset": 4},
                    style={"margin-bottom": "20px"},
                ),
                dbc.Col(radioitems, width={"size": 3, "offset": 0}),
            ]
        ),
        dbc.Row(
            dbc.Col(
                dcc.Slider(
                    id="my-slider",
                    min=25,
                    max=150,
                    step=None,
                    marks={
                        25: "25 Images",
                        50: "50 Images",
                        75: "75 Images",
                        100: "100 Images",
                        125: "125 Images",
                        150: "150 Images",
                    },
                    value=50,
                ),
                width={"size": 8, "offset": 2},
            )
        ),
        html.Div(id="slider-output-container"),
        dbc.Row(
            dbc.Col(
                dbc.Alert(
                    "It may take a few minutes to generate first set of images.",
                    id="alert-fade",
                    dismissable=True,
                    is_open=True,
                ),
                width={"size": 6, "offset": 3},
            )
        ),
        dcc.Loading(
            id="loading-1",
            type="default",
            style={"margin-top": "70px"},
            children=html.Div(id="loading-output-1"),
        ),
        dbc.Row(dbc.Col(dbc.Container(id="output_container"))),
        html.P(id="placeholder", style={"visibility": "none"}),
    ]
)


@app.callback(
    dash.dependencies.Output("mybadge", "children"),
    [dash.dependencies.Input("my-slider", "value")],
)
def update_img_no(value):
    global img_no
    img_no = value
    return value


@app.callback(
    Output("alert-fade", "is_open"),
    [Input("alert-toggle-fade", "n_clicks")],
    [State("alert-fade", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse", "is_open"),
    [Input("Generate_images", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    app.callback(
        Output("collapse", "is_open"),
        [Input("Generate_images", "n_clicks")],
        [State("collapse", "is_open")],
    )
    return is_open


@app.callback(
    [Output("output_container", "children"), Output("loading-output-1", "children")],
    [Input("Generate_images", "n_clicks_timestamp")],
)
def update_output(n_clicks):
    if n_clicks < 1:
        raise PreventUpdate

    global selected
    pickle_path = select_random_pickle(selected)
    random_seeds_string = generate_random_seeds(img_no)
    subprocess.run(
        "python stylegan2/run_generator.py generate-images --network="
        + pickle_path
        + " --seeds="
        + random_seeds_string
        + " --truncation-psi=0.5",
        shell=True,
        check=True,
    )

    images, images_dir = latest_results(resultdir)
    print(images)
    images_div = []

    for image in images:
        encoded_image = base64.b64encode(open(images_dir + "/" + image, "rb").read())
        images_div.append(
            html.Div(
                html.A(
                    [
                        html.Img(
                            src="data:image/png;base64,{}".format(
                                encoded_image.decode()
                            ),
                            style={
                                "height": "128px",
                                "width": "128px",
                                "float": "left",
                                "position": "relative",
                                "padding-left": 0,
                                "margin-left": "10px",
                            },
                        )
                    ],
                    href="data:image/png;base64,{}".format(encoded_image.decode()),
                    target="_blank",
                ),
            )
        )
    return None, images_div


@app.callback(
    Output("placeholder", "children"), [Input("radioitems-input", "value")],
)
def on_form_change(radio_items_value):
    global selected
    selected = radio_items_value
    return ""


# app.run_server(mode='inline')
