import os

_DEFAULT_INPUT_FLIGHT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "data",
                                          "airports.csv.gz")

INPUT_FLIGHT_FILE = os.getenv("INPUT_FLIGHT_FILE", _DEFAULT_INPUT_FLIGHT_FILE)

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///{}/airports.db".format(
    os.path.join(os.path.dirname(os.path.abspath(__file__)))))
