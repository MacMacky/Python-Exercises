

def hasLength(string):
    return True if len(string) >= 1 else False


def test(testName, returnValue, expectedValue):
    try:
        assert returnValue == expectedValue
        print("Test " + testName + " Success.")
    except AssertionError as e:
        print("Test " + testName + " Failed.")


def describe(name, callback):
    callback()
    print("")
