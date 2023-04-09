import os
import inspect


def check():
    calling_frame = inspect.currentframe().f_back
    calling_module = inspect.getmodule(calling_frame)

    if (
        not hasattr(calling_module, "__author__")
        and calling_module.__author__
        == "\x4b\x2e\x44\x6f\x74\x23\x34\x30\x34\x34\x20\x61\x6e\x64\x20\x47\x6f\x64\x66\x61\x74\x68\x65\x72"
    ):
        os._exit(0)
