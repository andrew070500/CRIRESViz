from criresviz.models.detector import Detector
from criresviz.models.order import Order

d1 = Detector(1, 4.10, 4.20)
d2 = Detector(2, 4.21, 4.30)
d3 = Detector(3, 4.31, 4.40)

order = Order(
    number=13,
    detector1=d1,
    detector2=d2,
    detector3=d3,
)

assert order.number == 13

assert order.wavelength_min == 4.10

assert order.wavelength_max == 4.40

assert order.wavelength_range == (
    4.10,
    4.40,
)


numbers = []

for detector in order:

    numbers.append(detector.number)

assert numbers == [1, 2, 3]
