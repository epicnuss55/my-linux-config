#!/bin/bash

line=`playerctl -l | head -1`

firefox='firefox'
spotify='spotify'

if [[ "$line" == "$firefox"* ]]; then
    out=`playerctl metadata --format " {{artist}}: {{title}}"`
    format="%{u#ff0000}%{+u}"
    echo $format$out | sed 's/\(.\{75\}\).*/\1.../'
elif [[ "$line" == "$spotify"* ]]; then
    out=`playerctl metadata --format " {{artist}}: {{title}}"`
    format="%{u#1db954}%{+u}"
    echo $format$out | sed 's/\(.\{75\}\).*/\1.../'
else
    out=`playerctl metadata --format " {{artist}}: {{title}}"`
    format="%{u#87fff1}%{+u}"
    echo $format$out | sed 's/\(.\{75\}\).*/\1.../'
fi

