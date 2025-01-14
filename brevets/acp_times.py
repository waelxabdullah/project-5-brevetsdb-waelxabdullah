"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described https://rusa.org/pages/rulesForRiders
and https://rusa.org/pages/acp-brevet-control-times-calculator

You MUST provide the following two functions
with the specified signatures. Otherwise, we will not
be able to run our automated test-cases for grading.
You must keep these signatures even if you don't use
all the same arguments. Arguments are explained in the
docstring.
"""
import arrow


Misp = [(0, 200, 15), (200, 400, 15), (400, 600, 15),
         (600, 1000, 11.428), (1000, 1300, 13.333)]
maxsp = [(0, 200, 34), (200, 400, 32), (400, 600, 30),
          (600, 1000, 28), (1000, 1300, 28)]

# Final control times (at or exceeding brevet distance) are special cases
fincl = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}
max_value = 1300




def open_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    """

    :param control_dist_km:  A number. The control distance in kilometers.
    :param brevet_dist_km: A number. The nominal distance of the brevet
        in kilometers, which must be one of 200, 300, 400, 600, or 1000
        (the only official ACP brevet distances).
    :param brevet_start_time: An ISO 8601 format date-time string indicating
        the official start date and time of the brevet.
    :return: An ISO 8601 format date string indicating the control open time.
        This will be in the same time zone as the brevet start time.
    """

    #control_dist_km = km
    if control_dist_km < 0 :
        return False
    startt = arrow.get(brevet_start_time, normalize_whitespace=True)
    startt = startt.shift(hours=-3)

    remain_h = 0
    disleft = control_dist_km
    for fromdi, todi, speed in maxsp:
            seg_length = todi - fromdi
            if disleft > seg_length:
                remain_h += seg_length / speed
                disleft -= seg_length
            else:
                remain_h += disleft / speed
                if remain_h == 0:
                    openti = startt
                    return openti.isoformat()
                openti = startt.shift(hours=remain_h)
                return openti.isoformat()
        # open_time = start_time.replace(hours=elapsed_hours)
        # return open_time.isoformat()
        #return arrow.now().isoformat()



def close_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    """
    Args:
    :param control_dist_km: A number. The control distance in kilometers.
    :parma brevet_dist_km: A number. The nominal distance of the brevet
        in kilometers, which must be one of 200, 300, 400, 600, or 1000
        (the only official ACP brevet distances).
    :param brevet_start_time: An ISO 8601 format date-time string indicating
        the official start time of the brevet.
    :return: An ISO 8601 format date string indicating the control close time.
        This will be in the same time zone as the brevet start time.
    """

    startti = arrow.get(brevet_start_time, normalize_whitespace=True)
    startti = startti.shift(hours=-3)
    last = control_dist_km
    first_close = 1
    if last == 0:
        openti = startti.shift(hours=+1)
        return openti.isoformat()
    else:
        if control_dist_km >= brevet_dist_km:
            duration = fincl[brevet_dist_km]
            finishti = startti.shift(hours=duration)
            return finishti.isoformat()
        remain_h = 0
        dislast = control_dist_km
        for from_dist, to_dist, speed in Misp:
            seg_length = to_dist - from_dist
            if dislast > seg_length:
                remain_h += seg_length / speed
                dislast -= seg_length
            else:
                remain_h += dislast / speed
                cut_time = startti.shift(hours=remain_h)
                return cut_time.isoformat()