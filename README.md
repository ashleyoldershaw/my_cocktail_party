# my_cocktail_party

How to run the demonstration:

Demo plan in simulation:
`cocktail_party_interaction.plan`: plan containing the normal task (e.g., output from a planner)

1. Learning phase

* Run the `cocktail_party_interaction` plan

`<robotname>` is `diago_0` by default on the simulator

* When you see a problem, run the interrupt sender to begin the recovery procedure

* Interact with the robot to teach it the recovery procedure

2. After-learning phase

* Run the `cocktail_party_interaction` plan (including the new execution rules)

For example,

```
./runplan.sh diago_0 cocktail_party_interaction
```

The robot will now execute the learned recovery procedure.


Note: to run plans:


```
cd my_cocktail_party/plans
./runplan.sh <robotname> <planname>
```

to stop plans:

```
./runplan.sh <robotname> stop
```


Notes for starting the demo in simulation for the virtual machine, starting from the root directory:

* Run the simulation starter

```
./run_default_demo.sh
```

* Click start

* Open a new tab and run the MODIM starter

```
./setup_modim.sh
```

* Open a new tab and run the PNP listener script

```
cd demos/my_cocktail_party/plans
./generateRules.py
```

* Open a new tab and run the rule generator listener

```
cd demos/my_cocktail_party/plans
./pnpListener.py
```

* Open a new tab and run the interrupt listener

```
cd demos/my_cocktail_party/plans
./interrupt_listener.py
```

How to add checkpoints to a plan:

* Add labels as:

LABEL_CHECKPOINT_<checkpoint_name>;

Example:

LABEL_CHECKPOINT_find_a_person;


* Generate the checkpoint MODIM action:

```
cd my_cocktail_party/plans
python generateCheckpointList.py <planname>
```

Output is the MODIM action `actions/getcheckpoint`


* Generate the recovery procedure stubs MODIM action:

```
cd my_cocktail_party/plans
python generateActionList.py <planname>
```
Output is the MODIM action `actions/recoverychoices`
