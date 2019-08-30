import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


def define_template(nb, profile_length):
    """
    gets the templates to use for correlation
    """
    if int(profile_length/10) < 5:
        npts = 5
    else:
        npts = int(profile_length/10)

    if nb == 1:
        print('using exp')
        template = -np.exp(np.linspace(0, 1, npts)/50)+3  # this parameters were empirically determined to look like an ocean profile's exponential
    elif nb == 2:
        print('using gauss')
        template = gaussian(np.linspace(0, 1, npts), 0.5, 1)
    elif nb == 3:
        print('step')
        template = [0., 0, 1, 1]
    else:
        print("I don't undertsand the template shape")
        exit(0)
    return template


def find_correlation(in_signal, coord, template, cut_range):
    """
    Function to find max correlation between a template shape
    and a signal, and find the location of that maximum.
    user input: in_signal ( = a 1D array with the profile),
    coord ( = corresponding 1D array with coordinate values),
    template ( = number, corresponding to pre-defined template shape, nb 1, 2,
    or 3)
    cut_range ( = x times the template width will be used for fitting)
    returns:
    """
    temp = define_template(template, len(in_signal))
    corr_array = signal.correlate(in_signal, temp,  mode='same')  # xcorr
    loc = np.where(np.abs(corr_array) == np.max(np.abs(corr_array)))
    loc_med = np.median(loc)
    print('loc_med = ', loc_med)
    cut_beg = int(loc_med-cut_range*len(temp))
    cut_end = int(loc_med+cut_range*len(temp))
    if cut_beg < 0:
        cut_beg = 0
    if cut_end >= len(coord):
        cut_end = len(coord)-1
    print('starting figure')
    fig, (ax0, ax1, ax2, ax3) = plt.subplots(1, 4, figsize=(10, 5), sharey=True)
    print('initialised fig')
    ax0.set_title('Template nb ' + str(template))
    ax0.plot(temp, coord[:len(temp)], label='template')
    ax0.invert_yaxis()
    ax0.set_ylabel('Vertical coordinates')
    ax1.set_title('This is the signal \n you provided')
    ax1.plot(in_signal, coord, label='signal')
    ax2.set_title('This is the correlation \n between them')
    ax2.plot(corr_array, coord, label='correlation')
    ax3.set_title('This is where I find \n the maximum correlation')
    ax3.plot(temp, coord[:len(temp)]+coord[int(loc_med)]-coord[len(temp)]/2., label='shifted template')
    ax3.axhline(coord[cut_beg], ls='--', c='k')
    ax3.axhline(coord[cut_end], ls='--', c='k')
    for ax in [ax0, ax1, ax2, ax3]:
        ax.legend(loc=0)
    plt.tight_layout()
    plt.show()
    print('exiting, see ya!')
    return in_signal[cut_beg:cut_end+1], coord[cut_beg:cut_end+1]