import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import Habit, track_habit

def main():
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2025, 1, 10, 8), cost=1, minutes_used=5),
        track_habit('Quit smoking', datetime(2025, 11, 8, 18), cost=10, minutes_used=30),
    ]

    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == '__main__':
    main()