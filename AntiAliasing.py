import pygfx as gfx
from pygfx.renderers.wgpu import WgpuRenderer, register_wgpu_render_function, WorldObjectShader, RenderMask, Binding

tp = 'render'

@register_wgpu_render_function(SomeWorldObject, SomeMaterial)
class FXAA(WorldObjectShader):
    type = tp

    def get_binding(self, wobject, shared):
        bindings = [
            Binding("u_stdinfo", "buffer/uniform", shared.uniform_buffer),
            Binding("u_wobject", "buffer/uniform", wobject.uniform_buffer),
            Binding("u_material", "buffer/uniform", wobject.material.uniform_buffer),
            ...
        ]
        bindings = {i:b for i, b in enumerate(bindings)}

        self.define_bindings(0, bindings)

        return {
            0: bindings,
        }

    def get_pipeline_info(self, wobject, shared):
        return {
            "primitive_topology": wgpu.PrimitiveTopology.triangle_list,
            "cull_mode": wgpu.CullMode.none,
        }

    def get_render_info(self, wobject, shared):
        n_vertices = ...
        n_instances = 1
        render_mask = wobject.render_mask
        if not render_mask:
            render_mask = RenderMask.all

        return {
            "indices": (n_vertices, n_instances),
            "render_mask": render_mask,
        }

    def get_code(self):
         return (
            self.code_definitions()
            + self.code_common()
            + self.code_vertex()
            + self.code_fragment()
        )
    def code_vertex(self):
        return """
        @stage(vertex)
        fn vs_main(@builtin(vertex_index) VertexIndex: u32) -> [[builtin(position)]] vec4<f32> {
            ...
        }
        """

    def code_fragment(self):
        return """
        @stage(fragment)
        fn fs_main() -> FragmentOutput{
            ...
        }
        """

class MSAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

class SSAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

    def get_code(self):
        pass

    def code_vertex(self):
        pass

    def code_fragment(self):
        pass

class SMAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

    def get_code(self):
        pass

    def code_vertex(self):
        pass

    def code_fragment(self):
        pass

class TAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

    def get_code(self):
        pass

    def code_vertex(self):
        pass

    def code_fragment(self):
        pass

class CSAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

    def get_code(self):
        pass

    def code_vertex(self):
        pass

    def code_fragment(self):
        pass

class DLAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

    def get_code(self):
        pass

    def code_vertex(self):
        pass

    def code_fragment(self):
        pass

class EQAA:
    type = tp

    def get_binding(self, wobject, shared):
        pass

    def get_pipeline_info(self, wobject, shared):
        pass

    def get_render_info(self, wobject, shared):
        pass

    def get_code(self):
        pass

    def code_vertex(self):
        pass

    def code_fragment(self):
        pass