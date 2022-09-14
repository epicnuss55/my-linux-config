from i3ipc import Connection

i3 = Connection()
workspaces = i3.get_workspaces()
focused = i3.get_tree().find_focused().workspace().num

out = ""

if 1 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    out += " " + "" + " "

if 2 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    out += " " + "" + " "

if 3 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    out += " " + "" + " "

if 4 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    out += " " + "" + " "

if 5 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    exists = False
    for ws in workspaces:
        if ws.num == 5:
            exists = True
            out += " " + "" + " "
            break
    if not exists:
        out += " " + "" + " "

if 6 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    exists = False
    for ws in workspaces:
        if ws.num == 6:
            exists = True
            out += " " + "" + " "
            break
    if not exists:
        out += " " + "" + " "

if 7 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    exists = False
    for ws in workspaces:
        if ws.num == 7:
            exists = True
            out += " " + "" + " "
            break
    if not exists:
        out += " " + "" + " "

if 8 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    exists = False
    for ws in workspaces:
        if ws.num == 8:
            exists = True
            out += " " + "" + " "
            break
    if not exists:
        out += " " + "" + " "

if 9 == focused:
    out += "%{B#3b4252}%{F#87fff1} " + "" + " %{B-}%{F-}"
else:
    exists = False
    for ws in workspaces:
        if ws.num == 9:
            exists = True
            out += " " + "" + " "
            break
    if not exists:
        out += " " + "" + " "

if 0 == focused:
    out += "%{B#3b4252}%{F#87fff1}  %{B-}%{F-}"
else:
    out += "  "



print(out)