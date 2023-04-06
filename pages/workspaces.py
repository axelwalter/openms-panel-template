import panel as pn
from pathlib import Path


pn.state.session_args["workspace"] = Path("workspaces", "default")
if not pn.state.session_args["workspace"].exists():
    pn.state.session_args["workspace"].mkdir()

ws_selector = pn.widgets.Select(
    name="Select Workspace",
    options=[path.name for path in Path("workspaces").iterdir()],
)

current_ws_indicator = pn.pane.Alert(
    f"Your current workspace: **default**",
    alert_type="primary",
)


def set_current_workspace(event):
    pn.state.session_args["workspace"] = Path("workspace", ws_selector.value)
    current_ws_indicator.object = (
        f"Your current workspace: **{pn.state.session_args['workspace'].name}**"
    )


ws_selector.param.watch(set_current_workspace, "value")

new_ws_name = pn.widgets.TextInput(
    value="", placeholder="Enter new workspace name here..."
)
new_ws_button = pn.widgets.Button(name="Create Workspace", button_type="success")


def create_workspace(event):
    pn.state.session_args["workspace"] = Path("workspaces", new_ws_name.value)
    if not pn.state.session_args["workspace"].exists():
        pn.state.session_args["workspace"].mkdir()


new_ws_button.on_click(create_workspace)

workspace_page = pn.Column(
    pn.Row(
        ws_selector,
        current_ws_indicator,
    ),
    pn.Row(
        pn.Card(new_ws_name, new_ws_button, title="Create Workspace"),
        pn.Card(title="Delete Workspace"),
    ),
)

if __name__ == "__main__":
    pn.extension()
    pn.config.sizing_mode = "stretch_width"
    workspace_page.servable()

# {pn.state.session_args['workspace'].name}
