from loguru import logger

from omni_converter.solver.astar import AstarSolver
from omni_cv_rules.rulebook import CV_RULEBOOK

target_conversions=[
    ("[image_path]","numpy_rgb"),
    ("pix2pix_batch,nc=3","image,RGB,RGB")
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
        logger.info(res)