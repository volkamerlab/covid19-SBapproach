"""
sdf_to_smi.py

Converts a SDF dataset to a list of SMILES
"""

import os
import sys

from openforcefield.topology import Molecule


def main(sdf_path):
    if not os.path.isfile(sdf_path):
        raise ValueError(f"File {sdf_path} is not available.")

    molecules = Molecule.from_file(sdf_path, allow_undefined_stereo=True)
    smiles = [m.to_smiles() for m in molecules]
    base, ext = os.path.splitext(sdf_path)
    with open(f"{base}.smi", "w") as f:
        f.write("\n".join(smiles))
    return smiles


if __name__ == "__main__":
    main(sys.argv[1])
    print(f"Done! Check {os.path.splitext(sys.argv[1])[0]}.smi")
