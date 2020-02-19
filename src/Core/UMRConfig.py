import pathlib
import yaml
from typing import Dict, List
from . import UMRLogging
from Util.Helper import check_attribute
# load config from home directory

logger = UMRLogging.getLogger('Config')
config: Dict

home = str(pathlib.Path.home())

try:
    config = yaml.load(open(f'{home}/.umr/config.yaml'), Loader=yaml.FullLoader)

    # test attributes
    attributes = [
        ('ForwardList', False, None),   # directed graph contains forward relationships
        ('Driver', False, None),        # configs for each driver
        ('DataRoot', False, None),      # file root for images
        ('CommandPrefix', True, '!!'),  # command hint format, e.g. "/" for /start, /stop type of commands
        ('BotAdmin', True, dict()),     # Bot administrators, highest privilege users
        ('Debug', True, True)           # verbose output
    ]
    check_attribute(config, attributes, logger)

except FileNotFoundError:
    logger.error(f'config.yaml not found under "{home}/.umr/"!')
    exit(-1)

