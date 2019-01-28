package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"time"
)

func economyBot(bot *ogame.OGame) {
	logPrefix := "[ECONOMY]"
	for {
		//for _, planet := range bot.GetPlanets() {
		//	planet.Build(210, 1)
		//}
		log.Println(logPrefix, "Building...")
		time.Sleep(5 * time.Minute)
	}
}


