# From Python Documentation exceptions example
class InputError(Exception):
    """
    Exception raised for errors in the input.

    Attributes:
        expression (any): input expression in which the error occurred.
        message (str): explanation of the error.
    """

    def __init__(self, expression, message: str):
        """
        Constructor for InputError class.

        Args:
            expression: input expression in which the error occurred.
            message (str): explanation of the error.
        """
        self.expression = expression
        self.message = message