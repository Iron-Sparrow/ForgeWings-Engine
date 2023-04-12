import pygfx as gfx

class Camera:
    def __init__(self,fov: int,  width: int, height: int, near: float, far: int):
        self.fov = fov
        self.width = width
        self.height = height
        self.near = near
        self.far = far

class AntiAliasing:
    def __init__(self, type: str):
        type = type.upper()
        if(type == 'FXAA'):
            pass
        elif(type == 'MSAA'):
            pass
        elif(type == 'SSAA'):
            pass
        elif(type == 'SMAA'):
            pass
        elif(type == 'TAA'):
            pass
        elif(type == 'CSAA'):
            pass
        elif(type == 'DLAA'):
            pass
        elif(type == 'EQAA'):
            pass
        elif(type == 'NONE' or type == 'OFF'):
            pass
        else:
            raise ValueError("AntiAliasing type not found")

class Upscaling:
    def __init__(self, type: str):
        type = type.upper()
        if(type == 'BICUBIC' or type == 'BC'):
            pass
        elif(type == 'BILINEAR' or type == 'BL'):
            pass
        elif(type == 'NEARESTNEIGHBOR' or type == 'NN' or type == "NEAR"):
            pass
        elif(type == 'LANCZOS' or type == 'LZ'):
            pass
        elif(type == 'FIDELITYFX' or type == 'FSR1' or type == 'FIDELITYFXSUPERRESOLUTION'):
            pass
        elif(type == 'FSR2' or type == 'FIDELITYFX2' or type == 'FIDELITYFXSUPPERRESOLUTION2'):
            pass
        elif(type == 'DLSS' or type == 'DEEPLEARNINGSUPERSAMPLING'):
            pass
        elif(type == 'NONE' or type == 'OFF'):
            pass
        else:
            raise ValueError("Upscaling type not found")

