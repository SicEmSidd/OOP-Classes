import PatientClass as pa
import ProcedureClass as pr

Procedure1 = pr.Procedure("Physical Exam","2/15/2022", "Dr. Irvine", 250, 1)
Procedure2 = pr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
Procedure3 = pr.Procedure("CT Scan","2/17/2022", "Dr. Hamilton", 1200, 2)

listofprocedures = [Procedure1, Procedure2, Procedure3]

Patient = pa.Patient(1, "Matt Jones","123 Main St., Waco, TX 76706","254-555-7415","TRUE")

print("*** Patient Bill ***")
print(f"Name: {Patient.getname()}")
print(f"Address: {Patient.getaddress()}")
print(f"Phone: {Patient.getphone()}")

subtotal = 0
for i in range(len(listofprocedures)):
    if listofprocedures[i].get_patient_id() == Patient.getidentification():
        print(f"\nProcedure: {listofprocedures[i].get_name_of_procedure()}")
        print(f"Date: {listofprocedures[i].get_date()}")
        print(f"Practitioner: {listofprocedures[i].get_name_of_practitioner()}")
        print(f"Charge: ${listofprocedures[i].get_charge()}")
        subtotal += listofprocedures[i].get_charge()

if Patient.getveteranstatus() == "TRUE":
    total = subtotal - (subtotal * .4)
else:
    total = subtotal
print(f"\nTotal Charges: ${total}")