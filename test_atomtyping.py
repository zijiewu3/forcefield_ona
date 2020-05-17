from glob import glob

import parmed as pmd
import pytest

from foyer import Forcefield
from foyer.tests.utils import atomtype

MOL2_FILES = glob('test_molecules/ds.mol2')
FORCEFIELD_FILES = glob('ONA.xml')

FORCEFIELD = Forcefield(forcefield_files=FORCEFIELD_FILES)

@pytest.mark.parametrize('mol2_file', MOL2_FILES)
def test_atomtyping(mol2_file):
    structure = pmd.load_file(mol2_file, structure=True)
    structure_typed = FORCEFIELD.apply(structure, assert_dihedral_params=False)
    structure_typed.save('ds_typed.top')


