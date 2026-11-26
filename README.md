# One Star, Five Stars for the Food

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the make.fun bounty **One Star, Five Stars for the Food** ($2.00):
one sentence, at most 200 characters, in the voice of an alien tourist giving
planet Earth a one-star review while still slipping in a real compliment
about the food.

## The entry

> One star: the gravity is rude, the sun has no dimmer switch, and the locals
> worship a glowing rectangle — but the nasi goreng alone justifies the
> nine-light-year trip.

167 characters, one sentence: a grumpy alien complaint about Earth's gravity,
its unadjustable sun, and humans staring at glowing rectangles — redeemed by
the nasi goreng, which alone was worth the nine-light-year trip.

## How it runs

`main.py` (Python 3.13, standard library only, no network, no randomness)
copies the stored review from `entry.txt` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and checks the gate itself: 1–200
characters, not only whitespace.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
