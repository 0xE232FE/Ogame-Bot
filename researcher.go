package main

import (
	"fmt"
	"github.com/alaingilbert/ogame"
	"time"
)

func researcher_bot(bot *ogame.OGame) {
	for {
		fmt.Printf("research... ")
		time.Sleep(5 * time.Minute)
	}
}
