 # Athlete Performance Tracking System
# Author: Anant Veer
# Description: Tracks and compares athletes' performance stats.

class Athlete:
    def __init__(self, name, sport, best_time):
        self.name = name
        self.sport = sport
        self.best_time = best_time  # in seconds

    def update_performance(self, new_time):
        if new_time < self.best_time:
            print(f"🎯 New record for {self.name}!")
            self.best_time = new_time
        else:
            print(f"No improvement for {self.name}. Keep training!")

    def display(self):
        print(f"Athlete: {self.name} | Sport: {self.sport} | Best Time: {self.best_time}s")

# Example usage
if __name__ == "__main__":
    a1 = Athlete("Michael Phelps", "Swimming", 21.4)
    a1.display()
    a1.update_performance(21.2)
    a1.display()
