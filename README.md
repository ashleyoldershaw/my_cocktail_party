# my_cocktail_party

How to run the demonstration:

Important plans:

In simulation:
```cocktail_party_interaction.plan```: plan containing the normal task (e.g., output from a planner)

On Pepper robot:
```pepper.plan```: plan containing the normal task (e.g., output from a planner)

```recover.plan```: plan implementing the recovery procedure

```metaplan.plan```: metaplan, running ```pepperplan``` until Pepper head is touched and then switching to ```recover``` plan
(to be modified if referring to another plan)


1. Learning phase

* Run the ```metaplan``` plan

* Touch the head of Pepper robot to activate the ```pepperheadtouched``` condition

In simulation run the command 
```
rosparam set /pepper/PNPconditionbuffer/pepperheadtouched 1
```

* Interact with the robot to teach it the recovery procedure

TO CHECK: the script generateRules.py adds the execution rule generated during the interaction in ```generatedRules.er``` file


2. After-learning phase

* Run the ```pepper``` plan (including the new execution rules)

For example,

```
./gen_plan.sh pepper.plan generatedRules.er
```

The robot will now execute the learned recovery procedure.


Note: to run plans:


```
cd my_cocktail_party/plans
./runplan.sh pepper <planname>
```

to stop plans:

```
./runplan.sh pepper stop
```


Notes for starting the demo in simulation:

* Follow instructions in robocupathome_pnp/README 

* Run the checkpoint listener script

```
cd my_cocktail_party/scripts
python checkpointListener.py
```


Notes for starting the demo on Pepper robot:

* start MODIM on the Pepper robot

```
source ~/.bashrc
cd spqrel_app/html/my_cocktail_party
python -m ws_server -robot pepper
```

* start ROS naoqi_driver

```
cd ~/src/Pepper
export PEPPER_IP=<IP of Pepper robot>
./run_naoqi_driver.sh
```

* start PNP

```
roslaunch robocupathome_pnp rcathome_pnp.launch robotname:=pepper
```



How to add checkpoints to a plan:

* Add labels as:

LABEL_CHECKPOINT_<checkpoint_name>;

Example:

LABEL_CHECKPOINT_find_a_person;


* Generate the checkpoint list files and MODIM actions:

```
cd my_cocktail_party/plans
python generateCheckpointList.py <planname>
```

Output is ```<planname>.checkpoints``` and the MODIM action ```actions/getcheckpoint```


