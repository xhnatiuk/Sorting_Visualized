from PIL import Image
from src.graph_illustrator import ColorProfile

COLORS = ColorProfile((255, 255, 255, 255), (0, 0, 0, 255), (33, 150, 243, 255), (33, 45, 243, 255), (243, 33, 45, 255))
def compare_images(fp_actual: str, fp_expected: str):
    actual = Image.open(fp_actual)
    expected = Image.open(fp_expected)
    assert_image_equal(actual, expected)

# From  python-pillow/Pillow/tests/helper.py

def assert_image_equal(a, b, msg=None):
    assert a.mode == b.mode, msg or "got mode {!r}, expected {!r}".format(
        a.mode, b.mode
    )
    assert a.size == b.size, msg or "got size {!r}, expected {!r}".format(
        a.size, b.size
    )
    if a.tobytes() != b.tobytes():
        assert False, msg or "got different content"