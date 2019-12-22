import collections
import json

import pandas as pd

data = json.load(open('scores.json'))
members = data['members']

days = range(1, 26)
parts = (1, 2)

df = pd.DataFrame.from_records(
    [
        {
            'name': member['name'],
            'score': 0,
            'stars': member['stars'],
            'local_score': member['local_score'],
            **{
                (int(n), int(part)): int(day[part]['get_star_ts'])
                for n, day in member['completion_day_level'].items()
                for part in map(str, parts)
                if "2" in day
            },
        }
        for member in members.values()
    ],
    columns=['name', 'score', 'local_score', 'stars']
    + [(day, part) for day in days for part in parts],
)

scores = collections.Counter({name: 0 for name in df['name']})
orig_place = {
    name: i
    for i, name in enumerate(df.sort_values('local_score', ascending=False)['name'], 1)
}

for day in days:
    df[day] = df[(day, 2)] - df[(day, 1)]
    s = df[(df[day].notnull())].sort_values(day)
    for i, name in enumerate(s['name']):
        scores[name] += len(df) - i
for i, (name, score) in enumerate(scores.most_common(), 1):
    if score > 0:
        d = orig_place[name] - i
        ds = f'+{d}' if d > 0 else str(d)
        print(f'{i: >2}) ({ds: >2}) {2 * score: >4} {name}')
