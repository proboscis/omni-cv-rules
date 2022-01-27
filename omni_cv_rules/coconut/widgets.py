#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4a8871c

# Compiled with Coconut version 1.6.0 [Vocational Guidance Counsellor]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == "__coconut__":
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == "__coconut__":
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

from omni_cv_rules.coconut.omni_converter import AutoTuple  # from omni_cv_rules.coconut.omni_converter import AutoTuple
from ipywidgets import widgets  # from ipywidgets import widgets

def any2widget(state):  # def any2widget(state):
    return ([(lambda ary: Text(str(ary)), "widget", "anything_to_text_widget", 1000), ])  #     return [(ary->Text(str(ary)),"widget","anything_to_text_widget",1000)]

def auto_tuple2widget(state):  # def auto_tuple2widget(state):
    _coconut_case_match_to_0 = state  #     case state:
    _coconut_case_match_check_0 = False  #     case state:
    _coconut_match_set_name_items = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_0, AutoTuple)) and (_coconut.len(_coconut_case_match_to_0) == 1):  #     case state:
        _coconut_match_set_name_items = _coconut_case_match_to_0[0]  #     case state:
        _coconut_case_match_check_0 = True  #     case state:
    if _coconut_case_match_check_0:  #     case state:
        if _coconut_match_set_name_items is not _coconut_sentinel:  #     case state:
            items = _coconut_case_match_to_0[0]  #     case state:
    if _coconut_case_match_check_0 and not (all((i == "widget" for i in items))):  #     case state:
        _coconut_case_match_check_0 = False  #     case state:
    if _coconut_case_match_check_0:  #     case state:
        return ([(lambda values: widgets.VBox(values), "widget", "auto_tuple of widgets to a widget", 1), ])  #             return [
