import sys; sys.path.insert(0,'/home/claude/deals')
import importlib, engine
ep=importlib.import_module(sys.argv[1]); fmt=sys.argv[2]; name=sys.argv[3]
E=engine.Episode(ep)
import os
wav=f"/home/claude/deals/out/{name}_audio.wav"
if not os.path.exists(wav): E.audio(wav)
E.render(fmt, f"/home/claude/deals/out/{name}_{fmt}.mp4", wav)
print("done", name, fmt, round(E.TOTAL,1))
