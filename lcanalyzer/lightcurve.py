import pandas as pd
import numpy as np

class Lightcurve:
    """A Lightcurve class"""
    def __init__(self, obj_id, mjds, mags, mag_errs = None):
        self.obj_id = obj_id
        self.lc = {
                   'mjd': np.array([]),
                   'mag': np.array([])
                  }
        if mjds is not None:
            self.add_observations(mjds, mags, mag_errs = None)

    def __str__(self):
      return str(self.obj_id)

    def add_observations(self, mjds, mags, mag_errs=None):
        """
        Adds observations to the light curve.
    
        Args:
          mjds: A vector of Modified Julian Dates (x values).
          mags: A vector of luminosities (y values).
        """

        self.convert_to_array(mjds)
        self.convert_to_array(mags)
        
        observation_arrays = [mjds, mags]
        
        self.lc['mjd'] = np.array(mjds)
        self.lc['mag'] = np.array(mags)
        if mag_errs is not None:
            self.convert_to_array(mag_errs)
            observation_arrays.append(mag_errs)
            self.lc['mag_errs'] = np.array(mag_errs)

        self.compare_len(observation_arrays)

        return

    def __len__(self):
        """
        Returns length of lightcurve
        """
        return len(self.lc['mjd'])


    def convert_to_array(self, var):
        if not isinstance(var, np.ndarray):
            if isinstance(var, (list, tuple, pd.Series)):
                var = np.array(var)
            elif isinstance(var, (int, float)):
                var = np.array([var])
            else:
               raise ValueError("Data must be array-like, int, or float")

        return var

    def compare_len(self, arrays):
        for array in arrays:
            if len(array) != self.__len__():
                raise Exception("All observational arrays must have the same length")
                
    @property
    def mean_mag(self):
        return np.mean(self.lc['mags'])