import panel as pn
import numpy as np
import holoviews as hv

pn.extension()

vanilla = pn.template.VanillaTemplate(title="Vanilla Template")

xs = np.linspace(0, np.pi)
freq = pn.widgets.FloatSlider(name="Frequency", start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi)


@pn.depends(freq=freq, phase=phase)
def sine(freq, phase):
    return hv.Curve((xs, np.sin(xs * freq + phase))).opts(
        responsive=True, min_height=400
    )


@pn.depends(freq=freq, phase=phase)
def cosine(freq, phase):
    return hv.Curve((xs, np.cos(xs * freq + phase))).opts(
        responsive=True, min_height=400
    )


vanilla.sidebar.append(freq)
vanilla.sidebar.append(phase)

vanilla.main.append(
    pn.Row(
        pn.Card(hv.DynamicMap(sine), title="Sine"),
        pn.Card(hv.DynamicMap(cosine), title="Cosine"),
    )
)
vanilla.servable()
