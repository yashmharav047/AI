class CookingPlanner:
    def __init__(self):
        self.state = {
            "kettle_empty": True,
            "water_available": True,
            "tea_leaves": True,
            "hot_water": False,
            "tea_mixture": False,
            "cup_empty": True,
            "cup_with_tea": False
        }
        self.plan = []

    def fill_kettle(self):
        if self.state["kettle_empty"] and self.state["water_available"]:
            self.state["kettle_empty"] = False
            print("Filled kettle with water")
            self.plan.append("FillKettle")

    def boil_water(self):
        if not self.state["kettle_empty"]:
            self.state["hot_water"] = True
            print("Boiled water")
            self.plan.append("BoilWater")

    def add_tea_leaves(self):
        if self.state["hot_water"] and self.state["tea_leaves"]:
            self.state["tea_mixture"] = True
            print("Added tea leaves")
            self.plan.append("AddTeaLeaves")

    def pour_tea(self):
        if self.state["tea_mixture"] and self.state["cup_empty"]:
            self.state["cup_with_tea"] = True
            self.state["cup_empty"] = False
            print("Poured tea into cup")
            self.plan.append("PourTea")

    def make_tea(self):
        self.fill_kettle()
        self.boil_water()
        self.add_tea_leaves()
        self.pour_tea()
        if self.state["cup_with_tea"]:
            print("\n✅ Goal achieved: Cup of tea ready!")
            print("Plan followed:", self.plan)


# Run the planner
planner = CookingPlanner()
planner.make_tea()
