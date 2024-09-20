import moderngl as mgl
import glfw
import time as t
import const
import numba
import numpy as np

width, height = 960, 600

@numba.jit(fastmath=True)
def Update(window, ctx, program, vao) -> None:
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        ot = t.time()
        ctx.clear()
        ctx.program = program  # Lier le programme ici
        vao.render()
        glfw.swap_buffers(window)
        glfw.poll_events()
        dt = t.time() - ot

if __name__ == '__main__':
    glfw.init()

    if not glfw.init():
        raise Exception("GLFW initialization failed")

    window = glfw.create_window(width, height, "ModernGL Window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Window Creation Failed")

    ctx = mgl.create_context(standalone=True, require=330)

    vertex_shader = """
    #version 330
    in vec2 in_vert;
    void main() {
        gl_Position = vec4(in_vert, 0.0, 1.0);
    }
    """

    fragment_shader = """
    #version 330
    out vec4 frag_color;
    void main() {
        frag_color = vec4(1.0, 0.0, 0.0, 1.0);  // Red color
    }
    """

    prog = ctx.program(
        vertex_shader=vertex_shader,
        fragment_shader=fragment_shader)

    vertices = np.array([-0.6, -0.6, 0.6, -0.6, 0.0, 0.6], dtype='f4')
    vbo = ctx.buffer(vertices)
    vao = ctx.simple_vertex_array(prog, vbo)

    Update(window, ctx, prog, vao)
