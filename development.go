package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"math/rand"
	"time"
)

type economy struct {
	logPrefix string
	priorityBuildings []ogame.ID
}

type research struct {
	logPrefix string
	priorityResearches []ogame.ID
}

func initializeDevelopmentBots() (economy, research){
	return economy{
			"[ECONOMY] ",
			[]ogame.ID{
				ogame.MetalMineID, ogame.CrystalMineID, ogame.DeuteriumSynthesizerID,
				ogame.SolarPlantID, ogame.FusionReactorID, ogame.RoboticsFactoryID, ogame.ShipyardID,
				ogame.ResearchLabID, ogame.SpaceDockID,
				},
			},
		research{
			"[RESEARCHER] ",
			[]ogame.ID{
				ogame.CombustionDriveID, ogame.HyperspaceDriveID, ogame.EnergyTechnologyID,
				ogame.WeaponsTechnologyID, ogame.ArmourTechnologyID, ogame.LaserTechnologyID, ogame.EspionageProbeID,
				ogame.ShieldingTechnologyID, ogame.ImpulseDriveID, ogame.ComputerTechnologyID, ogame.IonTechnologyID,
				ogame.AstrophysicsID,
			},
		}
}

func developmentBot(bot *ogame.OGame) {
	builderBot, researcherBot := initializeDevelopmentBots()

	for {
		userData := getUserData(bot)

		for _, planet := range bot.GetPlanets() {
			planetData := getPlanetData(bot, planet)

			log.Println(researcherBot.logPrefix, "Check researches on ", planet.ID, " ...")
			performPriorityResearches(researcherBot, userData, planetData)

			time.Sleep(time.Duration(rand.Intn(60)) * time.Second)

			log.Println(builderBot.logPrefix, "Check buildings on ", planet.ID, " ...")
			performPriorityBuildings(builderBot, userData, planetData)
		}
		time.Sleep(time.Duration(rand.Intn(15)) * time.Minute)
	}
}

func performPriorityBuildings(builderBot economy, userData userInfo, planetData planetInfo){
	for _, buildingID := range builderBot.priorityBuildings {
		currentLevel := 0
		building := ogame.Objs.ByID(buildingID)

		if ogame.IsResourceBuildingID(buildingID.Int()) {
			currentLevel = planetData.planetResourcesBuildings.ByID(buildingID)
		} else if ogame.IsFacilityID(buildingID.Int()) {
			currentLevel = planetData.planetFacilitiesBuildings.ByID(buildingID)
		}

		developmentBuild(userData, planetData, builderBot.logPrefix, building, currentLevel + 1)
		time.Sleep(time.Duration(rand.Intn(30)) * time.Second)
	}
}

func performPriorityResearches(researcherBot research, userData userInfo, planetData planetInfo){
	for _, researchID := range researcherBot.priorityResearches {
		research := ogame.Objs.ByID(researchID)
		currentLevel := userData.userResearches.ByID(researchID)

		developmentBuild(userData, planetData, researcherBot.logPrefix, research, currentLevel + 1)
		time.Sleep(time.Duration(rand.Intn(30)) * time.Second)
	}
}

func developmentBuild(userData userInfo, planetData planetInfo, logPrefix string, building ogame.BaseOgameObj, levelToBuild int){
	price := building.GetPrice(levelToBuild)
	if canAffordWrapper(userData, planetData, price, building) {
		log.Println(logPrefix, "try to build new level of ", building)

		err := planetData.planet.Build(building.GetID(), 1)
		if err != nil {
			log.Fatal(logPrefix, err)
		}else{
			planetData.planetResources = planetData.planetResources.Sub(price)
			log.Println(logPrefix, "Building new level of ", building)
		}
	}
}
