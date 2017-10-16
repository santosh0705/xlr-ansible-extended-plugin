from ansibleExtended.api_client import APIClientExtended

APIClientExtended.validate_input(task)

host = task.pythonScript.getProperty("host")
client = APIClientExtended(host,task.pythonScript.getProperty('environmentVars'),task.pythonScript.getProperty('ansibleCmd'),task.pythonScript.getProperty('cmdParams'))

if task.pythonScript.getProperty('playbookPath'):
    response = client.execute_local_playbook(task.pythonScript.getProperty('playbookPath'))
elif task.pythonScript.getProperty('playbookUrl'):
    playbook = APIClientExtended.download_file(task.pythonScript.getProperty('playbookUrl'),task.pythonScript.getProperty('username'),task.pythonScript.getProperty('password'))
    response = client.execute_playbook(playbook)
else:
    response = client.execute_playbook(task.pythonScript.getProperty('playbook'))

output = response.stdout
error = response.stderr

