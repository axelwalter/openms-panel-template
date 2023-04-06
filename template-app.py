import panel as pn

# Import all pages for your app
from pages.home import home
from pages.workspaces import WorkspacesPage


pn.extension()
pn.config.sizing_mode = "stretch_width"


# global params
pn.state.session_args["workspace"] = "default"

wsp = WorkspacesPage()


# test printing the state
button = pn.widgets.Button(name="Click me", button_type="primary")


def printstate(event):
    print(pn.state.session_args)


button.on_click(printstate)

fsp = pn.Column(button)

# Set pages (pn.Column objects with content) from /pages directory
pages = pn.Tabs(
    ("🏠 Home", home),
    ("🖥️ Workspaces", wsp.content),
    ("📂 File Selection", fsp),
    ("👀 Raw Data Visualization", home),
    ("🧪 Workflow", home),
)

app = pn.Column(
    pn.Row(
        pn.Column(width=10),
        pn.Column(
            # Set app name
            pn.Row(
                pn.pane.Markdown(
                    """
                #
                # Template App""",
                    style={"color": "#555555"},
                ),
                pn.pane.PNG("assets/OpenMS.png", width=100),
                # Add your additional icons here
            ),
            pages,
        ),
        pn.Column(width=10),
    )
)


app.servable()

# XS = np.linspace(0, np.pi)


# def sine(freq, phase):
#     return (
#         hv.Curve((XS, np.sin(XS * freq + phase)))
#         .opts(responsive=True, min_height=400, title="Sine")
#         .opts(line_width=6)
#     )


# def cosine(freq, phase):
#     return (
#         hv.Curve((XS, np.cos(XS * freq + phase)))
#         .opts(responsive=True, min_height=400, title="Cosine")
#         .opts(line_width=6)
#     )


# freq = pn.widgets.FloatSlider(name="Frequency", start=0, end=10, value=2)
# phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi)

# sine = pn.bind(sine, freq=freq, phase=phase)
# cosine = pn.bind(cosine, freq=freq, phase=phase)

# c1 = pn.Row(
#     pn.Card(hv.DynamicMap(sine), title="Sine"),
#     pn.Card(hv.DynamicMap(cosine), title="Cosine"),
#     name="Plot",
# )

# c2 = pn.Column(
#     pn.widgets.Button(name="button", button_type="warning"),
#     name="📂 File Selection",
# )
