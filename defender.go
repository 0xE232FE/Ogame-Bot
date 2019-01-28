package main

import (
	"fmt"
	"github.com/alaingilbert/ogame"
	"time"
)

func defender_bot(bot *ogame.OGame) {
	for {
		attacked := bot.IsUnderAttack()
		fmt.Println(attacked) // False
		time.Sleep(10 * time.Second)
	}
}
