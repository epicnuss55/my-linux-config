#!/bin/bash
BRIGHTNESS_VALUE=`brightnessctl | grep -o "(.*" | tr -d "()"`
BRIGHTNESS_NR=${BRIGHTNESS_VALUE//%}
BRIGHTNESS_ICON=''

echo "$BRIGHTNESS_VALUE"
