package main

import (
	"strconv"
	"fmt"
	"os"
	"bufio"
)

var path = "input.txt"

func main() {
	fmt.Println("Part 1:",partOne(path),"\nPart 2:", partTwo(path))
}

//add numbers of file
func partOne(path string) (freq int) {
	file,_ := os.Open(path)
	scan := bufio.NewScanner(file)
	for scan.Scan() {
		freq += stringToSignedInt(scan.Text())
	}
	return
}
func partTwo(path string) (int) {
	freq := 0
	//indices are frequencies we've seen
	freqMap := make(map[int]bool) 
	for {
		file,_ := os.Open("input.txt")
		scan := bufio.NewScanner(file)
		for scan.Scan() {
			freq += stringToSignedInt(scan.Text())
			//if it's been seen, this is the second occurence
			if freqMap[freq]{ 
				return freq
			}
			freqMap[freq] = true
		}
	}
}

//Converts Strings of the form +Num or -Num into their integer equivalent
func stringToSignedInt(lineString string) (n int){
	sign := lineString[0:1]
	n,_ = strconv.Atoi(lineString[1:])
	if sign == "-" {
		n *= -1
	}
	return
}