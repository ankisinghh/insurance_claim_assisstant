import json
from claim_rules import evaluate_claim

def load_claims():
    with open("sample_claims.json", "r") as file:
        return json.load(file)

def process_claims():
    claims = load_claims()
    for claim in claims:
        result = evaluate_claim(claim)
        print(f"Claim ID {claim['id']}: {result}")

if __name__ == "__main__":
    process_claims()
