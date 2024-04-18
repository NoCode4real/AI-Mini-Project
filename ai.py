class MedicalDiagnosis:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.symptoms = {}

    def accept_details(self):
        self.name = input("What is the name of the patient? ==> ")
        print()
        self.age = int(input("What is the age of {}? ==> ".format(self.name)))

    def add_symptom(self, symptom):
        choice = input("Does {} have {}? (y/n) ".format(self.name, symptom))
        self.symptoms[symptom] = choice.lower() == 'y'

    def is_infected(self, symptom):
        return self.symptoms.get(symptom, False)

    def has_disease(self, disease, required_symptoms):
        return all(self.is_infected(symptom) for symptom in required_symptoms)

    def conclude(self, disease):
        print("\n{} probably has {}".format(self.name, disease))


def main():
    print("\n\n\n")

    obj = MedicalDiagnosis()
    obj.accept_details()

    symptoms_to_ask = ["fever", "rash", "headache", "runny_nose", "conjuctivities",
                       "cough", "body_ahce", "chills", "soar_throat", "sneezing", "swollen_glands"]

    for symptom in symptoms_to_ask:
        obj.add_symptom(symptom)

    nothing_detected = True

    diseases = {
        "measles": ["fever", "cough", "conjuctivities", "runny_nose", "rash"],
        "german_measles": ["fever", "headache", "runny_nose", "rash"],
        "flu": ["fever", "headache", "body_ahce", "conjuctivities", "chills", "soar_throat", "cough", "runny_nose"],
        "common_cold": ["headache", "sneezing", "soar_throat", "chills", "runny_nose"],
        "mumps": ["fever", "swollen_glands"],
        "chicken_pox": ["fever", "rash", "body_ahce", "chills"],
        "whooping_cough": ["cough", "sneezing", "runny_nose"]
    }

    for disease, symptoms in diseases.items():
        if obj.has_disease(disease, symptoms):
            obj.conclude(disease)
            nothing_detected = False
            break

    if nothing_detected:
        print("\nI am sorry, I am unable to identify the disease ...")

    print("\n\nPRESS ANY KEY TO EXIT")
    input()  # Wait for user input before exiting


if __name__ == "__main__":
    main()
