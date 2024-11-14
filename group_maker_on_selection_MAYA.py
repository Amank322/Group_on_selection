import maya.cmds as cmds

# Get the current selection
selection = cmds.ls(sl=True)

if selection:
    # Create a group with the name of the selected object and append '_outliner'
    group_name = f"{selection[0]}_outliner"
    group = cmds.group(em=True, name=group_name)

    # Parent the selected objects to the group
    cmds.parent(group , selection)

    # Set the group's attributes
    cmds.setAttr(f"{group}.rotateX", 0)
    cmds.setAttr(f"{group}.rotateY", 0)
    cmds.setAttr(f"{group}.rotateZ", 0)
    cmds.setAttr(f"{group}.translateX", 0)
    cmds.setAttr(f"{group}.translateY", 0)
    cmds.setAttr(f"{group}.translateZ", 0)
else:
    print("No objects selected.")
