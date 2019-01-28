package main

import (
	"fmt"
	"github.com/alaingilbert/ogame"
	"time"
)

func economy_bot(bot *ogame.OGame) {
	for {
		//for _, planet := range bot.GetPlanets() {
		//	planet.Build(210, 1)
		//}
		fmt.Printf("build... ")
		time.Sleep(5 * time.Minute)
	}
}


