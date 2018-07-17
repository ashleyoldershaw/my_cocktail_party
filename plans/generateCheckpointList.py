import sys

if (len(sys.argv) >= 2):
    output = ""
    inputfile  = open(sys.argv[1]+".preplan", "r")
    for line in inputfile:
        if line[0:17] == "LABEL_CHECKPOINT_":
            output += line[17:-2] + '\n'
            print "Adding checkpoint: " + line[17:-2]
    if output != "":
        outputfile = open(sys.argv[1]+".checkpoints", "w")
        print "Writing to file: " + outputfile.name
        outputfile.write(output)
    else:
        print "No checkpoints found. Not writing anything..."
