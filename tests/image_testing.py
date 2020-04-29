import PIL
from PIL import Image
from src.graph_illustrator import ColorProfile


COLORS = ColorProfile((255, 255, 255, 255), (0, 0, 0, 255), (33, 150, 243, 255), (116, 130, 142, 255), (21, 94, 152, 255), (243, 33, 45, 255))
def compare_images(fp_actual: str, fp_expected: str):
    actual = Image.open(fp_actual)
    expected = Image.open(fp_expected)
    assert_image_equal(actual, expected)

def compare_gifs(fp_actual: str, fp_expected: str):
    actual = Image.open(fp_actual)
    expected = Image.open(fp_expected)
    assert_gif_equal(actual, expected)

def assert_simple(a, b):
    assert a.mode == b.mode, "got mode {!r}, expected {!r}".format(
        a.mode, b.mode
    )
    assert a.size == b.size, "got size {!r}, expected {!r}".format(
        a.size, b.size
    )

def assert_image_equal(a, b):
    assert_simple(a, b)
    if a.tobytes() != b.tobytes():
        assert False, "got different content"

def assert_gif_equal(a, b):
    assert_simple(a, b)
    assert a.n_frames == b.n_frames, "got n_frames {!r}, n_frames {!r}".format(
        a.n_frames, b.n_frames
    )
    for i in range(a.n_frames):
        a.seek(i)
        b.seek(i)
        assert a.tobytes() == b.tobytes(), "frame's {!r} have different data".format(i)
    