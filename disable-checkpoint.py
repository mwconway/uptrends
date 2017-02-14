import sys
import probes
import checkpointservers

user = sys.argv[1]
secret = sys.argv[2]
probeId = sys.argv[3]
checkpoint_name = sys.argv[4]

#get the probe to be updated and the id of the checkpoint to disable
checkpoint = checkpointservers.findCheckpointByName(checkpoint_name, user, secret)
print("Found checkpoint " + str(checkpoint["CheckPointID"])
    + " named " + checkpoint["CheckPointName"])

probe = probes.getProbe(probeId, user, secret)

print("Removing checkpoint " + str(checkpoint["CheckPointID"])
    + " from exclusion list on probe " + probe["Name"])
probes.addCheckpointExclusion(checkpoint["CheckPointID"], probe, user, secret)

print("Complete")