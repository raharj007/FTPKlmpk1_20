def pathconvert(root, path):
    if root in path:
        path=path.replace(root, "\\")
        return path
    return path