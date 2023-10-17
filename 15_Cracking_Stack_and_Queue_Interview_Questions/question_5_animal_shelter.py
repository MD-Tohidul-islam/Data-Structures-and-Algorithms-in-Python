# implement a cat and dog queue for an animal shelter.
class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []
    def enqueue(self, animal, type):
        if type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    def dequeuecat(self):
        if len(self.cats) ==0:
            return None
        else:
            cat = self.cats.pop(0)
        return cat
    def dequeuedog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
        return dog
    def dequeueany(self):
        if len(self.cats) ==0:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)
customqueue = AnimalShelter()
customqueue.enqueue('cat1', 'cat')
customqueue.enqueue('cat2', 'cat')
customqueue.enqueue('dog1', 'dog')
customqueue.enqueue('cat3', 'cat')
customqueue.enqueue('dog2', 'dog')
customqueue.enqueue('dog3', 'dog')
print(customqueue.dequeuecat())
print(customqueue.dequeueany())
