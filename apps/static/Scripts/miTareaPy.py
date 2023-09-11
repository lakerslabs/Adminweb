import os
import datetime
import win32com.client

""" python -m pip install --upgrade pywin32 """

def create_task(name, path, start_time):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Create trigger
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    TASK_TRIGGER_TIME = 1
    trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
    trigger.StartBoundary = start_time.isoformat()

    # Create action
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'DO NOTHING'
    action.Path = 'C:\\Windows\\System32\\cmd.exe'
    action.Arguments = '/c python {}'.format(path)

    # Set parameters
    task_def.RegistrationInfo.Description = name
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False

    # Register task
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    root_folder.RegisterTaskDefinition(
        name,  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        'eduardo.berga',  # No user
        'lcdmpt_85',  # No password
        TASK_LOGON_NONE)

# Example usage:
ruta_actual = r'C:\Users\eduardo.berga\Desktop\Proyectos\Lakers_Lab\Adminweb\apps\static\Scripts'
archivo = r'\inputBox.py'
script_path = ruta_actual + archivo
create_task('My Task', script_path, '2023-09-11 10:20:00')
