import pytest
from mock_data.function import deidentify_value


def test_deidentify_value():
    # Test case 1: Short value
    value = "12345"
    deidentified_value = deidentify_value(value)
    assert len(deidentified_value) == 15
    assert deidentified_value.startswith(value[:2])
    assert deidentified_value[2:].isdigit()

    # Test case 2: Long value
    value = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    deidentified_value = deidentify_value(value)
    assert len(deidentified_value) == 15
    assert deidentified_value.startswith(value[:2])
    assert deidentified_value[2:].isdigit()

    # Test case 3: Empty value
    value = ""
    deidentified_value = deidentify_value(value)
    assert len(deidentified_value) == 0

    # Test case 4: Non-string value
    value = 12345
    with pytest.raises(AttributeError):
        deidentify_value(value)
