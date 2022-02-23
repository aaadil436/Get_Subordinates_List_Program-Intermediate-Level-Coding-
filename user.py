class User:
    id: int
    role: int
    name: str

    def __init__(self, id: int, name: str, role: int):
        self.id = id
        self.name = name
        self.role = role
