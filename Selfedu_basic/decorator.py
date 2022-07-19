def decorated(string, tag="h1", up=True):
    if up:
        tag = tag.upper()

    return f"<{tag}>{string}</{tag}>"


s = input()
print(decorated(s, tag="div"))
print(decorated(s, tag="div", up=False))
