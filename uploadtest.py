import panel as pn
import time
from pathlib import Path

pn.extension()


# def upload(event):
#     progress.active = True
#     # file_input.active = False
#     if file_input.filename is not None:
#         with open(str(Path("workspaces/default/mzML", file_input.filename)), "wb") as f:
#             f.write(file_input.value)
#     progress.active = False
#     file_input.active = True


def upload(event):
    for name, value in zip(file_input.filename, file_input.value):
        if file_input.value is not None:
            with open(str(Path("workspaces/default/mzML", name)), "wb") as f:
                f.write(value)


file_input = pn.widgets.FileInput(multiple=True)
progress = pn.widgets.Progress(active=False)
# file_input.jscallback(
#     args={"progress": progress},
#     value="""
#         progress.active = true;
#         source.disabled = true;
#     """,
# )

file_input.param.watch(upload, "value")
col = pn.Column(progress, file_input)
col.servable()
