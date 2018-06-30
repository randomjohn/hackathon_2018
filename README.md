# hackathon_2018
Convert Greenville SC bikeshare station data to GeoJSON

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
