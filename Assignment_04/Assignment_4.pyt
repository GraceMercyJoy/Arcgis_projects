import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Geospatial Processor"
        self.alias = "geoprocessor"
        self.tools = [GeoprocessingTool]

class GeoprocessingTool(object):
    def __init__(self):
        """Define the tool (tool name, label, and description)."""
        self.label = "Kumar"
        self.description = "A custom tool featuring Feature Class, String, and SQL Expression parameters."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        
        # Parameter 1: DEFeatureClass (Input Feature Class)
        param0 = arcpy.Parameter(
            displayName="Feature Class",
            name="in_features",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input"
        )

        # Parameter 2: String (GPString)
        param1 = arcpy.Parameter(
            displayName="String",
            name="in_string",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        # Parameter 3: GPSQLExpression (SQL Expression helper)
        param2 = arcpy.Parameter(
            displayName="SQL Expression",
            name="sql_expression",
            datatype="GPSQLExpression",
            parameterType="Required",
            direction="Input"
        )

        # Tie the SQL Expression helper to the fields of the chosen Feature Class (param0)
        param2.parameterDependencies = [param0.name]

        params = [param0, param1, param2]
        return params

    def isLicensed(self):
        """Allow the tool to run."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is run."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each parameter."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        feature_class = parameters[0].valueAsText
        input_string = parameters[1].valueAsText
        sql_query = parameters[2].valueAsText

        messages.addMessage(f"Input Feature Class: {feature_class}")
        messages.addMessage(f"Input String: {input_string}")
        messages.addMessage(f"SQL Filter applied: {sql_query}")
        return