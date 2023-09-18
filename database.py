"""
Initial, query, append, or otherwise alter a SQL database for CREST-Kit
"""

import json
import sqlite3

from pubchem_handler import query_pubchem

def extract_fields_from_json(js):
    """
    Extract the key value pairs from a Pubchem JSON object.
    """

    # Convert the JSON to a Python dictionary
    data = json.loads(js)
    print(data)



x = extract_fields_from_json(query_pubchem('O'))