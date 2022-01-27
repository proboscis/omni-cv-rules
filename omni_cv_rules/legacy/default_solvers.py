from omni_converter.auto_data.solver import DEFAULT_ASTAR_DESIGN
from omni_converter.coconut.auto_data import AutoSolver, AutoData
from omni_converter.solver.astar import AstarSolver
from omni_cv_rules.rulebook import non_recursive_rules, recursive_rules

SOLVER = None


def get_init_solver():
    from omni_converter.auto_data.default_rules import DEFAULT_RULES
    # return AutoSolver(
    #     rules=list(DEFAULT_RULES.rules),
    #     smart_rules=[],
    #     heuristics=tuple_widget_heuristics,
    #     edge_cutter=tuple_edge_cutter,
    #     debug_hook=debug
    # )
    d = DEFAULT_ASTAR_DESIGN.bind_instance(
        non_recursive_rules=non_recursive_rules,
        recursive_rules=recursive_rules
    )
    solver = d.provide(AstarSolver)
    return solver

def solver_getter():
    if SOLVER is None:
        reset_solver()
    return SOLVER


def reset_solver():
    global SOLVER
    SOLVER = get_init_solver()

#
# def auto_img(format):
#     def _get_value(value):
#         return AutoData(value, format, solver_getter)
#
#     return _get_value
