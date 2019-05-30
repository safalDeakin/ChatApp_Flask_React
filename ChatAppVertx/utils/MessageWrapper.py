

class EventMessageWrapper(object):

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (EventMessageWrapper,cls).__new__(cls)
        return cls.instance

    def wrap(self,event,jsonMessage,sender):

        newMessage = {'event': event, 'data':{ 'msg': jsonMessage,'sender':sender}}
        return newMessage


MessageWrapper = EventMessageWrapper()
