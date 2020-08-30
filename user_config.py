import os
import os.path as osp

# Where experiment outputs are saved by default:
DEFAULT_DATA_DIR = osp.join(osp.abspath(osp.dirname(__file__)),'data')
DEFAULT_IMG_DIR = osp.join(osp.abspath(osp.dirname(__file__)),'imgs')
DEFAULT_VIDEO_DIR = osp.join(osp.abspath(osp.dirname(__file__)),'videos')

# Whether to automatically insert a date and time stamp into the names of
# save directories:
FORCE_DATESTAMP = False

# Whether GridSearch provides automatically-generated default shorthands:
DEFAULT_SHORTHAND = True

# Tells the GridSearch how many seconds to pause for before launching 
# experiments.
WAIT_BEFORE_LAUNCH = 5