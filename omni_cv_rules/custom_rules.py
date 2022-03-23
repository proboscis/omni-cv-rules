import base64
from io import BytesIO

import PIL
from omni_converter.solver.rules import AutoRuleBook
from toolz.functoolz import memoize



def make_rule(src, dst):
    def _inner(converter):
        def rule_impl(s):
            if s == src:
                return [(converter, dst)]

        return rule_impl

    return _inner




@make_rule("image,RGB,RGB", "base64_png")
def pil_img_to_base64(img: PIL.Image.Image):
    buf = BytesIO()
    img.save(buf, format="png")
    img_str = base64.b64encode(buf.getvalue()).decode("ascii")
    return img_str


@make_rule("base64_png", "html")
def base64_png_to_html(base64_str):
    return f"""<img src="data:image/png;base64,{base64_str}"/>"""


@make_rule("dataframe", "html")
def custom_dataframe_viz(df):
    def _formatter(item):
        if hasattr(item, "_repr_html_"):
            return item._repr_html_()
        else:
            return repr(item)

    formatters = {k: _formatter for k in df.columns}
    return df.to_html(escape=False, formatters=formatters)


custom_rule_book = AutoRuleBook(id="custom_rule_book").add_rules(
    pil_img_to_base64,
    base64_png_to_html,
    custom_dataframe_viz
).add_alias("html", "_repr_html_").add_alias("base64","base64_png").set_id("custom_rule_book")
