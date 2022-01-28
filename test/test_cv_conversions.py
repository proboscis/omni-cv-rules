from loguru import logger

from omni_converter.auto_data.solver import DEFAULT_ASTAR_DESIGN
from omni_converter.solver.astar import AstarSolver
from omni_cv_rules.rulebook import CV_RULEBOOK

target_conversions=[
    ("[image_path]","numpy_rgb"),
    ("pix2pix_batch,nc=3","image,RGB,RGB")
]

def test_solver():
    d = DEFAULT_ASTAR_DESIGN.bind_instance(
        rulebook = CV_RULEBOOK
    )
    solver = d.provide(AstarSolver)
    for tgt,dst in target_conversions:
        res = solver.solve(tgt,dst)
        logger.info(res)