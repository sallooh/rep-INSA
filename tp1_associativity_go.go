// tp1_associativity_go.go
package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

func testAssociativity(n int) (int, int, float64) {
	success := 0
	for i := 0; i < n; i++ {
		x := rand.Float64()*2e16 - 1e16
		y := rand.Float64()*2e16 - 1e16
		z := rand.Float64()*2e16 - 1e16

		if (x+y)+z == x+(y+z) {
			success++
		}
	}
	percentage := float64(success) / float64(n) * 100
	return n, success, percentage
}

func main() {
	rand.Seed(time.Now().UnixNano())
	n, success, percentage := testAssociativity(10000)

	fmt.Printf("Sur %d tests :\n", n)
	fmt.Printf(" - Succès exacts : %d\n", success)
	fmt.Printf(" - Pourcentage de réussite : %.6f%%\n", percentage)

	// Sauvegarde du résultat
	file, err := os.Create("answer_associativity_llm.txt")
	if err != nil {
		fmt.Println("Erreur d’écriture :", err)
		return
	}
	defer file.Close()

	fmt.Fprintf(file, "Sur %d tests :\n", n)
	fmt.Fprintf(file, " - Succès exacts : %d\n", success)
	fmt.Fprintf(file, " - Pourcentage de réussite : %.6f%%\n", percentage)
	fmt.Println("\nRésultat enregistré dans 'answer_associativity_llm.txt'")
}
