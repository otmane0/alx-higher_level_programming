#!/usr/bin/python3"
"""a class"""

class MyInt(int):
    """equale or no"""

    def __eq__(self, number):
        """Override == operator"""

        return super().__ne__(number)

    def __ne__(self, number):
        """Override != operator"""

        return super().__eq__(number)

