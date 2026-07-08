from criresviz.models.detector import Detector


def test_detector_properties():

    detector = Detector(
        number=1,
        wavelength_min=4.321,
        wavelength_max=4.367,
    )

    assert detector.number == 1

    assert detector.width == 0.046

    assert detector.center == (4.321 + 4.367) / 2

    assert detector.wavelength_range == (
        4.321,
        4.367,
    )


def test_detector_contains():

    detector = Detector(
        number=1,
        wavelength_min=4.3,
        wavelength_max=4.4,
    )

    assert 4.35 in detector

    assert 4.5 not in detector
