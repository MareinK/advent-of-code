import math

import numpy as np
import scipy.signal

# input reading
tile_str_to_array = lambda tile_str: np.array(
    [[int(c == "#") for c in line] for line in tile_str.splitlines()]
)
unique_tiles = {
    int(tile_id_str[5:-1]): tile_str_to_array(tile_str)
    for tile_id_str, tile_str in (
        t.split("\n", 1) for t in open("20.txt").read().split("\n\n")
    )
}
dim = int(math.sqrt(len(unique_tiles)))
pattern_str = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
pattern = tile_str_to_array(pattern_str)

# tile variants (symmetries)
variants = lambda tile: (
    np.rot90(tile, 0),
    np.rot90(tile, 1),
    np.rot90(tile, 2),
    np.rot90(tile, 3),
    np.flipud(np.rot90(tile, 0)),
    np.flipud(np.rot90(tile, 1)),
    np.flipud(np.rot90(tile, 2)),
    np.flipud(np.rot90(tile, 3)),
)
tile_variants = {
    (tid, vid): variant
    for tid, tile in unique_tiles.items()
    for vid, variant in enumerate(variants(tile))
}

# search for solution
def search(state_tvids, used_tids):
    if len(state_tvids) >= len(unique_tiles):
        return state_tvids

    x, y = len(state_tvids) // dim, len(state_tvids) % dim
    valid_tvids = {
        (tid, vid)
        for tid, vid in tile_variants.keys()
        if tid not in used_tids
        and (
            x == 0
            or np.array_equal(
                tile_variants[(tid, vid)][0, :],
                tile_variants[state_tvids[(x - 1, y)]][-1, :],
            )
        )
        and (
            y == 0
            or np.array_equal(
                tile_variants[(tid, vid)][:, 0],
                tile_variants[state_tvids[(x, y - 1)]][:, -1],
            )
        )
    }

    for tid, vid in valid_tvids:
        # prepare
        state_tvids[(x, y)] = (tid, vid)
        used_tids.add(tid)

        # recurse
        if r := search(state_tvids, used_tids):
            return r

        # repair
        used_tids.remove(tid)
        del state_tvids[(x, y)]


solution = search({}, set())

# part 1
print(
    math.prod(
        tid
        for tid, vid in (
            solution[(0, 0)],
            solution[(0, dim - 1)],
            solution[(dim - 1, 0)],
            solution[(dim - 1, dim - 1)],
        )
    )
)

# part 2
print(
    min(
        image.sum()
        - pattern.sum()
        * len(
            np.where(scipy.signal.convolve2d(image, pattern, "valid") == pattern.sum())[
                0
            ]
        )
        for image in variants(
            np.block(
                [
                    [tile_variants[solution[(x, y)]][1:-1, 1:-1] for y in range(dim)]
                    for x in range(dim)
                ]
            )
        )
    )
)
