#Coded on MacOS X Sonoma
from pprint import pprint
import moderngl as mgl
import glfw
import time as t
import const
# vars
width, height = 1280, 700
TUS = 0.0 #TUS means TimedUpdateSpeed
HzTUS = 0.0
glfw_exit = False


def Update(window):
    glfw.make_context_current(window)
    ctx = mgl.create_context(standalone=True, require=410)

    while not glfw.window_should_close(window):
        ctx.clear(0.0, 0.0, 0.0)
        #Update Loop

        glfw.swap_buffers(window)
        glfw.poll_events()

if __name__ == '__main__':
    glfw.init()
    # Preload Section
    TUS = 60.0 #TUS means TimeUpdateSpeed
    HzTUS = 1.0 / TUS
    
    if not glfw.init():
        raise Exception("GLFW initialization failed")
    
    window = glfw.create_window(width, height, "ModernGL Window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Window Creation Failed")
    else:
        Update(window)