import panel as pn
from pathlib import Path

pn.extension()
pn.config.sizing_mode = "stretch_width"

# Make sure the default workspace exists
pn.state.cache["workspace"] = Path("workspaces", "default")
if not pn.state.cache["workspace"].exists():
    pn.state.cache["workspace"].mkdir()
pn.state.cache["mzML"] = Path(pn.state.cache["workspace"], "mzML")
if not pn.state.cache["mzML"].exists():
    pn.state.cache["mzML"].mkdir()

# Import all pages for your app
from pages.home import home
from pages.workspaces import workspaces

# from pages.fileselection import fileselection


# test printing the state
button = pn.widgets.Button(name="Click me", button_type="primary")


def printstate(event):
    print(pn.state.cache)


button.on_click(printstate)

fsp = pn.Column(button)

# Set pages (pn.Column objects with content) from /pages directory
pages = pn.Tabs(
    ("🏠 Home", home),
    ("🖥️ Workspaces", workspaces),
    ("📂 File Selection", home),
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
        pn.Column(width=30),
    )
)


app.servable()
