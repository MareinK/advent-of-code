import collections
import itertools


def solve(n_dims, cubes_array):
    cubes = {
        (0,) * (n_dims - 2) + (y, x)
        for y, x in itertools.product(
            range(len(cubes_array)), range(len(cubes_array[0]))
        )
        if cubes_array[y][x] == "#"
    }

    neighbors_dxs = set(itertools.product((-1, 0, 1), repeat=n_dims)) ^ {(0,) * n_dims}

    for _ in range(6):
        new_cubes = cubes.copy()
        for xs in itertools.product(
            *(range(min(d) - 1, max(d) + 2) for d in zip(*cubes))
        ):
            neighbor_count = len(
                {tuple(map(sum, zip(xs, dxs))) for dxs in neighbors_dxs} & cubes
            )
            if xs in cubes and neighbor_count not in (2, 3):
                new_cubes.remove(xs)
            if xs not in cubes and neighbor_count == 3:
                new_cubes.add(xs)
        cubes = new_cubes

    return len(cubes)


cubes_array = open("17.txt").read().splitlines()
print(solve(3, cubes_array))
print(solve(4, cubes_array))


# k = 4
# for w in range(-k + 3, k - 2):
#     for z in range(-k + 3, k - 2):
#         print(f"{z=}, {w=}")
#         for y in range(-k + 3, k):
#             for x in range(-k + 3, k):
#                 print([".", "#"][cubes[(w, z, y, x)]], end="")
#             print()
#         print()
#         print()