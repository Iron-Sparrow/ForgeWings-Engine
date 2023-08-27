import sys
import sdl2.ext
import sdl2

RESSOURCES = sdl2.ext.Resources(__file__, "res")

sdl2.ext.init()
window = sdl2.ext.Window("Hello World", size=(960, 600))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image(RESSOURCES.get_path("hello.png"))

sprite.position = 16, 10

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)

processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()