# Extract City and State from simple_zipcode

This is a simple script to create a JSON file where each key is a common zip code in US and each value is a object with its name and state.

To achieve this we use [uszipcode](https://pypi.org/project/uszipcode/) Python package wich downloads the [simple_zipcode database](https://datahub.io/machu-gwu/uszipcode-0.2.0-simple_db)

Result json is stored in zip_codes.json

