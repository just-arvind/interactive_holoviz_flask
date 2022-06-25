import holoviews as hv
import panel as pn
import numpy as np

hv.extension('bokeh')

def sine(frequency, phase, amplitude):
    xs = np.linspace(0, np.pi*4)
    return hv.Curve((xs, np.sin(frequency*xs+phase)*amplitude)).options(width=800)

if __name__ == '__main__':
    ranges = dict(frequency=(1, 5), phase=(-np.pi, np.pi), amplitude=(-2, 2), y=(-2, 2))
    dmap = hv.DynamicMap(sine, kdims=['frequency', 'phase', 'amplitude']).redim.range(**ranges)
    pn.serve(dmap, port=5006, allow_websocket_origin=["127.0.0.1:5000"], show=False)
