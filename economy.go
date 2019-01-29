package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"math/rand"
	"time"
)

func economyBot(bot *ogame.OGame) {
	logPrefix := "[ECONOMY] "
	priorityBuildings := []ogame.ID{
		ogame.MetalMineID, ogame.CrystalMineID, ogame.DeuteriumSynthesizerID,
		ogame.SolarPlantID, ogame.FusionReactorID, ogame.RoboticsFactoryID, ogame.ShipyardID,
		ogame.ResearchLabID,
	}
	for {
		researches := bot.GetResearch()

		performPriorityBuildings(bot, logPrefix, priorityBuildings, researches)

		time.Sleep(time.Duration(rand.Intn(15)) * time.Minute)
	}
}

func performPriorityBuildings(bot *ogame.OGame, logPrefix string, priorityBuildings []ogame.ID, researches ogame.Researches){
	for _, planet := range bot.GetPlanets() {
		log.Println(logPrefix, "Check buildings on ", planet.ID, " ...")

		resources, _ := planet.GetResources()
		resourcesBuildings, _ := planet.GetResourcesBuildings()
		facilitiesBuildings, _ := planet.GetFacilities()

		for _, buildingID := range priorityBuildings {
			currentLevel := 0
			building := ogame.Objs.ByID(buildingID)

			if ogame.IsResourceBuildingID(buildingID.Int()) {
				currentLevel = resourcesBuildings.ByID(buildingID)
			} else if ogame.IsFacilityID(buildingID.Int()) {
				currentLevel = facilitiesBuildings.ByID(buildingID)
			}

			log.Println(logPrefix, "try to build new level of ", building)

			price := building.GetPrice(currentLevel + 1)
			if resources.CanAfford(price) && building.IsAvailable(planet.GetType(), resourcesBuildings, facilitiesBuildings, researches, resources.Energy){
				log.Println(logPrefix, "Building new level of ", building)
				err := planet.Build(buildingID, 1)
				if err != nil {
					log.Fatal(logPrefix, err)
				}
			}
			time.Sleep(time.Duration(rand.Intn(30)) * time.Second)
		}
		time.Sleep(time.Duration(rand.Intn(60)) * time.Second)
	}
}

