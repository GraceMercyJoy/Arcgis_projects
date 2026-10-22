# -*- coding: utf-8 -*-

import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Buffer Toolbox"
        self.alias = "buffertool"
        self.tools = [Tool]


class Tool(object):

    def __init__(self):
        self.label = "Buffer Tool"
        self.description = "Creates a buffer around input features"

    def getParameterInfo(self):

        input_fc = arcpy.Parameter(
            displayName="Input Features",
            name="input_fc",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )

        distance = arcpy.Parameter(
            displayName="Buffer Distance",
            name="distance",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        output_fc = arcpy.Parameter(
            displayName="Output Feature Class",
            name="output_fc",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"
        )

        return [input_fc, distance, output_fc]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):

        arcpy.analysis.Buffer(
            in_features=parameters[0].valueAsText,
            out_feature_class=parameters[2].valueAsText,
            buffer_distance_or_field=parameters[1].valueAsText
        )

        arcpy.AddMessage("Buffer created successfully")

    def postExecute(self, parameters):
        return