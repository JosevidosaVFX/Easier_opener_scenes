obj = hou.node("/obj")
geo = obj.children()

def easier():
    """Turn off the node display and save the scene +1"""
    # Goes through the nodes of the geo type.
    for node in geo:
        node_type = node.type().name()
        if node_type == "geo" or node_type== "subnet":
            
            # Turn off the display.                        
            node.setDisplayFlag(False)               
            
    # Save the scene with increment.        
    scene = hou.hipFile.saveAndIncrementFileName() 

# Call the function.
easier()