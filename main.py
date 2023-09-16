from pprint import pprint
import moderngl as mgl
import multiprocessing as mpr
import glfw
import time as t

# vars
width, height = 1280, 700
TUS = 0.0 # TimedUpdate() Speed
HzTUS = 0.0

GLFW_CLOSE_WINDOW = False

def Update(ctx, window):
    pprint(ctx.info["GL_VENDOR"])
    glfw.make_context_current(window)
    
    while GLFW_CLOSE_WINDOW == False:
        ctx.clear(0.0, 0.0, 0.0)
        #loop

        glfw.swap_buffers(window)
        glfw.poll_events()

def TimedUpdate(TUS, HzTUS):
    if TUS < 1.0 or HzTUS <= 0.0:
        glfw.terminate()
        raise ValueError(f"Problem with TUS: {TUS} or with HzTUS: {HzTUS}.")
    while GLFW_CLOSE_WINDOW == False:
        st = t.time()
        #loop
        
        if((t.time() - st) < HzTUS):
            t.sleep(abs(HzTUS - t.time()))

def Quit(UpdateProcess, TimedUpdateProcess):
    UpdateProcess.join()
    TimedUpdateProcess.join()
    UpdateProcess.terminate()
    TimedUpdateProcess.terminate()
    glfw.terminate()

def GlobalCheck(window):
    while True:
        if glfw.window_should_close(window):
            GLFW_CLOSE_WINDOW.value = True
              
if __name__ == '__main__':
    #Preload Section
    TUS = 60.0
    HzTUS = 1.0/TUS
    
    glfw.init()
    if not glfw.init():
        raise Exception("GLFW initialization failed")
    
    window = glfw.create_window(width, height, "ModernGL Window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Window Creation Failed")
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
       
        Quit(UpdateProcess, TimedUpdateProcess)