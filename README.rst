Code time tracker
=================

simply tracks ellapsed time of decorated code and print it when script is finished.

In order to use it, just do::

    from code_time_tracker import code_time_tracked

and later decorate your code like this::

    @code_time_tracked
    def my_func():
        do_stuff()

And with that, if you run a script with such decoration you'll get something like this output::

    ]$ python sample.py
    ... (script output if any)
    <Code time tracker __main__.my_func: 0:00:00.001063 timedelta, 2 calls>
