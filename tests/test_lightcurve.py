"""Tests for Lightcurve objects created by lightcurve.py"""

import numpy as np

def test_add_observations():
    #Test if observations are added when using Lightcurve().add_observations()
    from lcanalyzer import lightcurve
    np.random.seed(999)
    test_mjds = np.arange(50000,55000,1)
    test_mags = np.random.random(len(test_mjds))
    lc_obj = lightcurve.Lightcurve(obj_id = 123, mjds=None, mags=None)
    lc_obj.add_observations(mjds = test_mjds, mags = test_mags)

    assert lc_obj.lc['mjd'] is not None
    assert lc_obj.lc['mag'] is not None