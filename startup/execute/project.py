import IECore
import Gaffer

dispatchers = []
import GafferDeadline
dispatchers.append(GafferDeadline.DeadlineDispatcher)

for dispatcher in dispatchers:
    Gaffer.Metadata.registerValue(dispatcher, "jobName", "userDefault", "${script:name}")
    directoryName = dispatcher.staticTypeName().rpartition(":")[2].replace("Dispatcher", "").lower()
    Gaffer.Metadata.registerValue(dispatcher, "jobsDirectory", "userDefault", "${project:rootDirectory}/dispatcher/" + directoryName)
