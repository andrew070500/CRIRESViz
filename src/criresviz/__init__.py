"""
CRIRESViz

Visualization tools for CRIRES+ wavelength settings,
molecular bands and atmospheric transmission.
"""

__version__ = "1.0.0"

from .plotting import plot

from .models import (
    CRIRESSetting,
    Detector,
    Order,
    Molecule,
    Sky,
    CRIRESBand
)

__all__ = [
    "plot",
    "CRIRESSetting",
    "Detector",
    "Order",
    "Molecule",
    "Sky",
    "CRIRESBand",
]
