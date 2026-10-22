import arcpy

gdb = r"C:\Users\Harshavarthan Madras\Documents\ArcGIS\Projects\Assignment_02\DataCreation\DataCreation.gdb"

arcpy.env.workspace = gdb
arcpy.env.overwriteOutput = True

sr = arcpy.SpatialReference(4326)

# Create Feature Dataset
arcpy.management.CreateFeatureDataset(
    out_dataset_path=gdb,
    out_name="Dataset_Name",
    spatial_reference=sr
)

# Create Line Feature Class
arcpy.management.CreateFeatureclass(
    out_path=gdb,
    out_name="OutFeatureClass_Name",
    geometry_type="POLYLINE",
    spatial_reference=sr
)

# Create Point Feature Class inside Feature Dataset
dataset = gdb + "\\Dataset_Name"

arcpy.management.CreateFeatureclass(
    out_path=dataset,
    out_name="FeatureClass_Name",
    geometry_type="POINT",
    spatial_reference=sr
)

print("Feature classes created successfully.")