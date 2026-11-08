# Deal Behind the Deal — build kit (backup)

Restore in a new Claude session:
1. `git clone` this repo, then `mkdir -p /home/claude/deals/{vo,out,scripts,master}` and copy this folder's files back (vo/prep_vo.py -> /home/claude/deals/vo/).
2. Stage fonts from the Mac: `~/taxbookscfo-content-agent/assets/fonts/` (DMSerifDisplay-Regular/Italic.ttf, SourceSans3.ttf). engine.py reads them from `/mnt/user-data/uploads/taxbookscfo-content-agent/assets/fonts/`.
3. Stage the pitch footage from `~/Downloads/<name>.mp4` and symlink it to `/home/claude/deals/<name>.mp4`.
4. Write `ep_<name>.py` (copy ep_groovebook.py: SRC, VO, EPLABEL, ORDER, TEXT, SHOTS, CALLOUTS) and `scripts/<name>_script.txt` (the ElevenLabs text with [serious]/[pause] tags).
5. `bash build.sh <elevenlabs.mp3> <name> ep_<name> TaxBooksCFO_EPxx_<Company>` -> out/ gets _9x16, _1x1, _16x9 mp4 + contact sheet.

Needs: python3, numpy, Pillow, ffmpeg.
