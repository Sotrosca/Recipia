

class Recipe:
    def __init__(self, name, description, ingredients, steps, tags):
        self.name = name
        self.ingredients = ingredients
        self.description = description
        self.steps = steps
        self.tags = tags


    def __dict__(self):
        return {
            'name': self.name,
            'description': self.description,
            'ingredients': self.ingredients,
            'steps': self.steps,
            'tags': self.tags
        }
