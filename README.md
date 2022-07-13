# Setup Blender Defaults

It's good occasionally to reset your default blender scene to the factory default as it gets updated. But I've collected a pile of changes that I like to make to the startup file that are a pain to redo every time I reset to default. So I wrote this script to automate as much of that as possible.

To use the script:

  - Load Factory Defaults
  - Switch to Scripting Workspace
  - Open the script
  - Run the script
  - Save factory defaults
  
  What settings does the stock script change?
  
  - Turn on Cycles
  - Set to Use GPU (you still need to enable your GPU device in settings)
  - Set Units to Millimeters
  - Set Preview samples to 200
  - Set Render samples to 1000
  - Turn on viewport denoising
  - turn on film transparent
  
  - Zoom to Mouse
  - Advanced Numeric Input
  - Turn off Splash
  - Show developer options
  - Show python tooltips
  
  - Turn off Gizmos in all 3d viewports
  - Turn on Cavity, Shadows and Stats in 'Layout' and 'Modeling'
  
  - Enable these add-ons
    - curve_tools
    - add_curve_extra_objects
    - add_mesh_extra_objects
    - mesh_looptools
    - pace_view3d_modifier_tools
    - space_view3d_align_tools
    - object_boolean_tools
    - object_edit_linked
    - node_wrangler
    - io_import_images_as_planes
    - matslotcleaner-master
    - ImagePaste-main
    - set_viewport_color

  - Delete all scene items
  - Add a straight aligned camera
  - Remove setup script
  - Save settings
