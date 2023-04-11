import panel as pn
from pathlib import Path

# Import all pages for your app
from pages.home import home
from pages.workspaces import workspaces


pn.extension()
pn.config.sizing_mode = "stretch_width"

# Setting up global variables
pn.state.session_args["workspace"] = Path("workspaces", "default")

# test printing the state
button = pn.widgets.Button(name="Click me", button_type="primary")


def printstate(event):
    print(pn.state.session_args)


button.on_click(printstate)

fsp = pn.Column(button)

# Set pages (pn.Column objects with content) from /pages directory
pages = pn.Tabs(
    ("🏠 Home", home),
    ("🖥️ Workspaces", workspaces),
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
        pn.Column(width=30),
    )
)


app.servable()
