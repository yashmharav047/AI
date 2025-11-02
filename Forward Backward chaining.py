# ===== Knowledge Base (KB) =====
KB = [
    ("rule", "Human(x) -> Mortal(x)"),
    ("fact", "Human(Socrates)")
]

# ===== Forward Chaining =====
def forward_chaining(KB):
    facts = {f for t, f in KB if t == "fact"}
    changed = True

    while changed:
        changed = False

        # Rule: Human(x) -> Mortal(x)
        for f in list(facts):
            if f.startswith("Human("):
                entity = f[6:-1]
                if f"Mortal({entity})" not in facts:
                    facts.add(f"Mortal({entity})")
                    changed = True
    return facts


# ===== Backward Chaining =====
def backward_chaining(goal, KB):
    facts = {f for t, f in KB if t == "fact"}

    if goal in facts:
        return True

    if goal.startswith("Mortal("):
        ent = goal[7:-1]
        return backward_chaining(f"Human({ent})", KB)

    return False


# ===== Resolution (Demo) =====
def resolution_demo():
    print("\n=== Resolution Proof for Mortal(Socrates) ===")
    print("1. ¬Human(x) ∨ Mortal(x)")
    print("2. Human(Socrates)")
    print("Negated Goal: ¬Mortal(Socrates)")
    print("From (1)+(2): Mortal(Socrates)")
    print("Contradiction with ¬Mortal(Socrates) → Proven ✅")


# ===== Main Run =====
if __name__ == "__main__":
    print("=== Forward Chaining Results ===")
    facts = forward_chaining(KB)
    for f in sorted(facts):
        print("•", f)

    print("\n=== Backward Chaining ===")
    print("Mortal(Socrates):", backward_chaining("Mortal(Socrates)", KB))

    resolution_demo()
