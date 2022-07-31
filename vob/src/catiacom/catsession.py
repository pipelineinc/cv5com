import catbase.client as cb

class catia():
    """
    catia session
    """
    def __init__(self):
        super.__init__()
        self.session = self.connect()

    def _connect():
        """
        com handle to catia session
        """
        return cb.SafeDispatch("CATIA.Application")

    def getApp(self):
        """
        get app
        """
        return self
    
    def openDocument(self, filename):
        """
        open document
        """
        pass