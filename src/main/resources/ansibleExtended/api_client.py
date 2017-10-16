from ansible.api_client import APIClient

class APIClientExtended(APIClient):

    def __init__(self, host, environment_vars, ansible_path, cmd_params):
        cmd = "%s %s" % (environment_vars if environment_vars else '', ansible_path)
        APIClient.__init__(self, host, cmd, cmd_params)
