# Options.py
from typing import Dict

from Options import Choice, Option, Toggle

def set_option(self, option, value):
    if option in self.options:
        self.options[option] = value
    else:
        print(f"Unknown option: {option}")

def get_option(self, option):
    return self.options.get(option, None)


ftl_options: Dict[str, type(Option)] = {
}
