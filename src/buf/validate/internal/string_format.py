from celpy import celtypes
import celpy


class StringFormat:
    """An implementation of string.format() in CEL."""

    def __init__(self, locale: str):
        self.locale = locale

    def format(self, fmt: celtypes.Value, args: celtypes.Value) -> celpy.Result:
        if not isinstance(fmt, celtypes.StringType):
            return celpy.native_to_cel(
                celpy.new_error("format() requires a string as the first argument")
            )
        if not isinstance(args, celtypes.ListType):
            return celpy.native_to_cel(
                celpy.new_error("format() requires a list as the second argument")
            )
        return celtypes.StringType(fmt)
