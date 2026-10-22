# import arcpy
# import os

# gdb = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Data_Creation\Data_Creation.gdb"

# print(os.path.exists(gdb))

# arcpy.env.workspace = gdb
# arcpy.env.overwriteOutput = True

# sr = arcpy.SpatialReference(4326)

# arcpy.management.CreateFeatureDataset(
#     out_dataset_path=gdb,
#     out_name="Dataset_Name",
#     spatial_reference=sr
# )

# arcpy.management.CreateFeatureclass(
#     out_path=gdb,
#     out_name="OutFeatureClass_Name",
#     geometry_type="POLYLINE",
#     spatial_reference=sr
# )

# dataset = gdb + "\\Dataset_Name"

# arcpy.management.CreateFeatureclass(
#     out_path=dataset,
#     out_name="FeatureClass_Name",
#     geometry_type="POINT",
#     spatial_reference=sr
# )



# # -------------------------------------------------
# # Environment
# # -------------------------------------------------

# gdb = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Assignment_02\DataCreation\DataCreation.gdb"

# arcpy.env.workspace = gdb
# arcpy.env.overwriteOutput = True

# # WGS 84
# sr = arcpy.SpatialReference(4326)

# # -------------------------------------------------
# # Create Feature Dataset
# # -------------------------------------------------

# dataset_name = "Dataset_Name"

# if not arcpy.Exists(os.path.join(gdb, dataset_name)):
#     arcpy.management.CreateFeatureDataset(
#         out_dataset_path=gdb,
#         out_name=dataset_name,
#         spatial_reference=sr
#     )

# import arcpy

# arcpy.env.overwriteOutput = True

# sr = arcpy.SpatialReference(4326)

# csv_file = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Assignment_02\DataCreation\Input\IndiaCities.csv"

# print(os.path.exists(csv_file))

# output_shp = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Assignment_02\DataCreation\IndiaCities_XYTableToPoint.shp"

# try:
#     arcpy.management.XYTableToPoint(
#         in_table=csv_file,
#         out_feature_class=output_shp,
#         x_field="Lon",
#         y_field="Lat",
#         coordinate_system=sr
#     )

#     print("Shapefile created successfully!")

#     print(arcpy.GetMessages())

# import arcpy

# gdb = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Data_Creation\Data_Creation.gdb"

# input_shp = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Assignment_02\DataCreation\IndiaCities_XYTableToPoint.shp"

# output_fc = gdb + r"\IndiaCities"

# arcpy.env.overwriteOutput = True

# arcpy.management.CopyFeatures(
#     in_features=input_shp,
#     out_feature_class=output_fc
# )

# print("Shapefile copied into Geodatabase successfully!")

import arcpy

aprx = arcpy.mp.ArcGISProject(r"CURRENT")
m = aprx.activeMap

gdb = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Data_Creation\Data_Creation.gdb"

output_fc = gdb + r"\IndiaCities"

m.addDataFromPath(output_fc)

print("Layer added to map.")