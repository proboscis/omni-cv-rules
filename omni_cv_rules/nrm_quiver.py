import io
import itertools
from functools import partial
from typing import List, Any

import numpy as np
from loguru import logger
from matplotlib import pyplot as plt

from omni_converter.solver.rules import RuleEdge


def to_nrm_quiver_auto(nrm: "AutoData",auto_func) -> "AutoData":
    return to_nrm_quiver(nrm.to("numpy,float32,HWC,XYZ,-1_1"),auto_func)


def to_nrm_quiver(nrm: np.ndarray,auto_func) -> "AutoData":
    # fmt: numpy,float32,HWC,XYZ,-1_1
    # converting an image to nrm_quiver destructs semantic consistency. should I avoid adding this to rule?
    # I guess not.
    # we need 10 for 256 px so
    np_nrm = nrm  # == ("numpy,float32,HWC,XYZ,-1_1")
    h, w, c = np_nrm.shape
    figw = w / 256 * 10
    figh = h / 256 * 10
    logger.info(f"using fig size:{(figw, figh)}")
    fig, ax = plt.subplots(figsize=(figw, figh))
    quiver_sample_n = int(min(w, h) / 256 * 50)

    x, y = np.meshgrid(np.linspace(0, w - 1, quiver_sample_n), np.linspace(0, h - 1, quiver_sample_n))
    sampled = np_nrm[-y.astype(int), x.astype(int)]  # (n,n,3)
    quiver = ax.quiver(x, y, sampled[:, :, 0], sampled[:, :, 1])
    ax.tick_params(length=5)
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img = plt.imread(buf)
    return auto_func("numpy,float32,HWC,RGBA,0_1",img)


def swap_channel_order(img: np.ndarray, src_idx, dst_idx):
    assert len(img.shape) == 4, "only support BHWC type of ndarray image"
    copied = np.copy(img)
    src = copied[:, :, :, src_idx]
    copied[:, :, :, src_idx] = copied[:, :, :, dst_idx]
    copied[:, :, :, dst_idx] = src
    return src


import re

CH_MATCHER = re.compile("[A-Z][a-z]*")


def extract_channels(ch_repr: str):
    return CH_MATCHER.findall(ch_repr)


def swap_element(items: list, i, j):
    items = items.copy()
    tmp = items[i]
    items[i] = items[j]
    items[j] = tmp
    return items


def rule_to_swap_channel_order(state):
    from pampy import match
    def _swap_rules(s: dict):
        channels = extract_channels(s["ch_rpr"])
        axis = list(range(len(channels)))
        res = []
        for src_i, dst_i in itertools.combinations(axis, 2):
            new_chs = swap_element(channels, src_i, dst_i)
            new_state = s.copy()
            new_state["ch_rpr"] = "".join(new_chs)
            res.append(RuleEdge(
                converter=partial(swap_channel_order, src_idx=src_i, dst_idx=dst_i),
                new_state=new_state,
                cost=1,
                name=f"swap channel {channels[src_i]} to {channels[dst_i]}"
            ))
        return res

    match(state,
          {"type": "numpy", "arrange": "BHWC"}, _swap_rules,
          Any, lambda state: None
          )


def rule_to_nrm_quiver(state) -> List[RuleEdge]:
    if state == "numpy,float32,HWC,XYZ,-1_1":
        return [RuleEdge(
            to_nrm_quiver,
            "nrm_quiver",
            1,
            "normal map to quiver plot"
        )]
