# -*- coding: utf-8 -*-
from . import helpers
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


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
