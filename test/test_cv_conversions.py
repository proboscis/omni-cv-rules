import frozendict
from loguru import logger

from omni_converter import AutoDataFactory
from omni_converter.solver.astar import AstarSolver
from omni_cv_rules.coconut.omni_converter import AutoList
from omni_cv_rules.rulebook import CV_RULEBOOK

target_conversions=[
    ("[image_path]","numpy_rgb"),
    ("pix2pix_batch,nc=3","image,RGB,RGB"),
    ("torch,float32,CHW,RGB,0_1","base64"),
    ("torch,float32,CHW,RGB,0_1","widget"),
    ("numpy,float32,CHW,RGB,0_1","[image,L,L]"),
    ("numpy,float32,BCHW,RGB,0_1","[image,L,L]"),
    ("[numpy,float32,CHW,RGB,0_1]","[image,L,L]"),
    ("numpy,float32,BHW,L,None","numpy,float32,BHWC,RGB,None"),
    (AutoList(frozendict.frozendict({'arrange': 'HWC', 'meta': frozendict.frozendict({'shape': (None, None, 1)}), 'type': 'numpy', 'dtype': 'float32', 'ch_rpr': 'L', 'v_range': 'None'})),
     AutoList(frozendict.frozendict({'type': 'numpy', 'arrange': 'HWC', 'ch_rpr': 'LLL', 'meta': frozendict.frozendict({'shape': (None, None, 3)}), 'dtype': 'float32', 'v_range': 'None'})))
]

def test_solver():
    solver = AstarSolver(
        heuristics=lambda x,y:0,
        neighbors=CV_RULEBOOK,
        max_depth=100,
        silent=False
    )
    for tgt,dst in target_conversions:
        res = solver.solve(tgt,dst)
        #logger.info(res)

def test_auto():
    auto = AutoDataFactory(CV_RULEBOOK)
    #auto(None,None).solver.solve_cache.clear()
    for tgt,dst in target_conversions:
        c = auto(tgt,None).converter(dst)
        #logger.info(c)

