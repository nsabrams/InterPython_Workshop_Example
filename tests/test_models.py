"""Tests for statistics functions within the Model layer."""

import pandas as pd
import numpy as np
import pytest
import pandas.testing as pdt


@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        1),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_min_mag_integers(test_df, test_colname, expected):
    # Test that min_mag function works for integers
    from lcanalyzer.models import min_mag
    assert min_mag(test_df, test_colname) == expected

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        pytest.approx(np.mean([1, 7, 3]), 0.01)),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_mean_mag_integers(test_df, test_colname, expected):
    # Test that mean_mag function works for integers
    from lcanalyzer.models import mean_mag

    assert mean_mag(test_df, test_colname) == expected

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

def test_calc_stats_integers():
    # Test that calc_stats function works for integers
    from lcanalyzer.models import calc_stats
    
    size = (4,3)
    np.random.seed(0)
    df1 = pd.DataFrame(data=np.random.randint(0, 10, size), columns=list("abc"))
    np.random.seed(1)
    df2 = pd.DataFrame(data=np.random.randint(0, 10, size), columns=list("abc"))
    np.random.seed(2)
    df3 = pd.DataFrame(data=np.random.randint(0, 10, size), columns=list("abc"))

    test_input = {"df1": df1, "df2": df2, "df3": df3}
    test_output = pd.DataFrame(data=[[7,8,8],[4.75,4.25,5.25],[0,0,1]],columns=['df1','df2','df3'],index=['max','mean','min'])
    test_input_colname = "b"
    pdt.assert_frame_equal(calc_stats(test_input, ["df1", "df2", "df3"], test_input_colname),
                       test_output,
                       check_exact=False,
                       atol=0.01)
                       

def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)
    