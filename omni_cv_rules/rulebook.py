from omni_converter.solver.rules import AutoRuleBook, CastLambda, ConversionLambda, RuleEdge
from omni_cv_rules.coconut.convert import imdef_neighbors, rule_xyz_to_rgb, rule_batch_xyz_to_rgb, \
    rule_VR_None_to_normalized, rule_add_channel, rule_swap_RGB_BGR
from omni_cv_rules.coconut.omni_converter import cast_imdef_str_to_imdef, cast_imdef_to_imdef_str, dict2imdef, \
    cast_ary_str_to_ary_type, img_list_is_imgs, lll_is_rgb, cast_tuple2auto_tuple, rule_format, rule_imgs2tile, \
    rule_batch_to_tiled, rule_img2widget, rule_numpy2img, rule_image2gray, rule_image_path_to_image, numpys_to_numpy, \
    tensor_to_list, rgb_to_rgba, repeat_ch, torch_img_to_pixpix_input, torch_img_to_vgg_prep, rule_to_spectrum, \
    cast_imdef_to_dict
from omni_cv_rules.coconut.recursive import intra_list_conversions
from omni_cv_rules.coconut.to_bytes import rule_image_str_to_jpg_bytes
from omni_cv_rules.coconut.widgets import any2widget, auto_tuple2widget
from omni_cv_rules.custom_rules import custom_rule_book


def create_cast_rule(rule, name=None, cost=1):
    """
    rule: State->List[State] # should return list of possible casts without data conversion.
    """
    return CastLambda(rule, name, cost=cost)


def create_conversion_rule(rule):
    return ConversionLambda(rule)


def create_alias_rule(a, b):
    def caster(state):
        if state == a:
            return [b]
        elif state == b:
            return [a]

    return create_cast_rule(caster, f"alias:{a}=={b}")

def rule_to_hsv(state):
    if state=="image,RGB,RGB":
        return [RuleEdge(
            converter = lambda img:img.convert("HSV"),
            new_format="image,HSV,HSV",
            cost=1,
            name=f"PIL RGB to PIL HSV"
        )]

CV_RULEBOOK = AutoRuleBook(id="CV_RULEBOOK").add_rules(
    imdef_neighbors,
    rule_xyz_to_rgb,
    rule_batch_xyz_to_rgb,
    rule_VR_None_to_normalized,
    rule_add_channel,
    rule_swap_RGB_BGR,
    create_cast_rule(cast_imdef_to_dict, "cast_imdef_to_dict"),
    create_cast_rule(cast_imdef_str_to_imdef, "cast_imdef_str_to_imdef"),
    create_cast_rule(cast_imdef_to_imdef_str, "cast_imdef_to_imdef_str"),
    create_cast_rule(dict2imdef, "dict2imdef"),
    create_cast_rule(cast_ary_str_to_ary_type, "cast_ary_str_to_ary_type"),
    create_cast_rule(img_list_is_imgs, "img_list_is_imgs"),
    create_cast_rule(lll_is_rgb, "lll_is_rgb", cost=10),
    create_cast_rule(cast_tuple2auto_tuple, "tuple <--> auto_tuple"),
    # AutoSolver.create_cast_rule(dict2visdomable),
    create_conversion_rule(any2widget),
    create_conversion_rule(rule_format),
    create_conversion_rule(rule_imgs2tile),
    create_conversion_rule(rule_batch_to_tiled),
    create_conversion_rule(rule_img2widget),
    create_conversion_rule(rule_numpy2img),
    create_conversion_rule(rule_image2gray),
    create_conversion_rule(rule_image_path_to_image),
    create_conversion_rule(rule_image_str_to_jpg_bytes),
    # AutoSolver.create_conversion_rule(rule_image2lab),
    # AutoSolver.create_conversion_rule(rule_rgba2laba),
    # AutoSolver.create_conversion_rule(rule_lab_value_conversion),
    create_conversion_rule(numpys_to_numpy),
    create_conversion_rule(tensor_to_list),
    create_conversion_rule(rule_to_hsv),
    create_conversion_rule(rgb_to_rgba),
    create_conversion_rule(repeat_ch),
    create_conversion_rule(torch_img_to_pixpix_input),
    create_conversion_rule(torch_img_to_vgg_prep),
    # AutoSolver.create_conversion_rule(intra_tuple_conversions),
    create_conversion_rule(rule_to_spectrum),
    create_conversion_rule(auto_tuple2widget),
    create_alias_rule("numpy_rgb", "numpy,uint8,HWC,RGB,0_255"),
    create_alias_rule("numpy_rgba", "numpy,uint8,HWC,RGBA,0_255"),
) + custom_rule_book.add_recursive_rule(
    intra_list_conversions
).set_id("CV_RULEBOOK")
