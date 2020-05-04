#!/usr/bin/env python
# this can be modified to dynamically create all sorts of MODIM pages which would be very useful
import sys

if (len(sys.argv) >= 2 and sys.argv[1] != "interrupt"):
    print ("Creating action file for {}")
    output = ""
    inputfile  = open(sys.argv[1], "r")
    modimoutputfile = open("../actions/recoverychoices", "w")
    modimoutputfile.write("""TEXT
<*,*,*,*>: "Choose a recovery action."
----
TTS
<*,*,*,*>: "Choose a recovery action for me to learn."
----
BUTTONS

""")
    reserved = ["restartplan", "restartaction", "failplan", "skipaction", "GOTO", "unknownvar"]
    actions = set()
    for line in inputfile:
        if line[0:17] != "LABEL_CHECKPOINT_" and line[0:11] != "CHECKPOINT_" \
        and line[0] != "#" and line[0] != "<":
            output += line[17:-2] + '\n'
            action = line.split("_")[0].strip(";")
            if action not in actions and action not in reserved:
                print "Adding action to set: " + action
                actions.add(action)

    for action in actions:
        modimoutputfile.write(action + "_notext\n<*,*,*,*>: \"" + action.capitalize() + "\"\n")
    modimoutputfile.write("""recovery_goto_notext
<*,*,*,*>: "Go to a location"
recovery_say_text
<*,*,*,*>: "Say something out loud"
recovery_restartplan_notext
<*,*,*,*>: "Restart the plan from the beginning"
recovery_restartaction_notext
<*,*,*,*>: "Restart the action I was doing"
recovery_failplan_notext
<*,*,*,*>: "Plan is finished/failed"
recovery_skipaction_notext
<*,*,*,*>: "Skip to the next action"
recovery_GOTO_notext
<*,*,*,*>: "Go to a specific point in the plan"
----""")
    modimoutputfile.close()

    if output != "":
        checkpointfile = open(sys.argv[1].split('.')[0]+".actions", "w")
        print "Writing to file: " + checkpointfile.name
        checkpointfile.write(output)
        checkpointfile.close()

    else:
        print "No actions found. Not writing anything..."
