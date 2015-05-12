
Usefull links

http://suite.opengeo.org/4.1/dataadmin/pgGettingStarted/shp2pgsql.html
http://prj2epsg.org/search


GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]

CRID

4326 - GCS_WGS_1984


Command to see info 
zdimon@home:~/www/fbr_ve/fbr/vector_data$ ogrinfo slope_250.shx slope_250 -so



INFO: Open of `cotter_veg_original.shp'
      using driver `ESRI Shapefile' successful.

Layer name: cotter_veg_original
Geometry: Polygon
Feature Count: 291
Extent: (659752.727281, 6040783.679494) - (676400.894535, 6095665.781663)
Layer SRS WKT:
PROJCS["AGD_1966_AMG_Zone_55",
    GEOGCS["GCS_Australian_1966",
        DATUM["Australian_Geodetic_Datum_1966",
            SPHEROID["Australian",6378160.0,298.25]],
        PRIMEM["Greenwich",0.0],
        UNIT["Degree",0.0174532925199433]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["False_Easting",500000.0],
    PARAMETER["False_Northing",10000000.0],
    PARAMETER["Central_Meridian",147.0],
    PARAMETER["Scale_Factor",0.9996],
    PARAMETER["Latitude_Of_Origin",0.0],
    UNIT["Meter",1.0]]
Veg_Key: Integer (9.0)
Veg_Types: String (254.0)



INFO: Open of `radiation250.shp'
      using driver `ESRI Shapefile' successful.

Layer name: radiation250
Geometry: Polygon
Feature Count: 3127
Extent: (148.767047, -35.761276) - (148.902290, -35.573877)
Layer SRS WKT:
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.0174532925199433]]
ID: Integer (10.0)
GRIDCODE: Integer (10.0)



INFO: Open of `slope_250.shx'
      using driver `ESRI Shapefile' successful.

Layer name: slope_250
Geometry: Polygon
Feature Count: 2548
Extent: (148.767047, -35.761276) - (148.902290, -35.573877)
Layer SRS WKT:
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.0174532925199433]]
ID: Integer (10.0)
GRIDCODE: Integer (10.0)

#######Instalation POSTGIS in Ubuntu

Repo for ubuntu 14 in  /etc/apt/sources.list.d/postgresql.list

deb http://apt.postgresql.org/pub/repos/apt/ codename-pgdg main

ls /usr/share/postgresql/9.3/extension


Creating temlplate

createdb -E UTF8 template_postgis

createdb test_db -T template_postgis2.1


psql -d template_postgis2.1 -f /usr/share/postgresql/9.1/extension/postgis--2.1.0SVN.sql
psql -d template_postgis2.1 -c "GRANT ALL ON geometry_columns TO PUBLIC;"
psql -d template_postgis2.1 -c "GRANT ALL ON geography_columns TO PUBLIC;"
psql -d template_postgis2.1 -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"

psql -d template_postgis -f /usr/share/postgresql/9.3/extension/postgis--2.1.4.sql




Import to db files
radiation250.shp
slope_250.shp
cotter_veg_original.shp


shp2pgsql -I -s 4326 radiation250.shp  public.map_radiation | psql -d fbr
shp2pgsql -I -s 4326 cotter_veg_original.shp  public.map_cotter | psql -d fbr
shp2pgsql -I -s 4326 slope_250.shp  public.map_slope | psql -d fbr

















