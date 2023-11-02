def penup_always(func):

    def pen_up(*args, **kwargs):
        canvas = args[0].canvas
        canvas.penup()
        func(*args, **kwargs)
        canvas.penup()

    return pen_up
