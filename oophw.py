class DigitalTwin:
    def __init__(self):
        self.chambers = []
        self.filters = []

    def runProcess(self):
        for chamber in self.chambers:
            chamber.startReaction()
        for f in self.filters:
            f.filterFlow()

    def addChamber(self, chamber):
        self.chambers.append(chamber)

    def addFilter(self, filter_system):
        self.filters.append(filter_system)


class Chamber:
    def __init__(self, temperature=25.0, pressure=1.0, impurities=0.0):
        self.temperature = temperature
        self.pressure = pressure
        self.impurities = impurities

    def startReaction(self):
        pass


class AmmoniaChamber(Chamber):
    def __init__(self, catalyst=None, **kwargs):
        super().__init__(**kwargs)
        self.catalyst = catalyst

    def addCatalyst(self, catalyst):
        self.catalyst = catalyst


class OxidationChamber(Chamber):
    def __init__(self, catalyst=None, oxygen_percent=21.0, **kwargs):
        super().__init__(**kwargs)
        self.catalyst = catalyst
        self.oxygen_percent = oxygen_percent

    def startReaction(self):
        print(f"Окисление аммиака при {self.temperature}C и {self.pressure} атм")


class ConcentrationChamber(Chamber):
    def __init__(self, waterContent=50.0, **kwargs):
        super().__init__(**kwargs)
        self.waterContent = waterContent

    def removeExcessWater(self):
        if self.waterContent > 10:
            self.waterContent -= 10


class Catalyst:
    def __init__(self, catalyst_type, batch_id):
        self.type = catalyst_type
        self.currentBatchID = batch_id
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class FilterSystem:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.contamination = 0.0

    def filterFlow(self):
        self.contamination += 1.0

    def washFilter(self):
        self.contamination = 0.0
