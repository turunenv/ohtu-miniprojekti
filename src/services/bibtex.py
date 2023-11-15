class Bibtex():
    def __init__(self, docutype, citekey):
        self.docutype = docutype
        self.citekey = citekey
        self.bibDict = {}
    def __str__(self):
        looped = self.loop_to_string()
        return(
            f"@{docutype}\{{citekey},"
            f"{looped}"
            f"\}"
        )
    def loop_to_string(self):
        ret = ""
        for x in self.bibDict:
            ret += "\n  "
            ret += x
            ret += " = \""
            ret += bibDict(x)
            ret += "\","

    def add(key, value):
        self.bibDict[key] = value