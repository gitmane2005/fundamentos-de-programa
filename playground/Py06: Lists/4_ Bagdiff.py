def bagdiff(xs, ys):
    for a in ys:
        for b in xs:
            if a == b:
                xs.remove(b)
                break

    return xs