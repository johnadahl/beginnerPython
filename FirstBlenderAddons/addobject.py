import bpy

class Test_Panel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = 'PT_TestPanel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'phart'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = 'your mom', icon = 'MESH_CUBE')
        row = layout.row()
        row.operator('mesh.primitive_cube_add')
        
        
        
        
def register():
    bpy.utils.register_class(Test_Panel)
    
def unregister():
    bpy.utils.unregister_class(Test_Panel)
    
if __name__ == "__main__":
    register()
    