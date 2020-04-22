bl_info = {
    "name" : "Shortcuts for Blending modes",
    "author" : "Alumx",
    "description" : "Adds ability to create shortcuts for blending modes",
    "blender" : (2, 90, 0),
    "version" : (0, 1, 3),
    "location" : "",
    "warning" : "",
    "category" : "Paint",
    "wiki_url": "https://github.com/Alumx/BlendingHotkeys",
}

import bpy
from bpy.types import Menu



class BlendModeMix(bpy.types.Operator):
    bl_idname = "blendmode.mix"
    bl_label = "Set blending mode to mix"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'MIX'
        return {'FINISHED'}
      
    
class BlendModeDark(bpy.types.Operator):
    bl_idname = "blendmode.dark"
    bl_label = "Set blending mode to dark"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'DARKEN'
        return {'FINISHED'}
  
  

class BlendModeMul(bpy.types.Operator):
    bl_idname = "blendmode.mul"
    bl_label = "Set blending mode to multiply"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'MUL'
        return {'FINISHED'}
  


class BlendModeColorburn(bpy.types.Operator):
    bl_idname = "blendmode.colorburn"
    bl_label = "Set blending mode to colorburn"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'COLORBURN'
        return {'FINISHED'}
  
  

class BlendModeLinearburn(bpy.types.Operator):
    bl_idname = "blendmode.linearburn"
    bl_label = "Set blending mode to linearburn"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'LINEARBURN'
        return {'FINISHED'}
  


class BlendModeLighten(bpy.types.Operator):
    bl_idname = "blendmode.lighten"
    bl_label = "Set blending mode to lighten"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'LIGHTEN'
        return {'FINISHED'}
  
  

class BlendModeScreen(bpy.types.Operator):
    bl_idname = "blendmode.screen"
    bl_label = "Set blending mode to screen"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'SCREEN'
        return {'FINISHED'}
  
  

class BlendModeColordodge(bpy.types.Operator):
    bl_idname = "blendmode.colordodge"
    bl_label = "Set blending mode to color dodge"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'COLORDODGE'
        return {'FINISHED'}
  
  

class BlendModeOverlay(bpy.types.Operator):
    bl_idname = "blendmode.overlay"
    bl_label = "Set blending mode to overlay"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'OVERLAY'
        return {'FINISHED'}
  


class BlendModeSoftlight(bpy.types.Operator):
    bl_idname = "blendmode.softlight"
    bl_label = "Set blending mode to soft light"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'SOFTLIGHT'
        return {'FINISHED'}
  


class BlendModeHardlight(bpy.types.Operator):
    bl_idname = "blendmode.hardlight"
    bl_label = "Set blending mode to hard light"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'HARDLIGHT'
        return {'FINISHED'}
  



class BlendModeVividlight(bpy.types.Operator):
    bl_idname = "blendmode.vividlight"
    bl_label = "Set blending mode to vivid light"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'VIVIDLIGHT'
        return {'FINISHED'}
  



class BlendModeLinearlight(bpy.types.Operator):
    bl_idname = "blendmode.linearlight"
    bl_label = "Set blending mode to linear light"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'LINEARLIGHT'
        return {'FINISHED'}
  



class BlendModePinlight(bpy.types.Operator):
    bl_idname = "blendmode.pinlight"
    bl_label = "Set blending mode to pin light"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'PINLIGHT'
        return {'FINISHED'}
  



class BlendModeDifference(bpy.types.Operator):
    bl_idname = "blendmode.difference"
    bl_label = "Set blending mode to difference"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'DIFFERENCE'
        return {'FINISHED'}
  



class BlendModeExclusion(bpy.types.Operator):
    bl_idname = "blendmode.exclusion"
    bl_label = "Set blending mode to exclusion"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'EXCLUSION'
        return {'FINISHED'}
  



class BlendModeSub(bpy.types.Operator):
    bl_idname = "blendmode.sub"
    bl_label = "Set blending mode to subtract"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'SUB'
        return {'FINISHED'}
  



class BlendModeHue(bpy.types.Operator):
    bl_idname = "blendmode.hue"
    bl_label = "Set blending mode to hue"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'HUE'
        return {'FINISHED'}
  



class BlendModeSaturation(bpy.types.Operator):
    bl_idname = "blendmode.saturation"
    bl_label = "Set blending mode to saturation"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'SATURATION'
        return {'FINISHED'}
  



class BlendModeCalor(bpy.types.Operator):
    bl_idname = "blendmode.color"
    bl_label = "Set blending mode to color"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'COLOR'
        return {'FINISHED'}
  



class BlendModeLuminosity(bpy.types.Operator):
    bl_idname = "blendmode.luminosity"
    bl_label = "Set blending mode to luminosity"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'LUMINOSITY'
        return {'FINISHED'}
  



class BlendModeErase_alpha(bpy.types.Operator):
    bl_idname = "blendmode.erase_alpha"
    bl_label = "Set blending mode to erase alpha"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'ERASE_ALPHA'
        return {'FINISHED'}
  



class BlendModeAdd_alpha(bpy.types.Operator):
    bl_idname = "blendmode.add_alpha"
    bl_label = "Set blending mode to add alpha"

    def execute(self, context):
        bpy.context.tool_settings.image_paint.brush.blend = 'ADD_ALPHA'
        return {'FINISHED'}
  




def register():
    bpy.utils.register_class(BlendModeAdd_alpha)
    bpy.utils.register_class(BlendModeCalor)
    bpy.utils.register_class(BlendModeColorburn)
    bpy.utils.register_class(BlendModeColordodge)
    bpy.utils.register_class(BlendModeDark)
    bpy.utils.register_class(BlendModeDifference)
    bpy.utils.register_class(BlendModeErase_alpha)
    bpy.utils.register_class(BlendModeExclusion)
    bpy.utils.register_class(BlendModeHardlight)
    bpy.utils.register_class(BlendModeHue)
    bpy.utils.register_class(BlendModeLighten)
    bpy.utils.register_class(BlendModeLinearburn)
    bpy.utils.register_class(BlendModeLuminosity)
    bpy.utils.register_class(BlendModeMix)
    bpy.utils.register_class(BlendModeMul)
    bpy.utils.register_class(BlendModeOverlay)
    bpy.utils.register_class(BlendModePinlight)
    bpy.utils.register_class(BlendModeSaturation)
    bpy.utils.register_class(BlendModeScreen)
    bpy.utils.register_class(BlendModeSoftlight)
    bpy.utils.register_class(BlendModeSub)
    bpy.utils.register_class(BlendModeVividlight)

def unregister():
    bpy.utils.register_class(BlendModeAdd_alpha)
    bpy.utils.register_class(BlendModeCalor)
    bpy.utils.register_class(BlendModeColorburn)
    bpy.utils.register_class(BlendModeColordodge)
    bpy.utils.register_class(BlendModeDark)
    bpy.utils.register_class(BlendModeDifference)
    bpy.utils.register_class(BlendModeErase_alpha)
    bpy.utils.register_class(BlendModeExclusion)
    bpy.utils.register_class(BlendModeHardlight)
    bpy.utils.register_class(BlendModeHue)
    bpy.utils.register_class(BlendModeLighten)
    bpy.utils.register_class(BlendModeLinearburn)
    bpy.utils.register_class(BlendModeLuminosity)
    bpy.utils.register_class(BlendModeMix)
    bpy.utils.register_class(BlendModeMul)
    bpy.utils.register_class(BlendModeOverlay)
    bpy.utils.register_class(BlendModePinlight)
    bpy.utils.register_class(BlendModeSaturation)
    bpy.utils.register_class(BlendModeScreen)
    bpy.utils.register_class(BlendModeSoftlight)
    bpy.utils.register_class(BlendModeSub)
    bpy.utils.register_class(BlendModeVividlight)    


if __name__ == "__main__":
    register()    
