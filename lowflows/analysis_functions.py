#!/bin/python

import xarray as xr
import numpy as np

def get_quantile_flow(timeseries, quantile):
    '''
    Inputs:
    - timeseries is the daily xarray timeseries you want to base
    your quantile mapping on
    - quantile is a fraction from 0 to 1 (0.1 would be the lower 
    10th percentile)
    Outputs:
    the value of the timeseries corresponding to the quantile you specified
    '''
    return timeseries.quantile(q=quantile).values

def count_annual_days_below_threshold(timeseries, threshold):
    above = timeseries.where(timeseries > threshold)
    count = np.isnan(above).resample(time='A').sum()
    return count

def aug_sept(month):
    return (month>=8) & (month<=9)

def consecutive_days(timeseries):
    '''
    Inputs: 
    - timeseries: a timeseries of hi/low flows - can use get_quantile_flow to get this
    Outputs:
    - the longest length of consecutive days of hi/low flow
    '''
    flow_dates = timeseries.time
    # spacing between each hi/low flow date:
    differences = flow_dates.diff('time')
    # length of one day:
    delta = np.timedelta64(86400000000000,'ns')
    # filter out hi/low flow periods greater than 1 day
    greatest_ind = np.where(differences > delta)[0]
    # return the longest number of consecutive days of hi/low flow
    return np.diff(greatest_ind).max()-1

