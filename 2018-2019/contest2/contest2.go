/*

| A Simon Narang creation
|
| Commissioned by:
| _____________________
|
| 	   ~ACSL~
| _____________________
|
| American Computer Science League
| 10 Brisas Drive
| West Warwick, RI 02893
| info@acsl.org

*/

package main

// These are NOT external libraries, they are part of Go but syntactically need to be "imported"
import (
	"fmt"
	"strings"
	"sort"
)

// The main script
func main() {

	for i := 0; i < 5; i++ {

		var former, latter string
		var output []string
		output = append(output, "", "", "", "")
		fmt.Scanf("%s %s\n", &former, &latter)
		former, latter = strings.ToLower(former), strings.ToLower(latter)
		var form, lat = former, latter

		for g := 0; g < 4; g++ {
			// Generate the output with common strings
			for _, formerChar := range former {
				for latterPos, latterChar := range latter {
					if latterChar == formerChar && !strings.Contains(output[g], string(formerChar)) {
						output[g] += string(formerChar)
						latter = trimLeftChars(latter, latterPos + 1)
					}
				}

			}

			// We're looking at the rule of fours here, thus we need to rearrange the strings every so often.
			if g == 0 {
				former, latter = lat, form
			} else if g == 1 {
				former, latter = reverse(lat), reverse(form)
			} else if g == 2 {
				former, latter = reverse(form), reverse(lat)
			}
		}

		fmt.Println(outputAlphabetized(output))
	}
}

func outputAlphabetized(output []string) string {
	final := intersect(strings.Split(output[0], ""), strings.Split(output[1], ""))
	final = intersect(final, strings.Split(output[2], ""))
	final = intersect(final, strings.Split(output[3], ""))

	final = removeDuplicatesUnordered(final)
	sort.Strings(final)

	outputAlpha := strings.Join(final, "")

	if outputAlpha == "" { outputAlpha = "NONE"}
	return outputAlpha
}

func trimLeftChars(s string, n int) string {
	m := 0
	for i := range s {
		if m >= n {
			return s[i:]
		}
		m++
	}
	return s[:0]
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func intersect(as, bs []string) []string {
	i := make([]string, 0, max(len(as), len(bs)))
	for _, a := range as {
		for _, b := range bs {
			if a == b {
				i = append(i, a)
			}
		}
	}
	return i
}

func removeDuplicatesUnordered(elements []string) []string {
	encountered := map[string]bool{}

	for v:= range elements {
		encountered[elements[v]] = true
	}

	result := []string{}
	for key, _ := range encountered {
		result = append(result, key)
	}
	return result
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
