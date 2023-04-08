from time import sleep
import glfw
import moderngl as mgl
from settings import *
from const import *
from texture import *

# initialize glfw
glfw.init()

# create window
window = glfw.create_window(1280, 720, 'preview', None, None)
glfw.make_context_current(window)

# create moderngl context
ctx = mgl.create_context(require=410, standalone=True)

# load the background texture
background, _ = LoadBackground("Lines.png", ctx)

#debug

def loop():
    while not glfw.window_should_close(window):
        # render
        ctx.clear(0.0, 0.0, 0.0, 1.0)

        # render the background texture
        background.use()

        # show frame
        glfw.swap_buffers(window)

        # user input    
        if glfw.get_key(window, glfw.KEY_BACKSPACE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)
            
        # events
        glfw.poll_events()

        # cap
        sleep(c1000)
        
    while glfw.window_should_close(window):
        glfw.terminate()

loop()
