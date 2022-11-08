# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/10_patch.ipynb.

# %% auto 0
__all__ = ['monkey_patch']

# %% ../nbs/10_patch.ipynb 3
import jax.numpy as jnp
from fastcore.foundation import patch_to
import matplotlib.pyplot as plt

from .repr_str import StrProxy
# from lovely_tensors.repr_rgb import RGBProxy
# from lovely_tensors.repr_plt import PlotProxy
# from lovely_tensors.repr_chans import ChanProxy

# %% ../nbs/10_patch.ipynb 4
def monkey_patch(cls=jnp.DeviceArray):
    "Monkey-patch lovely features into `cls`" 

    # print(cls)
    # print(cls.__repr__)
    # print(cls.__repr)

    if not hasattr(cls, '_plain_repr'):
        cls._plain_repr = cls.__repr__

    @patch_to(cls)
    def __repr__(self: jnp.DeviceArray):
        
        return str(StrProxy(self))

    # Plain - the old behavior
    @patch_to(cls, as_prop=True)
    def p(self: jnp.DeviceArray):
        return StrProxy(self, plain=True)

    # Verbose - print both stats and plain values
    @patch_to(cls, as_prop=True)
    def v(self: jnp.DeviceArray):
        return StrProxy(self, verbose=True)

    @patch_to(cls, as_prop=True)
    def deeper(self: jnp.DeviceArray):
        return StrProxy(self, depth=1)

    # @patch_to(cls, as_prop=True)
    # def rgb(t: torch.Tensor):
    #     return RGBProxy(t)
    
    # @patch_to(cls, as_prop=True)
    # def chans(t: torch.Tensor):
    #     return ChanProxy(t)

    # @patch_to(cls, as_prop=True)
    # def plt(t: torch.Tensor):
    #     return PlotProxy(t)
