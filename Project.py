"""Entry point for inspecting plant configuration data."""
from pprint import pprint

from data import PLANT_CONFIGURATIONS, as_dict_list


if __name__ == "__main__":
    pprint(as_dict_list())
    print()
    pprint(PLANT_CONFIGURATIONS)
