
class MessageWrapper(object):

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (MessageWrapper,cls).__new__(cls)
        return cls.instance

    def wrap(self,event,jsonMessage,sender):

        newMessage = {'event': event, 'data':{ 'msg': jsonMessage,'sender':sender}}
        return newMessage


MessageWrapper = MessageWrapper()
