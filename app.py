import panel as pn

pn.extension(sizing_mode="stretch_width")

from pathlib import Path

# Set up initial cache variables before importing the modules
# Default workspace directory
pn.state.cache["workspace"] = Path("workspaces", "default")
# mzML file directory within workspace
pn.state.cache["mzML"] = Path(pn.state.cache["workspace"], "mzML")
pn.state.cache["mzML"].mkdir(parents=True, exist_ok=True)
# File with a list of all currently selected mzML files
path = Path(pn.state.cache["workspace"], "selected-mzML.txt")
if path.exists():
    with open(path, "r") as f:
        pn.state.cache["selected-mzML"] = [Path(l) for l in f.readlines()]
else:
    pn.state.cache["selected-mzML"] = []

from src.home import home
from src.workspaces import workspaces


app = pn.template.VanillaTemplate(
    title="OpenMS - TemplateApp",
    header_background="#4575B4",
)

# For TESTING!
button = pn.widgets.Button(name="Show panel session cache!", button_type="primary")


def b(event):
    print(pn.state.cache)


button.on_click(b)

test = pn.Row(button)


# Setting up the File Selection Page
selector = pn.widgets.MultiChoice(
    name="Select files that have been uploaded to your workspace. They will be used for data analysis.",
    value=[p.name for p in pn.state.cache["mzML"].iterdir()],
    options=[p.name for p in pn.state.cache["mzML"].iterdir()],
    solid=False,
)


def update_selection(x):
    pn.state.cache["selected-mzML"] = [
        Path(pn.state.cache["mzML"], file) for file in x.new
    ]
    with open(Path(pn.state.cache["workspace"], "selected-mzML-files.txt"), "w") as f:
        f.write("\n".join([str(p) for p in pn.state.cache["selected-mzML"]]))


selector.param.watch(update_selection, "value")

files = pn.widgets.FileSelector("~", only_files=True, file_pattern="*.mzML", width=800)

files.param.watch(update_selection, "value")

fileselection = pn.Column(
    pn.Card(
        selector,
        title="File Selection",
        collapsible=False,
        # max_width=600,
    ),
    files,
    pn.Card(title="File Upload", collapsible=False),
)


pages = pn.Tabs(
    ("🏠 Home", home),
    ("🖥️ Workspaces", workspaces),
    ("📂 mzML Files", fileselection),
    ("👀 Raw Data Visualization", home),
    ("🧪 Workflow", home),
    ("🚧 Test", test),
)
# app.modal.append(pn.widgets.Button(name="Click"))
app.main.append(pages)

app.servable()
