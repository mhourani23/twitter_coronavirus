#!/bin/sh



for day_number in /data/Twitter\ dataset/geoTwitter20-*; do
    nohup ./src/map.py "--input_path=$day_number" &
    #echo $day_number
done


