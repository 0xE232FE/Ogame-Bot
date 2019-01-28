package main

import (
	"github.com/alaingilbert/ogame"
	"os"
)

func main() {
	universe := os.Getenv("UNIVERSE")
	username := os.Getenv("USERNAME")
	password := os.Getenv("PASSWORD")
	language := os.Getenv("LANGUAGE")
	bot, err := ogame.New(universe, username, password, language)
	if err != nil {
		panic(err)
	}

	go economyBot(bot)
	go attackerBot(bot)
	go defenderBot(bot)
	go researcherBot(bot)

	select{ }
}
