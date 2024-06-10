from typing import List

from enum import Enum


class Colors(Enum):
    """
    Enumerator class to store color values as hexadecimal strings.
    """

    YELLOW = "#FFFF00"
    BLUE = "#0000FF"
    WHITE = "white"
    BACKGROUND = "#1A0A1A"

    @classmethod
    def list_members(cls) -> List[str]:
        """
        Return a list of the color names.

        :return: List of color names.
        """
        return list(cls)

    def __str__(self) -> str:
        """
        Return the color name as a string.

        :return: Color name as a string.
        """
        return self.name

    def __repr__(self) -> str:
        """
        Return the color name as a string.

        :return: Color name as a string.
        """
        return f"{self.__class__.__name__}.{self.name}({self.value})"
