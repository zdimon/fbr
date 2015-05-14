
Usefull links

http://suite.opengeo.org/4.1/dataadmin/pgGettingStarted/shp2pgsql.html
http://prj2epsg.org/search


GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]

CRID

4326 - GCS_WGS_1984


Command to see info 
zdimon@home:~/www/fbr_ve/fbr/vector_data$ ACVege_Cut_projected.shx slope_250 -so

ogrinfo vegetation_structure.shx vegetation_structure -so

ogrinfo vegetation_structure.shx vegetation_structure -so


---------------------------------------------

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
---------------------------------------------------



----------------------------------------------------
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

-----------------------------------------------------


-------------------------------------------------------

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
---------------------------------------------------------


--------------------------------------------------------
INFO: Open of `vegetation_structure.shx'
      using driver `ESRI Shapefile' successful.

Layer name: vegetation_structure
Geometry: Polygon
Feature Count: 152
Extent: (148.766423, -35.760452) - (148.903227, -35.573661)
Layer SRS WKT:
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.0174532925199433]]
ID: Integer (10.0)
GRIDCODE: Integer (10.0)
STRUCTURE: String (32.0)
----------------------------------------------------------




---------------------------------------------------------------
INFO: Open of `ACVege_Cut_projected.shx'
      using driver `ESRI Shapefile' successful.

Layer name: ACVege_Cut_projected
Geometry: 3D Polygon
Feature Count: 129
Extent: (148.767047, -35.761276) - (148.902290, -35.573877)
Layer SRS WKT:
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.0174532925199433]]
OBJECTID: Real (11.0)
AREA: Real (19.15)
PERIMETER: Real (19.15)
VEG_: Real (19.15)
VEG_ID: Real (19.15)
VEG_SP_1: String (25.0)
VEG_SP_2: String (25.0)
VEG_SP_3: String (25.0)
STRUCTURE: String (20.0)
CLASS: Integer (6.0)
SYMBOL: Real (19.15)
STATE: String (6.0)
FuelType: Integer (6.0)
FuelCode_V: String (50.0)
Acres: Real (19.15)
Hectares: Real (19.15)
-----------------------------------------------------------







#######Instalation POSTGIS in Ubuntu

Repo for ubuntu 14 in  /etc/apt/sources.list.d/postgresql.list

deb http://apt.postgresql.org/pub/repos/apt/ codename-pgdg main

ls /usr/share/postgresql/9.3/extension


Creating temlplate

su postgres
createdb -E UTF8 template_postgis
psql -d template_postgis -f /usr/share/postgresql/9.3/extension/postgis--2.1.4.sql

createdb test_db -T template_postgis2.1


psql -d template_postgis2.1 -f /usr/share/postgresql/9.1/extension/postgis--2.1.0SVN.sql
psql -d template_postgis2.1 -c "GRANT ALL ON geometry_columns TO PUBLIC;" я тебе для удобства захода на сервер сделал команду fbr
[14:27:27] Dima: запуская ее ты попадаешь на сервер
[14:27:51] Dima: далее чтобы вывести список работающий скринов набираешь screen -ls
[14:28:08] Dima: там щас один скрин с запущенным веб сервером
[14:28:43] Dima: There is a screen on:
	10405.fbr-server	(05/11/15 12:02:16)	(Detached)
1 Socket in /var/run/screen/S-zdimon.
[14:29:12] Dima: чтоб к нему присоединиться нужно набрать screen -r fbr-server или screen -r 10405 (по идентификатору)
[14:29:27] Dima: и там ты увидишь причину
[14:30:17] Dima: когда ты протупила с blanc зы загнала на сервер код с синтаксической (грубой) ошибкой и обрушила сервер в скрине
[14:30:50] Dima: все что нужно это остановить его по crtl+c и запустить снова (стрелочка вверх)
[14:31:23] Dima: далее чтобы выйти из скрина нужно нажать комбинацию ctrl+a и потом d
[14:31:42] Dima: и ты попадеш в обычный терминал сервера
[14:33:12] Dima: сам скрин это копия терминала в памяти которая продолжает работу после того как ты покидаешь сервер
[14:33:52] Dima: в противном случае чтобы работал сайт нужно постоянно держать открытым терминал с запущенным сервером
[14:35:11] Dima: впринципе неплохо перед деплоем заходить в скрин и смотреть что там происходит после деплоя

psql -d template_postgis2.1 -c "GRANT ALL ON geography_columns TO PUBLIC;"
psql -d template_postgis2.1 -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"

psql -d template_postgis -f /usr/share/postgresql/9.3/extension/postgis--2.1.4.sql




Import to db files
radiation250.shp
slope_250.shp
cotter_veg_original.shp


ИМПОРТ SHP

Скопировать файлы в vector_data

сделать деплой

зайти на сервер

ssh zdimon@hntu.com.ua

перейти в эту директорию cd fbr_ve/fbr/vector_data

перейти в пользователя postgres
sudo -s
su postgres

запустить команду

shp2pgsql -I -s 4326 <shape file>  public.<table name> | psql -d fbr

например

shp2pgsql -I -s 4326 radiation250.shp  public.map_radiation | psql -d fbr
shp2pgsql -I -s 4326 vegetation_structure.shp  public.map_veget | psql -d fbr
shp2pgsql -I -s 4326 slope_250.shp  public.map_slope | psql -d fbr





shp2pgsql -I -s 4326 vegetation_structure.shp  public.veg_tmp | psql -d fbr




ALTER TABLE map_veget
  ADD CONSTRAINT struct_id_refs_id_custom FOREIGN KEY (struct_id)
      REFERENCES map_structure (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;












