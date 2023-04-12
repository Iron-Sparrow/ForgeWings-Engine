import pygfx as gfx

class Camera:
    def __init__(self,fov: int,  width: int, height: int, near: float, far: int):
        self.fov = fov
        self.width = width
        self.height = height
        self.near = near
        self.far = far
