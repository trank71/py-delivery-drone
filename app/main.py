class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class  BaseRobot:
    def __init__(self
                 ,name: str
                 , weight: int
                 , coords: list | None = None
                 ) -> None:
        self.weight = weight
        self.name = name
        self.coords = coords or [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step = 1) -> None:
        self.coords[1] += step

    def go_back(self, step = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step = 1) -> None:
        self.coords[0] += step

    def go_left(self, step = 1) -> None:
        self.coords[0] -= step

