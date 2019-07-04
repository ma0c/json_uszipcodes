#!/usr/bin/env python

import json

from uszipcode import SearchEngine
from uszipcode.db import connect_to_simple_zipcode_db


def extract_data_from_simple_zip_code():
    # This will download tha simple_zipcode database
    SearchEngine()

    # We get the cursor from SQLAlchemy
    db = connect_to_simple_zipcode_db()
    connection = db.connect()
    query = "select zipcode, major_city, state from simple_zipcode"
    result = connection.execute(query)
    all_zips = dict()
    data = result.fetchone()
    while data is not None:
        all_zips[data[0]] = {
            "city": data[1],
            "state": data[2]
        }
        data = result.fetchone()

    with open("zip_codes.json", "w+") as f:
        json.dump(all_zips, f)


if __name__ == "__main__":
    extract_data_from_simple_zip_code()
