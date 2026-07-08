from criresviz import CRIRESSetting


setting = CRIRESSetting.from_name("M4368")

assert setting.name == "M4368"

assert setting.band == "M"

assert len(setting.orders) == 6

order = setting.get_order(13)

assert order.number == 13
