from time import sleep
from settings import *
from const import *
from colors import *
import pygfx as gfx
from wgpu.gui.auto import WgpuCanvas, run

canv = WgpuCanvas(title="PyGFX", size=(1280, 720))
rend = gfx.renderers.WgpuRenderer(canv)
camera = Camera(80, 1280, 720, 0.1, 2000)
cam = gfx.PerspectiveCamera(80, camera.width / camera.height, 0.1, 2000) # type: ignore
disp = gfx.Display(canvas= canv, renderer= rend, camera= cam)
#initialising
scene = gfx.Scene()

def loop():
    while True:
        disp.show(scene)
        # cap
        sleep(c1000)

loop()