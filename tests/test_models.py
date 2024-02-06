"""Tests for statistics functions within the Model layer."""

import pandas as pd
import numpy as np

def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_integers():
    # Test that min_mag function works for integers
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 1

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_integers():
    # Test that mean_mag function works for integers
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = np.mean([1, 7, 3])

    assert mean_mag(test_input_df, test_input_colname) == test_output
    
def test_max_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_calc_stat_integers():
    # Test that calc_stat function works for integers
    from lcanalyzer.models import calc_stat

    test_input_df1 = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_df2 = pd.DataFrame(data=[[7, 3, 2], 
                                        [8, 4, 2], 
                                        [5, 6, 4]], columns=list("abc"))
    test_input_df3 = pd.DataFrame(data=[[2, 6, 3], 
                                        [1, 3, 6], 
                                        [8, 9, 1]], columns=list("abc"))
    
    test_input = {"df1": test_input_df1, "df2": test_input_df2, "df3": test_input_df3}
    test_input_colname = "b"
    test_output = {"df1_max": 8, "df2_max": 6, "df3_max": 9}
    
    assert calc_stat(test_input, ["df1", "df2", "df3"], test_input_colname) == test_output
    