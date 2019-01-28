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

	go economy_bot(bot)
	go attacker_bot(bot)
	go defender_bot(bot)
	go researcher_bot(bot)

	select{ }
}
