import random

class Space():
    def __init__(self, height, width, num_hospitals):
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set()
        self.hospitals = set()

    def add_house(self, row, col):
        self.houses.add((row, col))

    def available_sapces(self):
        candidates = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
        )
        for house in self.houses:
            candidates.remove(house)
        for hospital in self.hospitals:
            candidates.remove(hospital)
        return candidates 
        
    def get_cost(self, hospitals):
        cost = 0
        for house in self.houses:
            cost += min(abs(house[0]-hospital[0]) + 
                        abs(house[0]-hospital[0])
                        for hospital in hospitals)
        return cost
    
    def get_neighbors(self, row, col):
        candidates = [
            (row-1, col),
            (row+1, col),
            (row, col-1),
            (row, col+1)
        ]
        neighbors = []
        for r,c in candidates:
            if(r,c) in self.houses or (r,c) in self.hospitals:
                continue
            if (0<=r<=self.height) or (0<=c<=self.height):
                neighbors.append((r,c))
        return neighbors
    
    def output_image(self, filename):
        """Generates image with all houses and hospitals."""
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "white"
        )
        house = Image.open("assets/images/House.png").resize(
            (cell_size, cell_size)
        )
        hospital = Image.open("assets/images/Hospital.png").resize(
            (cell_size, cell_size)
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):

                # Draw cell
                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="black")

                if (i, j) in self.houses:
                    img.paste(house, rect[0], house)
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0], hospital)

        # Add cost
        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "black"
        )
        draw.text(
            (padding, self.height * cell_size + padding),
            f"Cost: {self.get_cost(self.hospitals)}",
            fill="white",
            font=font
        )

        img.save(filename)
    
    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        count = 0
        self.hospitals = set()
        for i in range(self.num_hospitals):
            self.hospitals.add(random.choice(list(self.available_sapces())))
        if log:
            print("Initial state cost: ", self.get_cost(self.hospitals))
        if image_prefix:
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")
        while maximum is None or count < maximum:
            count += 1
            best_solutions = []
            best_solution_cost = None
            for hospital in self.hospitals:
                for neighbor in self.get_neighbors(*hospital):
                    candidate_solution = self.hospitals.copy()
                    candidate_solution.remove(hospital)
                    candidate_solution.add(neighbor)
                    cost = self.get_cost(candidate_solution)
                    if(best_solution_cost is None or cost < best_solution_cost):
                        best_solutions = [candidate_solution]
                    elif best_solution_cost == cost:
                        best_solutions.append(candidate_solution)