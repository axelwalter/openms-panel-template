import param
import panel as pn
from pathlib import Path
import shutil

pn.extension()


class Workspaces(param.Parameterized):
    # Initialize with default workspaces directory in session args
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Watch selector for workspace changes
        self.param.watch(self.set_current_workspace, "selector")

    # Selector for currently available workspaces
    selector = param.Selector(
        default="default",
        objects=[p.name for p in Path("workspaces").iterdir()],
    )

    # Text field for creating new workspaces
    create = param.String()

    # Button to create new workspace -> calls create_worspace function
    create_action = param.Action(lambda self: self.create_workspace())

    # Delete currently selected workspace button
    delete_action = param.Action(lambda self: self.delete_workspace())

    # Sets current workspace whenever selector widget changes, either manually or by new workspace
    def set_current_workspace(self, event):
        pn.state.cache["workspace"] = Path("workspaces", self.selector)
        pn.state.cache["mzML"] = Path(pn.state.cache["workspace"], "mzML")
        # pn.state.cache["selected"].options = [
        #     p.name for p in pn.state.cache["mzML"].iterdir()
        # ]
        # pn.state.cache["selected"].value = [
        #     p.name for p in pn.state.cache["mzML"].iterdir()
        # ]

    # Creates new workspace directory and updates selector widget
    def create_workspace(self):
        if self.create:
            path = Path("workspaces", self.create, "mzML")
            path.mkdir(parents=True, exist_ok=True)
            l = self.param.selector.objects.copy()
            l.append(self.create)
            self.param.selector.objects = l
            self.selector = self.create
            self.create = ""

    # Deletes selected workspace if it's not default
    def delete_workspace(self):
        if self.selector != "default":
            shutil.rmtree(pn.state.cache["workspace"])
            l = self.param.selector.objects.copy()
            l.remove(self.selector)
            self.param.selector.objects = l
            self.selector = "default"


# Build the content of the workspaces page
workspaces = pn.Card(
    pn.Param(
        Workspaces().param,
        widgets={
            "selector": {
                "widget_type": pn.widgets.Select,
                "name": "Select Workspace",
                "margin": (10, 10, 30, 10),
            },
            "create": {
                "widget_type": pn.widgets.TextInput,
                "placeholder": "Enter new workspace name here...",
                "name": "Create a new workspace",
            },
            "create_action": {
                "widget_type": pn.widgets.Button,
                "button_type": "success",
                "name": "Create Workspace",
                "margin": (10, 10, 30, 10),
            },
            "delete_action": {
                "widget_type": pn.widgets.Button,
                "button_type": "danger",
                "name": "Delete Selected Workspace",
            },
        },
        show_name=False,
    ),
    title="Workspace Settings",
    collapsible=False,
    max_width=300,
)


# ws = Workspaces()

# content = ws.content()

# content.servable()
