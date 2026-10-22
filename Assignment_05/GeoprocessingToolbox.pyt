import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Geospatial Data Processing Toolbox"
        self.alias = "GeospatialToolbox"
        # List of tool classes associated with this toolbox
        self.tools = [AppendWithFieldMapping]

class AppendWithFieldMapping(object):
    def __init__(self):
        """Define the tool (tool name, label, and description)."""
        self.label = "Append with Field Mapping"
        self.description = "Appends point data from a source layer to a target layer using explicit field mapping."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        
        # 1. Checkbox to Enable/Disable Target Layer
        param0 = arcpy.Parameter(
            displayName="Enable Target Layer Selection",
            name="enable_target",
            datatype="GPBoolean",
            parameterType="Required",
            direction="Input"
        )
        param0.value = True # Default to checked

        # 2. Target Layer (Required)
        param1 = arcpy.Parameter(
            displayName="Target Layer",
            name="target_layer",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )
        
        # 3. Checkbox to Enable/Disable Input Layer
        param2 = arcpy.Parameter(
            displayName="Enable Input Layer Selection",
            name="enable_input",
            datatype="GPBoolean",
            parameterType="Required",
            direction="Input"
        )
        param2.value = True

        # 4. Input Layer (Optional, restricted to Point Feature Classes)
        param3 = arcpy.Parameter(
            displayName="Input Layer (Points Only)",
            name="input_layer",
            datatype="GPFeatureLayer",
            parameterType="Optional",
            direction="Input"
        )
        # Apply filter to only accept Point geometry
        param3.filter.list = ["Point"]

        # 5. Field Mapping Parameter
        param4 = arcpy.Parameter(
            displayName="Field Map",
            name="field_mapping",
            datatype="GPFieldMapping",
            parameterType="Optional",
            direction="Input"
        )
        # Tie the field mapping schema directly to the Target Layer
        param4.parameterDependencies = [param1.name]

        return [param0, param1, param2, param3, param4]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the characteristics of parameters before internal validation is called.
        This method is called whenever a parameter has been changed."""
        
        # Enable or Disable Target Layer based on its checkbox
        if not parameters[0].altered:
            parameters[1].enabled = parameters[0].value
        else:
            parameters[1].enabled = parameters[0].value

        # Enable or Disable Input Layer based on its checkbox
        if not parameters[2].altered:
            parameters[3].enabled = parameters[2].value
        else:
            parameters[3].enabled = parameters[2].value

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool parameter.
        This method is called after internal validation."""
        
        # Custom Validation: If Target Layer is enabled but left empty, raise an error
        if parameters[1].enabled and not parameters[1].hasBeenValidated:
            if not parameters[1].value:
                parameters[1].setErrorMessage("Target Layer is required when selection is enabled.")
                
        # Custom Validation: If Input Layer checkbox is enabled but no layer is provided
        if parameters[3].enabled and not parameters[3].value:
            parameters[3].setWarningMessage("Input Layer is optional, but current selection is empty.")

        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        target_layer = parameters[1].valueAsText
        input_layer = parameters[3].valueAsText
        field_mapping = parameters[4].value

        # Only execute if both layers are provided
        if input_layer and target_layer:
            messages.addMessage(f"Appending {input_layer} into {target_layer} using field mappings...")
            try:
                # Perform the append operation with Field Mapping
                arcpy.management.Append(
                    inputs=input_layer,
                    target=target_layer,
                    schema_type="NO_TEST", # Uses field mapping rules
                    field_mapping=field_mapping
                )
                messages.addMessage("Append operation completed successfully.")
            except arcpy.ExecuteError:
                messages.addErrorMessage(arcpy.GetMessages(2))
        else:
            messages.addWarningMessage("Append skipped: Missing input or target layer configuration.")
        
        return