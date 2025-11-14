class Rule:
    def __init__(self, conditions, diagnosis):
        self.conditions = conditions
        self.diagnosis = diagnosis


class ExpertSystem:
    def __init__(self):
        self.rules = []    # <-- REQUIRED!

    def add_rule(self, conditions, diagnosis):
        self.rules.append(Rule(conditions, diagnosis))

    def diagnose(self, symptoms):
        matches = []
        for rule in self.rules:
            if all(condition in symptoms for condition in rule.conditions):
                matches.append(rule.diagnosis)
        return matches



def main():
    print("🤖 Welcome to the Rule-Based Expert System!")
    print("This system diagnoses common illnesses based on symptoms.\n")

    system = ExpertSystem()
    system.add_rule(["fever", "cough", "sore throat"], "You might have the Common Cold.")
    system.add_rule(["fever", "body ache", "fatigue"], "You might have the Flu.")
    system.add_rule(["headache", "nausea", "sensitivity to light"], "You might have a Migraine.")
    system.add_rule(["stomach pain", "vomiting", "loose motion"], "You might have Food Poisoning.")
    system.add_rule(["sneezing", "runny nose", "itchy eyes"], "You might have an Allergy.")

    print("Please enter your symptoms one by one.")
    print("Type 'done' when finished.\n")

    symptoms = []
    while True:
        symptom = input("Enter a symptom: ").strip().lower()
        if symptom == "done":
            break
        if symptom:
            symptoms.append(symptom)

    print("\nAnalyzing your symptoms...")
    diagnosis = system.diagnose(symptoms)
    print(f"\n🩺 Diagnosis: {diagnosis}\n")
    print("✨ Thank you for using the Expert System!")


main()
git remote add origin https://github.com/aastha18263/expert_system.git
