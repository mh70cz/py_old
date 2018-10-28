"""
Bite 114. Implement a Color class with classmethods 

https://codechalleng.es/bites/114
"""
import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
# urllib.request.urlretrieve('https://bit.ly/2MSuu4z',  color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper(), None)

    @classmethod
    def hex2rgb(self, hexa):
        """Class method that converts a hex value into an rgb one"""
        if not isinstance(hexa, str):
            raise ValueError
        if len(hexa) != 7:
           raise ValueError
        try:
            rgb = int("0x" + hexa[1:], 16)
            if not(0 <= rgb <= 256**3):
                raise ValueError
            return(rgb // (256**2) , (rgb // 256) % 256 , rgb % 256)
        except:
            raise ValueError
    
    @classmethod
    def rgb2hex(self, rgb):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb, tuple):
            raise ValueError
        if len(rgb) != 3:
           raise ValueError
        for e in rgb:
            if not (isinstance(e, int) and (0 <= e <= 255)):
                raise ValueError
        return "#{:0>6x}".format(rgb[0]*256*256 + rgb[1]*256 + rgb[2])
        # return "#{:0>2x}{:0>2x}{:0>2x}".format(*rgb)
            

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{(self.color)}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb)
        
                
import pytest
@pytest.mark.parametrize("color, expected", [
    ("white", (255, 255, 255)),
    ("black", (0, 0, 0)),
    ("blue", (0, 0, 255)),
    ("red", (255, 0, 0)),
    ("green", (0, 128, 0)),
    ("orange", (255, 128, 0)),
    ("puke", None),
])
def test_color_class(color, expected):
    c = Color(color)
    assert c.rgb == expected


@pytest.mark.parametrize("rgb, expected", [
    ((255, 255, 255), "#ffffff"),
    ((0, 0, 0), "#000000"),
    ((0, 0, 255), "#0000ff"),
    ((255, 0, 0), "#ff0000"),
    ((0, 128, 0), "#008000"),
    ((255, 128, 0), "#ff8000"),
])
def test_color_classmethod_rgb2hex(rgb, expected):
    assert Color.rgb2hex(rgb) == expected


@pytest.mark.parametrize("rgb", [
    ("puke"),
    ("0, 0, 0"),
    ((0, -5, 255)),
    ((256, 0, 0)),
])

def test_color_rgb2hex_bad_value(rgb):
    with pytest.raises(ValueError):
        Color.rgb2hex(rgb)


@pytest.mark.parametrize("value", [
    ("puke"),
    ("#ccc"),
    ("#stopit"),
    ("pink"),
])
def test_color_hex2rgb_bad_value(value):
    with pytest.raises(ValueError):
        Color.hex2rgb(value)


def test_color_string_output():
    color = Color("brown")
    assert str(color) == "(165, 42, 42)"


def test_color_repr_output():
    color = Color("brown")
    assert repr(color) == "Color('brown')"

    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          