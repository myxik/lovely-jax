# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_repr_chans.ipynb.

# %% auto 0
__all__ = ['chans']

# %% ../nbs/05_repr_chans.ipynb 5
from typing import Any, Optional as O

import jax, jax.numpy as jnp
from matplotlib import pyplot as plt, axes, figure
from IPython.core.pylabtools import print_figure

from lovely_numpy.utils.utils import cached_property
from lovely_numpy.repr_chans import fig_chans
from lovely_numpy import config as np_config

from .utils.misc import to_numpy
from .utils.config import get_config


# %% ../nbs/05_repr_chans.ipynb 6
class ChanProxy():   
    def __init__(self, t: jax.Array):
        self.t = t
        self.params = dict(cmap = "twilight", 
                    cm_below="blue",
                    cm_above="red",
                    cm_ninf="cyan",
                    cm_pinf="fuchsia",
                    cm_nan="yellow",
                    view_width=966,
                    gutter_px=3,
                    frame_px=1,
                    scale=1,
                    cl=True,
                    ax=None)

    def __call__(self,
                 cmap       :O[str]=None, 
                 cm_below   :O[str]=None,
                 cm_above   :O[str]=None,
                 cm_ninf    :O[str]=None,
                 cm_pinf    :O[str]=None,
                 cm_nan     :O[str]=None,
                 view_width :O[int]=None,
                 gutter_px  :O[int]=None,
                 frame_px   :O[int]=None,
                 scale      :O[int]=None,
                 cl         :Any=None,
                 ax         :O[axes.Axes]=None):
        
        self.params.update( {   k:v for
                                k,v in locals().items()
                                if k != "self" and v is not None } )
        _ = self.fig # Trigger figure generation
        return self

    @cached_property
    def fig(self) -> figure.Figure:
        cfg = get_config()
        with np_config(fig_close=cfg.fig_close, fig_show=cfg.fig_show):
            return fig_chans(to_numpy(self.t), **self.params)

    def _repr_png_(self):
        return print_figure(self.fig, fmt="png", pad_inches=0,
            metadata={"Software": "Matplotlib, https://matplotlib.org/"})

# %% ../nbs/05_repr_chans.ipynb 7
def chans(  x: jax.Array,                # Input, shape=([...], H, W)
            cmap        :str    ="twilight",# Use matplotlib colormap by this name
            cm_below    :str    ="blue",    # Color for values below -1
            cm_above    :str    ="red",     # Color for values above 1
            cm_ninf     :str    ="cyan",    # Color for -inf values
            cm_pinf     :str    ="fuchsia", # Color for +inf values
            cm_nan      :str    ="yellow",  # Color for NaN values
            view_width  :int    =966,       # Try to produce an image at most this wide
            gutter_px   :int    =3,         # Draw write gutters when tiling the images
            frame_px    :int    =1,         # Draw black frame around each image
            scale       :int    =1,
            cl          :Any    =True,
            ax          :O[axes.Axes]=None
        ) -> ChanProxy:

    "Map tensor values to colors. RGB[A] color is added as channel-last"
    args = locals()
    del args["x"]

    return ChanProxy(x)(**args)
