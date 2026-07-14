#!/bin/bash

echo "Running 01_single_setting.py..."
python3 01_single_setting.py

echo "Running 02_multiple_settings.py..."
python3 02_multiple_settings.py

echo "Running 03_single_molecule.py..."
python3 03_single_molecule.py

echo "Running 04_multiple_molecules.py..."
python3 04_multiple_molecules.py

echo "Runnig 05_sky_transmission.py..."
python3 05_sky_transmission.py

echo "Running 06_sky_emission.py..."
python3 06_sky_emission.py 

echo "Running 07_compact_layout.py..."
python3 07_compact_layout.py

echo "Running 08_everything_together.py..."
python3 08_everything_together.py




