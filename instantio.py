# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Instant Instance Object",
    "author" : "Enthralpy",
    "description" : "Autocreates particle with object instance.  Select two and only two objects.  The active object gets the particle system, and the other object becomes the child.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

class instantio_OT_Operator(bpy.types.Operator):
    bl_idname = "instantio.create"
    bl_label = "Simple operator"
    bl_description = "Autocreates particle with object instance.  Select two and only two objects.  The active object gets the particle system, and the other object becomes the child."
    
    def execute(self, context):
        obj = bpy.context.active_object
        obj.modifiers.new("ParticleSystem", type='PARTICLE_SYSTEM')
        ParticleSystem = obj.particle_systems[-1]
        settings = ParticleSystem.settings
        settings.render_type = 'OBJECT'
        objList = bpy.context.selected_objects
        objAct = bpy.context.active_object
        print(objList)
        selected = [obj for obj in objList if obj != objAct]
        print(selected)
        print(selected[0])
        settings.instance_object = bpy.data.objects[selected[0].name]
        return {'FINISHED'}
    
class instantio_PT_Panel (bpy.types.Panel):
    bl_idname = "InstantIO_PT_Panel"
    bl_label = "InstantIO Panel"
    bl_category = "InstantIO Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("instantio.create", text = "Create particle system")

classes = (instantio_OT_Operator, instantio_PT_Panel)
register, unregister = bpy.utils.register_classes_factory(classes)