class Role:
    id: int
    parent: int
    name: str

    def __init__(self, id: int, name: str, parent: int):
        self.id = id
        self.name = name
        self.parent = parent
