# Example class using in the proxy testing above.
class Television:
    def __init__(self):
        self._channel = None
        self._power = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        if self._power == 'on':
            self._power = 'off'
        else:
            self._power = 'on'

    def is_on(self):
        return self._power == 'on'

class Proxy:
    def __init__(self, target_object):
#       WRITE CODE HERE
        self._msglogs = list()
#        self._msglogs = {'test_counter' : 0}
        #initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object

#   WRITE CODE HERE

    def __setattr__(self, msg_call, value):
#        try:
#            self._msglogs[msg_call] += 1
#        except:
#            self._msglogs.update({msg_call : 1})

#        self._obj__setattr__(msg_call, value)
        try:
            self._obj__setattr__(msg_call, value)
        except:
            super().__setattr__(msg_call, value)


    def __getattr__(self, msg_call, *args):
#        try:
#            self._msglogs[msg_call] += 1
#        except:
#            self._msglogs.update({msg_call : 1})

#        return getattr(self._obj, msg_call, *args)
        try:
            self._obj__getattribute__(msg_call, *args)
        except:
            super().__getattribute__(msg_call, *args)

    def messages(self):
        return [key for key in self._msglogs.keys()]

    def was_called(self, msg_call):
        return msg_call in self._msglogs

    def number_of_times_called(self, msg_call):
        return [count for key, count in self._msglogs.items() if key == msg_call]
