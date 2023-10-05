class Procedure:
    def __init__(self, nmpro, dt, nmpra, ch, pid):
        self.name_of_procedure = nmpro
        self.name_of_practitioner = nmpra
        self.charge = ch
        self.date = dt
        self.patient_id = pid
    def get_name_of_procedure(self):
        return self.name_of_procedure
    def get_name_of_practitioner(self):
        return self.name_of_practitioner
    def get_patient_id(self):
        return self.patient_id
    def get_date(self):
        return self.date
    def get_charge(self):
        return self.charge