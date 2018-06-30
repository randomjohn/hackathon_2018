# -*- coding: utf-8 -*-
"""
BCycle to GeoJson

The purpose of this program is to convert the ad hoc JSON for bicycle stations at Greenville BCycle
https://gbfs.bcycle.com/bcycle_greenville/station_information.json
to GeoJSON (RFC 7946)
Information on GeoJSON is at http://www.geojson.org

The reason for this is that the Open Data Greenville Map Layers at https://data.openupstate.org/map-layers
Are in GeoJSON and it would be very nice to add bike layers to these datasets

This program is designed to have minimal dependencies, but was programmed in Python 3.6 using
the Anaconda version of Python downloaded 6/30/2018.

The bikeshare specification feed docs can be found at
https://github.com/NABSA/gbfs

Modification history:
    6/30/2018: Created by John Johnson (part of SC Hackathon 2018)
"""
import urllib.request, json 

# Global variables
bcycle_url = "https://gbfs.bcycle.com/bcycle_greenville/station_information.json"
out_file = "BCycle_stations.geojson"

# read in the data from the BCycle site
with urllib.request.urlopen(bcycle_url) as url:
    data = json.loads(url.read().decode())

"""
For a list of station objects read in form the BCycle site, convert to a GeoJSON Feature
that will eventually be included as part of a larger GeoJSON FeatureCollection

Example entry assumed for input:
 {'lon': -82.40027,
  'lat': 34.84841,
  'address': '206 S. Main St.',
  'name': 'City Hall',
  'station_id': 'bcycle_greenville_2189'}

Note that station_id is ignored here, but if further data is needed from BCycle,
you'll need to include it in this function.    
"""
def to_geo_entry(obj):
    geo_str = "  {\n    \"type\": \"Feature\",\n"
    geo_str += "    \"geometry\": {\n"
    geo_str += "      \"type\": \"Point\",\n"
    geo_str += "      \"Coordinates\": [" + str(obj['lon']) + ", " + str(obj['lat']) + "],\n"
    geo_str += "      },\n"
    geo_str += "    \"properties\": {\n"
    geo_str += "      \"title\": \"" + obj['name'] + "\",\n"
    geo_str += "      \"hours\": \"\",\n"
    geo_str += "      \"type\": \"" + obj['address'] + "\",\n"
    geo_str += "      \"website\": \"https://greenville.bcycle.com\"\n"
    geo_str += "    }\n  }"
    return geo_str
    
# [to_geo_entry(obj) for obj in data['data']['stations']]

################################
# Write out to file
################################
    
geojson_file = open(out_file,"w")
# header information
geojson_file.write("{\"type\": \"FeatureCollection\",\n\"features\": [\n")

# write out features read in from bcycle
for obj_idx in range(len(data['data']['stations'])):
    geojson_file.write(to_geo_entry(data['data']['stations'][obj_idx]))
    if obj_idx < len(data['data']['stations'])-1:
        geojson_file.write(',\n')
    else:
        geojson_file.write('\n')

# closing matter
geojson_file.write("]\n}")

geojson_file.close()