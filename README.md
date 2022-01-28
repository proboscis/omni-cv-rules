# Omni-CV-Rules
This module is a set of image related conversion rules for use with [omni-converter](https://github.com/proboscis/omni-converter).

# Installation
`pip instasll omni-cv-rules`

# Quickstart
```python
from omni_converter import AutoDataFactory
from omni_cv_rules import CV_RULEBOOK
auto = AutoDataFactory(CV_RULEBOOK)
# loading an image
img:"IAutoData" = auto("image_path","path/to/image")
# You can convert it to any format by calling 'to'
# this will automatically search for a composition of functions to convert 'image_path' into numpy array.
ary:np.ndarray = img.to("numpy,uint8,HWC,RGB,0_255")
# CHW means that the tensor shape is (Channel, Height, Widgth).
torch_img:torch.Tensor = img.to("torch,float32,CHW,RGB,0_1")
# BCHW means that the tensor shape is (Batch, Channel, Height, Widgth).
torch_batch:torch.Tensor = img.to("torch,float32,BCHW,RGB,0_1")
# you can start searching from any format
base64_str:str = auto("torch,float32,CHW,RGB,0_1",torch_img).to("base64")
# everything can be changed at once
np_ary:np.ndarray = auto("torch,float32,CHW,RGB,0_1",torch_img).to("numpy,float64,BHWC,BGR,0_1")
# list of format is supported. enclosing any valid format with square bracket means that the data is list of that format. 
paths = ["1.png","2.png"]
auto("[image_path]")(paths).to("torch,float32,BCHW,RGB,0_1")
# and back also
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[torch,float32,CHW,RGB,0_1]") # list of torch array from a batch!
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[image,RGB,RGB]") # list of PIL.Image.Image!
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[base64]") # list of base64
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[html]") # list of base64
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("widget") # ipywidget for displaying in notebook
```

# Formats

## numpy/torch tensor
```
tensor_like = tensor_type,dtype,arrange,channel_representation,value_range
tensor_type ::== numpy | torch
dtype ::= uint8 | float32 | float64 | int32 | int64
arrange ::= HWC | CHW | BHWC | BCHW | HW
channel_representation ::= RGB | BGR | YCbCr| RGBA | L | LLL| RRR | GGG | BBB | XYZ |...
value_range ::= 0_1 | 0_255 | -1_1 | None | ...
```
example: `"numpy,float32,BCHW,RGB,0_1"`

## PIL Image
examples: `"image,RGB,RGB"`, `"image,YCbCr,YCbCr"`

## base64 encoded png image
`"base64_str""`

## html tag with base64 encoded png
`"html"`

## ipywidget
`"widget"`

## image path
`"image_path"`

## Normal Map

## intra-list-conversion
`"[{any_format}]"`
any list of data can be expressed as a list of format.
examples: `"[image_path]"`,`[image,RGB,RGB]`,`[numpy,uint8,HW,L,0_255]`