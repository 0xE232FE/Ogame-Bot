from ogame_bot.actions.action import Action
from ogame_bot.ogame.constants import Research


class Researcher(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)
        self.priority_list = [
            Research.WeaponsTechnology,
            Research.ShieldingTechnology,
            Research.ArmourTechnology,
            Research.EspionageTechnology,
            Research.ComputerTechnology,
            Research.EnergyTechnology,
            Research.LaserTechnology,
            Research.CombustionDrive,
            Research.IonTechnology,
            Research.ImpulseDrive,
            Research.Astrophysics,
            Research.HyperspaceTechnology,
            Research.HyperspaceDrive
        ]

    def perform_action(self, planet):
        pass
