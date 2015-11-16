usage = "segGen.py [--options] gpsstart gpsend"
description = "generates segments based on transmitted light signals"
author = "Reed Essick (reed.essick@ligo.org)"


from ConfigParser import SafeConfigParser
from optparse import OptionParser

#=================================================

parser = OptionParser(usage=usage, description=description)

parser.add_option("-v", "--verbose", default=False, action="store_true")

parser.add_option("-c", "--config", default="./config.ini", type="string")

opts, args = parser.parse_args()

if len(args) != 2:
    raise ValueError("please supply exactly 2 input arguments")
gpsstart = float(args[0])
gpsend = float(args[1])

#=================================================

### load config file
if opts.verbose:
    print "loading config : %s"%(opts.config)
config = SafeConfigParser()
config.load( opts.config )

### define segment logic (how we build segments based on aux triggers)



### go findeth triggers

### write segments -> build a segment table? (or just ascii to start?)


