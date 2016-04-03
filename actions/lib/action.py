# project
from st2actions.runners.pythonrunner import Action

# 3p
import chronos

class ChronosBaseAction(Action):
    def __init__(self, config):
        super(ChronosBaseAction, self).__init__(config)
        self.chronos = self._get_client()

    def _get_client(self):
        servers = self.config.get('servers')
        proto = self.config.get('proto', 'http')
        username = self.config.get('username', None)
        password = self.config.get('password', None)

        client = chronos.connect(servers, proto, username, password)
        return client
