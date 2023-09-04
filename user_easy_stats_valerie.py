# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger
logger, logname = setup_logger(__file__)


# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import statistics
import sys

print("Funds collected from crowdsourcing over the last five years")

Years = [1, 2, 3, 4, 5]
Funds_collected = [234543, 432564, 332412, 432678, 503210]

mean_years = statistics.mean(Years)
median_years = statistics.median(Years)
mode_years = statistics.mode(Years)

mean_Funds_collected = statistics.mean(Funds_collected)
median_Funds_collected = statistics.median(Funds_collected)
mode_Funds_collected = statistics.mode(Funds_collected)

lowestyears = min(Years)
highestyears = max(Years)
lowestFunds_collected = min(Funds_collected)
highestFunds_collected = max(Funds_collected)

var_Years = statistics.variance(Years)
var_Funds_collected = statistics.variance(Funds_collected)
var_Years = round(var_Years, 2)
var_Funds_collected = round(var_Funds_collected, 2)

stdev_Years = statistics.stdev(Years)
stdev_Funds_collected = statistics.stdev(Funds_collected)
stdev_Years = round(stdev_Years, 2)
stdev_Funds_collected = round(stdev_Funds_collected, 2)

logger.info(f"Years collecting funds mean is {mean_years}")
logger.info(f"Years collecting funds median is {median_years}")
logger.info(f"Years collecting funds mode is {mode_years}")

logger.info(f"Total funds collected mean is {mean_Funds_collected}")
logger.info(f"Total funds collected median is {median_Funds_collected}")
logger.info(f"Total funds collected mode is {mode_Funds_collected}")

logger.info(f"Lowest years collecting funds is {min(Years)}")
logger.info(f"Highest years collecting funds is {max(Years)}")
logger.info(f"Lowest total funds collected is {min(Funds_collected)}")
logger.info(f"Highest total funds collected is {max(Funds_collected)}")

logger.info(f"Variance of years collecting funds is {var_Years}")
logger.info(f"Variance in total funds collected is {var_Funds_collected}")

logger.info(f"Standard deviation of years collecting funds is {stdev_Years}")
logger.info(f"Standard deviation of total funds collected is {stdev_Funds_collected}")
