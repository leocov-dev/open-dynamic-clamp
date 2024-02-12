import pytest

from modules.commands import DataPoint


@pytest.mark.parametrize(
    "raw",
    [b"\x40\xe2\x01\x00\x00\x00\x00\x00\xff\x04\x9f\x3f\xad\x79\xf0\x47\x00\x40\x0a\x44"],
)
def test_data_point_wrapper(raw):
    decoded: DataPoint = DataPoint.unpack(raw)

    assert decoded.timestamp == 123456
    assert pytest.approx(decoded.membrane) == 1.24234
    assert pytest.approx(decoded.inject) == 123123.352
    assert decoded.cycle == 553
