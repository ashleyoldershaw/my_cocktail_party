#!/usr/bin/env python
import sys
import re

if (len(sys.argv) >= 2):
    newstring = ""
    inputfile  = open(sys.argv[1]+".preplan", "r")
    outputfile = open(sys.argv[1]+".plan", "w")
    # go through the file one line at ta time
    for line in inputfile:
        rules = []
        # split the line up into pieces, then make a new list of the actual rules
        splitline = line.split("!")
        for item in splitline:
            if (item[0:4] == "*if*"):
                rules.append(item)
        if (len(rules) !=0):
            # go through the rules, deal with them as the confidence says
            for rule in rules:
                print "New rule to add:", rule
                confidence = float(rule[-3:])
                if (confidence < 0.25):
                    print "Confidence too low (", confidence, ") : not adding rule..."
                    regex = "!" + rule + "!";
                    line = line.replace(regex,"");
                else:
                    recovery = rule[rule.find("*do*")+4:rule.find("*confidence*")].strip()
                    newrecovery = recovery
                    if confidence > 0.75:
                        newrecovery = "interact_executingplan; " + recovery
                    else:
                        newrecovery = "interact_asktoexecute000reply_@E; " + recovery # TODO work out what to do if the answer is no
                    line = line.replace (recovery, newrecovery)
        if line != '\n':
            outputfile.write(line)
    inputfile.close()
    outputfile.close()
else:
    print ("Needs a filename argument, eg 'demo', with no extension")
