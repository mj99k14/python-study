def bar():
    print("hello")


def foo(arg_name):
    arg_name()


foo(bar)
