#!/bin/sh
# Use: ./runplan.sh <robotname> <planname>
# Example: ./runplan.sh diago_0 cocktail_party

rosparam set /diago_0/pnp/plan_folder `pwd`
./genplan.sh $2.plan generatedRules.er
rostopic pub /$1/planToExec std_msgs/String "data: '$2'" --once

