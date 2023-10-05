class Patient:
    def __init__(self, iden, nm, ad, ph, vs):
        self.identification = iden
        self.name = nm
        self.address = ad
        self.phone = ph
        self.veteran_status = vs

    def getidentification(self):
        return self.identification
    
    def getname(self):
        return self.name
    def getaddress(self):
        return self.address
    def getphone(self):
        return self.phone
    def getveteranstatus(self):
        return self.veteran_status