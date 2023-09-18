"""
Use Crest and xTB to generate 3D conformers with GFN2-xTB force field,
rank, screen, and save them for further analysis.
"""

import shutil

# find the crest executable in the PATH
CREST_EXE = shutil.which("crest")

schemas = {
    "conformers": { "" },
    "nci": { "" },
    "tautomers": { "" },
    "qcg": { "" }
}

