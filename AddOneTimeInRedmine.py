import json
from redmine import Redmine

redmine = Redmine('http://redmine.bintime.com', key='' )

# issue_id = 11575
time_entries_str = '''18350|2015-08-03|1,0|testing
18010|2015-07-30|1,0|testing
'''

def time_entry_parse(time_entry):
    time_entry_tmp = {}
    time_entry = time_entry.split("|")
    time_entry_tmp["issue_id"] = time_entry[0].strip()
    time_entry_tmp["hours"] = float(time_entry[2].strip().strip("h").replace(",","."))
    time_entry_tmp["spent_on"] = time_entry[1].strip()
    time_entry_tmp["subject"] = time_entry[3].strip()
    time_entry_tmp["activity_id"] = 11
    time_entry_tmp["custom_fields"] = [
        {
        "id": 5,
        "name": "Description",
        "value": time_entry_tmp["subject"]
        }
    ]
    return time_entry_tmp


time_entries_list = map(time_entry_parse,time_entries_str.splitlines())



for time_entry in time_entries_list:
    # print(time_entry)
    print(str(time_entry["spent_on"]) + " : " + str(time_entry["hours"])   + " on " + time_entry["subject"])
    time_entry_rdm = redmine.time_entry.create(issue_id=time_entry["issue_id"], spent_on=time_entry["spent_on"], hours=time_entry["hours"], activity_id=time_entry["activity_id"], comments=time_entry["subject"],custom_fields=time_entry["custom_fields"])
    print('Time entry for issue #'+str(time_entry["issue_id"])+' added with #' + str(time_entry_rdm.id))






















