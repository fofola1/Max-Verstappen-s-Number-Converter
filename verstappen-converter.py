#!/usr/bin/env python3

from argparse import ArgumentParser
from random import choice

VERSTAPPEN_NUMBER = 69
QUOTES = [
    "Mate, I don't care about the calculations, the delta is exactly {}, simply lovely... now I'm going back to my sim rig.",
    "Mate, the car feels completely undriveable, jumping around like a kangaroo, but somehow we are {} tenths ahead, haha, yes boys!",
    "GP, my tires are completely gone, but the gap to P2 is still {} seconds, simply lovely.",
    "I've been doing 24-hour endurance races on iRacing all night, so calculating {} is the hardest thing I've done all weekend.",
    "Christian, you can tell the stewards to give me a ten-second penalty, I'll still finish {} seconds in front of everyone else.",
    "So basically we just survived turn one, and after that the pace was a solid {} out of 10, just an unbelievable race."
]


def convert_number(number: int) -> tuple[int, int]:
    multiplication = number // VERSTAPPEN_NUMBER
    addition = number % VERSTAPPEN_NUMBER
    return multiplication, addition


def format_string(multiplication: int, addition: int) -> str:
    str_output = ""
    match multiplication:
        case 1:
            str_output = f"{VERSTAPPEN_NUMBER}"
        case -1:
            str_output = f"-{VERSTAPPEN_NUMBER}"
        case _:
            str_output = f"{multiplication} * {VERSTAPPEN_NUMBER}"

    if addition > 0:
        str_output += f" + {addition}"
    elif addition < 0:
        str_output += f" - {abs(addition)}"
    return str_output


def main() -> None:
    parser = ArgumentParser(
        description="Convert a number to Max Verstappen's number format."
    )
    parser.add_argument("number", type=int, help="The number to convert.")
    parser.add_argument(
        "-r",
        "--result-only",
        action="store_true",
        help="Only display the converted number.",
    )
    args = parser.parse_args()

    multiplication, addition = convert_number(args.number)
    str_output = format_string(multiplication, addition)

    if args.result_only:
        print(str_output)
    else:
        quote = choice(QUOTES).format(str_output)
        print(quote)


if __name__ == "__main__":
    main()