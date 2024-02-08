"""Module containing code for plotting a lightcurve."""

from matplotlib import pyplot as plt
    
def plot_lightcurve(mjds, mags, x_label='mjd (days)', y_label='mag', color='blue', marker='o'):
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(1,1,1)
    ax.scatter(
        mjds,
        mags,
        color=color,
        marker=marker
    )
    ax.minorticks_on()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.tight_layout()
    plt.gca().invert_yaxis()
    plt.show()

