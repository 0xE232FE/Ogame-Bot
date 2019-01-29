package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"math/rand"
	"time"
)

func researcherBot(bot *ogame.OGame) {
	logPrefix := "[RESEARCH] "
	priorityResearches := []ogame.ID{
		ogame.CombustionDriveID, ogame.HyperspaceDriveID, ogame.EnergyTechnologyID,
		ogame.WeaponsTechnologyID, ogame.ArmourTechnologyID, ogame.LaserTechnologyID, ogame.EspionageProbeID,
		ogame.ShieldingTechnologyID, ogame.ImpulseDriveID, ogame.ComputerTechnologyID, ogame.IonTechnologyID,
		ogame.AstrophysicsID,
	}
	for {
		researches := bot.GetResearch()

		performPriorityResearches(bot, logPrefix, priorityResearches, researches)

		time.Sleep(time.Duration(rand.Intn(15)) * time.Minute)
	}
}

func performPriorityResearches(bot *ogame.OGame, logPrefix string, priorityResearches []ogame.ID, researches ogame.Researches){
	for _, planet := range bot.GetPlanets() {
		log.Println(logPrefix, "Check researches on ", planet.ID, " ...")

		resources, _ := planet.GetResources()
		resourcesBuildings, _ := planet.GetResourcesBuildings()
		facilitiesBuildings, _ := planet.GetFacilities()

		for _, researchID := range priorityResearches {
			research := ogame.Objs.ByID(researchID)
			currentLevel := researches.ByID(researchID)

			log.Println(logPrefix, "try to research new level of ", research)

			price := research.GetPrice(currentLevel + 1)
			if resources.CanAfford(price) && research.IsAvailable(planet.GetType(), resourcesBuildings, facilitiesBuildings, researches, resources.Energy){
				log.Println(logPrefix, "Building new level of ", research)
				err := planet.Build(researchID, 1)
				if err != nil {
					log.Fatal(logPrefix, err)
				}else{
					resources = resources.Sub(price)
				}
			}
			time.Sleep(time.Duration(rand.Intn(30)) * time.Second)
		}
		time.Sleep(time.Duration(rand.Intn(60)) * time.Second)
	}
}
