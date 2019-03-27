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
