#Coded on MacOS X Sonoma 14
from pprint import pprint
import moderngl as mgl
import multiprocessing as mpr
import glfw
import time as t

# vars
width, height = 1280, 700
TUS = 0.0 #TUS means TimedUpdateSpeed
HzTUS = 0.0

def Update(ctx, window, GLFW_CLOSE_WINDOW):
    glfw.make_context_current(window)
    
    while not GLFW_CLOSE_WINDOW.value:
        ctx.clear(0.0, 0.0, 0.0)
        #Update Loop

        glfw.swap_buffers(window)
        glfw.poll_events()

def TimedUpdate(ctx, TUS, HzTUS, GLFW_CLOSE_WINDOW):
    if TUS < 1.0 or HzTUS <= 0.0:
        glfw.terminate()
        raise ValueError(f"Problem with TUS: {TUS} or with HzTUS: {HzTUS}.")
    while not GLFW_CLOSE_WINDOW.value:
        st = t.time()
        #TimedUpdate Loop

        if (t.time() - st) < HzTUS:
            t.sleep(abs(HzTUS - t.time()))

def Quit(UpdateProcess, TimedUpdateProcess):
    UpdateProcess.terminate()
    TimedUpdateProcess.terminate()
    UpdateProcess.join()
    TimedUpdateProcess.join()
    glfw.terminate()

def GlobalCheck(window, GLFW_CLOSE_WINDOW):
    while not GLFW_CLOSE_WINDOW.value:
        if glfw.window_should_close(window):
            GLFW_CLOSE_WINDOW.value = True

if __name__ == '__main__':
    # Preload Section
    TUS = 60.0 #TUS means TimeUpdateSpeed
    HzTUS = 1.0 / TUS
    
    glfw.init()
    if not glfw.init():
        raise Exception("GLFW initialization failed")
    
    window = glfw.create_window(width, height, "ModernGL Window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Window Creation Failed")

    # Create a shared ModernGL context
    with mpr.Manager() as manager:
        GLFW_CLOSE_WINDOW = manager.Value('b', False)
        shared_ctx = mgl.create_context(standalone=True, require=410, share=True)

        UpdateProcess = mpr.Process(target=Update, args=(shared_ctx, window, GLFW_CLOSE_WINDOW))
        TimedUpdateProcess = mpr.Process(target=TimedUpdate, args=(shared_ctx, TUS, HzTUS, GLFW_CLOSE_WINDOW))
        CheckProcess = mpr.Process(target=GlobalCheck, args=(window, GLFW_CLOSE_WINDOW))
        # End of Preload Section
        UpdateProcess.start()
        TimedUpdateProcess.start()
        CheckProcess.start()