# ZillaTools
A bunch of scripts that I use for work.
They use python-bugzilla to connect and fetch data to be parsed and used for
my day to day work. The data is saved as CSV and later uploaded to google 
sheets.

## Notice
This tool uses custom fields specific for Red Hat bugs and as such requires
sufficient permissions for it to work.

## Before we start
This script was written with python 2.7 in mind, so make sure that you have
that and the latest version of python-bugzilla:
```
> _your favorite pkg manager_ update/upgrade
> _your favorite pkg manager_ install pip
> pip install python-bugzilla
```
Once installed, run this command once to create a working token:
```
> bugzilla --login
  Logging into bugzilla.redhat.com
  Bugzilla Username: nosuchuser@redhat.com
  Bugzilla Password:
```
You might see this error:
```Unexpected action 'None'```
but if a token file was created in  ~/.cache/python-bugzilla/ then you should 
be fine.

Now you can 'git clone' this project anywhere and run the scripts inside.

## BugState
Goes over _meaningful_ bugs that were opened in each major RHOSP version 
starting in Newton. The output of it is a simple CSV that can be used, for 
instance to calculate changes between versions for a specific DFG.

## UserState
Goes over a list of predefined users and fetches specific data on each and
saves that as a CSV.

## BugBacklog
Goes over the number of bugs that are open per RFE per week since 01/01/2017
and saves that data.

## RFEBacklog
Same as bug backlog, but for open RFEs.

### Usage
Run the script directly from CLI to produce a CSV file that contains all the
data. You can add --help for help or --file '\<filename\>' to change the 
file's name and path.

```
/<SomePath>/ZillaTools/zillatools/scriptname.py
```

## TODO
Is written in a file called TODO.
