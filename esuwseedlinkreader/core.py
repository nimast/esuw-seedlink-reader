# -*- coding: utf-8 -*-
from . import helpers
import numpy as np
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient


class GsiClient(EasySeedLinkClient):
    """
    Read seedlink
    """

    def on_data(self, trace):
        """
        Override the on_data callback
        """
        print('Received trace:')
        print(trace)
        print()
        trace.detrend(type='linear')
        div = np.true_divide(trace.data, 405966.0)
        print(div)


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
