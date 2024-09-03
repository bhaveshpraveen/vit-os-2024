package main

import (
    "fmt"
    "runtime"
    "sync"
)

func worker(id int, wg *sync.WaitGroup) {
    defer wg.Done()
    fmt.Printf("Goroutine-%d started.\n", id)
    
    // Perform a CPU-intensive task
    total := 0
    for i := 0; i < 10_000_000_000; i++ {
        total += i
    }
    
    fmt.Printf("Goroutine-%d finished. Total: %d\n", id, total)
}

func main() {
    numCores := runtime.NumCPU()
    fmt.Printf("Available Cores: %d\n", numCores)
    
    runtime.GOMAXPROCS(numCores) // Set the maximum number of CPUs that can be executing simultaneously

    var wg sync.WaitGroup
    for i := 0; i < numCores; i++ {
        wg.Add(1)
        go worker(i, &wg)
    }

    wg.Wait() // Wait for all goroutines to complete
}

