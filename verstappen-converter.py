#!/usr/bin/env python3

from argparse import ArgumentParser
from random import choice


VERSTAPPEN_NUMBER = 69
PLACEHOLDER = "%formatted_number%"
QUOTES = [
    f"Mate, I don't care about the calculations, the delta is exactly {PLACEHOLDER}, simply lovely... now I'm going back to my sim rig.",
    f"Mate, the car feels completely undriveable, jumping around like a kangaroo, but somehow we are {PLACEHOLDER} tenths ahead, haha, yes boys!",
    f"GP, my tires are completely gone, but the gap to P2 is still {PLACEHOLDER} seconds, simply lovely.",
    f"I've been doing 24-hour endurance races on iRacing all night, so calculating {PLACEHOLDER} is the hardest thing I've done all weekend.",
    f"Christian, you can tell the stewards to give me a ten-second penalty, I'll still finish {PLACEHOLDER} seconds in front of everyone else.",
    f"So basically we just survived turn one, and after that the pace was a solid {PLACEHOLDER} out of 10, just an unbelievable race."
]



def convert_number(number) -> tuple[int, int]:
    multiplication = number // VERSTAPPEN_NUMBER
    addition = number % VERSTAPPEN_NUMBER
    return multiplication, addition


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Convert a number to Max Verstappen's number format."
    )
    parser.add_argument("number", type=int, help="The number to convert.")
    parser.add_argument(
        "-r",
        "--result-only",
        action="store_true",
        default=False,
        help="Only display the converted number.",
    )
    args = parser.parse_args()
    args.result_only = args.result_only or False

    multiplication, addition = convert_number(args.number)
    str_output = f"{multiplication} * {VERSTAPPEN_NUMBER} + {addition}"

    if args.result_only:
        print(str_output)
    else:
        quote = choice(QUOTES)
        quote = quote.replace(PLACEHOLDER, str_output)
        print(quote)