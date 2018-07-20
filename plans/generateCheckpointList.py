#!/usr/bin/env python
import sys

if (len(sys.argv) >= 2 and sys.argv[1] != "interrupt"):
    output = ""
    inputfile  = open(sys.argv[1]+".plan", "r")
    modimoutputfile = open("../actions/getcheckpoint", "w")
    modimoutputfile.write("""TEXT
<*,*,*,*>: "Choose a checkpoint to go to."
----
TTS
<*,*,*,*>: "Where should I go?"
----
BUTTONS
""")
    for line in inputfile:
        if line[0:17] == "LABEL_CHECKPOINT_":
            output += line[17:-2] + '\n'
            cpname = line[17:-2]
            print "Adding checkpoint: " + cpname
            modimoutputfile.write(cpname.replace("_", "95") + "\n<*,*,*,*>: \"" + cpname.replace("_", " ").capitalize() + "\"\n")
    modimoutputfile.write("----\n")
            
    if output != "":
        listoutputfile = open(sys.argv[1]+".checkpoints", "w")
        print "Writing to file: " + listoutputfile.name
        listoutputfile.write(output)
        
    else:
        print "No checkpoints found. Not writing anything..."
