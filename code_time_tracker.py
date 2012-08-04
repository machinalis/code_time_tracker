from functools import wraps
from datetime import datetime, timedelta


class CTTracker(object):
    def __init__(self, name=""):
        self.name = name
        self._tdelta = timedelta()
        self._calls = 0

    def start_call(self):
        self._start = datetime.now()

    def finish_call(self):
        self._tdelta += datetime.now() - self._start
        self._calls += 1
        del self._start

    def __del__(self):
        print "<Code time tracker %s: %s timedelta, %s calls>" % (
            self.name, self._tdelta, self._calls)


_singleton = {}


def code_time_tracked(function):
    def inner_func(*args, **kwargs):
        from code_time_tracker import _singleton
        key = '.'.join([function.__module__, function.__name__])
        if key not in _singleton:
            _singleton[key] = CTTracker(key)
        tracker = _singleton[key]
        tracker.start_call()
        result = function(*args, **kwargs)
        tracker.finish_call()
        return result
    return inner_func
