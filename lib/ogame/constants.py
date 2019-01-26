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
        'prerequisites': {}
    },
    Facilities.ResearchLab: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [400, 2], Resources.Deuterium: [200, 2]},
        'prerequisites': {}
    },
    Facilities.NaniteFactory: {
        'cost': {Resources.Metal: [1000000, 2], Resources.Crystal: [500000, 2], Resources.Deuterium: [100000, 2]},
        'prerequisites': {}
    },
    Facilities.Terraformer: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [50000, 2], Resources.Deuterium: [100000, 2]},
        'prerequisites': {}
    },
    Facilities.MissileSilo: {
        'cost': {Resources.Metal: [20000, 2], Resources.Crystal: [20000, 2], Resources.Deuterium: [1000, 2]},
        'stock': [10, 5],
        'prerequisites': {}
    },
    Facilities.AllianceDepot: {
        'cost': {Resources.Metal: [20000, 2], Resources.Crystal: [20000, 2], Resources.Deuterium: [1000, 2]},
        'prerequisites': {}
    },
    Research.EspionageTechnology: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [1000, 2], Resources.Deuterium: [200, 2]},
        'prerequisites': {}
    },
    Research.ComputerTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [400, 2], Resources.Deuterium: [600, 2]},
        'prerequisites': {}
    },
    Research.WeaponsTechnology: {
        'cost': {Resources.Metal: [800, 2], Resources.Crystal: [200, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {}
    },
    Research.ShieldingTechnology: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [600, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {}
    },
    Research.ArmourTechnology: {
        'cost': {Resources.Metal: [1000, 2], Resources.Crystal: [0, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {}
    },
    Research.EnergyTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [800, 2], Resources.Deuterium: [400, 2]},
        'prerequisites': {}
    },
    Research.HyperspaceTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [4000, 2], Resources.Deuterium: [2000, 2]},
        'prerequisites': {}
    },
    Research.CombustionDrive: {
        'cost': {Resources.Metal: [400, 2], Resources.Crystal: [0, 2], Resources.Deuterium: [600, 2]},
        'prerequisites': {}
    },
    Research.ImpulseDrive: {
        'cost': {Resources.Metal: [2000, 2], Resources.Crystal: [4000, 2], Resources.Deuterium: [600, 2]},
        'prerequisites': {}
    },
    Research.HyperspaceDrive: {
        'cost': {Resources.Metal: [10000, 2], Resources.Crystal: [20000, 2], Resources.Deuterium: [6000, 2]},
        'prerequisites': {}
    },
    Research.LaserTechnology: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [100, 2], Resources.Deuterium: [0, 2]},
        'prerequisites': {}
    },
    Research.IonTechnology: {
        'cost': {Resources.Metal: [1000, 2], Resources.Crystal: [300, 2], Resources.Deuterium: [100, 2]},
        'prerequisites': {}
    },
    Research.PlasmaTechnology: {
        'cost': {Resources.Metal: [2000, 2], Resources.Crystal: [4000, 2], Resources.Deuterium: [1000, 2]},
        'prerequisites': {}
    },
    Research.IntergalacticResearchNetwork: {
        'cost': {Resources.Metal: [240000, 2], Resources.Crystal: [400000, 2], Resources.Deuterium: [160000, 2]},
        'prerequisites': {}
    },
    Research.GravitonTechnology: {
        'cost': {Resources.Metal: [0, 2], Resources.Crystal: [0, 2], Resources.Deuterium: [0, 2], Resources.Energy: [300000, 2]},
        'prerequisites': {}
    },
    Research.Astrophysics: {
        'cost': {Resources.Metal: [4000, 2], Resources.Crystal: [8000, 2], Resources.Deuterium: [4000, 2]},
        'prerequisites': {}
    },
    Ships.SolarSatellite: {
        'cost': {Resources.Metal: [0, 0], Resources.Crystal: [0, 0], Resources.Deuterium: [0, 0]},
        'production': [30],
        'prerequisites': {}
    },
    Ships.Bomber: {
        'cost': {Resources.Metal: [50000, 0], Resources.Crystal: [25000, 0], Resources.Deuterium: [15000, 0]},
        'prerequisites': {}
    },
    Ships.EspionageProbe: {
        'cost': {Resources.Metal: [0, 0], Resources.Crystal: [1000, 0], Resources.Deuterium: [0, 0]},
        'prerequisites': {}
    },
    Ships.Recycler: {
        'cost': {Resources.Metal: [10000, 0], Resources.Crystal: [6000, 0], Resources.Deuterium: [2000, 0]},
        'prerequisites': {}
    },
    Ships.ColonyShip: {
        'cost': {Resources.Metal: [10000, 0], Resources.Crystal: [20000, 0], Resources.Deuterium: [10000, 0]},
        'prerequisites': {}
    },
    Ships.Battleship: {
        'cost': {Resources.Metal: [45000, 0], Resources.Crystal: [15000, 0], Resources.Deuterium: [0, 0]},
        'prerequisites': {}
    },
    Ships.Cruiser: {
        'cost': {Resources.Metal: [20000, 0], Resources.Crystal: [7000, 0], Resources.Deuterium: [2000, 0]},
        'prerequisites': {}
    },
    Ships.HeavyFighter: {
        'cost': {Resources.Metal: [6000, 0], Resources.Crystal: [4000, 0], Resources.Deuterium: [0, 0]},
        'prerequisites': {}
    },
    Ships.LightFighter: {
        'cost': {Resources.Metal: [3000, 0], Resources.Crystal: [1000, 0], Resources.Deuterium: [0, 0]},
        'prerequisites': {}
    },
    Ships.LargeCargo: {
        'cost': {Resources.Metal: [6000, 0], Resources.Crystal: [6000, 0], Resources.Deuterium: [0, 0]},
        'stock': [5000],
        'prerequisites': {}
    },
    Ships.SmallCargo: {
        'cost': {Resources.Metal: [2000, 0], Resources.Crystal: [2000, 0], Resources.Deuterium: [0, 0]},
        'stock': [25000],
        'prerequisites': {}
    },
    Ships.Destroyer: {
        'cost': {Resources.Metal: [60000, 0], Resources.Crystal: [50000, 0], Resources.Deuterium: [15000, 0]},
        'prerequisites': {}
    },
    Ships.Deathstar: {
        'cost': {Resources.Metal: [5000000, 0], Resources.Crystal: [4000000, 0], Resources.Deuterium: [1000000, 0]},
        'prerequisites': {}
    },
    Ships.Battlecruiser: {
        'cost': {Resources.Metal: [30000, 0], Resources.Crystal: [40000, 0], Resources.Deuterium: [15000, 0]},
        'prerequisites': {}
    }
}
