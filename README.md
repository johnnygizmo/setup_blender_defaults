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
  - Adpative Threshold to 0.05
  - Preview Adaptive Threshold to 0.2
  - Enable Optix
  - Enable All Render Devices
   
  - Zoom to Mouse
  - Advanced Numeric Input
  - Turn off Splash
  - Show developer options
  - Show python tooltips
  
  - Add a list of asset library paths
  - Add a list of modules to enable
  
  - Turn off Gizmos in all 3d viewports
  - Turn on Cavity and Stats in 'Layout' and 'Modeling' workspaces

  - Delete all scene items
  - Add a straight aligned camera
  - Remove setup script
  - Save settings
