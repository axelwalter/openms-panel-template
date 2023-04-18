import param
import panel as pn
from pathlib import Path
import shutil
import io

pn.extension()

pn.state.cache["mzML"] = Path("workspaces/default/mzML")

pn.state.cache["selected"] = pn.widgets.MultiChoice(
    name="Select mzML files for analysis",
    value=[p.name for p in pn.state.cache["mzML"].iterdir()],
    options=[p.name for p in pn.state.cache["mzML"].iterdir()],
    solid=False,
)

file_input = pn.widgets.FileInput(accept=".mz*", multiple=True)
upload_button = pn.widgets.Button(name="Upload files", button_type="primary")


def file_upload(event):
    for name, value in zip(file_input.filename, file_input.value):
        if file_input.value is not None:
            with open(str(Path("../workspaces/default/mzML", name)), "wb") as f:
                f.write(value)

            new_options = pn.state.cache["selected"].options.copy()
            new_values = pn.state.cache["selected"].value.copy()
            new_options.append(name)
            pn.state.cache["selected"].options = new_options
            pn.state.cache["selected"].value = new_values

            # pn.state.cache["selected"].options.append(name)


# upload_button.on_click(file_upload)

# attach the file_upload function to the widget's 'change' event
file_input.param.watch(file_upload, "value")

# Build the content of the workspaces page
fileselection = pn.Column(
    pn.Card(
        pn.state.cache["selected"],
        title="File Selection",
        collapsible=False,
        # max_width=600,
    ),
    pn.Row(file_input, upload_button),
)


fileselection.servable()
