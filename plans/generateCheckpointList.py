#!/usr/bin/env python
# this can be modified to dynamically create all sorts of MODIM pages which would be very useful
import sys

if (len(sys.argv) >= 2 and sys.argv[1] != "interrupt"):
    print ("Creating checkpoint file for {}")
    output = ""
    inputfile  = open(sys.argv[1], "r")
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
    modimoutputfile.close()
