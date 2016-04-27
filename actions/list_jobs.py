from lib import action

class ChronosListJobsAction(action.ChronosBaseAction):
    def run(self):
        return self.chronos.list()
