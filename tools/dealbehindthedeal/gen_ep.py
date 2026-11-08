"""Write ep_<name>.py files in the same layout as ep_groovebook.py / ep_poppi.py."""
import pprint
import nov_scripts as N

def write(name, cold, shots, callouts):
    ep = N.EPS[name]["ep"]
    T = N.text_dict(name)
    src = f'''import json, os
SRC = "/home/claude/deals/{name}.mp4"
VO = "/home/claude/deals/vo/{name}_vo.wav"
TAIL = 0.8
EPLABEL = "DEAL BEHIND THE DEAL · EP{ep}"
ORDER = {N.ORDER!r}
_b = "/home/claude/deals/vo/{name}_beats_raw.json"
if os.path.exists(_b):
    _j = json.load(open(_b)); BT = dict(zip(ORDER, _j["BT_LIST"])); VO_END, SIL = _j["VO_END"], _j["SIL"]
TEXT = {pprint.pformat(T, width=200)}
COLD_SHOTS = {cold!r}
SHOTS = {pprint.pformat(shots, width=200)}
CALLOUTS = {pprint.pformat(callouts, width=200)}
'''
    open(f"/home/claude/deals/ep_{name}.py", "w").write(src)
