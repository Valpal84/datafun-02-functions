"""Valerie Johnson 9/3/23 Crowdsourcing regarding office space and funding"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

# calculate the area of office space required for crowdsourcing 

def get_area_of_crowdsourcing_office(height, width) :
    logger.info(f"CALLING get_area_of_crowdsourcing_office({height, width})")

    try: 
        area = height * width
        logger.info(f"The office area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: (ex)")
        return None
    
# calculate average monthly funds raised
    
def average_monthly_funds_raised(funds, months) :

    logger.info(f"CALLING average monthly funds raised({funds, months})")

    try:
        average_funds = funds / months
        logger.info(f"The average monthly funds are {average_funds}")
        return average_funds
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
# calculate average donations per person

def average_donations_per_person(donations, number_of_people) :

    logger.info(f"CALLING Average donations per person({donations, number_of_people})")

    try:
        average_donations_per_person = donations / number_of_people
        logger.info(f"The average donation per person is {average_donations_per_person}")
        return average_donations_per_person
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

# calculate average total weekly donations

def average_total_weekly_donations(donations, weeks) :

    logger.info(f"CALLING Average total weekly donations({donations, weeks})")

    try:
        average_total_weekly_donations = donations / weeks
        logger.info(f"The average weekly donation is {average_total_weekly_donations}")
        return average_total_weekly_donations
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
if __name__ == "main" :

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info("")

    logger.info("TRY: call get_area_of_a_crowdsourcing_office () with different values")
    get_area_of_crowdsourcing_office(24,15)
    get_area_of_crowdsourcing_office(45,36)
    get_area_of_crowdsourcing_office(23,28)
    logger.info("")

    logger.info("TRY: call average_monthly_funds_raised () with different values")
    average_monthly_funds_raised(245563,12)
    average_monthly_funds_raised(304235,12)
    average_monthly_funds_raised(123657,12)
    logger.info("")

    logger.info("Try: call average_donations_per_person () with different values")
    average_donations_per_person(245563,500)
    average_donations_per_person(304235,500)
    average_donations_per_person(123657,12)
    logger.info("")

    logger.info("TRY: call average_total_weekly_donations () with different values")
    average_total_weekly_donations(245563,52)
    average_total_weekly_donations(304235,52)
    average_total_weekly_donations(123657,52)
    logger.info("")

    print("Done. Please see log file for more details")
    
