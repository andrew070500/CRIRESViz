from criresviz import CRIRESSetting


def test_setting():

    setting = CRIRESSetting.from_name("M4368")

    assert setting.band == "M"

    assert setting.central_wavelength == 4.368

    assert len(setting.orders) == 7