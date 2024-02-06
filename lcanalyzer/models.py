"""Module containing models representing lightcurves.

The Model layer is responsible for the 'business logic' part of the software.

The lightcurves are saved in a table (2D array) where each row corresponds to a single observation. 
Depending on the dataset (LSST or Kepler), 
a table can contain observations of a single or several objects, 
in a single or different bands.
"""

import pandas as pd
import numpy as np
from astropy.timeseries import LombScargle

def load_dataset(filename):
    """Load a table from CSV file.
    
    :param filename: The name of the .csv file to load.
    :returns: pd.DataFrame with the data from the file.
    """
    return pd.read_csv(filename)


def mean_mag(data,mag_col):
    """Calculate the mean magnitude of a lightcurve.
    
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The mean value of the column
    """
    return data[mag_col].mean()


def max_mag(data,mag_col):
    """Calculate the max magnitude of a lightcurve.
    
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The max value of the column
    """
    return data[mag_col].max()


def min_mag(data,mag_col):
    """Calculate the min magnitude of a lightcurve.
    
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The min value of the column.
    """
    return data[mag_col].min()

def calc_stat(lc, bands, mag_col):
    """
    Get maximum values for all bands
    
    :param lc: Dictionary of pd.DataFrame with observed magnitudes for a single source.
    :param bands: string of band names.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: A dictionary with the max value of the column for each dataset.
    """
    # Define an empty dictionary where we will store the results
    stat = {}
    # For each band get the maximum value and store it in the dictionary
    for b in bands:
        stat[b + "_max"] = max_mag(lc[b], mag_col)
    return stat

def calc_stats(lc, bands, mag_col):
    """
    Calculate max, mean and min values for all bands of a light curve

    :param lc: Dictionary of pd.DataFrame with observed magnitudes for a single source.
    :param bands: string of band names.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: A pd.Dataframe with the max, mean, and min values of the column for each dataset.
    """
    stats = {}
    for b in bands:
        stat = {}
        stat["max"] = max_mag(lc[b], mag_col)
        stat["mean"] = mean_mag(lc[b], mag_col)
        stat["min"] = min_mag(lc[b], mag_col)
        stats[b] = stat
    return pd.DataFrame.from_records(stats)
