package main

import (
	"fmt"
	"github.com/alaingilbert/ogame"
	"time"
)

func attacker_bot(bot *ogame.OGame) {
	for {
		fmt.Printf("attack... ")
		time.Sleep(5 * time.Minute)
	}
}
