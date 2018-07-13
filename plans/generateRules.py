import rospy

terminal_actions = ["skip_action", "fail_plan", "goal", "restart_plan", "restart_action"]

while True:
    recoveryAction = ""
    rospy.set_param('/interrupt', 0)
    interrupt_start = raw_input ("Press enter to add a rule, or 'quit' to quit: ")
    if interrupt_start == 'quit':
        break
    rospy.set_param('/interrupt', 1)
    # ask Luca if he knows how to find out where in the pnp we are
    action = raw_input ("What action was being performed? ")
    condition = raw_input ("What condition made the input necessary? ")
    while True:
        rule_str = raw_input ("What's the next step? ")
        rule_str = rule_str.strip()
        recoveryAction += rule_str
        if (rule_str in terminal_actions or rule_str[:11] == "GOTO_LABEL_"):
            # pub.publish(recoveryAction)
            rule_file = open("generatedRules.er", "a")
            rule_file.write("*if* " + condition.strip() + " *during* " + action.strip() + " *do* " + recoveryAction + '\n');
            rule_file.close()
            break
        else:
            recoveryAction += "; "

