Resource = {
    'Metal',
    'Crystal',
    'Deuterium'
}

Buildings = {'MetalMine': 1,
             'CrystalMine': 2,
             'DeuteriumSynthesizer': 3,
             'SolarPlant': 4,
             'FusionReactor': 12,
             'MetalStorage': 22,
             'CrystalStorage': 23,
             'DeuteriumTank': 24,
             'ShieldedMetalDen': 25,
             'UndergroundCrystalDen': 26,
             'SeabedDeuteriumDen': 27,

             # NL
             'Metaalmijn': 1,
             'Kristalmijn': 2,
             'Deuteriumfabriek': 3,
             'Zonne-energiecentrale': 4,
             'Fusiecentrale': 12,
             'Metaalopslag': 22,
             'Kristalopslag': 23,
             'Deuteriumtank': 24}

Facilities = {'AllianceDepot': 34,
              'RoboticsFactory': 14,
              'Shipyard': 21,
              'ResearchLab': 31,
              'MissileSilo': 44,
              'NaniteFactory': 15,
              'Terraformer': 33,
              'SpaceDock': 36,

              # NL
              'Alliantiehanger': 34,
              'Robotfabriek': 14,
              'Werf': 21,
              'Onderzoekslab': 31,
              'Raketsilo': 44,
              'Nanorobotfabriek': 15,
              'Terravormer': 33,
              'Ruimtewerf': 36}

Defense = {'RocketLauncher': 401,
           'LightLaser': 402,
           'HeavyLaser': 403,
           'GaussCannon': 404,
           'IonCannon': 405,
           'PlasmaTurret': 406,
           'SmallShieldDome': 407,
           'LargeShieldDome': 408,
           'AntiBallisticMissiles': 502,
           'InterplanetaryMissiles': 503,

           # NL
           'Raketlanceerder': 401,
           'Kleinelaser': 402,
           'Grotelaser': 403,
           'Gausskannon': 404,
           'Ionkannon': 405,
           'Plasmakannon': 406,
           'Kleineplanetaireschildkoepel': 407,
           'GroteplanetaireschildkoepelLargeShieldDome': 408,
           'Antiballistischeraketten': 502,
           'Interplanetaireraketten': 503}

Ships = {'SmallCargo': 202,
         'LargeCargo': 203,
         'LightFighter': 204,
         'HeavyFighter': 205,
         'Cruiser': 206,
         'Battleship': 207,
         'ColonyShip': 208,
         'Recycler': 209,
         'EspionageProbe': 210,
         'Bomber': 211,
         'SolarSatellite': 212,
         'Destroyer': 213,
         'Deathstar': 214,
         'Battlecruiser': 215,

         # FR
         'Petittransporteur': 202,
         'Grandtransporteur': 203,
         'Chasseurléger': 204,
         'Chasseurlourd': 205,
         'Croiseur': 206,
         'Vaisseaudebataille': 207,
         'Vaisseaudecolonisation': 208,
         'Recycleur': 209,
         'Sonded`espionnage': 210,
         'Bombardier': 211,
         'Satellitesolaire': 212,
         'Destructeur': 213,
         'Étoiledelamort': 214,
         'Traqueur': 215,

         # NL
         'Kleinvrachtschip': 202,
         'Grootvrachtschip': 203,
         'Lichtgevechtsschip': 204,
         'Zwaargevechtsschip': 205,
         'Kruiser': 206,
         'Slagschip': 207,
         'Kolonisatiesschip': 208,
         'Recycler': 209,
         'Spionagesonde': 210,
         'Bommenwerper': 211,
         'Zonne-energiesatelliet': 212,
         'Vernietiger': 213,
         'Sterdesdoods': 214,
         'Interceptor': 215}

Research = {'EspionageTechnology': 106,
            'ComputerTechnology': 108,
            'WeaponsTechnology': 109,
            'ShieldingTechnology': 110,
            'ArmourTechnology': 111,
            'EnergyTechnology': 113,
            'HyperspaceTechnology': 114,
            'CombustionDrive': 115,
            'ImpulseDrive': 117,
            'HyperspaceDrive': 118,
            'LaserTechnology': 120,
            'IonTechnology': 121,
            'PlasmaTechnology': 122,
            'IntergalacticResearchNetwork': 123,
            'Astrophysics': 124,
            'GravitonTechnology': 199,

            # NL
            'Spionagetechniek': 106,
            'Computertechniek': 108,
            'Wapentechniek': 109,
            'Schildtechniek': 110,
            'Pantsertechniek': 111,
            'Energietechniek': 113,
            'Hyperruimtetechniek': 114,
            'Verbrandingsmotor': 115,
            'Impulsmotor': 117,
            'Hyperruimtemotor': 118,
            'Lasertechniek': 120,
            'Iontechniek': 121,
            'Plasmatechniek': 122,
            'IntergalactischOnderzoeksnetwerk': 123,
            'Astrofysica': 124,
            'Gravitontechniek': 199}

Speed = {'10%': 1,
         '20%': 2,
         '30%': 3,
         '40%': 4,
         '50%': 5,
         '60%': 6,
         '70%': 7,
         '80%': 8,
         '90%': 9,
         '100%': 10}

Missions = {'Attack': 1,
            'GroupedAttack': 2,
            'Transport': 3,
            'Park': 4,
            'ParkInThatAlly': 5,
            'Spy': 6,
            'Colonize': 7,
            'RecycleDebrisField': 8,
            'Destroy': 9,
            'Expedition': 15}

Calculate = {
    'Buildings': {
        'MetalMine': {
            'cost': {'Metal': [60, 1.5], 'Crystal': [15, 1.5], 'Deuterium': [0, 0]},
            'production': [30, 1.1],
            'consummation': [10, 1.1],
            'prerequisiteite': {},
        },
        'CrystalMine': {
            'cost': {'Metal': [48, 1.6], 'Crystal': [24, 1.6], 'Deuterium': [0, 0]},
            'production': [20, 1.1],
            'consummation': [10, 1.1],
            'prerequisite': {},
        },
        'DeuteriumSynthesizer': {
            'cost': {'Metal': [225, 1.5], 'Crystal': [75, 1.5], 'Deuterium': [0, 0]},
            'production': [10, 1.1],
            'consummation': [20, 1.1],
            'prerequisite': {},
        },
        'MetalStorage': {
            'cost': {'Metal': [500, 2], 'Crystal': [0, 0], 'Deuterium': [0, 0]},
            'capacite': [1.6],
            'consummation': [0, 0],
            'prerequisite': {},
        },
        'CrystalStorage': {
            'cost': {'Metal': [500, 2], 'Crystal': [250, 2], 'Deuterium': [0, 0]},
            'capacite': [1.6],
            'consummation': [0, 0],
            'prerequisite': {},
        },
        'DeuteriumTank': {
            'cost': {'Metal': [1000, 2], 'Crystal': [1000, 2], 'Deuterium': [0, 0]},
            'capacite': [1.6],
            'consummation': [0, 0],
            'prerequisite': {},
        },
        'SolarPlant': {
            'cost': {'Metal': [75, 1.5], 'Crystal': [30, 1.5], 'Deuterium': [0, 0]},
            'production': [20, 1.1],
            'consummation': [0, 0],
            'prerequisite': {},
        },
        'RoboticsFactory': {
            'cost': {'Metal': [400, 2], 'Crystal': [120, 2], 'Deuterium': [200, 2]},
            'production': [0, 0],
            'consummation': [0, 0],
            'prerequisite': {},
        },
        'Shipyard': {
            'cost': {'Metal': [400, 2], 'Crystal': [200, 2], 'Deuterium': [100, 2]},
            'production': [0, 0],
            'consummation': [0, 0],
            'prerequisite': [['RoboticsFactory', 2]],
        },
        'ResearchLab': {
            'cost': {'Metal': [200, 2], 'Crystal': [400, 2], 'Deuterium': [200, 2]},
            'production': [0, 0],
            'consummation': [0, 0],
            'prerequisite': [],
        },
    },
    'Energy': {
        'SolarPlant': {
            'cost': {'Metal': [75, 1.5], 'Crystal': [30, 1.5], 'Deuterium': [0, 0]},
            'production': [20, 1.1],
            'consummation': [0, 0]
        },
        'SolarSatellite': {
            'cost': {'Metal': [0, 0], 'Crystal': [0, 0], 'Deuterium': [0, 0]},
            'production': [],
            'consummation': [0, 0]
        },
        'FusionReactor': {
            'cost': {'Metal': [0, 0], 'Crystal': [0, 0], 'Deuterium': [0, 0]},
            'production': [],
            'consummation': [10, 1.1]
        },
        'RoboticsFactory': {
            'cost': {'Metal': [400, 2], 'Crystal': [120, 2], 'Deuterium': [200, 2]},
            'prerequisite': {},
        },
    },
    'Facilities': {
        'RoboticsFactory': {
            'cost': {'Metal': [400, 2], 'Crystal': [120, 2], 'Deuterium': [200, 2]},
            'prerequisite': {},
        }
    }
}