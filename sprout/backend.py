import datetime
import psutil
import os

# .sprout file (csv-like iterator config):
# essentially, each line '\n' (new_iterator) is a seperate iterator (usually a list),
# where within each line ',' (new_element) seperates elements within a iterator.
# and ' NL ' (new_subiterator) creates another iterator within the line iterator, for example:
#       info 1, info 3, ND info 2, info 4
#       info 8, info 9, ND info 7, info 8
# if read like a list, would be:
# [[info1, info3], [info2, info4]] and [[info8, info9], [info7, info8]]
# if no new_subiterator declarators are within a .sprout file, then the file doesn't need to worry about it!
# (In our case the new_line declarator is used for the weekly info)
# You can read an entire .sprout file and create an iterable from that, where '\n' ()

week_session = [False, False, False, False, False, False, False] # days of the week

# the amount of implements in the info
def find_info_length():
    with open('info.sprout') as file:
        contents = file.readlines()
    
    return len(contents)

# Kills the inputted process as string
def kill_process(app : str):
    os.system("taskkill /f /m {process}".format(process = app))

# returns info about a specific app limit or app limit parameter
def read_config(app_name, app_parameter = None):
    with open('info.sprout') as file:
        contents = file.readlines()

    app_list = [value.split(',') for value in contents]

    selected_app = []

    for values in app_list:
        if values[0] == app_name:
            selected_app = values

    if app_parameter:
        return selected_app[app_parameter]
    
    return selected_app

# A 2D list that contains the info of each app
def read_all_config():
    with open('info.sprout') as file:
        contents = file.readlines()
    
    app_list = {}
    for value in contents:
        a = value.split(',')
        app_list.update(({a.pop(0), a}))

    return app_list

# Returns a list of the names of all currently running applications
def get_current_running_applications() -> list[str]:
    raw_app_list = psutil.process_iter()
    app_list = []
    for value in raw_app_list:
        if '.exe' in value.name() and value.name() not in app_list:
            app_list.append(value.name())

    return app_list

# Returns the time in milliseconds that the process has been running for
# first input is the name of the process
def process_uptime(process_name: str):
    for process in psutil.process_iter(attrs=['pid', 'name', 'create_time']):
        if process.info['name'] == process_name:
            tc = process.info['create_time']
            return tc
    else:
        return None

# Returns a list of all currently running applications within info.sprout as Process objects
def get_listed_running_applications() -> list[psutil.Process]:
    listed_applications = []
    
    for value in get_current_running_applications():
        app_name = value
        if read_config(app_name) != []:
            if app_name not in listed_applications:
                listed_applications.append(value)
                
    return listed_applications


def get_daily_info(param1) -> dict:
    with open('infoweekly.sprout', 'r', encoding='utf-8') as file:
        contents = file.read()
    # Split by every day (see .sprout syntax)
    day = contents.split('\n')
    a = day[param1].split(' ND ')
    result = {}
    for ii in a:
        try:
            result.update({(ii.split(','))[0]: (ii.split(','))[1]})
        except:
            pass
    
    return result

# Appends application to info.sprout given application parameters
append_application = lambda app_name, i_time_limit, : open('info.sprout', 'a', encoding='utf-8').writelines('\n' + app_name + ',' + str(i_time_limit))

def check_weekly_reset():
    global week_session
    if week_session[datetime.datetime.now().weekday()] != 0:
        with open('infoweekly.sprout', 'w', encoding='utf-8') as file:
            file.write("None\nNone\nNone\nNone\nNone\nNone\nNone")
        week_session = [0, 0, 0, 0, 0, 0, 0]

# TODO: Append app + time daily to the current day, find day using datetime from initial day
def append_daily_info(day_info):
    check_weekly_reset()

    with open('infoweekly.sprout', 'r+', encoding='utf-8') as file:
        week_info = file.readlines()
        as_sprout = ''
        for value in day_info:
            as_sprout += value + ','
            as_sprout += str(day_info[value]) + ' ND '
    
        as_sprout += '\n'

        week_info[datetime.datetime.now().weekday()] = as_sprout

        file.write(as_sprout)

# Redundant / Not needed, delete later
# def get_Datetime_object(string):
#     return datetime.datetime.strptime(string, '%H:%M:%S')