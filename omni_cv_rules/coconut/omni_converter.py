#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd82d6f65

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

from math import sqrt  # from math import sqrt

import PIL.Image  # import PIL.Image

from omni_cv_rules.coconut.convert import *  # from omni_cv_rules.coconut.convert import *
from frozendict import frozendict  # from frozendict import frozendict
from typing import Mapping  # from typing import Mapping
from loguru import logger  # from loguru import logger
import numpy as np  # import numpy as np
from omni_cv_rules.coconut.visualization import infer_widget  # from omni_cv_rules.coconut.visualization import infer_widget
from omni_cv_rules.place_holder.torch_proxy import torch  # from omni_cv_rules.place_holder.torch_proxy import torch
def imagedef2dict(imdef: 'ImageDef'):  # def imagedef2dict(imdef:ImageDef):
    _coconut_case_match_to_1 = imdef  #     case imdef:
    _coconut_case_match_check_1 = False  #     case imdef:
    _coconut_match_set_name_data_type = _coconut_sentinel  #     case imdef:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case imdef:
    if (_coconut.isinstance(_coconut_case_match_to_1, ImageDef)) and (_coconut.len(_coconut_case_match_to_1) == 2):  #     case imdef:
        _coconut_match_set_name_data_type = _coconut_case_match_to_1[0]  #     case imdef:
        _coconut_match_set_name_meta = _coconut_case_match_to_1[1]  #     case imdef:
        _coconut_case_match_check_1 = True  #     case imdef:
    if _coconut_case_match_check_1:  #     case imdef:
        if _coconut_match_set_name_data_type is not _coconut_sentinel:  #     case imdef:
            data_type = _coconut_case_match_to_1[0]  #     case imdef:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case imdef:
            meta = _coconut_case_match_to_1[1]  #     case imdef:
    if _coconut_case_match_check_1:  #     case imdef:
        _coconut_case_match_to_0 = data_type  #     case imdef:
        _coconut_case_match_check_0 = False  #     case imdef:
        _coconut_match_set_name_dtype = _coconut_sentinel  #     case imdef:
        _coconut_match_set_name_arrange = _coconut_sentinel  #     case imdef:
        _coconut_match_set_name_ch_rpr = _coconut_sentinel  #     case imdef:
        _coconut_match_set_name_v_range = _coconut_sentinel  #     case imdef:
        if (_coconut.isinstance(_coconut_case_match_to_0, Numpy)) and (_coconut.len(_coconut_case_match_to_0) == 4):  #     case imdef:
            _coconut_match_set_name_dtype = _coconut_case_match_to_0[0]  #     case imdef:
            _coconut_match_set_name_arrange = _coconut_case_match_to_0[1]  #     case imdef:
            _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[2]  #     case imdef:
            _coconut_match_set_name_v_range = _coconut_case_match_to_0[3]  #     case imdef:
            _coconut_case_match_check_0 = True  #     case imdef:
        if _coconut_case_match_check_0:  #     case imdef:
            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #     case imdef:
                dtype = _coconut_case_match_to_0[0]  #     case imdef:
            if _coconut_match_set_name_arrange is not _coconut_sentinel:  #     case imdef:
                arrange = _coconut_case_match_to_0[1]  #     case imdef:
            if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #     case imdef:
                ch_rpr = _coconut_case_match_to_0[2]  #     case imdef:
            if _coconut_match_set_name_v_range is not _coconut_sentinel:  #     case imdef:
                v_range = _coconut_case_match_to_0[3]  #     case imdef:
        if _coconut_case_match_check_0:  #     case imdef:
            info = dict(type="numpy", dtype=dtype, arrange=arrange, ch_rpr=ch_rpr, v_range=str(v_range))  #                     info = dict(type="numpy",dtype=dtype,arrange=arrange,ch_rpr=ch_rpr,v_range=str(v_range))
        if not _coconut_case_match_check_0:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_dtype = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_arrange = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_v_range = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            if (_coconut.isinstance(_coconut_case_match_to_0, Torch)) and (_coconut.len(_coconut_case_match_to_0) == 4):  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_dtype = _coconut_case_match_to_0[0]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_arrange = _coconut_case_match_to_0[1]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[2]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_v_range = _coconut_case_match_to_0[3]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_case_match_check_0 = True  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            if _coconut_case_match_check_0:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    dtype = _coconut_case_match_to_0[0]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_arrange is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    arrange = _coconut_case_match_to_0[1]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    ch_rpr = _coconut_case_match_to_0[2]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_v_range is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    v_range = _coconut_case_match_to_0[3]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            if _coconut_case_match_check_0:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                info = dict(type="torch", dtype=dtype, arrange=arrange, ch_rpr=ch_rpr, v_range=str(v_range))  #                     info = dict(type="torch",dtype=dtype,arrange=arrange,ch_rpr=ch_rpr,v_range=str(v_range))
        if not _coconut_case_match_check_0:  #                 match PILImages(mode,ch_rpr):
            _coconut_match_set_name_mode = _coconut_sentinel  #                 match PILImages(mode,ch_rpr):
            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #                 match PILImages(mode,ch_rpr):
            if (_coconut.isinstance(_coconut_case_match_to_0, PILImages)) and (_coconut.len(_coconut_case_match_to_0) == 2):  #                 match PILImages(mode,ch_rpr):
                _coconut_match_set_name_mode = _coconut_case_match_to_0[0]  #                 match PILImages(mode,ch_rpr):
                _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[1]  #                 match PILImages(mode,ch_rpr):
                _coconut_case_match_check_0 = True  #                 match PILImages(mode,ch_rpr):
            if _coconut_case_match_check_0:  #                 match PILImages(mode,ch_rpr):
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #                 match PILImages(mode,ch_rpr):
                    mode = _coconut_case_match_to_0[0]  #                 match PILImages(mode,ch_rpr):
                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #                 match PILImages(mode,ch_rpr):
                    ch_rpr = _coconut_case_match_to_0[1]  #                 match PILImages(mode,ch_rpr):
            if _coconut_case_match_check_0:  #                 match PILImages(mode,ch_rpr):
                info = dict(type="images", ch_rpr=ch_rpr, mode=mode)  #                     info = dict(type="images",ch_rpr=ch_rpr,mode=mode)
        if not _coconut_case_match_check_0:  #                 match PILImage(mode,ch_rpr):
            _coconut_match_set_name_mode = _coconut_sentinel  #                 match PILImage(mode,ch_rpr):
            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #                 match PILImage(mode,ch_rpr):
            if (_coconut.isinstance(_coconut_case_match_to_0, PILImage)) and (_coconut.len(_coconut_case_match_to_0) == 2):  #                 match PILImage(mode,ch_rpr):
                _coconut_match_set_name_mode = _coconut_case_match_to_0[0]  #                 match PILImage(mode,ch_rpr):
                _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[1]  #                 match PILImage(mode,ch_rpr):
                _coconut_case_match_check_0 = True  #                 match PILImage(mode,ch_rpr):
            if _coconut_case_match_check_0:  #                 match PILImage(mode,ch_rpr):
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #                 match PILImage(mode,ch_rpr):
                    mode = _coconut_case_match_to_0[0]  #                 match PILImage(mode,ch_rpr):
                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #                 match PILImage(mode,ch_rpr):
                    ch_rpr = _coconut_case_match_to_0[1]  #                 match PILImage(mode,ch_rpr):
            if _coconut_case_match_check_0:  #                 match PILImage(mode,ch_rpr):
                info = dict(type="image", ch_rpr=ch_rpr, mode=mode)  #                     info = dict(type="image",ch_rpr=ch_rpr,mode=mode)
        if not _coconut_case_match_check_0:  #             else:
            raise RuntimeError("cannot convert unknown imagedef:{_coconut_format_0} to dict.".format(_coconut_format_0=(imdef)))  #                 raise RuntimeError(f"cannot convert unknown imagedef:{imdef} to dict.")
        return (frozendict(meta=meta, **info))  #             return frozendict(
    if not _coconut_case_match_check_1:  #     else:
        raise RuntimeError("cannot convert unknown imdef:{_coconut_format_0} to dict.".format(_coconut_format_0=(imdef)))  #         raise RuntimeError(f"cannot convert unknown imdef:{imdef} to dict.")


def cast_imdef_to_dict(state):  # def cast_imdef_to_dict(state):
    if isinstance(state, ImageDef):  #     if isinstance(state,ImageDef):
        return ([imagedef2dict(state), ])  #         return [imagedef2dict(state)]

def cast_imdef_str_to_imdef(state):  # def cast_imdef_str_to_imdef(state):
    if isinstance(state, str):  #     if isinstance(state,str):
        try:  #         try:
            res = str_to_img_def(state)  #             res = str_to_img_def(state)
            return ([res, ])  #             return [res]
        except Exception as e:  #         except Exception as e:
            pass  #             pass
def imdef2imdef_str(imdef):  # def imdef2imdef_str(imdef):
    _coconut_case_match_to_3 = imdef  #     case imdef:
    _coconut_case_match_check_3 = False  #     case imdef:
    _coconut_match_set_name_data_type = _coconut_sentinel  #     case imdef:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case imdef:
    if (_coconut.isinstance(_coconut_case_match_to_3, ImageDef)) and (_coconut.len(_coconut_case_match_to_3) == 2):  #     case imdef:
        _coconut_match_set_name_data_type = _coconut_case_match_to_3[0]  #     case imdef:
        _coconut_match_set_name_meta = _coconut_case_match_to_3[1]  #     case imdef:
        _coconut_case_match_check_3 = True  #     case imdef:
    if _coconut_case_match_check_3:  #     case imdef:
        if _coconut_match_set_name_data_type is not _coconut_sentinel:  #     case imdef:
            data_type = _coconut_case_match_to_3[0]  #     case imdef:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case imdef:
            meta = _coconut_case_match_to_3[1]  #     case imdef:
    if _coconut_case_match_check_3:  #     case imdef:
        _coconut_case_match_to_2 = data_type  #     case imdef:
        _coconut_case_match_check_2 = False  #     case imdef:
        _coconut_match_set_name_dtype = _coconut_sentinel  #     case imdef:
        _coconut_match_set_name_arrange = _coconut_sentinel  #     case imdef:
        _coconut_match_set_name_ch_rpr = _coconut_sentinel  #     case imdef:
        _coconut_match_set_name_v_range = _coconut_sentinel  #     case imdef:
        if (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) == 4):  #     case imdef:
            _coconut_match_set_name_dtype = _coconut_case_match_to_2[0]  #     case imdef:
            _coconut_match_set_name_arrange = _coconut_case_match_to_2[1]  #     case imdef:
            _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[2]  #     case imdef:
            _coconut_match_set_name_v_range = _coconut_case_match_to_2[3]  #     case imdef:
            _coconut_case_match_check_2 = True  #     case imdef:
        if _coconut_case_match_check_2:  #     case imdef:
            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #     case imdef:
                dtype = _coconut_case_match_to_2[0]  #     case imdef:
            if _coconut_match_set_name_arrange is not _coconut_sentinel:  #     case imdef:
                arrange = _coconut_case_match_to_2[1]  #     case imdef:
            if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #     case imdef:
                ch_rpr = _coconut_case_match_to_2[2]  #     case imdef:
            if _coconut_match_set_name_v_range is not _coconut_sentinel:  #     case imdef:
                v_range = _coconut_case_match_to_2[3]  #     case imdef:
        if _coconut_case_match_check_2:  #     case imdef:
            base = "numpy,{_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3}".format(_coconut_format_0=(dtype), _coconut_format_1=(arrange), _coconut_format_2=(ch_rpr), _coconut_format_3=(v_range))  #                     base = f"numpy,{dtype},{arrange},{ch_rpr},{v_range}"
        if not _coconut_case_match_check_2:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_dtype = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_arrange = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_set_name_v_range = _coconut_sentinel  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            if (_coconut.isinstance(_coconut_case_match_to_2, Torch)) and (_coconut.len(_coconut_case_match_to_2) == 4):  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_dtype = _coconut_case_match_to_2[0]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_arrange = _coconut_case_match_to_2[1]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[2]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_match_set_name_v_range = _coconut_case_match_to_2[3]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_case_match_check_2 = True  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            if _coconut_case_match_check_2:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    dtype = _coconut_case_match_to_2[0]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_arrange is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    arrange = _coconut_case_match_to_2[1]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    ch_rpr = _coconut_case_match_to_2[2]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                if _coconut_match_set_name_v_range is not _coconut_sentinel:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                    v_range = _coconut_case_match_to_2[3]  #                 match Torch(dtype,arrange,ch_rpr,v_range):
            if _coconut_case_match_check_2:  #                 match Torch(dtype,arrange,ch_rpr,v_range):
                base = "torch,{_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3}".format(_coconut_format_0=(dtype), _coconut_format_1=(arrange), _coconut_format_2=(ch_rpr), _coconut_format_3=(v_range))  #                     base = f"torch,{dtype},{arrange},{ch_rpr},{v_range}"
        if not _coconut_case_match_check_2:  #                 match PILImages(mode,ch_rpr):
            _coconut_match_set_name_mode = _coconut_sentinel  #                 match PILImages(mode,ch_rpr):
            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #                 match PILImages(mode,ch_rpr):
            if (_coconut.isinstance(_coconut_case_match_to_2, PILImages)) and (_coconut.len(_coconut_case_match_to_2) == 2):  #                 match PILImages(mode,ch_rpr):
                _coconut_match_set_name_mode = _coconut_case_match_to_2[0]  #                 match PILImages(mode,ch_rpr):
                _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[1]  #                 match PILImages(mode,ch_rpr):
                _coconut_case_match_check_2 = True  #                 match PILImages(mode,ch_rpr):
            if _coconut_case_match_check_2:  #                 match PILImages(mode,ch_rpr):
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #                 match PILImages(mode,ch_rpr):
                    mode = _coconut_case_match_to_2[0]  #                 match PILImages(mode,ch_rpr):
                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #                 match PILImages(mode,ch_rpr):
                    ch_rpr = _coconut_case_match_to_2[1]  #                 match PILImages(mode,ch_rpr):
            if _coconut_case_match_check_2:  #                 match PILImages(mode,ch_rpr):
                base = "images,{_coconut_format_0},{_coconut_format_1}".format(_coconut_format_0=(mode), _coconut_format_1=(ch_rpr))  #                     base = f"images,{mode},{ch_rpr}"
        if not _coconut_case_match_check_2:  #                 match PILImage(mode,ch_rpr):
            _coconut_match_set_name_mode = _coconut_sentinel  #                 match PILImage(mode,ch_rpr):
            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #                 match PILImage(mode,ch_rpr):
            if (_coconut.isinstance(_coconut_case_match_to_2, PILImage)) and (_coconut.len(_coconut_case_match_to_2) == 2):  #                 match PILImage(mode,ch_rpr):
                _coconut_match_set_name_mode = _coconut_case_match_to_2[0]  #                 match PILImage(mode,ch_rpr):
                _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[1]  #                 match PILImage(mode,ch_rpr):
                _coconut_case_match_check_2 = True  #                 match PILImage(mode,ch_rpr):
            if _coconut_case_match_check_2:  #                 match PILImage(mode,ch_rpr):
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #                 match PILImage(mode,ch_rpr):
                    mode = _coconut_case_match_to_2[0]  #                 match PILImage(mode,ch_rpr):
                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #                 match PILImage(mode,ch_rpr):
                    ch_rpr = _coconut_case_match_to_2[1]  #                 match PILImage(mode,ch_rpr):
            if _coconut_case_match_check_2:  #                 match PILImage(mode,ch_rpr):
                base = "image,{_coconut_format_0},{_coconut_format_1}".format(_coconut_format_0=(mode), _coconut_format_1=(ch_rpr))  #                     base = f"image,{mode},{ch_rpr}"
        if not _coconut_case_match_check_2:  #             else:
            raise RuntimeError("cannot convert unknown imagedef:{_coconut_format_0} to str.".format(_coconut_format_0=(imdef)))  #                 raise RuntimeError(f"cannot convert unknown imagedef:{imdef} to str.")
        if "shape" in meta:  #             if "shape" in meta:
            shape_str = ":".join([str(s) for s in meta["shape"]])  #                 shape_str = ":".join([str(s) for s in meta["shape"]])
            res = base + "," + shape_str  #                 res =  base+","+shape_str
        else:  #             else:
            res = base  #                 res = base
#logger.info(f"imdef_to_str:{res}")
        return (res)  #             return res
    if not _coconut_case_match_check_3:  #     else:
        raise RuntimeError("cannot convert unknown imdef:{_coconut_format_0} to str.".format(_coconut_format_0=(imdef)))  #         raise RuntimeError(f"cannot convert unknown imdef:{imdef} to str.")
def cast_imdef_to_imdef_str(imdef):  # def cast_imdef_to_imdef_str(imdef):
    _coconut_case_match_to_4 = imdef  #     case imdef:
    _coconut_case_match_check_4 = False  #     case imdef:
    if (_coconut.isinstance(_coconut_case_match_to_4, ImageDef)) and (_coconut.len(_coconut_case_match_to_4) == 2):  #     case imdef:
        _coconut_case_match_check_4 = True  #     case imdef:
    if _coconut_case_match_check_4:  #     case imdef:
        res = [imdef2imdef_str(imdef), ]  #             res = [imdef2imdef_str(imdef)]
        return (res)  #             return res
    if not _coconut_case_match_check_4:  #     else:
        return (None)  #         return None

def imgs2tile_shape(shape, w=1024, h=1024, max_image=100, padding=1):  # def imgs2tile_shape(shape,w=1024,h=1024,max_image=100,padding=1):
    _coconut_case_match_to_5 = shape  #     case shape:
    _coconut_case_match_check_5 = False  #     case shape:
    _coconut_match_set_name_B = _coconut_sentinel  #     case shape:
    _coconut_match_set_name_H = _coconut_sentinel  #     case shape:
    _coconut_match_set_name_W = _coconut_sentinel  #     case shape:
    if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 3):  #     case shape:
        _coconut_match_set_name_B = _coconut_case_match_to_5[0]  #     case shape:
        _coconut_match_set_name_H = _coconut_case_match_to_5[1]  #     case shape:
        _coconut_match_set_name_W = _coconut_case_match_to_5[2]  #     case shape:
        _coconut_case_match_check_5 = True  #     case shape:
    if _coconut_case_match_check_5:  #     case shape:
        if _coconut_match_set_name_B is not _coconut_sentinel:  #     case shape:
            B = _coconut_case_match_to_5[0]  #     case shape:
        if _coconut_match_set_name_H is not _coconut_sentinel:  #     case shape:
            H = _coconut_case_match_to_5[1]  #     case shape:
        if _coconut_match_set_name_W is not _coconut_sentinel:  #     case shape:
            W = _coconut_case_match_to_5[2]  #     case shape:
    if _coconut_case_match_check_5:  #     case shape:
        ch = 1  #             ch = 1
    if not _coconut_case_match_check_5:  #         match (B,H,W,ch):
        _coconut_match_set_name_B = _coconut_sentinel  #         match (B,H,W,ch):
        _coconut_match_set_name_H = _coconut_sentinel  #         match (B,H,W,ch):
        _coconut_match_set_name_W = _coconut_sentinel  #         match (B,H,W,ch):
        _coconut_match_set_name_ch = _coconut_sentinel  #         match (B,H,W,ch):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 4):  #         match (B,H,W,ch):
            _coconut_match_set_name_B = _coconut_case_match_to_5[0]  #         match (B,H,W,ch):
            _coconut_match_set_name_H = _coconut_case_match_to_5[1]  #         match (B,H,W,ch):
            _coconut_match_set_name_W = _coconut_case_match_to_5[2]  #         match (B,H,W,ch):
            _coconut_match_set_name_ch = _coconut_case_match_to_5[3]  #         match (B,H,W,ch):
            _coconut_case_match_check_5 = True  #         match (B,H,W,ch):
        if _coconut_case_match_check_5:  #         match (B,H,W,ch):
            if _coconut_match_set_name_B is not _coconut_sentinel:  #         match (B,H,W,ch):
                B = _coconut_case_match_to_5[0]  #         match (B,H,W,ch):
            if _coconut_match_set_name_H is not _coconut_sentinel:  #         match (B,H,W,ch):
                H = _coconut_case_match_to_5[1]  #         match (B,H,W,ch):
            if _coconut_match_set_name_W is not _coconut_sentinel:  #         match (B,H,W,ch):
                W = _coconut_case_match_to_5[2]  #         match (B,H,W,ch):
            if _coconut_match_set_name_ch is not _coconut_sentinel:  #         match (B,H,W,ch):
                ch = _coconut_case_match_to_5[3]  #         match (B,H,W,ch):
        if _coconut_case_match_check_5:  #         match (B,H,W,ch):
            pass  #             pass
#nrow = int(sqrt(len(imgs[:max_image]))+0.5)
    if shape[0] is None:  #     if shape[0] is None:
# we cannot estimate actual shape.
        return ((None, None, ch))  #         return (None,None,ch)
    n_imgs = min(shape[0], max_image)  #     n_imgs = min(shape[0],max_image)
    nrow = int(sqrt(n_imgs))  #     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #     if (nrow*nrow < n_imgs):
        nrow += 1  #         nrow += 1
    r = int((w - ((nrow + 1) * padding)) / nrow)  # width/height of each tile  #     r = int((w-((nrow+1)*padding))/nrow) # width/height of each tile
    new_shape = (r * nrow, r * nrow, ch)  #     new_shape = (r*nrow,r*nrow,ch)
    return (new_shape)  #     return new_shape

ms_imgs2tile = (_coconut.functools.partial(_coconut.functools.partial, ss_to_ms))(imgs2tile_shape)  # ms_imgs2tile = imgs2tile_shape |> ss_to_ms$

def imgs2tile(imgs, w=1024, h=1024, max_image=100, padding=1):  # def imgs2tile(imgs,w=1024,h=1024,max_image=100,padding=1):
    mode = imgs[0].mode  #     mode = imgs[0].mode
    ch = len(mode)  #     ch = len(mode)
#nrow = int(sqrt(len(imgs[:max_image]))+0.5)
    n_imgs = len(imgs[:max_image])  #     n_imgs = len(imgs[:max_image])
    nrow = int(sqrt(n_imgs))  #     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #     if (nrow*nrow < n_imgs):
        nrow += 1  #         nrow += 1
    r = int((w - ((nrow + 1) * padding)) / nrow)  #     r = int((w-((nrow+1)*padding))/nrow)

    imgs = np.array([((np.array)(img.resize((r, r)))) for img in imgs[:max_image]])  #     imgs = np.array([(img.resize((r,r)) |> np.array) for img in imgs[:max_image]])
    if ch == 1:  #     if ch == 1:
        imgs = imgs[:, :, :, None]  #         imgs = imgs[:,:,:,None]
    return (make_grid(imgs, nrow, padding=padding))  #     return make_grid(imgs,nrow,padding=padding)

def rule_imgs2tile(state):  # def rule_imgs2tile(state):
    _coconut_case_match_to_6 = state  #     case state:
    _coconut_case_match_check_6 = False  #     case state:
    _coconut_match_set_name_mode = _coconut_sentinel  #     case state:
    _coconut_match_set_name_chrpr = _coconut_sentinel  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_6, ImageDef)) and (_coconut.len(_coconut_case_match_to_6) == 2) and (_coconut.isinstance(_coconut_case_match_to_6[0], PILImages)) and (_coconut.len(_coconut_case_match_to_6[0]) == 2):  #     case state:
        _coconut_match_set_name_mode = _coconut_case_match_to_6[0][0]  #     case state:
        _coconut_match_set_name_chrpr = _coconut_case_match_to_6[0][1]  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_6[1]  #     case state:
        _coconut_case_match_check_6 = True  #     case state:
    if _coconut_case_match_check_6:  #     case state:
        if _coconut_match_set_name_mode is not _coconut_sentinel:  #     case state:
            mode = _coconut_case_match_to_6[0][0]  #     case state:
        if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #     case state:
            chrpr = _coconut_case_match_to_6[0][1]  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_6[1]  #     case state:
    if _coconut_case_match_check_6:  #     case state:
        return ([(imgs2tile, ImageDef(Numpy("uint8", "HWC", chrpr, VR_0_255), (ms_imgs2tile)(meta)), "imgs2tile", 10), ])  #             return [(

# todo
def batch_to_tiled(ary, max_size=1024, padding=1):  # def batch_to_tiled(ary,max_size=1024,padding=1):
# ary shape == (B,H,W,C)
    w = ary.shape[2]  #     w = ary.shape[2]
    n_imgs = min((max_size // w)**2, ary.shape[0])  #     n_imgs = min((max_size//w)**2,ary.shape[0])
    ary = ary[:n_imgs]  #     ary = ary[:n_imgs]
    nrow = int(sqrt(n_imgs))  #     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #     if (nrow*nrow < n_imgs):
        nrow += 1  #         nrow += 1
    return (make_grid(ary, nrow, padding=padding))  #     return make_grid(ary,nrow,padding=padding)
def batch_to_tiled_shape_shift(shape, max_size=1024, padding=1):  # def batch_to_tiled_shape_shift(shape,max_size=1024,padding=1):
    b, h, w, c = shape  #     b,h,w,c = shape
    if b is None:  #     if b is None:
        return ((None, None, c))  #         return (None,None,c)
    if w is None:  #     if w is None:
        return ((None, None, c))  #         return (None,None,c)
    n_imgs = min((max_size // w)**2, shape[0])  #     n_imgs = min((max_size//w)**2,shape[0])
#n_imgs = min(max_size//w,b.shape[0])
    nrow = int(sqrt(n_imgs))  #     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #     if (nrow*nrow < n_imgs):
        nrow += 1  #         nrow += 1
    r = int((w - ((nrow + 1) * padding)) / nrow)  # width/height of each tile  #     r = int((w-((nrow+1)*padding))/nrow) # width/height of each tile
    nh = (nrow - 1) * padding + nrow * h  #     nh = (nrow-1)*padding + nrow*h
    nw = (nrow - 1) * padding + nrow * w  #     nw = (nrow-1)*padding + nrow*w
    new_shape = (nh, nw, c)  #     new_shape = (nh,nw,c)
    return (new_shape)  #     return new_shape
ms_batch_to_tiled = (_coconut.functools.partial(_coconut.functools.partial, ss_to_ms))(batch_to_tiled_shape_shift)  # ms_batch_to_tiled = batch_to_tiled_shape_shift |> ss_to_ms$
def rule_batch_to_tiled(state):  # def rule_batch_to_tiled(state):
    _coconut_case_match_to_7 = state  #     case state:
    _coconut_case_match_check_7 = False  #     case state:
    _coconut_match_set_name_dt = _coconut_sentinel  #     case state:
    _coconut_match_set_name_chrpr = _coconut_sentinel  #     case state:
    _coconut_match_set_name_vr = _coconut_sentinel  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_7, ImageDef)) and (_coconut.len(_coconut_case_match_to_7) == 2) and (_coconut.isinstance(_coconut_case_match_to_7[0], Numpy)) and (_coconut.len(_coconut_case_match_to_7[0]) == 4) and (_coconut_case_match_to_7[0][1] == "BHWC"):  #     case state:
        _coconut_match_set_name_dt = _coconut_case_match_to_7[0][0]  #     case state:
        _coconut_match_set_name_chrpr = _coconut_case_match_to_7[0][2]  #     case state:
        _coconut_match_set_name_vr = _coconut_case_match_to_7[0][3]  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_7[1]  #     case state:
        _coconut_case_match_check_7 = True  #     case state:
    if _coconut_case_match_check_7:  #     case state:
        if _coconut_match_set_name_dt is not _coconut_sentinel:  #     case state:
            dt = _coconut_case_match_to_7[0][0]  #     case state:
        if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #     case state:
            chrpr = _coconut_case_match_to_7[0][2]  #     case state:
        if _coconut_match_set_name_vr is not _coconut_sentinel:  #     case state:
            vr = _coconut_case_match_to_7[0][3]  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_7[1]  #     case state:
    if _coconut_case_match_check_7:  #     case state:
        return ([(batch_to_tiled, ImageDef(Numpy(dt, "HWC", chrpr, vr), ms_batch_to_tiled(meta)), "numpy bhwc to hwc by tiling", 20), ])  #             return [(

def rule_img2widget(state):  # def rule_img2widget(state):
    _coconut_case_match_to_8 = state  #     case state:
    _coconut_case_match_check_8 = False  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_8, ImageDef)) and (_coconut.len(_coconut_case_match_to_8) == 2) and (_coconut.isinstance(_coconut_case_match_to_8[0], PILImage)) and (_coconut.len(_coconut_case_match_to_8[0]) == 2):  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_8[1]  #     case state:
        _coconut_case_match_check_8 = True  #     case state:
    if _coconut_case_match_check_8:  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_8[1]  #     case state:
    if _coconut_case_match_check_8:  #     case state:
        return ([(infer_widget, "widget", "infer_widget", 1), ])  #             return [(

def dict2imdef(state):  # def dict2imdef(state):
    if isinstance(state, Mapping):  #     if isinstance(state,Mapping):
        _coconut_case_match_to_9 = state  #         case state:
        _coconut_case_match_check_9 = False  #         case state:
        _coconut_match_set_name__dtype = _coconut_sentinel  #         case state:
        _coconut_match_set_name__arng = _coconut_sentinel  #         case state:
        _coconut_match_set_name__ch_rpr = _coconut_sentinel  #         case state:
        _coconut_match_set_name__v_range = _coconut_sentinel  #         case state:
        _coconut_match_set_name_meta = _coconut_sentinel  #         case state:
        if (_coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_9) == 6):  #         case state:
            _coconut_match_temp_0 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #         case state:
            _coconut_match_temp_1 = _coconut_case_match_to_9.get("dtype", _coconut_sentinel)  #         case state:
            _coconut_match_temp_2 = _coconut_case_match_to_9.get("arrange", _coconut_sentinel)  #         case state:
            _coconut_match_temp_3 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #         case state:
            _coconut_match_temp_4 = _coconut_case_match_to_9.get("v_range", _coconut_sentinel)  #         case state:
            _coconut_match_temp_5 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #         case state:
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_5 is not _coconut_sentinel):  #         case state:
                _coconut_match_set_name__dtype = _coconut_match_temp_1  #         case state:
                _coconut_match_set_name__arng = _coconut_match_temp_2  #         case state:
                _coconut_match_set_name__ch_rpr = _coconut_match_temp_3  #         case state:
                _coconut_match_set_name__v_range = _coconut_match_temp_4  #         case state:
                _coconut_match_set_name_meta = _coconut_match_temp_5  #         case state:
                _coconut_case_match_check_9 = True  #         case state:
        if _coconut_case_match_check_9:  #         case state:
            if _coconut_match_set_name__dtype is not _coconut_sentinel:  #         case state:
                _dtype = _coconut_match_temp_1  #         case state:
            if _coconut_match_set_name__arng is not _coconut_sentinel:  #         case state:
                _arng = _coconut_match_temp_2  #         case state:
            if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #         case state:
                _ch_rpr = _coconut_match_temp_3  #         case state:
            if _coconut_match_set_name__v_range is not _coconut_sentinel:  #         case state:
                _v_range = _coconut_match_temp_4  #         case state:
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #         case state:
                meta = _coconut_match_temp_5  #         case state:
        if _coconut_case_match_check_9:  #         case state:
            return ([ImageDef(Numpy(_dtype, _arng, _ch_rpr, _v_range), meta), ])  #                 return [ImageDef(Numpy(_dtype,_arng,_ch_rpr,_v_range),meta)]
        if not _coconut_case_match_check_9:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__dtype = _coconut_sentinel  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__arng = _coconut_sentinel  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__ch_rpr = _coconut_sentinel  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__v_range = _coconut_sentinel  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            if (_coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_9) == 6):  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_0 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_1 = _coconut_case_match_to_9.get("dtype", _coconut_sentinel)  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_2 = _coconut_case_match_to_9.get("arrange", _coconut_sentinel)  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_3 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_4 = _coconut_case_match_to_9.get("v_range", _coconut_sentinel)  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_5 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_5 is not _coconut_sentinel):  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__dtype = _coconut_match_temp_1  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__arng = _coconut_match_temp_2  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__ch_rpr = _coconut_match_temp_3  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__v_range = _coconut_match_temp_4  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_5  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_case_match_check_9 = True  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            if _coconut_case_match_check_9:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__dtype is not _coconut_sentinel:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _dtype = _coconut_match_temp_1  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__arng is not _coconut_sentinel:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _arng = _coconut_match_temp_2  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _ch_rpr = _coconut_match_temp_3  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__v_range is not _coconut_sentinel:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _v_range = _coconut_match_temp_4  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    meta = _coconut_match_temp_5  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            if _coconut_case_match_check_9:  #             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                return ([ImageDef(Torch(_dtype, _arng, _ch_rpr, _v_range), meta), ])  #                 return [ImageDef(Torch(_dtype,_arng,_ch_rpr,_v_range),meta)]
        if not _coconut_case_match_check_9:  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__mode = _coconut_sentinel  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__ch_rpr = _coconut_sentinel  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if (_coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_9) == 4):  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_0 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_1 = _coconut_case_match_to_9.get("mode", _coconut_sentinel)  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_2 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_3 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "image") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel):  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__mode = _coconut_match_temp_1  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__ch_rpr = _coconut_match_temp_2  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_3  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_case_match_check_9 = True  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__mode is not _coconut_sentinel:  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _mode = _coconut_match_temp_1  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _ch_rpr = _coconut_match_temp_2  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    meta = _coconut_match_temp_3  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                return ([ImageDef(PILImage(_mode, _ch_rpr), meta), ])  #                 return [ImageDef(PILImage(_mode,_ch_rpr),meta)]
        if not _coconut_case_match_check_9:  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__mode = _coconut_sentinel  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__ch_rpr = _coconut_sentinel  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if (_coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_9) == 4):  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_0 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_1 = _coconut_case_match_to_9.get("mode", _coconut_sentinel)  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_2 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_3 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "images") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel):  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__mode = _coconut_match_temp_1  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__ch_rpr = _coconut_match_temp_2  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_3  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_case_match_check_9 = True  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__mode is not _coconut_sentinel:  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _mode = _coconut_match_temp_1  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _ch_rpr = _coconut_match_temp_2  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    meta = _coconut_match_temp_3  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                return ([ImageDef(PILImages(_mode, _ch_rpr), meta), ])  #                 return [ImageDef(PILImages(_mode,_ch_rpr),meta)]

def rule_numpy2img(state):  # def rule_numpy2img(state):
    if isinstance(state, Mapping):  #     if isinstance(state,Mapping):
        _coconut_case_match_to_10 = state  #         case state:
        _coconut_case_match_check_10 = False  #         case state:
        _coconut_match_set_name_cr = _coconut_sentinel  #         case state:
        _coconut_match_set_name_meta = _coconut_sentinel  #         case state:
        if (_coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_10) == 6):  #         case state:
            _coconut_match_temp_0 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #         case state:
            _coconut_match_temp_1 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #         case state:
            _coconut_match_temp_2 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #         case state:
            _coconut_match_temp_3 = _coconut_case_match_to_10.get("arrange", _coconut_sentinel)  #         case state:
            _coconut_match_temp_4 = _coconut_case_match_to_10.get("v_range", _coconut_sentinel)  #         case state:
            _coconut_match_temp_5 = _coconut_case_match_to_10.get("meta", _coconut_sentinel)  #         case state:
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "uint8") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "HWC") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "0_255") and (_coconut_match_temp_5 is not _coconut_sentinel):  #         case state:
                _coconut_match_set_name_cr = _coconut_match_temp_2  #         case state:
                _coconut_match_set_name_meta = _coconut_match_temp_5  #         case state:
                _coconut_case_match_check_10 = True  #         case state:
        if _coconut_case_match_check_10:  #         case state:
            _coconut_case_match_check_10 = False  #         case state:
            if (_coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_10) == 6):  #         case state:
                _coconut_match_temp_0 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #         case state:
                _coconut_match_temp_1 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #         case state:
                _coconut_match_temp_2 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #         case state:
                if (not _coconut_case_match_check_10) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "uint8") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "RGB"):  #         case state:
                    _coconut_match_set_name_cr = _coconut_match_temp_2  #         case state:
                    _coconut_case_match_check_10 = True  #         case state:
            if (_coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_10) == 6):  #         case state:
                _coconut_match_temp_0 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #         case state:
                _coconut_match_temp_1 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #         case state:
                _coconut_match_temp_2 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #         case state:
                if (not _coconut_case_match_check_10) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "uint8") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "RGBA"):  #         case state:
                    _coconut_match_set_name_cr = _coconut_match_temp_2  #         case state:
                    _coconut_case_match_check_10 = True  #         case state:
            if (_coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_10) == 6):  #         case state:
                _coconut_match_temp_0 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #         case state:
                _coconut_match_temp_1 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #         case state:
                _coconut_match_temp_2 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #         case state:
                if (not _coconut_case_match_check_10) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "uint8") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "YCbCr"):  #         case state:
                    _coconut_match_set_name_cr = _coconut_match_temp_2  #         case state:
                    _coconut_case_match_check_10 = True  #         case state:

        if _coconut_case_match_check_10:  #         case state:
            if _coconut_match_set_name_cr is not _coconut_sentinel:  #         case state:
                cr = _coconut_match_temp_2  #         case state:
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #         case state:
                meta = _coconut_match_temp_5  #         case state:
        if _coconut_case_match_check_10:  #         case state:
            return ([(Image.fromarray, ImageDef(PILImage(cr, cr), meta), "Image.fromarray", 1), ])  #                 return [(
        if not _coconut_case_match_check_10:  #                     Image.fromarray,
            _coconut_match_set_name_meta = _coconut_sentinel  #                     Image.fromarray,
            if (_coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_10) == 6):  #                     Image.fromarray,
                _coconut_match_temp_0 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #                     Image.fromarray,
                _coconut_match_temp_1 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #                     Image.fromarray,
                _coconut_match_temp_2 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #                     Image.fromarray,
                _coconut_match_temp_3 = _coconut_case_match_to_10.get("arrange", _coconut_sentinel)  #                     Image.fromarray,
                _coconut_match_temp_4 = _coconut_case_match_to_10.get("v_range", _coconut_sentinel)  #                     Image.fromarray,
                _coconut_match_temp_5 = _coconut_case_match_to_10.get("meta", _coconut_sentinel)  #                     Image.fromarray,
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "uint8") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "L") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "HW") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "0_255") and (_coconut_match_temp_5 is not _coconut_sentinel):  #                     Image.fromarray,
                    _coconut_match_set_name_meta = _coconut_match_temp_5  #                     Image.fromarray,
                    _coconut_case_match_check_10 = True  #                     Image.fromarray,
            if _coconut_case_match_check_10:  #                     Image.fromarray,
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #                     Image.fromarray,
                    meta = _coconut_match_temp_5  #                     Image.fromarray,
            if _coconut_case_match_check_10:  #                     Image.fromarray,
                return ([(Image.fromarray, ImageDef(PILImage("L", "L"), meta), "Image.fromarray", 1), ])  #                 return [(

def rule_image_path_to_image(state):  # def rule_image_path_to_image(state):
    if isinstance(state, str) and state == "image_path":  #     if isinstance(state,str) and state == "image_path":
        return ([(lambda p: Image.open(p).convert("RGB"), "image,RGB,RGB", "PIL.open ..> .convert('RGB')", 1), ])  #        return [

def rule_format(state):  # def rule_format(state):
    if hasattr(state, "__neighbors__"):  #     if hasattr(state,"__neighbors__"):
        ngs = state.__neighbors__()  #         ngs = state.__neighbors__()
        if not isinstance(ngs, list):  #         if not isinstance(ngs,list):
            ngs = [ngs, ]  #             ngs = [ngs]
        return (ngs)  #         return ngs

def to_spectral_img(img: '"PIL.Image.Image"'):  # def to_spectral_img(img:"PIL.Image.Image"):
#gray_img = img.convert('L')
# NumPy 配列にする
    f_xy = np.asarray(img)  #     f_xy = np.asarray(img)

# 2 次元高速フーリエ変換で周波数領域の情報を取り出す
    f_uv = np.fft.fft2(f_xy)  #     f_uv = np.fft.fft2(f_xy)
# 画像の中心に低周波数の成分がくるように並べかえる
    shifted_f_uv = np.fft.fftshift(f_uv)  #     shifted_f_uv = np.fft.fftshift(f_uv)

# パワースペクトルに変換する
    magnitude_spectrum2d = 20 * np.log(np.absolute(shifted_f_uv))  #     magnitude_spectrum2d = 20 * np.log(np.absolute(shifted_f_uv))
    return (magnitude_spectrum2d)  #     return magnitude_spectrum2d
#return auto("numpy,float64,HW,L,None")(magnitude_spectrum2d)

def rule_to_spectrum(state):  # def rule_to_spectrum(state):
    if state == "image,L,L":  #     if state == "image,L,L":
        return ([(to_spectral_img, "spectrum", "image,L,L => spectrum", 1), ])  #         return [(

ms_img2L = (_coconut.functools.partial(_coconut.functools.partial, ss_to_ms))((lambda s: (s[0], s[1])))  # ms_img2L = (s->(s[0],s[1])) |> ss_to_ms$
ms_img2LA = (_coconut.functools.partial(_coconut.functools.partial, ss_to_ms))((lambda s: (s[0], s[1], 2)))  # ms_img2LA = (s->(s[0],s[1],2)) |> ss_to_ms$
def rule_image2gray(state):  # def rule_image2gray(state):
    _coconut_case_match_to_11 = state  #     case state:
    _coconut_case_match_check_11 = False  #     case state:
    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #     case state:
    _coconut_match_set_name_ch_rpr2 = _coconut_sentinel  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)) and (_coconut.len(_coconut_case_match_to_11) == 2) and (_coconut.isinstance(_coconut_case_match_to_11[0], PILImage)) and (_coconut.len(_coconut_case_match_to_11[0]) == 2):  #     case state:
        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_11[0][0]  #     case state:
        _coconut_match_set_name_ch_rpr2 = _coconut_case_match_to_11[0][1]  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_11[1]  #     case state:
        _coconut_case_match_check_11 = True  #     case state:
    if _coconut_case_match_check_11:  #     case state:
        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #     case state:
            ch_rpr = _coconut_case_match_to_11[0][0]  #     case state:
        if _coconut_match_set_name_ch_rpr2 is not _coconut_sentinel:  #     case state:
            ch_rpr2 = _coconut_case_match_to_11[0][1]  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_11[1]  #     case state:
    if _coconut_case_match_check_11:  #     case state:
        return ([(_coconut.operator.methodcaller("convert", "L"), ImageDef(PILImage("L", "L"), (ms_img2L)(meta)), "image2gray", 10), (_coconut.operator.methodcaller("convert", "LA"), ImageDef(PILImage("LA", "LA"), (ms_img2LA)(meta)), "image2gray-alpha", 10)])  #             return [

def rule_image2lab(state):  # def rule_image2lab(state):
    from skimage import color  #     from skimage import color
    _coconut_case_match_to_12 = state  #     case state:
    _coconut_case_match_check_12 = False  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)) and (_coconut.len(_coconut_case_match_to_12) == 2) and (_coconut.isinstance(_coconut_case_match_to_12[0], Numpy)) and (_coconut.len(_coconut_case_match_to_12[0]) == 4) and (_coconut_case_match_to_12[0][0] == "float64") and (_coconut_case_match_to_12[0][1] == "HWC") and (_coconut_case_match_to_12[0][2] == "RGB") and (_coconut_case_match_to_12[0][3] == "0_1"):  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_12[1]  #     case state:
        _coconut_case_match_check_12 = True  #     case state:
    if _coconut_case_match_check_12:  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_12[1]  #     case state:
    if _coconut_case_match_check_12:  #     case state:
        return ([(color.rgb2lab, ImageDef(Numpy("float64", "HWC", "LAB", "LAB"), meta), "sklearn.color.rgb2lab"), ])  #             return [
    if not _coconut_case_match_check_12:  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
        _coconut_match_set_name_meta = _coconut_sentinel  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
        if (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)) and (_coconut.len(_coconut_case_match_to_12) == 2) and (_coconut.isinstance(_coconut_case_match_to_12[0], Numpy)) and (_coconut.len(_coconut_case_match_to_12[0]) == 4) and (_coconut_case_match_to_12[0][0] == "float64") and (_coconut_case_match_to_12[0][1] == "HWC") and (_coconut_case_match_to_12[0][2] == "LAB") and (_coconut_case_match_to_12[0][3] == "LAB"):  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
            _coconut_match_set_name_meta = _coconut_case_match_to_12[1]  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
            _coconut_case_match_check_12 = True  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
        if _coconut_case_match_check_12:  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
                meta = _coconut_case_match_to_12[1]  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
        if _coconut_case_match_check_12:  #                 (color.rgb2lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"sklearn.color.rgb2lab")
            return ([(color.lab2rgb, ImageDef(Numpy("float64", "HWC", "RGB", "0_1"), meta), "sklearn.color.lab2rgb"), ])  #             return [

def convert_ignore_channel(ary, f):  # def convert_ignore_channel(ary,f):
    """
    shape:(H,W,C)
    """  #     """
    ignored = ary[:, :, [-1, ]]  #     ignored = ary[:,:,[-1]]
    tgt = ary[:, :, :-1]  #     tgt = ary[:,:,:-1]
    converted = f(tgt)  #     converted = f(tgt)
    result = np.concatenate((tgt, ignored), axis=-1)  #     result = np.concatenate((tgt,ignored),axis=-1)
    return (result)  #     return result

def rule_rgba2laba(state):  # def rule_rgba2laba(state):
    from skimage import color  #     from skimage import color
    _coconut_case_match_to_13 = state  #     case state:
    _coconut_case_match_check_13 = False  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_13, ImageDef)) and (_coconut.len(_coconut_case_match_to_13) == 2) and (_coconut.isinstance(_coconut_case_match_to_13[0], Numpy)) and (_coconut.len(_coconut_case_match_to_13[0]) == 4) and (_coconut_case_match_to_13[0][0] == "float64") and (_coconut_case_match_to_13[0][1] == "HWC") and (_coconut_case_match_to_13[0][2] == "RGBA") and (_coconut_case_match_to_13[0][3] == "0_1"):  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_13[1]  #     case state:
        _coconut_case_match_check_13 = True  #     case state:
    if _coconut_case_match_check_13:  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_13[1]  #     case state:
    if _coconut_case_match_check_13:  #     case state:
        return ([(lambda a: convert_ignore_channel(a, color.rgb2lab), ImageDef(Numpy("float64", "HWC", "LABA", "LABA"), meta), "rgba2laba (ignores alpha)"), ])  #             return [
    if not _coconut_case_match_check_13:  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
        _coconut_match_set_name_meta = _coconut_sentinel  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
        if (_coconut.isinstance(_coconut_case_match_to_13, ImageDef)) and (_coconut.len(_coconut_case_match_to_13) == 2) and (_coconut.isinstance(_coconut_case_match_to_13[0], Numpy)) and (_coconut.len(_coconut_case_match_to_13[0]) == 4) and (_coconut_case_match_to_13[0][0] == "float64") and (_coconut_case_match_to_13[0][1] == "HWC") and (_coconut_case_match_to_13[0][2] == "LABA") and (_coconut_case_match_to_13[0][3] == "LABA"):  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
            _coconut_match_set_name_meta = _coconut_case_match_to_13[1]  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
            _coconut_case_match_check_13 = True  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
        if _coconut_case_match_check_13:  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
                meta = _coconut_case_match_to_13[1]  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
        if _coconut_case_match_check_13:  #                 (a->convert_ignore_channel(a,color.rgb2lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"rgba2laba (ignores alpha)")
            return ([(lambda a: convert_ignore_channel(a, color.lab2rgb), ImageDef(Numpy("float64", "HWC", "RGBA", "0_1"), meta), "laba2rgba (ignores alpha)"), ])  #             return [


def rule_lab_value_conversion(state):  # def rule_lab_value_conversion(state):
    _coconut_case_match_to_14 = state  #     case state:
    _coconut_case_match_check_14 = False  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) == 2) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) == 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LAB") and (_coconut_case_match_to_14[0][3] == "LAB"):  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #     case state:
        _coconut_case_match_check_14 = True  #     case state:
    if _coconut_case_match_check_14:  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_14[1]  #     case state:
    if _coconut_case_match_check_14:  #     case state:
        return ([((_vr_lab_to_0_1, ImageDef(Numpy("float64", "HWC", "LAB", "0_1"), meta), "vr_lab_to_0_1")), ])  #             return [((_vr_lab_to_0_1,ImageDef(Numpy("float64","HWC","LAB","0_1"),meta),"vr_lab_to_0_1"))]
    if not _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        _coconut_match_set_name_meta = _coconut_sentinel  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        if (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) == 2) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) == 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LABA") and (_coconut_case_match_to_14[0][3] == "LABA"):  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            _coconut_case_match_check_14 = True  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        if _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                meta = _coconut_case_match_to_14[1]  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        if _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            return ([((lambda a: convert_ignore_channel(a, _vr_lab_to_0_1), ImageDef(Numpy("float64", "HWC", "LABA", "0_1"), meta), "vr_laba_to_0_1")), ])  #             return [((a->convert_ignore_channel(a,_vr_lab_to_0_1),ImageDef(Numpy("float64","HWC","LABA","0_1"),meta),"vr_laba_to_0_1"))]
    if not _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        _coconut_match_set_name_meta = _coconut_sentinel  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        if (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) == 2) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) == 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LAB") and (_coconut_case_match_to_14[0][3] == "0_1"):  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            _coconut_case_match_check_14 = True  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        if _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                meta = _coconut_case_match_to_14[1]  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        if _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            return ([((_0_1_to_vr_lab, ImageDef(Numpy("float64", "HWC", "LAB", "LAB"), meta), "0_1_to_vr_lab")), ])  #             return [((_0_1_to_vr_lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"0_1_to_vr_lab"))]
    if not _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        _coconut_match_set_name_meta = _coconut_sentinel  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        if (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) == 2) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) == 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LABA") and (_coconut_case_match_to_14[0][3] == "0_1"):  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            _coconut_case_match_check_14 = True  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        if _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                meta = _coconut_case_match_to_14[1]  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        if _coconut_case_match_check_14:  #         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            return ([((lambda a: convert_ignore_channel(a, _0_1_to_vr_lab), ImageDef(Numpy("float64", "HWC", "LABA", "LABA"), meta), "vr_0_1_to_laba")), ])  #             return [((a->convert_ignore_channel(a,_0_1_to_vr_lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"vr_0_1_to_laba"))]

def _vr_lab_to_0_1(ary):  # def _vr_lab_to_0_1(ary):
    r = ary.copy()  #     r = ary.copy()
    r[:, :, 0] = ary[:, :, 0] * 0.01  #     r[:,:,0] = ary[:,:,0] * 0.01
    r[:, :, 1] = (ary[:, :, 1] + 128.0) / 255.0  #     r[:,:,1] = (ary[:,:,1] + 128.0) / 255.0
    r[:, :, 2] = (ary[:, :, 2] + 128.0) / 255.0  #     r[:,:,2] = (ary[:,:,2] + 128.0) / 255.0
    return (r)  #     return r

def _0_1_to_vr_lab(ary):  # def _0_1_to_vr_lab(ary):
    r = ary.copy()  #     r = ary.copy()
    r[:, :, 0] = ary[:, :, 0] * 100  #     r[:,:,0] = ary[:,:,0] * 100
    r[:, :, 1] = (ary[:, :, 1] * 255) - 128.0  #     r[:,:,1] = (ary[:,:,1] * 255) - 128.0
    r[:, :, 2] = (ary[:, :, 2] * 255) - 128.0  #     r[:,:,2] = (ary[:,:,2] * 255) - 128.0
    return (r)  #     return r

class AutoTuple(_coconut.collections.namedtuple("AutoTuple", ('formats',))):  # data AutoTuple(formats is tuple)
    __slots__ = ()  # data AutoTuple(formats is tuple)
    __ne__ = _coconut.object.__ne__  # data AutoTuple(formats is tuple)
    def __eq__(self, other):  # data AutoTuple(formats is tuple)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  # data AutoTuple(formats is tuple)
    def __hash__(self):  # data AutoTuple(formats is tuple)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  # data AutoTuple(formats is tuple)
    __match_args__ = ('formats',)  # data AutoTuple(formats is tuple)
    def __new__(_coconut_cls, *_coconut_match_args, **_coconut_match_kwargs):  # data AutoTuple(formats is tuple)
        _coconut_match_check_0 = False  # data AutoTuple(formats is tuple)
        _coconut_match_set_name_formats = _coconut_sentinel  # data AutoTuple(formats is tuple)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  # data AutoTuple(formats is tuple)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "formats" in _coconut_match_kwargs)) == 1):  # data AutoTuple(formats is tuple)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("formats")  # data AutoTuple(formats is tuple)
            if (_coconut.isinstance(_coconut_match_temp_0, tuple)) and (not _coconut_match_kwargs):  # data AutoTuple(formats is tuple)
                _coconut_match_set_name_formats = _coconut_match_temp_0  # data AutoTuple(formats is tuple)
                _coconut_match_check_0 = True  # data AutoTuple(formats is tuple)
        if _coconut_match_check_0:  # data AutoTuple(formats is tuple)
            if _coconut_match_set_name_formats is not _coconut_sentinel:  # data AutoTuple(formats is tuple)
                formats = _coconut_match_temp_0  # data AutoTuple(formats is tuple)

        if not _coconut_match_check_0:  # data AutoTuple(formats is tuple)
            raise _coconut_FunctionMatchError('data AutoTuple(formats is tuple)', _coconut_match_args)  # data AutoTuple(formats is tuple)

        return _coconut.tuple.__new__(_coconut_cls, (formats, ))  # data AutoTuple(formats is tuple)



_coconut_call_set_names(AutoTuple)  # def isnamedtuple(x):
def isnamedtuple(x):  # def isnamedtuple(x):
    t = type(x)  #     t = type(x)
    b = t.__bases__  #     b = t.__bases__
    if hasattr(x, "__slots__"):  #     if hasattr(x,"__slots__"): return True
        return (True)  #     if hasattr(x,"__slots__"): return True
    if len(b) != 1 or b[0] != tuple:  #     if len(b) != 1 or b[0] != tuple: return False
        return (False)  #     if len(b) != 1 or b[0] != tuple: return False
    f = getattr(t, '_fields', None)  #     f = getattr(t, '_fields', None)
    if not isinstance(f, tuple):  #     if not isinstance(f, tuple): return False
        return (False)  #     if not isinstance(f, tuple): return False
    return (all((type(n) == str for n in f)))  #     return all(type(n)==str for n in f)

def cast_tuple2auto_tuple(state):  # def cast_tuple2auto_tuple(state):
    if isinstance(state, str):  #     if isinstance(state,str):
        return (None)  #         return None
    if isinstance(state, AutoTuple):  #     if isinstance(state,AutoTuple):
        res = [state.formats, ]  #         res = [state.formats]
        return (res)  #         return res
    elif type(state) == tuple:  #     elif type(state) == tuple:
        res = [AutoTuple(state), ]  #         res = [AutoTuple(state)]
        return (res)  #         return res

def map_tuple_i(t, i, f):  # def map_tuple_i(t,i,f):
    res = list(t)  #     res = list(t)
    res[i] = f(res[i])  #     res[i] = f(res[i])
    return (tuple(res))  #     return tuple(res)

def map_state(states, i, new_state):  # def map_state(states,i,new_state):
    res = list(states)  #     res = list(states)
    res[i] = new_state  #     res[i] = new_state
    return (tuple(res))  #     return tuple(res)


def map_each(t, mappers):  # def map_each(t,mappers):
#logger.warning(f"items:{t}")
#logger.warning(f"mappers:{mappers}")
    return (tuple([f(item) for f, item in zip(mappers, t)]))  #     return tuple([f(item) for f,item in zip(mappers,t)])


class AutoList(_coconut.collections.namedtuple("AutoList", ('state',))):  # data AutoList(state):
    __slots__ = ()  # data AutoList(state):
    __ne__ = _coconut.object.__ne__  # data AutoList(state):
    def __eq__(self, other):  # data AutoList(state):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  # data AutoList(state):
    def __hash__(self):  # data AutoList(state):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  # data AutoList(state):
    __match_args__ = ('state',)  # data AutoList(state):
    def __repr__(self):  #     def __repr__(self):
        return ("[{_coconut_format_0}]".format(_coconut_format_0=(self.state)))  #         return f"[{self.state}]"



_coconut_call_set_names(AutoList)  # def cast_ary_str_to_ary_type(state):
def cast_ary_str_to_ary_type(state):  # def cast_ary_str_to_ary_type(state):
    _coconut_case_match_to_15 = state  #     case state:
    _coconut_case_match_check_15 = False  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_15, _coconut.str)) and (_coconut_case_match_to_15.startswith("[")) and (_coconut_case_match_to_15.endswith("]")):  #     case state:
        element_state = _coconut_case_match_to_15[1:-1]  #     case state:
        _coconut_case_match_check_15 = True  #     case state:
    if _coconut_case_match_check_15:  #     case state:
        return ([AutoList(element_state), ])  #             return [AutoList(element_state)]
    if not _coconut_case_match_check_15:  #         match AutoList(es is str):
        _coconut_match_set_name_es = _coconut_sentinel  #         match AutoList(es is str):
        if (_coconut.isinstance(_coconut_case_match_to_15, AutoList)) and (_coconut.len(_coconut_case_match_to_15) == 1) and (_coconut.isinstance(_coconut_case_match_to_15[0], str)):  #         match AutoList(es is str):
            _coconut_match_set_name_es = _coconut_case_match_to_15[0]  #         match AutoList(es is str):
            _coconut_case_match_check_15 = True  #         match AutoList(es is str):
        if _coconut_case_match_check_15:  #         match AutoList(es is str):
            if _coconut_match_set_name_es is not _coconut_sentinel:  #         match AutoList(es is str):
                es = _coconut_case_match_to_15[0]  #         match AutoList(es is str):
        if _coconut_case_match_check_15:  #         match AutoList(es is str):
            return (["[{_coconut_format_0}]".format(_coconut_format_0=(es)), ])  #             return [f"[{es}]"]

#shape change!
ms_add_None_b_ch = (_coconut.functools.partial(_coconut.functools.partial, ss_to_ms))((lambda s: (None, *s)))  # ms_add_None_b_ch = (s->(None,*s)) |> ss_to_ms$
"adds 1 as batch shape"  # "adds 1 as batch shape"
ms_del_b_ch = (_coconut.functools.partial(_coconut.functools.partial, ss_to_ms))((lambda s: s[1:]))  # ms_del_b_ch = (s->s[1:])  |> ss_to_ms$
# TODO preserve length in AutoList
def img_list_is_imgs(state):  # def img_list_is_imgs(state):
    _coconut_case_match_to_16 = state  #     case state:
    _coconut_case_match_check_16 = False  #     case state:
    _coconut_match_set_name_m1 = _coconut_sentinel  #     case state:
    _coconut_match_set_name_m2 = _coconut_sentinel  #     case state:
    _coconut_match_set_name_meta = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_16, AutoList)) and (_coconut.len(_coconut_case_match_to_16) == 1) and (_coconut.isinstance(_coconut_case_match_to_16[0], ImageDef)) and (_coconut.len(_coconut_case_match_to_16[0]) == 2) and (_coconut.isinstance(_coconut_case_match_to_16[0][0], PILImage)) and (_coconut.len(_coconut_case_match_to_16[0][0]) == 2):  #     case state:
        _coconut_match_set_name_m1 = _coconut_case_match_to_16[0][0][0]  #     case state:
        _coconut_match_set_name_m2 = _coconut_case_match_to_16[0][0][1]  #     case state:
        _coconut_match_set_name_meta = _coconut_case_match_to_16[0][1]  #     case state:
        _coconut_case_match_check_16 = True  #     case state:
    if _coconut_case_match_check_16:  #     case state:
        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #     case state:
            m1 = _coconut_case_match_to_16[0][0][0]  #     case state:
        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #     case state:
            m2 = _coconut_case_match_to_16[0][0][1]  #     case state:
        if _coconut_match_set_name_meta is not _coconut_sentinel:  #     case state:
            meta = _coconut_case_match_to_16[0][1]  #     case state:
    if _coconut_case_match_check_16:  #     case state:
        return ([ImageDef(PILImages(m1, m2), (ms_add_None_b_ch)(meta)), ])  #             return [ImageDef(PILImages(m1,m2),meta |> ms_add_None_b_ch)]
    if not _coconut_case_match_check_16:  #         match ImageDef(PILImages(m1,m2),meta):
        _coconut_match_set_name_m1 = _coconut_sentinel  #         match ImageDef(PILImages(m1,m2),meta):
        _coconut_match_set_name_m2 = _coconut_sentinel  #         match ImageDef(PILImages(m1,m2),meta):
        _coconut_match_set_name_meta = _coconut_sentinel  #         match ImageDef(PILImages(m1,m2),meta):
        if (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) == 2) and (_coconut.isinstance(_coconut_case_match_to_16[0], PILImages)) and (_coconut.len(_coconut_case_match_to_16[0]) == 2):  #         match ImageDef(PILImages(m1,m2),meta):
            _coconut_match_set_name_m1 = _coconut_case_match_to_16[0][0]  #         match ImageDef(PILImages(m1,m2),meta):
            _coconut_match_set_name_m2 = _coconut_case_match_to_16[0][1]  #         match ImageDef(PILImages(m1,m2),meta):
            _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #         match ImageDef(PILImages(m1,m2),meta):
            _coconut_case_match_check_16 = True  #         match ImageDef(PILImages(m1,m2),meta):
        if _coconut_case_match_check_16:  #         match ImageDef(PILImages(m1,m2),meta):
            if _coconut_match_set_name_m1 is not _coconut_sentinel:  #         match ImageDef(PILImages(m1,m2),meta):
                m1 = _coconut_case_match_to_16[0][0]  #         match ImageDef(PILImages(m1,m2),meta):
            if _coconut_match_set_name_m2 is not _coconut_sentinel:  #         match ImageDef(PILImages(m1,m2),meta):
                m2 = _coconut_case_match_to_16[0][1]  #         match ImageDef(PILImages(m1,m2),meta):
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #         match ImageDef(PILImages(m1,m2),meta):
                meta = _coconut_case_match_to_16[1]  #         match ImageDef(PILImages(m1,m2),meta):
        if _coconut_case_match_check_16:  #         match ImageDef(PILImages(m1,m2),meta):
            return ([AutoList(ImageDef(PILImage(m1, m2), (ms_del_b_ch)(meta))), ])  #             return [AutoList(ImageDef(PILImage(m1,m2),meta |> ms_del_b_ch))]
def numpys_to_numpy(state):  # def numpys_to_numpy(state):
    _coconut_case_match_to_17 = state  #     case state:
    _coconut_case_match_check_17 = False  #     case state:
    _coconut_match_set_name_arng = _coconut_sentinel  #     case state:
    _coconut_match_set_name_shape = _coconut_sentinel  #     case state:
    if (_coconut.isinstance(_coconut_case_match_to_17, AutoList)) and (_coconut.len(_coconut_case_match_to_17) == 1) and (_coconut.isinstance(_coconut_case_match_to_17[0], _coconut.abc.Mapping)):  #     case state:
        _coconut_match_temp_0 = _coconut_case_match_to_17[0].get("type", _coconut_sentinel)  #     case state:
        _coconut_match_temp_1 = _coconut_case_match_to_17[0].get("arrange", _coconut_sentinel)  #     case state:
        _coconut_match_temp_2 = _coconut_case_match_to_17[0].get("meta", _coconut_sentinel)  #     case state:
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_2, _coconut.abc.Mapping)):  #     case state:
            _coconut_match_set_name_arng = _coconut_match_temp_1  #     case state:
            _coconut_match_temp_3 = _coconut_match_temp_2.get("shape", _coconut_sentinel)  #     case state:
            kwargs = dict((k, v) for k, v in _coconut_case_match_to_17[0].items() if k not in set(("type", "arrange", "meta")))  #     case state:
            if _coconut_match_temp_3 is not _coconut_sentinel:  #     case state:
                _coconut_match_set_name_shape = _coconut_match_temp_3  #     case state:
                other_meta = dict((k, v) for k, v in _coconut_match_temp_2.items() if k not in set(("shape",)))  #     case state:
                _coconut_case_match_check_17 = True  #     case state:
    if _coconut_case_match_check_17:  #     case state:
        if _coconut_match_set_name_arng is not _coconut_sentinel:  #     case state:
            arng = _coconut_match_temp_1  #     case state:
        if _coconut_match_set_name_shape is not _coconut_sentinel:  #     case state:
            shape = _coconut_match_temp_3  #     case state:
    if _coconut_case_match_check_17 and not ("B" not in arng):  #     case state:
        _coconut_case_match_check_17 = False  #     case state:
    if _coconut_case_match_check_17:  #     case state:
        return ([(lambda numpys: np.array(numpys), frozendict({"type": "numpy", "arrange": "B" + arng, "meta": fdict({"shape": (None, ) + shape, **other_meta}), **kwargs}), "merge arrays to array".format(), 10), ])  #             return [
def tensor_to_list(state):  # def tensor_to_list(state):
    _coconut_case_match_to_18 = state  #     case state:
    _coconut_case_match_check_18 = False  #     case state:
    _coconut_match_set_name_shape = _coconut_sentinel  #     case state:
    if _coconut.isinstance(_coconut_case_match_to_18, _coconut.abc.Mapping):  #     case state:
        _coconut_match_temp_0 = _coconut_case_match_to_18.get("arrange", _coconut_sentinel)  #     case state:
        _coconut_match_temp_1 = _coconut_case_match_to_18.get("meta", _coconut_sentinel)  #     case state:
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, _coconut.str)) and (_coconut_match_temp_0.startswith("B")) and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, _coconut.abc.Mapping)):  #     case state:
            arng = _coconut_match_temp_0[1:]  #     case state:
            _coconut_match_temp_2 = _coconut_match_temp_1.get("shape", _coconut_sentinel)  #     case state:
            kwargs = dict((k, v) for k, v in _coconut_case_match_to_18.items() if k not in set(("arrange", "meta")))  #     case state:
            if _coconut_match_temp_2 is not _coconut_sentinel:  #     case state:
                _coconut_match_set_name_shape = _coconut_match_temp_2  #     case state:
                other_meta = dict((k, v) for k, v in _coconut_match_temp_1.items() if k not in set(("shape",)))  #     case state:
                _coconut_case_match_check_18 = True  #     case state:
    if _coconut_case_match_check_18:  #     case state:
        if _coconut_match_set_name_shape is not _coconut_sentinel:  #     case state:
            shape = _coconut_match_temp_2  #     case state:
    if _coconut_case_match_check_18 and not (len(arng) > 1):  #     case state:
        _coconut_case_match_check_18 = False  #     case state:
    if _coconut_case_match_check_18:  #     case state:
        return ([(lambda tensor: [t for t in tensor], AutoList(fdict(arrange=arng, meta=fdict({"shape": shape[1:], **other_meta}), **kwargs)), "tensor to list of tensor".format(), 2), ])  #             return [
    if not _coconut_case_match_check_18:  #                 (tensor->[t for t in tensor],
        _coconut_match_set_name_shape = _coconut_sentinel  #                 (tensor->[t for t in tensor],
        _coconut_match_set_name_cr = _coconut_sentinel  #                 (tensor->[t for t in tensor],
        if _coconut.isinstance(_coconut_case_match_to_18, _coconut.abc.Mapping):  #                 (tensor->[t for t in tensor],
            _coconut_match_temp_0 = _coconut_case_match_to_18.get("arrange", _coconut_sentinel)  #                 (tensor->[t for t in tensor],
            _coconut_match_temp_1 = _coconut_case_match_to_18.get("meta", _coconut_sentinel)  #                 (tensor->[t for t in tensor],
            _coconut_match_temp_3 = _coconut_case_match_to_18.get("ch_rpr", _coconut_sentinel)  #                 (tensor->[t for t in tensor],
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, _coconut.str)) and (_coconut_match_temp_0.startswith("C")) and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, _coconut.abc.Mapping)) and (_coconut_match_temp_3 is not _coconut_sentinel):  #                 (tensor->[t for t in tensor],
                arng = _coconut_match_temp_0[1:]  #                 (tensor->[t for t in tensor],
                _coconut_match_temp_2 = _coconut_match_temp_1.get("shape", _coconut_sentinel)  #                 (tensor->[t for t in tensor],
                _coconut_match_set_name_cr = _coconut_match_temp_3  #                 (tensor->[t for t in tensor],
                kwargs = dict((k, v) for k, v in _coconut_case_match_to_18.items() if k not in set(("arrange", "meta", "ch_rpr")))  #                 (tensor->[t for t in tensor],
                if _coconut_match_temp_2 is not _coconut_sentinel:  #                 (tensor->[t for t in tensor],
                    _coconut_match_set_name_shape = _coconut_match_temp_2  #                 (tensor->[t for t in tensor],
                    other_meta = dict((k, v) for k, v in _coconut_match_temp_1.items() if k not in set(("shape",)))  #                 (tensor->[t for t in tensor],
                    _coconut_case_match_check_18 = True  #                 (tensor->[t for t in tensor],
        if _coconut_case_match_check_18:  #                 (tensor->[t for t in tensor],
            if _coconut_match_set_name_shape is not _coconut_sentinel:  #                 (tensor->[t for t in tensor],
                shape = _coconut_match_temp_2  #                 (tensor->[t for t in tensor],
            if _coconut_match_set_name_cr is not _coconut_sentinel:  #                 (tensor->[t for t in tensor],
                cr = _coconut_match_temp_3  #                 (tensor->[t for t in tensor],
        if _coconut_case_match_check_18 and not (len(arng) > 1):  #                 (tensor->[t for t in tensor],
            _coconut_case_match_check_18 = False  #                 (tensor->[t for t in tensor],
        if _coconut_case_match_check_18:  #                 (tensor->[t for t in tensor],
            return ([(lambda tensor: [t for t in tensor], AutoList(fdict(arrange=arng, meta=fdict({"shape": shape[1:], **other_meta}), ch_rpr="L", **kwargs)), "split CHW to [HW]".format(), 2), ])  #             return [


def rgb_to_rgba(state):  # def rgb_to_rgba(state):
    if state == "numpy,uint8,HWC,RGB,0_255":  #     if state == "numpy,uint8,HWC,RGB,0_255":
        return ([(lambda a: np.concatenate((a, np.ones((*a.shape[:2], 1), dtype="uint8") * 255), axis=2), "numpy,uint8,HWC,RGBA,0_255", "add 255 as alpha channel", 10), ])  #         return [(
    elif state == "numpy,uint8,BHWC,RGB,0_255":  #     elif state == "numpy,uint8,BHWC,RGB,0_255":
        return ([(lambda a: np.concatenate((a, np.ones((*a.shape[:3], 1), dtype="uint8") * 255), axis=3), "numpy,uint8,BHWC,RGBA,0_255", "add 255 as alpha channel to batch", 10), ])  #         return [(

@memoize()  # @memoize()
def pix2pix_normalizer(nc):  # def pix2pix_normalizer(nc):
    from torchvision import transforms  #     import torchvision.transforms as transforms
    return (transforms.Normalize((0.5, ) * nc, (0.5, ) * nc))  #     return transforms.Normalize((0.5,)*nc,(0.5,)*nc)


def torch_img_to_pixpix_input(state):  # def torch_img_to_pixpix_input(state):
    _coconut_case_match_to_19 = state  #     case state:
    _coconut_case_match_check_19 = False  #     case state:
    _coconut_match_set_name_rpr = _coconut_sentinel  #     case state:
    if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #     case state:
        _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #     case state:
        _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #     case state:
        _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #     case state:
        _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #     case state:
        _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #     case state:
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "CHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel):  #     case state:
            _coconut_match_set_name_rpr = _coconut_match_temp_4  #     case state:
            kwargs = dict((k, v) for k, v in _coconut_case_match_to_19.items() if k not in set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #     case state:
            _coconut_case_match_check_19 = True  #     case state:
    if _coconut_case_match_check_19:  #     case state:
        _coconut_case_match_check_19 = False  #     case state:
        if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #     case state:
            _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #     case state:
            _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #     case state:
            _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #     case state:
            _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #     case state:
            _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #     case state:
            if (not _coconut_case_match_check_19) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "CHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGB"):  #     case state:
                _coconut_match_set_name_rpr = _coconut_match_temp_4  #     case state:
                _coconut_case_match_check_19 = True  #     case state:
        if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #     case state:
            _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #     case state:
            _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #     case state:
            _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #     case state:
            _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #     case state:
            _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #     case state:
            if (not _coconut_case_match_check_19) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "CHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGBA"):  #     case state:
                _coconut_match_set_name_rpr = _coconut_match_temp_4  #     case state:
                _coconut_case_match_check_19 = True  #     case state:
        if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #     case state:
            _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #     case state:
            _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #     case state:
            _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #     case state:
            _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #     case state:
            _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #     case state:
            if (not _coconut_case_match_check_19) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "CHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "L"):  #     case state:
                _coconut_match_set_name_rpr = _coconut_match_temp_4  #     case state:
                _coconut_case_match_check_19 = True  #     case state:

    if _coconut_case_match_check_19:  #     case state:
        if _coconut_match_set_name_rpr is not _coconut_sentinel:  #     case state:
            rpr = _coconut_match_temp_4  #     case state:
    if _coconut_case_match_check_19:  #     case state:
        return ([(pix2pix_normalizer(len(rpr)), "pix2pix,nc={_coconut_format_0}".format(_coconut_format_0=(len(rpr))), "to pixpix normalized", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 pix2pix_normalizer(len(rpr)),
        _coconut_match_set_name_rpr = _coconut_sentinel  #                 pix2pix_normalizer(len(rpr)),
        if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #                 pix2pix_normalizer(len(rpr)),
            _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
            _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
            _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
            _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
            _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "BCHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel):  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_set_name_rpr = _coconut_match_temp_4  #                 pix2pix_normalizer(len(rpr)),
                kwargs = dict((k, v) for k, v in _coconut_case_match_to_19.items() if k not in set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #                 pix2pix_normalizer(len(rpr)),
                _coconut_case_match_check_19 = True  #                 pix2pix_normalizer(len(rpr)),
        if _coconut_case_match_check_19:  #                 pix2pix_normalizer(len(rpr)),
            _coconut_case_match_check_19 = False  #                 pix2pix_normalizer(len(rpr)),
            if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                if (not _coconut_case_match_check_19) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "BCHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGB"):  #                 pix2pix_normalizer(len(rpr)),
                    _coconut_match_set_name_rpr = _coconut_match_temp_4  #                 pix2pix_normalizer(len(rpr)),
                    _coconut_case_match_check_19 = True  #                 pix2pix_normalizer(len(rpr)),
            if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                if (not _coconut_case_match_check_19) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "BCHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGBA"):  #                 pix2pix_normalizer(len(rpr)),
                    _coconut_match_set_name_rpr = _coconut_match_temp_4  #                 pix2pix_normalizer(len(rpr)),
                    _coconut_case_match_check_19 = True  #                 pix2pix_normalizer(len(rpr)),
            if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_0 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_1 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_2 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_3 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                _coconut_match_temp_4 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #                 pix2pix_normalizer(len(rpr)),
                if (not _coconut_case_match_check_19) and (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "BCHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "L"):  #                 pix2pix_normalizer(len(rpr)),
                    _coconut_match_set_name_rpr = _coconut_match_temp_4  #                 pix2pix_normalizer(len(rpr)),
                    _coconut_case_match_check_19 = True  #                 pix2pix_normalizer(len(rpr)),

        if _coconut_case_match_check_19:  #                 pix2pix_normalizer(len(rpr)),
            if _coconut_match_set_name_rpr is not _coconut_sentinel:  #                 pix2pix_normalizer(len(rpr)),
                rpr = _coconut_match_temp_4  #                 pix2pix_normalizer(len(rpr)),
        if _coconut_case_match_check_19:  #                 pix2pix_normalizer(len(rpr)),
            return ([(lambda t: torch.cat([pix2pix_normalizer(len(rpr))(i)[None] for i in t], dim=0), "pix2pix_batch,nc={_coconut_format_0}".format(_coconut_format_0=(len(rpr))), "to pixpix normalized", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 t->torch.cat([pix2pix_normalizer(len(rpr))(i)[None] for i in t],dim=0),
        if _coconut_case_match_to_19 == "pix2pix_laba":  #                 t->torch.cat([pix2pix_normalizer(len(rpr))(i)[None] for i in t],dim=0),
            _coconut_case_match_check_19 = True  #                 t->torch.cat([pix2pix_normalizer(len(rpr))(i)[None] for i in t],dim=0),
        if _coconut_case_match_check_19:  #                 t->torch.cat([pix2pix_normalizer(len(rpr))(i)[None] for i in t],dim=0),
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,LABA,0_1".format(), "inverse pix2pix_laba to img ", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix_lab":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,LAB,0_1".format(), "inverse pix2pix_lab to img ", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix_laba_batch":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,LABA,0_1".format(), "inverse pix2pix_laba batch to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix_lab_batch":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,LAB,0_1".format(), "inverse pix2pix_laba batch to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix,nc=4":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,RGBA,0_1".format(), "inverse pix2pix to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix_batch,nc=4":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,RGBA,0_1".format(), "inverse pix2pix batch nc=4 to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix_batch,nc=3":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,RGB,0_1".format(), "inverse pix2pix batch nc=3 to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix,nc=3":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,RGB,0_1".format(), "inverse pix2pix to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix_batch,nc=1":  #                 a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                 a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                 a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,L,0_1".format(), "inverse pix2pix_batch,nc=1 to img", 1), ])  #             return [(
    if not _coconut_case_match_check_19:  #                a -> a*0.5+0.5,
        if _coconut_case_match_to_19 == "pix2pix,nc=1":  #                a -> a*0.5+0.5,
            _coconut_case_match_check_19 = True  #                a -> a*0.5+0.5,
        if _coconut_case_match_check_19:  #                a -> a*0.5+0.5,
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,L,0_1".format(), "inverse pix2pix,nc=1 to img", 1), ])  #             return [(

@memoize()  # @memoize()
def _VGG_NORMALIZER():  # def _VGG_NORMALIZER():
    from torchvision import transforms  #     import torchvision.transforms as transforms
    nrm = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  #     nrm = transforms.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225])
    return (nrm)  #     return nrm
def inverse_vgg_prep(tensor):  # def inverse_vgg_prep(tensor):
    return (tensor.cpu() * torch.tensor([0.229, 0.224, 0.225])[:, None, None] + torch.tensor([0.485, 0.456, 0.406])[:, None, None])  #     return tensor.cpu() * torch.tensor([0.229,0.224,0.225])[:,None,None] + torch.tensor([0.485,0.456,0.406])[:,None,None]
def inverse_vgg_prep_batch(tensor):  # def inverse_vgg_prep_batch(tensor):
    return (tensor.cpu() * torch.tensor([0.229, 0.224, 0.225])[None, :, None, None] + torch.tensor([0.485, 0.456, 0.406])[None, :, None, None])  #     return tensor.cpu() * torch.tensor([0.229,0.224,0.225])[None,:,None,None] + torch.tensor([0.485,0.456,0.406])[None,:,None,None]
def torch_img_to_vgg_prep(state):  # def torch_img_to_vgg_prep(state):
    VGG_NORMALIZER = _VGG_NORMALIZER()  #     VGG_NORMALIZER = _VGG_NORMALIZER()
    _coconut_case_match_to_20 = state  #     case state:
    _coconut_case_match_check_20 = False  #     case state:
    if _coconut_case_match_to_20 == "vgg_prep":  #     case state:
        _coconut_case_match_check_20 = True  #     case state:
    if _coconut_case_match_check_20:  #     case state:
        return ([(inverse_vgg_prep, "torch,float32,CHW,RGB,0_1", "inverse from vgg_prep", 1), ])  #             return [(
    if not _coconut_case_match_check_20:  #                 inverse_vgg_prep,
        if _coconut_case_match_to_20 == "vgg_prep_batch":  #                 inverse_vgg_prep,
            _coconut_case_match_check_20 = True  #                 inverse_vgg_prep,
        if _coconut_case_match_check_20:  #                 inverse_vgg_prep,
            return ([(inverse_vgg_prep_batch, "torch,float32,BCHW,RGB,0_1", "inverse from vgg_prep_batch", 1), ])  #             return [(
    if not _coconut_case_match_check_20:  #                 inverse_vgg_prep_batch,
        if _coconut.isinstance(_coconut_case_match_to_20, _coconut.abc.Mapping):  #                 inverse_vgg_prep_batch,
            _coconut_match_temp_0 = _coconut_case_match_to_20.get("type", _coconut_sentinel)  #                 inverse_vgg_prep_batch,
            _coconut_match_temp_1 = _coconut_case_match_to_20.get("dtype", _coconut_sentinel)  #                 inverse_vgg_prep_batch,
            _coconut_match_temp_2 = _coconut_case_match_to_20.get("arrange", _coconut_sentinel)  #                 inverse_vgg_prep_batch,
            _coconut_match_temp_3 = _coconut_case_match_to_20.get("v_range", _coconut_sentinel)  #                 inverse_vgg_prep_batch,
            _coconut_match_temp_4 = _coconut_case_match_to_20.get("ch_rpr", _coconut_sentinel)  #                 inverse_vgg_prep_batch,
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "CHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGB"):  #                 inverse_vgg_prep_batch,
                kwargs = dict((k, v) for k, v in _coconut_case_match_to_20.items() if k not in set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #                 inverse_vgg_prep_batch,
                _coconut_case_match_check_20 = True  #                 inverse_vgg_prep_batch,
        if _coconut_case_match_check_20:  #                 inverse_vgg_prep_batch,
            return ([(VGG_NORMALIZER, "vgg_prep".format(), "to vgg normalized", 1), ])  #             return [(
    if not _coconut_case_match_check_20:  #                 VGG_NORMALIZER,
        if _coconut.isinstance(_coconut_case_match_to_20, _coconut.abc.Mapping):  #                 VGG_NORMALIZER,
            _coconut_match_temp_0 = _coconut_case_match_to_20.get("type", _coconut_sentinel)  #                 VGG_NORMALIZER,
            _coconut_match_temp_1 = _coconut_case_match_to_20.get("dtype", _coconut_sentinel)  #                 VGG_NORMALIZER,
            _coconut_match_temp_2 = _coconut_case_match_to_20.get("arrange", _coconut_sentinel)  #                 VGG_NORMALIZER,
            _coconut_match_temp_3 = _coconut_case_match_to_20.get("v_range", _coconut_sentinel)  #                 VGG_NORMALIZER,
            _coconut_match_temp_4 = _coconut_case_match_to_20.get("ch_rpr", _coconut_sentinel)  #                 VGG_NORMALIZER,
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "BCHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGB"):  #                 VGG_NORMALIZER,
                kwargs = dict((k, v) for k, v in _coconut_case_match_to_20.items() if k not in set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #                 VGG_NORMALIZER,
                _coconut_case_match_check_20 = True  #                 VGG_NORMALIZER,
        if _coconut_case_match_check_20:  #                 VGG_NORMALIZER,
            return ([(lambda t: torch.cat([VGG_NORMALIZER(i)[None] for i in t], dim=0), "vgg_prep_batch".format(), "to vgg normalized batch", 1), ])  #             return [(
    if not _coconut_case_match_check_20:  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
        if _coconut.isinstance(_coconut_case_match_to_20, _coconut.abc.Mapping):  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            _coconut_match_temp_0 = _coconut_case_match_to_20.get("type", _coconut_sentinel)  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            _coconut_match_temp_1 = _coconut_case_match_to_20.get("dtype", _coconut_sentinel)  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            _coconut_match_temp_2 = _coconut_case_match_to_20.get("arrange", _coconut_sentinel)  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            _coconut_match_temp_3 = _coconut_case_match_to_20.get("v_range", _coconut_sentinel)  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            _coconut_match_temp_4 = _coconut_case_match_to_20.get("ch_rpr", _coconut_sentinel)  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "torch") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "float32") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_2 == "BCHW") and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_3 == "0_1") and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_4 == "RGBA"):  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
                kwargs = dict((k, v) for k, v in _coconut_case_match_to_20.items() if k not in set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
                _coconut_case_match_check_20 = True  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
        if _coconut_case_match_check_20:  #                 t->torch.cat([VGG_NORMALIZER(i)[None] for i in t],dim=0),
            return ([(lambda t: torch.cat([torch.cat((VGG_NORMALIZER(i[:3])[None], i[[3, ]][None]), dim=1) for i in t], dim=0), "vgg_prep_batch_masked".format(), "to vgg normalized batch", 1), ])  #             return [(
def repeat_ch(state):  # def repeat_ch(state):
    _coconut_case_match_to_21 = state  #     case state:
    _coconut_case_match_check_21 = False  #     case state:
    _coconut_match_set_name_ch = _coconut_sentinel  #     case state:
    _coconut_match_set_name_shape = _coconut_sentinel  #     case state:
    if _coconut.isinstance(_coconut_case_match_to_21, _coconut.abc.Mapping):  #     case state:
        _coconut_match_temp_0 = _coconut_case_match_to_21.get("type", _coconut_sentinel)  #     case state:
        _coconut_match_temp_1 = _coconut_case_match_to_21.get("mode", _coconut_sentinel)  #     case state:
        _coconut_match_temp_2 = _coconut_case_match_to_21.get("ch_rpr", _coconut_sentinel)  #     case state:
        _coconut_match_temp_3 = _coconut_case_match_to_21.get("meta", _coconut_sentinel)  #     case state:
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "image") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "L") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_3, _coconut.abc.Mapping)):  #     case state:
            _coconut_match_set_name_ch = _coconut_match_temp_2  #     case state:
            _coconut_match_temp_4 = _coconut_match_temp_3.get("shape", _coconut_sentinel)  #     case state:
            kwargs = dict((k, v) for k, v in _coconut_case_match_to_21.items() if k not in set(("type", "mode", "ch_rpr", "meta")))  #     case state:
            if _coconut_match_temp_4 is not _coconut_sentinel:  #     case state:
                _coconut_match_set_name_shape = _coconut_match_temp_4  #     case state:
                other = dict((k, v) for k, v in _coconut_match_temp_3.items() if k not in set(("shape",)))  #     case state:
                _coconut_case_match_check_21 = True  #     case state:
    if _coconut_case_match_check_21:  #     case state:
        if _coconut_match_set_name_ch is not _coconut_sentinel:  #     case state:
            ch = _coconut_match_temp_2  #     case state:
        if _coconut_match_set_name_shape is not _coconut_sentinel:  #     case state:
            shape = _coconut_match_temp_4  #     case state:
    if _coconut_case_match_check_21 and not (len(ch_splitter(ch)) == 1):  #     case state:
        _coconut_case_match_check_21 = False  #     case state:
    if _coconut_case_match_check_21:  #     case state:
        return ([(lambda a: np.repeat(np.array(a)[:, :, None], 3, axis=2), fdict(type="numpy", dtype="uint8", arrange="HWC", ch_rpr=ch * 3, v_range="0_255", meta=fdict({"shape": (shape[0], shape[1], 3), **other}), **kwargs), "repeat_channel_3", 10), ])  #             return [
    if not _coconut_case_match_check_21:  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
        _coconut_match_set_name_ch = _coconut_sentinel  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
        _coconut_match_set_name_shape = _coconut_sentinel  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
        if _coconut.isinstance(_coconut_case_match_to_21, _coconut.abc.Mapping):  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            _coconut_match_temp_0 = _coconut_case_match_to_21.get("type", _coconut_sentinel)  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            _coconut_match_temp_1 = _coconut_case_match_to_21.get("arrange", _coconut_sentinel)  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            _coconut_match_temp_2 = _coconut_case_match_to_21.get("ch_rpr", _coconut_sentinel)  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            _coconut_match_temp_3 = _coconut_case_match_to_21.get("meta", _coconut_sentinel)  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "numpy") and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut_match_temp_1 == "HWC") and (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_3, _coconut.abc.Mapping)):  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                _coconut_match_set_name_ch = _coconut_match_temp_2  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                _coconut_match_temp_4 = _coconut_match_temp_3.get("shape", _coconut_sentinel)  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                kwargs = dict((k, v) for k, v in _coconut_case_match_to_21.items() if k not in set(("type", "arrange", "ch_rpr", "meta")))  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                if _coconut_match_temp_4 is not _coconut_sentinel:  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                    _coconut_match_set_name_shape = _coconut_match_temp_4  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                    other = dict((k, v) for k, v in _coconut_match_temp_3.items() if k not in set(("shape",)))  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                    _coconut_case_match_check_21 = True  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
        if _coconut_case_match_check_21:  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            if _coconut_match_set_name_ch is not _coconut_sentinel:  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                ch = _coconut_match_temp_2  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            if _coconut_match_set_name_shape is not _coconut_sentinel:  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
                shape = _coconut_match_temp_4  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
        if _coconut_case_match_check_21 and not (len(ch_splitter(ch)) == 1):  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            _coconut_case_match_check_21 = False  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
        if _coconut_case_match_check_21:  #                 (a->np.repeat(np.array(a)[:,:,None],3,axis=2),
            return ([(lambda a: a[:, :, [0, 0, 0]], fdict(type="numpy", arrange="HWC", ch_rpr=ch * 3, meta=fdict({"shape": (shape[0], shape[1], 3), **other}), **kwargs), "numpy_repeat_channel_3", 10), ])  #             return [



def lll_is_rgb(state):  # def lll_is_rgb(state):
    _coconut_case_match_to_22 = state  #     case state:
    _coconut_case_match_check_22 = False  #     case state:
    if _coconut.isinstance(_coconut_case_match_to_22, _coconut.abc.Mapping):  #     case state:
        _coconut_match_temp_0 = _coconut_case_match_to_22.get("ch_rpr", _coconut_sentinel)  #     case state:
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_0 == "LLL"):  #     case state:
            kwargs = dict((k, v) for k, v in _coconut_case_match_to_22.items() if k not in set(("ch_rpr",)))  #     case state:
            _coconut_case_match_check_22 = True  #     case state:
    if _coconut_case_match_check_22:  #     case state:
        return ([frozendict(ch_rpr="RGB", **kwargs), ])  #             return [frozendict(ch_rpr="RGB",**kwargs)]



def debug(conv):  # def debug(conv):
    from IPython import embed  #     from IPython import embed
    n = conv.edges[-1]  #     n = conv.edges[-1]
    matched = False  #     matched = False
    _coconut_case_match_to_23 = (n.src, n.dst)  #     case (n.src,n.dst):
    _coconut_case_match_check_23 = False  #     case (n.src,n.dst):
    if (_coconut.isinstance(_coconut_case_match_to_23, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_23) == 2) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1]) == 1) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1][0]) == 1) and (_coconut.isinstance(_coconut_case_match_to_23[1][0][0], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1][0][0]) == 1):  #     case (n.src,n.dst):
        _coconut_case_match_check_23 = True  #     case (n.src,n.dst):
    if _coconut_case_match_check_23:  #     case (n.src,n.dst):
        logger.warning("debugging nested autolist".format())  #             logger.warning(f"debugging nested autolist")
        matched = True  #             matched = True
    if not _coconut_case_match_check_23:  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        _coconut_match_set_name_arng = _coconut_sentinel  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        _coconut_match_set_name_s = _coconut_sentinel  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        if (_coconut.isinstance(_coconut_case_match_to_23, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_23) == 2) and (_coconut.isinstance(_coconut_case_match_to_23[1], ImageDef)) and (_coconut.len(_coconut_case_match_to_23[1]) == 2) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], TensorLike)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 2) and (_coconut.isinstance(_coconut_case_match_to_23[1][1], _coconut.abc.Mapping)):  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            _coconut_match_set_name_arng = _coconut_case_match_to_23[1][0][1]  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            _coconut_match_temp_0 = _coconut_case_match_to_23[1][1].get("shape", _coconut_sentinel)  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            if _coconut_match_temp_0 is not _coconut_sentinel:  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                _coconut_match_set_name_s = _coconut_match_temp_0  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                _coconut_case_match_check_23 = True  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        if _coconut_case_match_check_23:  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            if _coconut_match_set_name_arng is not _coconut_sentinel:  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                arng = _coconut_case_match_to_23[1][0][1]  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            if _coconut_match_set_name_s is not _coconut_sentinel:  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                s = _coconut_match_temp_0  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        if _coconut_case_match_check_23:  #         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            if len(arng) != len(s):  #             if len(arng) != len(s):
                logger.warning("debug console for omni_converter".format())  #                 logger.warning(f"debug console for omni_converter")
                matched = True  #                 matched =True
    if not _coconut_case_match_check_23:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        _coconut_match_set_name_arng1 = _coconut_sentinel  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        _coconut_match_set_name_s1 = _coconut_sentinel  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        _coconut_match_set_name_arng2 = _coconut_sentinel  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        _coconut_match_set_name_s2 = _coconut_sentinel  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        if (_coconut.isinstance(_coconut_case_match_to_23, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_23) == 2) and (_coconut.isinstance(_coconut_case_match_to_23[0], ImageDef)) and (_coconut.len(_coconut_case_match_to_23[0]) == 2) and (_coconut.isinstance(_coconut_case_match_to_23[0][0], TensorLike)) and (_coconut.len(_coconut_case_match_to_23[0][0]) >= 2) and (_coconut.isinstance(_coconut_case_match_to_23[0][1], _coconut.abc.Mapping)) and (_coconut.isinstance(_coconut_case_match_to_23[1], ImageDef)) and (_coconut.len(_coconut_case_match_to_23[1]) == 2) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], TensorLike)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 2) and (_coconut.isinstance(_coconut_case_match_to_23[1][1], _coconut.abc.Mapping)) and (_coconut.len(_coconut_case_match_to_23[1][1]) == 1):  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_match_set_name_arng1 = _coconut_case_match_to_23[0][0][1]  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_match_temp_0 = _coconut_case_match_to_23[0][1].get("shape", _coconut_sentinel)  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_match_set_name_arng2 = _coconut_case_match_to_23[1][0][1]  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_match_temp_1 = _coconut_case_match_to_23[1][1].get("shape", _coconut_sentinel)  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                _coconut_match_set_name_s1 = _coconut_match_temp_0  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                _coconut_match_set_name_s2 = _coconut_match_temp_1  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                _coconut_case_match_check_23 = True  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        if _coconut_case_match_check_23:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                arng1 = _coconut_case_match_to_23[0][0][1]  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if _coconut_match_set_name_s1 is not _coconut_sentinel:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                s1 = _coconut_match_temp_0  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                arng2 = _coconut_case_match_to_23[1][0][1]  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if _coconut_match_set_name_s2 is not _coconut_sentinel:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                s2 = _coconut_match_temp_1  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        if _coconut_case_match_check_23:  #         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if (len(arng2) != len(s2)) or (len(arng1) != len(s1)):  #             if (len(arng2) != len(s2)) or (len(arng1) != len(s1)):
                logger.warning("debug console for omni_converter".format())  #                 logger.warning(f"debug console for omni_converter")
                matched = True  #                 matched = True
    if matched:  #     if matched:
        embed()  #         embed()
        raise RuntimeError("exit")  #         raise RuntimeError("exit")
