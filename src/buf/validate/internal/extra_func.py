import celpy

from buf.validate.internal import string_format


def make_extra_funcs(locale: str) -> dict[str, celpy.CELFunction]:
    string_fmt = string_format.StringFormat(locale)
    return {
        "format": string_fmt.format,
    }


EXTRA_FUNCS = make_extra_funcs("en_US")
