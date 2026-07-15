#!/bin/bash

echo "Running 01_single_setting.py..."
python3 01_single_setting.py

echo "Running 02_multiple_settings.py..."
python3 02_multiple_settings.py

echo "Running 03_single_molecule.py..."
python3 03_single_molecule.py

echo "Running 04_multiple_molecules.py..."
python3 04_multiple_molecules.py

echo "Running 05_sky_transmission.py..."
python3 05_sky_transmission.py

echo "Running 06_sky_emission.py..."
python3 06_sky_emission.py 

echo "Running 07_compact_layout.py..."
python3 07_compact_layout.py

echo "Running 08_everything_together.py..."
python3 08_everything_together.py

echo "Running 09_info.py..."
python3 09_info.py

echo "Running 10_band.py"
python3 10_band.py

echo "Running 11_coverage.py..."
python3 11_coverage.py

echo "Running 12_rank.py..."
python3 12_rank.py


