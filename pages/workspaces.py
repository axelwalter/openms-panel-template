import panel as pn

# pn.extension()
# # pn.config.sizing_mode = "stretch_width"


class WorkspacesPage:
    def __init__(self):
        text = pn.widgets.TextInput(value="Ready")
        button = pn.widgets.Button(name="Click me", button_type="primary")

        def create_workspace(event):
            pn.state.session_args["workspace"] = text.value

        button.on_click(create_workspace)
        self.content = pn.Column(pn.Row(button, text))
