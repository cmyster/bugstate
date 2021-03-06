"""
Common data. Here data is kept, its hard coded and not calculated.
"""

# These are the possible statuses a bug can be in.
BUG_STATUS = [
    'NEW',        # The bug has not been triaged yet.
    'ASSIGNED',   # The bug has been assigned and is in progress.
    'ON_DEV',     # The bug or feature has a complete patch set which has been
                  # posted upstream for review.
    'POST',       # The solution for the bugzilla has been merged upstream and
                  # is ready to be imported for a build.
    'MODIFIED',   # The bug or feature is included in a build and is ready to
                  # be consumed by QE.
    'ON_QA',      # The bug has been added to an erratum and should be ready
                  # for QE to test, if applicable.
    'VERIFIED',   # The bug has been verified as resolved with the build
                  # indicated in the Fixed-in-version field or a newer build.
    'RELEASE_PENDING',  # The fix is about to be shipped in the next release.
    'CLOSED'      # The bug has been closed, usually by errata tool at the end
                  # end of a testing cycle.
]


# Bugs that were closed with this state should not be used.
BAD_STATUS = [
    'NOTABUG',
    'WONTFIX',
    'DEFERRED',
    'WORKSFORME',
    'DUPLICATE',
    'CANTFIX',
    'INSUFFICIENT_DATA'
]


# Bugs started to be assigned to DFGs from this date.
START_DATE = '2017-01-01'

# RHOSP versions as coded into BZ with starting and ending dates.
VERSIONS = [
    ['10.0 (Newton)', '2016-07-28', '2016-12-15'],
    ['11.0 (Ocata)', '2016-11-30', '2017-05-08'],
    ['12.0 (Pike)', '2017-05-09', '2017-12-08'],
    ['13.0 (Queens)', '2017-12-01', '2018-06-29'],
    ['14.0 (Rocky)', '2018-06-29', '2018-01-10'],
]

# Main BZ URL
URL = 'bugzilla.redhat.com'

# These are the only needed fields. Less fields is less taxing. Bug id must
# always be used.
INCLUDE_FIELDS = [
    'id',
    'creation_time',
    'last_change_time',
    'resolution',
    'status',
    'version',
    'cf_internal_whiteboard',
]

# DFGs are defined here.
DFGS = [
    'DFG:Ceph',                                                               
    'DFG:CloudApp',                                                           
    'DFG:Compute',                                                            
    'DFG:DF',                                                                 
    'DFG:HardProv',                                                           
    'DFG:MetMon',                                                             
    'DFG:NFV',                                                                
    'DFG:Networking',                                                         
    'DFG:ODL',                                                                
    'DFG:OSasInfra',                                                          
    'DFG:PIDONE',                                                             
    'DFG:ReleaseDelivery',                                                    
    'DFG:Security',                                                           
    'DFG:Storage',                                                            
    'DFG:UI',                                                                 
    'DFG:Upgrades',                                                           
    'DFG:Workflows',
]

# Quicksearch link starts like this, then bug IDs are added with a comma.
QUICKSEARCH = 'https://bugzilla.redhat.com/buglist.cgi?quicksearch='

# Baseurl to google sheet so lines are shorter.
BASE_SHEET = "https://docs.google.com/spreadsheets/d"

# Red Hat Dot Com
RHDT = '@redhat.com'

# Path to API secrets file
API_SECRET = 'client_secret.json'

# Token for BugStatistics.
API_TOKEN = 'sheets.googleapis.com-python.json'

# Common range for sheets: Start at A1 and be open ended.
RANGE = 'DATA!A1'
