#!/bin/bash
# build.sh <mp3_path> <short_name> <ep_module> <OutName>
set -e
cd /home/claude/deals
MP3="$1"; N="$2"; EP="$3"; OUT="$4"
NB=$(python3 -c "import sys; sys.path.insert(0,'.'); import importlib; print(len(importlib.import_module('$EP').ORDER))")
cp "$MP3" vo/${N}_raw.mp3
EPMOD=$EP python3 vo/prep_vo.py vo/${N}_raw.mp3 vo/${N} $NB
rm -f out/${OUT}_audio.wav
python3 -c "
import sys; sys.path.insert(0,'.'); import engine, importlib
E=engine.Episode(importlib.import_module('$EP')); E.audio('out/${OUT}_audio.wav'); print('total', round(E.TOTAL,1))"
python3 run.py $EP 9x16 $OUT &
python3 run.py $EP 1x1 $OUT
wait
python3 run.py $EP 16x9 $OUT
ffmpeg -loglevel error -y -i out/${OUT}_9x16.mp4 -vf "fps=1/4,scale=216:-1,tile=9x4" -frames:v 1 out/${OUT}_sheet.jpg
echo BUILT $OUT
