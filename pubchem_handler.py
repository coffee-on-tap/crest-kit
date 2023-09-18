"""
Query PubChem for a given compound name and return the PubChem CID,
if available.
"""

import urllib.request

def query_pubchem(query):
    """
    Pass query to Pubchem and return data to be passed to a SQL database.
    """

    # First, determine if the query is a SMILES string or a CID
    query_type = determine_if_smiles_or_cid(query)

    # Next, query PubChem and return JSON of the data
    if query_type == 'cid':
        url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{query}/json'
    elif query_type == 'smiles':
        url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{query}/json'

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return data
    except urllib.error.HTTPError:
        return None

def determine_if_smiles_or_cid(query):
    """
    Determine if the query is a SMILES string or a CID.
    """

    if query.isdigit():
        return 'cid'
    else:
        return 'smiles'