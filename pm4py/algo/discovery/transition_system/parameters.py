from enum import Enum
from pm4py.util import constants

import warnings
warnings.warn("pm4py.algo.discovery.transition_system.parameters is deprecated. Please use the variant-specific parameters.")


class Parameters(Enum):
    VIEW_MULTI_SET = 'multiset'
    VIEW_SET = 'set'
    VIEW_SEQUENCE = 'sequence'

    VIEWS = {VIEW_MULTI_SET, VIEW_SET, VIEW_SEQUENCE}

    DIRECTION_FORWARD = 'forward'
    DIRECTION_BACKWARD = 'backward'
    DIRECTIONS = {DIRECTION_FORWARD, DIRECTION_BACKWARD}

    PARAM_KEY_VIEW = 'view'
    PARAM_KEY_WINDOW = 'window'
    PARAM_KEY_DIRECTION = 'direction'

    ACTIVITY_KEY = constants.PARAMETER_CONSTANT_ACTIVITY_KEY

    INCLUDE_DATA = 'include_data'
