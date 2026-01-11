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
        self.coords = coords if coords is not None else [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self
                 , name: str
                 , weight: int
                 , coords: list | None = None
                 ) -> None:
        coords = coords if coords is not None else [0, 0, 0]
        super().__init__(name, weight, coords[:2])
        self.coords = coords

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step

