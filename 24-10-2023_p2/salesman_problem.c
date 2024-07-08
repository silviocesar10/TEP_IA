#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_CITIES 10

typedef struct {
    double x;
    double y;
} City;

double distance(City city1, City city2) {
    return sqrt(pow(city1.x - city2.x, 2) + pow(city1.y - city2.y, 2));
}

double total_distance(int* tour, City* cities) {
    double dist = 0;
    for (int i = 0; i < NUM_CITIES - 1; i++) {
        dist += distance(cities[tour[i]], cities[tour[i + 1]]);
    }
    dist += distance(cities[tour[NUM_CITIES - 1]], cities[tour[0]]);
    return dist;
}

void copy_tour(int* source, int* dest) {
    for (int i = 0; i < NUM_CITIES; i++) {
        dest[i] = source[i];
    }
}

double acceptance_probability(double energy, double new_energy, double temperature) {
    if (new_energy < energy) {
        return 1.0;
    }
    return exp((energy - new_energy) / temperature);
}

void simulated_annealing(City* cities) {
    int current_tour[NUM_CITIES];
    int best_tour[NUM_CITIES];
    int temp_tour[NUM_CITIES];

    double current_energy, best_energy, temp_energy;
    double temperature = 1000.0;
    double cooling_rate = 0.995;

    // Initialize the current tour randomly
    for (int i = 0; i < NUM_CITIES; i++) {
        current_tour[i] = i;
    }
    random_shuffle(current_tour, NUM_CITIES);

    copy_tour(current_tour, best_tour);
    current_energy = total_distance(current_tour, cities);
    best_energy = current_energy;

    while (temperature > 1.0) {
        for (int i = 0; i < 100; i++) {
            int city1 = rand() % NUM_CITIES;
            int city2 = rand() % NUM_CITIES;

            copy_tour(current_tour, temp_tour);

            int temp = temp_tour[city1];
            temp_tour[city1] = temp_tour[city2];
            temp_tour[city2] = temp;

            temp_energy = total_distance(temp_tour, cities);

            if (acceptance_probability(current_energy, temp_energy, temperature) > ((double)rand() / RAND_MAX)) {
                copy_tour(temp_tour, current_tour);
                current_energy = temp_energy;

                if (current_energy < best_energy) {
                    copy_tour(current_tour, best_tour);
                    best_energy = current_energy;
                }
            }
        }
        temperature *= cooling_rate;
    }

    printf("Best Tour: ");
    for (int i = 0; i < NUM_CITIES; i++) {
        printf("%d ", best_tour[i]);
    }
    printf("\nBest Distance: %lf\n", best_energy);
}

void random_shuffle(int* array, int size) {
    for (int i = size - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

int main() {
    srand(time(NULL));

    City cities[NUM_CITIES];
    for (int i = 0; i < NUM_CITIES; i++) {
        cities[i].x = (double)rand() / RAND_MAX;
        cities[i].y = (double)rand() / RAND_MAX;
    }

    simulated_annealing(cities);

    return 0;
}
