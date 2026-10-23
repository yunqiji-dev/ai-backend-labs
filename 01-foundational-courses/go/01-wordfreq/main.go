package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Fprintln(os.Stderr, "usage: wordfreq input.txt output.txt")
		os.Exit(1)
	}

	f, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, "wordfreq:", err)
		os.Exit(1)
	}
	defer f.Close()
	fmt.Println("opened", f.Name())
}
