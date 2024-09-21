from fasthtml import common as fh

app, rt = fh.fast_app()


@rt("/")
def getIndex():
    return fh.Div(fh.P("Hello World"), hx_get="/change")


@rt("/change")
def getChange():
    return fh.P("Nice to be here!")


if __name__ == "__main__":
    fh.serve()
