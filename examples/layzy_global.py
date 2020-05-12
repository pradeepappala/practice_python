def _long_function():
    # print() function to show this is called only once
    print("Determining DOWNLOAD_FOLDER_PATH...")
    # Determine the module-level variable
    path = "/some/path/here"
    # Set the global (module scope)
    globals()['DOWNLOAD_FOLDER_PATH'] = path
    import sys
    sys._getframe().f_globals.update({'path' : '/mypath'})
    # ... and return it
    return path


def __getattr__(name):
    if name == "DOWNLOAD_FOLDER_PATH":
        return _long_function()

    if name == 'a':
        print('evaluating')
        globals()['a'] = 1
        return globals()['a']

    # Implicit else
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def calc(a, b):
    return a + b

