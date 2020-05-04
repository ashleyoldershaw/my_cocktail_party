#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Rule recieved: %s", data.data)
    rospy.loginfo("Modifying rule to add current action")
    currentaction = rospy.get_param("/diago_0/pnp/currentTask").split("_")[0]

    output = data.data
    i = output.find("*do*")
    output = output [:i] + " *during* " + currentaction + " " + output[i:]
    output = output.replace("95", "_")
    # these are here to convert MODIM outputs to PNP inputs
    output = output.replace("notpersonhere", "(not personhere)")
    output = output.replace("notclosetotarget", "(not closetotarget)")
    output = output.replace("failplan", "fail_plan")
    output = output.replace("restartaction", "restart_action")
    output = output.replace("restartplan", "restart_plan")
    output = output.replace("skipaction", "skip_action")
    output = output.strip()
    output = output.strip(";")

    outputfile = open("generatedRules.er", "a")
    outputfile.write(output)
    outputfile.close()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rulebuilder_listener', anonymous=True)

    rospy.Subscriber("/rulebuilder", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
