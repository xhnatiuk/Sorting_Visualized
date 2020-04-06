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