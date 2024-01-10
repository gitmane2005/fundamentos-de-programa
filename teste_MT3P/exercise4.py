def list_paths(dirtree):
    path = []
    if type(dirtree[1]) == str:
        return dirtree[1]
    else:
        for x in dirtree[1]:
            if type(x) == tuple:
                t = list_paths(x)
                for i in t:
                    path.append(dirtree[0]+ "/" + i)
            else:
                path.append(dirtree[0]+ "/" + x)
    return path

example = ("root",
             [("a",
                [("e",
                   ["i"]),
                "f.py",
                "g.c",
                "h.lst"
             ]),
             "b.txt",
             "c.dat",
             ("d",
                ["j",
                "d.py",
                "d.ext",
                "k"
             ])
           ])
example2 = ("a",
                [("e",
                   ["i"]),
                "f.py",
                "g.c",
                "h.lst"
             ])
#print(list_paths(example))