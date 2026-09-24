class Manufacturer:
    """Represents a vehicle manufacturer."""

    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country


    def __str__(self):
        return f"({self._name}, {self._country})"