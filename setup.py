import bpy

# Scene Settings Here
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'
bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
bpy.context.scene.cycles.preview_samples = 200
bpy.context.scene.cycles.samples = 1000
bpy.context.scene.cycles.use_preview_denoising = True
bpy.context.scene.cycles.adaptive_threshold = 0.05
bpy.context.scene.cycles.preview_adaptive_threshold = 0.2
bpy.context.scene.render.film_transparent = True

#Preferences
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = "OPTIX" # ('NONE', 'CUDA', 'OPTIX', 'HIP', 'ONEAPI')
for device in  bpy.context.preferences.addons['cycles'].preferences.devices:
    device.use = True

bpy.context.preferences.inputs.use_zoom_to_mouse=True
bpy.context.preferences.inputs.use_numeric_input_advanced=True
bpy.context.preferences.view.show_splash=False
bpy.context.preferences.view.show_developer_ui=True
bpy.context.preferences.view.show_tooltips_python=True

#Set Workspace Area Defaults

for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == "VIEW_3D":
            for space in area.spaces:
                space.show_gizmo = False


for i in bpy.data.screens['Layout'].areas:
    if i.type == "VIEW_3D":
        for j in i.spaces:
            j.shading.show_cavity = True
            j.overlay.show_stats = True
            
for i in bpy.data.screens['Modeling'].areas:
    if i.type == "VIEW_3D":
        for j in i.spaces:
            j.shading.show_cavity = True
            j.overlay.show_stats = True 
                   

# Addons to Enable
modules = [
    'curve_tools',
    'add_curve_extra_objects',
    'add_mesh_extra_objects',
    'mesh_looptools',
    'space_view3d_modifier_tools',
    'space_view3d_align_tools',
    'object_boolean_tools',
    'object_edit_linked',
    'node_wrangler',
    'io_import_images_as_planes',
    'matslotcleaner-master',
    'ImagePaste-main',
    'set_viewport_color'
]

# Default Setup
##Delete Everything
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

##Add New Camera Straigt on and X rotation locked
bpy.ops.object.camera_add(enter_editmode=False, location=(0, -6, 1.6764), rotation=(1.57079632679,0, 0), scale=(1, 1, 1))
##Deselect All
bpy.ops.object.select_all(action='DESELECT')

#Change to Layout Screen
bpy.context.window.workspace = bpy.data.workspaces['Layout']

###############################################################################
#
# DO NOT EDIT BELOW HERE
#
###############################################################################


message = ""
for m in modules:
    try:
        bpy.ops.preferences.addon_enable(module=m)
    except:
        message = message + m + ", "
        continue
    
def draw(self, context):
    self.layout.label(text=message)

if message != "":
    bpy.context.window_manager.popup_menu(draw, title="Not Installed", icon='INFO')    

bpy.ops.text.unlink()

bpy.ops.wm.save_homefile()
bpy.ops.wm.save_userpref()
