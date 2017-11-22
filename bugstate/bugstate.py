from __future__ import print_function
from bugzilla import RHBugzilla

# Local helpers
import functions
import data


bz_q = RHBugzilla(data.URL)

for version in data.versions:
    q = {
        'query_format': 'advanced',
        'f1': 'cf_internal_whiteboard',
        'v1': 'DFG:Upgrades',
        'j_top': 'OR',
        'o1': 'substring',
        'product': 'Red Hat OpenStack',
        'target_release': '{}'.format(version)
    }

    # No need for all possible fields, this saves time. ID must be there.
    q['include_fields'] = data.include_fields

    # This is where BZ is being queried.
    bugs = bz_q.query(q)

    # A couple of integers to help calculate average time.
    closed_bugs = 0
    time_to_close = 0

    print ('Total number of bugs opened in {} is {}'.format(
        version, len(bugs)))
    for bug in bugs:
        if bug.status in 'CLOSED' and bug.resolution not in data.bad_status:
            closed_bugs += 1
            delta = functions.get_delta(bug.creation_time.value,
                                        bug.last_change_time.value)
            time_to_close += delta

        hist_time = functions.get_status_times(bug.get_history_raw())
        # TODO:
        # new_to_on_qa = functions.get_new_to_on_qa(hist_time)
        for state_time, bug_state in hist_time.items():
            print ('Bug ID - {}; Status - {}; timestamp - {}'.format(
                bug.id, bug_state, state_time))

    if closed_bugs > 0:
        average_time = functions.get_average_time(time_to_close,
                                                  closed_bugs,
                                                  version)
        print (average_time)
