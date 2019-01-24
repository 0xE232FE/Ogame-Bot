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


class Defense(IntEnum):
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


Calculate = {
    Buildings.MetalMine: {
        'cost': {Resources.Metal: [60, 1.5], Resources.Crystal: [15, 1.5], Resources.Deuterium: [0, 0]},
        'production': [30, 1.1],
        'consummation': [10, 1.1],
        'prerequisite': {},
    },
    Buildings.CrystalMine: {
        'cost': {Resources.Metal: [48, 1.6], Resources.Crystal: [24, 1.6], Resources.Deuterium: [0, 0]},
        'production': [20, 1.1],
        'consummation': [10, 1.1],
        'prerequisite': {},
    },
    Buildings.DeuteriumSynthesizer: {
        'cost': {Resources.Metal: [225, 1.5], Resources.Crystal: [75, 1.5], Resources.Deuterium: [0, 0]},
        'production': [10, 1.1],
        'consummation': [20, 1.1],
        'prerequisite': {},
    },
    Buildings.MetalStorage: {
        'cost': {Resources.Metal: [500, 2], Resources.Crystal: [0, 0], Resources.Deuterium: [0, 0]},
        'capacite': [1.6],
        'consummation': [0, 0],
        'prerequisite': {},
    },
    Buildings.CrystalStorage: {
        'cost': {Resources.Metal: [500, 2], Resources.Crystal: [250, 2], Resources.Deuterium: [0, 0]},
        'capacite': [1.6],
        'consummation': [0, 0],
        'prerequisite': {},
    },
    Buildings.DeuteriumTank: {
        'cost': {Resources.Metal: [1000, 2], Resources.Crystal: [1000, 2], Resources.Deuterium: [0, 0]},
        'capacite': [1.6],
        'consummation': [0, 0],
        'prerequisite': {},
    },
    Buildings.SolarPlant: {
        'cost': {Resources.Metal: [75, 1.5], Resources.Crystal: [30, 1.5], Resources.Deuterium: [0, 0]},
        'production': [20, 1.1],
        'consummation': [0, 0],
        'prerequisite': {},
    },
    Facilities.RoboticsFactory: {
        'cost': {Resources.Metal: [400, 2], Resources.Crystal: [120, 2], Resources.Deuterium: [200, 2]},
        'prerequisite': {},
    },
    Facilities.Shipyard: {
        'cost': {Resources.Metal: [400, 2], Resources.Crystal: [200, 2], Resources.Deuterium: [100, 2]},
        'production': [0, 0],
        'consummation': [0, 0],
        'prerequisite': [[Facilities.RoboticsFactory, 2]],
    },
    Facilities.ResearchLab: {
        'cost': {Resources.Metal: [200, 2], Resources.Crystal: [400, 2], Resources.Deuterium: [200, 2]},
        'production': [0, 0],
        'consummation': [0, 0],
        'prerequisite': [],
    },
    Ships.SolarSatellite: {
        'cost': {Resources.Metal: [0, 0], Resources.Crystal: [0, 0], Resources.Deuterium: [0, 0]},
        'production': [],
        'consummation': [0, 0]
    },
}
