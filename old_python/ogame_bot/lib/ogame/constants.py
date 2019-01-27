from enum import Enum, IntEnum


class Resources(Enum):
    Metal = "metal"
    Crystal = "crystal"
    Deuterium = "deuterium"
    Energy = "energy"
    DarkMatter = "dark_matter"


class Me(Enum):
    Id = 'id'
    Name = 'name'
    Points = "points"
    Rank = "rank"
    Total = "total"
    HonourPoints = "honour_points"
    PlanetsId = "planet_ids"


class Buildings(IntEnum):
    MetalMine = 1
    CrystalMine = 2
    DeuteriumSynthesizer = 3
    SolarPlant = 4
    FusionReactor = 12
    MetalStorage = 22
    CrystalStorage = 23
    DeuteriumTank = 24
    ShieldedMetalDen = 25
    UndergroundCrystalDen = 26
    SeabedDeuteriumDen = 27


class Facilities(IntEnum):
    AllianceDepot = 34
    RoboticsFactory = 14
    Shipyard = 21
    ResearchLab = 31
    MissileSilo = 44
    NaniteFactory = 15
    Terraformer = 33
    SpaceDock = 36
    LunarBase = 41
    JumpGate = 43
    SensorPhalanx = 42


class Defenses(IntEnum):
    RocketLauncher = 401
    LightLaser = 402
    HeavyLaser = 403
    GaussCannon = 404
    IonCannon = 405
    PlasmaTurret = 406
    SmallShieldDome = 407
    LargeShieldDome = 408
    AntiBallisticMissiles = 502
    InterplanetaryMissiles = 503


class Ships(IntEnum):
    SmallCargo = 202
    LargeCargo = 203
    LightFighter = 204
    HeavyFighter = 205
    Cruiser = 206
    Battleship = 207
    ColonyShip = 208
    Recycler = 209
    EspionageProbe = 210
    Bomber = 211
    SolarSatellite = 212
    Destroyer = 213
    Deathstar = 214
    Battlecruiser = 215


class Research(IntEnum):
    EspionageTechnology = 106
    ComputerTechnology = 108
    WeaponsTechnology = 109
    ShieldingTechnology = 110
    ArmourTechnology = 111
    EnergyTechnology = 113
    HyperspaceTechnology = 114
    CombustionDrive = 115
    ImpulseDrive = 117
    HyperspaceDrive = 118
    LaserTechnology = 120
    IonTechnology = 121
    PlasmaTechnology = 122
    IntergalacticResearchNetwork = 123
    Astrophysics = 124
    GravitonTechnology = 199


class Speed(IntEnum):
    TEN_PERCENT = 1
    TWENTY_PERCENT = 2
    THIRTY_PERCENT = 3
    FORTY_PERCENT = 4
    FIFTY_PERCENT = 5
    SIXTY_PERCENT = 6
    SEVENTY_PERCENT = 7
    EIGHTY_PERCENT = 8
    NINETY_PERCENT = 9
    HUNDRED_PERCENT = 10


class Missions(IntEnum):
    Attack = 1
    GroupedAttack = 2
    Transport = 3
    Park = 4
    ParkInThatAlly = 5
    Spy = 6
    Colonize = 7
    RecycleDebrisField = 8
    Destroy = 9
    Expedition = 15


class TargetTypes(IntEnum):
    Planet = 1
    Debris = 2
    Moon = 3


class Coords(Enum):
    Galaxy = "galaxy"
    System = "system"
    Position = "position"
    Type = "type"


# from https://board.en.ogame.gameforge.com/index.php/Thread/78613-All-Buildings-Researches-Fleets-and-Defences/
Prices = {
    Buildings.MetalMine: {
        'cost': {Resources.Metal: [60, 1.5], Resources.Crystal: [15, 1.5], Resources.Deuterium: [0, 0]},
        'production': [30, 1.1],
        'consummation': [10, 1.1],
        'prerequisites': {}
    },
    Buildings.CrystalMine: {
        'cost': {Resources.Metal: [48, 1.6], Resources.Crystal: [24, 1.6], Resources.Deuterium: [0, 0]},
        'production': [20, 1.1],
        'consummation': [10, 1.1],
        'prerequisites': {}
    },
    Buildings.DeuteriumSynthesizer: {
        'cost': {Resources.Metal: [225, 1.5], Resources.Crystal: [75, 1.5], Resources.Deuterium: [0, 0]},
        'production': [10, 1.1],
        'consummation': [20, 1.1],
        'prerequisites': {}
    },
    Buildings.MetalStorage: {
        'cost': {Resources.Metal: [500, 2], Resources.Crystal: [0, 0], Resources.Deuterium: [0, 0]},
        'stock': [1.6],
        'prerequisites': {}
    },
    Buildings.CrystalStorage: {
        'cost': {Resources.Metal: [500, 2], Resources.Crystal: [250, 2], Resources.Deuterium: [0, 0]},
        'stock': [1.6],
        'prerequisites': {}
    },
    Buildings.DeuteriumTank: {
        'cost': {Resources.Metal: [1000, 2], Resources.Crystal: [1000, 2], Resources.Deuterium: [0, 0]},
        'stock': [1.6],
        'prerequisites': {}
    },
    Buildings.FusionReactor: {
        'cost': {Resources.Metal: [900, 1.8], Resources.Crystal: [360, 1.8], Resources.Deuterium: [180, 1.8]},
        'prerequisites': {Buildings.DeuteriumSynthesizer: 5, Research.EnergyTechnology: 3}
    },
    Buildings.SolarPlant: {
        'cost': {Resources.Metal: [75, 1.5], Resources.Crystal: [30, 1.5], Resources.Deuterium: [0, 0]},
        'production': [20, 1.1],
        'prerequisites': {}
    },
    Facilities.RoboticsFactory: {
        'cost': {Resources.Metal: [400, 2], Resources.Crystal: [120, 2], Resources.Deuterium: [200, 2]},
        'prerequisites': {}
    },
    Facilities.Shipyard: {
        'cost': {Resources.Metal: [400, 2], Resources.Crystal: [200, 2], Resources.Deuterium: [100, 2]},
        'prerequisites': {Facilities.RoboticsFactory: 2}
    },
    Facilities.ResearchLab: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [400, 2], Resources.Deuterium: [200, 2]},
        'prerequisites': {}
    },
    Facilities.NaniteFactory: {
        'cost': {Resources.Metal: [1000000, 2], Resources.Crystal: [500000, 2], Resources.Deuterium: [100000, 2]},
        'prerequisites': {Facilities.RoboticsFactory: 10, Research.ComputerTechnology: 10}
    },
    Facilities.Terraformer: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [50000, 2], Resources.Deuterium: [100000, 2]},
        'prerequisites': {Facilities.NaniteFactory: 1, Research.EnergyTechnology: 12}
    },
    Facilities.MissileSilo: {
        'cost': {Resources.Metal: [20000, 2], Resources.Crystal: [20000, 2], Resources.Deuterium: [1000, 2]},
        'stock': [10, 5],
        'prerequisites': {Facilities.Shipyard: 2}
    },
    Facilities.AllianceDepot: {
        'cost': {Resources.Metal: [20000, 2], Resources.Crystal: [20000, 2], Resources.Deuterium: [1000, 2]},
        'prerequisites': {}
    },
    Facilities.SpaceDock: {
        'cost': {Resources.Metal: [2500, 2], Resources.Crystal: [625, 2], Resources.Deuterium: [0, 2],
                 Resources.Energy: [156, 2]},
        'prerequisites': {Facilities.Shipyard: 2}
    },
    Facilities.LunarBase: {
        'cost': {Resources.Metal: [20000, 2], Resources.Crystal: [40000, 2], Resources.Deuterium: [20000, 2]},
        'prerequisites': {}
    },
    Facilities.SensorPhalanx: {
        'cost': {Resources.Metal: [20000, 2], Resources.Crystal: [40000, 2], Resources.Deuterium: [20000, 2]},
        'prerequisites': {Facilities.LunarBase: 1}
    },
    Facilities.JumpGate: {
        'cost': {Resources.Metal: [2000000, 2], Resources.Crystal: [4000000, 2], Resources.Deuterium: [2000000, 2]},
        'prerequisites': {Facilities.LunarBase: 1, Research.HyperspaceTechnology: 7}
    },
    Research.EspionageTechnology: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [1000, 2], Resources.Deuterium: [200, 2]},
        'prerequisites': {Facilities.ResearchLab: 3}
    },
    Research.ComputerTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [400, 2], Resources.Deuterium: [600, 2]},
        'prerequisites': {Facilities.ResearchLab: 1}
    },
    Research.WeaponsTechnology: {
        'cost': {Resources.Metal: [800, 2], Resources.Crystal: [200, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {Facilities.ResearchLab: 4}
    },
    Research.ShieldingTechnology: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [600, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {Facilities.ResearchLab: 6, Research.EnergyTechnology: 3}
    },
    Research.ArmourTechnology: {
        'cost': {Resources.Metal: [1000, 2], Resources.Crystal: [0, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {Facilities.ResearchLab: 2}
    },
    Research.EnergyTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [800, 2], Resources.Deuterium: [400, 2]},
        'prerequisites': {Facilities.ResearchLab: 1}
    },
    Research.HyperspaceTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [4000, 2], Resources.Deuterium: [2000, 2]},
        'prerequisites': {Facilities.ResearchLab: 7, Research.EnergyTechnology: 5, Research.ShieldingTechnology: 5}
    },
    Research.CombustionDrive: {
        'cost': {Resources.Metal: [400, 2], Resources.Crystal: [0, 2], Resources.Deuterium: [600, 2]},
        'prerequisites': {Research.EnergyTechnology: 1}
    },
    Research.ImpulseDrive: {
        'cost': {Resources.Metal: [2000, 2], Resources.Crystal: [4000, 2], Resources.Deuterium: [600, 2]},
        'prerequisites': {Facilities.ResearchLab: 2, Research.EnergyTechnology: 1}
    },
    Research.HyperspaceDrive: {
        'cost': {Resources.Metal: [10000, 2], Resources.Crystal: [20000, 2], Resources.Deuterium: [6000, 2]},
        'prerequisites': {Research.HyperspaceTechnology: 3}
    },
    Research.LaserTechnology: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [100, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {Research.EnergyTechnology: 2}
    },
    Research.IonTechnology: {
        'cost': {Resources.Metal: [1000, 2], Resources.Crystal: [300, 2], Resources.Deuterium: [100, 2]},
        'prerequisites': {Research.LaserTechnology: 5, Facilities.ResearchLab: 4, Research.EnergyTechnology: 4}
    },
    Research.PlasmaTechnology: {
        'cost': {Resources.Metal: [2000, 2], Resources.Crystal: [4000, 2], Resources.Deuterium: [1000, 2]},
        'prerequisites': {Research.EnergyTechnology: 8, Research.IonTechnology: 5, Research.LaserTechnology: 10}
    },
    Research.IntergalacticResearchNetwork: {
        'cost': {Resources.Metal: [240000, 2], Resources.Crystal: [400000, 2], Resources.Deuterium: [160000, 2]},
        'prerequisites': {Facilities.ResearchLab: 10, Research.ComputerTechnology: 8, Research.HyperspaceTechnology: 8}
    },
    Research.GravitonTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [0, 2], Resources.Deuterium: [0, 2],
                 Resources.Energy: [300000, 2]},
        'prerequisites': {Facilities.ResearchLab: 12}
    },
    Research.Astrophysics: {
        'cost': {Resources.Metal: [4000, 2], Resources.Crystal: [8000, 2], Resources.Deuterium: [4000, 2]},
        'prerequisites': {Research.EspionageTechnology: 4, Research.ImpulseDrive: 3}
    },
    Ships.SolarSatellite: {
        'cost': {Resources.Metal: [0, 1], Resources.Crystal: [2000, 1], Resources.Deuterium: [500, 1]},
        'production': [30],
        'prerequisites': {Facilities.Shipyard: 2}
    },
    Ships.Bomber: {
        'cost': {Resources.Metal: [50000, 1], Resources.Crystal: [25000, 1], Resources.Deuterium: [15000, 1]},
        'prerequisites': {Facilities.Shipyard: 8, Research.ImpulseDrive: 6, Research.PlasmaTechnology: 5}
    },
    Ships.EspionageProbe: {
        'cost': {Resources.Metal: [0, 1], Resources.Crystal: [1000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 3, Research.EspionageTechnology: 2}
    },
    Ships.Recycler: {
        'cost': {Resources.Metal: [10000, 1], Resources.Crystal: [6000, 1], Resources.Deuterium: [2000, 1]},
        'prerequisites': {Facilities.Shipyard: 4, Research.CombustionDrive: 6, Research.ShieldingTechnology: 2}
    },
    Ships.ColonyShip: {
        'cost': {Resources.Metal: [10000, 1], Resources.Crystal: [20000, 1], Resources.Deuterium: [10000, 1]},
        'prerequisites': {Facilities.Shipyard: 4, Research.ImpulseDrive: 3}
    },
    Ships.Battleship: {
        'cost': {Resources.Metal: [45000, 1], Resources.Crystal: [15000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 7, Research.HyperspaceDrive: 4}
    },
    Ships.Cruiser: {
        'cost': {Resources.Metal: [20000, 1], Resources.Crystal: [7000, 1], Resources.Deuterium: [2000, 1]},
        'prerequisites': {Facilities.Shipyard: 5, Research.IonTechnology: 2, Research.ImpulseDrive: 4}
    },
    Ships.HeavyFighter: {
        'cost': {Resources.Metal: [6000, 1], Resources.Crystal: [4000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 3, Research.ArmourTechnology: 2, Research.ImpulseDrive: 2}
    },
    Ships.LightFighter: {
        'cost': {Resources.Metal: [3000, 1], Resources.Crystal: [1000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 1, Research.CombustionDrive: 1}
    },
    Ships.LargeCargo: {
        'cost': {Resources.Metal: [6000, 1], Resources.Crystal: [6000, 1], Resources.Deuterium: [0, 1]},
        'stock': [5000],
        'prerequisites': {Facilities.Shipyard: 4, Research.CombustionDrive: 6}
    },
    Ships.SmallCargo: {
        'cost': {Resources.Metal: [2000, 1], Resources.Crystal: [2000, 1], Resources.Deuterium: [0, 1]},
        'stock': [25000],
        'prerequisites': {Facilities.Shipyard: 2, Research.CombustionDrive: 2}
    },
    Ships.Destroyer: {
        'cost': {Resources.Metal: [60000, 1], Resources.Crystal: [50000, 1], Resources.Deuterium: [15000, 1]},
        'prerequisites': {Facilities.Shipyard: 9, Research.HyperspaceTechnology: 5, Research.HyperspaceDrive: 6}
    },
    Ships.Deathstar: {
        'cost': {Resources.Metal: [5000000, 1], Resources.Crystal: [4000000, 1], Resources.Deuterium: [1000000, 1]},
        'prerequisites': {Facilities.Shipyard: 12, Research.GravitonTechnology: 1, Research.HyperspaceDrive: 7,
                          Research.HyperspaceTechnology: 6}
    },
    Ships.Battlecruiser: {
        'cost': {Resources.Metal: [30000, 1], Resources.Crystal: [40000, 1], Resources.Deuterium: [15000, 1]},
        'prerequisites': {Facilities.Shipyard: 8, Research.LaserTechnology: 12, Research.HyperspaceDrive: 5,
                          Research.HyperspaceTechnology: 5}
    },
    Defenses.LightLaser: {
        'cost': {Resources.Metal: [1500, 1], Resources.Crystal: [500, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 2, Research.LaserTechnology: 3}
    },
    Defenses.HeavyLaser: {
        'cost': {Resources.Metal: [6000, 1], Resources.Crystal: [2000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 4, Research.EnergyTechnology: 3, Research.LaserTechnology: 6}
    },
    Defenses.GaussCannon: {
        'cost': {Resources.Metal: [20000, 1], Resources.Crystal: [15000, 1], Resources.Deuterium: [2000, 1]},
        'prerequisites': {Facilities.Shipyard: 6, Research.WeaponsTechnology: 3, Research.EnergyTechnology: 6,
                          Research.ShieldingTechnology: 1}
    },
    Defenses.IonCannon: {
        'cost': {Resources.Metal: [2000, 1], Resources.Crystal: [6000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 4, Research.IonTechnology: 4}
    },
    Defenses.PlasmaTurret: {
        'cost': {Resources.Metal: [50000, 1], Resources.Crystal: [50000, 1], Resources.Deuterium: [30000, 1]},
        'prerequisites': {Facilities.Shipyard: 8, Research.PlasmaTechnology: 7}
    },
    Defenses.SmallShieldDome: {
        'cost': {Resources.Metal: [10000, 1], Resources.Crystal: [10000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 1, Research.ShieldingTechnology: 2}
    },
    Defenses.LargeShieldDome: {
        'cost': {Resources.Metal: [50000, 1], Resources.Crystal: [50000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.Shipyard: 6, Research.ShieldingTechnology: 6}
    },
    Defenses.AntiBallisticMissiles: {
        'cost': {Resources.Metal: [8000, 1], Resources.Crystal: [2000, 1], Resources.Deuterium: [0, 1]},
        'prerequisites': {Facilities.MissileSilo: 2}
    },
    Defenses.InterplanetaryMissiles: {
        'cost': {Resources.Metal: [12500, 1], Resources.Crystal: [2500, 1], Resources.Deuterium: [10000, 1]},
        'prerequisites': {Facilities.MissileSilo: 4, Research.ImpulseDrive: 1}
    }
}
