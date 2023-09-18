"""
Use RDKit to generate 3D conformers with MMFF94 force field,
and save them as .sdf files. Screens conformers with similar
torsion angles and energy.
"""

import os

from rdkit import Chem
from rdkit.Chem import AllChem

def generate_random_conformers():
    pass

def assign_conformer_torsion_labels(angle):
    """
    Assign labels to conformers based on torsion angles.
    """
    if angle < 0:
        angle += 360
    
    if angle >= 
