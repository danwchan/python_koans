class Proxy:
    def __init__(self, target_object):
        # WRITE CODE HERE
        self._msglog = dict()
        #initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object
        print('init called and run')

    # WRITE CODE HERE
    def __setattr__(self, msg_call, value):
        if msg_call in ['_msglog', '_obj']:
            
#            print('setattr: {} exceptions for init'.format(msg_call))
            return super().__setattr__(msg_call, value)
        
        else:
            
            if msg_call in self._msglog:
                self._msglog[msg_call] += 1
            else:
                self._msglog.update({msg_call : 1})
                
#            print('setattr: running on the instance {}'.format(self._obj.__str__()))
            return setattr(self._obj, msg_call, value)

    def __getattr__(self, msg_call):
        if msg_call in ['_msglog', '_obj']:
            
#            print('getattr: {} exceptions for init'.format(msg_call))
            return super().__getattr__(msg_call)
        
        else:
            
            if msg_call in self._msglog:
                self._msglog[msg_call] += 1
            else:
                self._msglog.update({msg_call : 1})

#            print('getattr: running on the instance {}'.format(self._obj.__str__()))
            return getattr(self._obj, msg_call)

    def messages(self):
        return [key for key in self._msglog.keys()]

    def was_called(self, msg_call):
        return msg_call in self._msglog

    def number_of_times_called(self, msg_call):
        return [count for key, count in self._msglog.items() if key == msg_call]

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
