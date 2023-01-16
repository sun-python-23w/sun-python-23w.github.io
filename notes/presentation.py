ESC = "\u001b"
RESET = f"{ESC}[0m"


class Color:
    BLACK = f"{ESC}[30m"
    RED = f"{ESC}[31m"
    GREEN = f"{ESC}[32m"
    YELLOW = f"{ESC}[33m"
    BLUE = f"{ESC}[34m"
    BLACK_BOLD = f"{ESC}[30;1m"
    WHITE_BOLD = f"{ESC}[37;1m"
    GREEN_BOLD = f"{ESC}[32;1m"
    YELLOW_BOLD = f"{ESC}[33;1m"


import os
from collections import namedtuple


def strip_margin(s: str) -> str:
    def _strip(l: str) -> str:
        if "|" not in l:
            return l
        else:
            bar_index = l.find("|")
            if l[:bar_index].isspace() or bar_index == 0:
                return l[bar_index + 1 :]
            else:
                return l

    stripped_s = s.strip()
    return "\n".join([_strip(line) for line in stripped_s.splitlines() if line != ""])


Slide = namedtuple("Slide", ("title", "content"))


def clear_screen() -> None:
    os.system("clear")


def show_slide(s: Slide, indent: int = 2) -> None:
    clear_screen()
    print()
    print()

    indent_str = " " * indent

    print(f"{indent_str}{Color.YELLOW_BOLD}{s.title}")
    separator = "-" * len(s.title)
    print(f"{indent_str}{Color.YELLOW_BOLD}{separator}")
    print(RESET)

    normalized_content = s.content  # .strip()

    for line in normalized_content.splitlines():
        print(f"{indent_str}{line}")

    padding = max(6 - len(normalized_content.splitlines()), 0)
    print("\n" * (padding), RESET)


def show_slides(slides: list[Slide], indent: int = 2) -> None:
    index = 0
    should_exit = False
    warn_first = False
    while index < len(slides) and not should_exit:
        slide = slides[index]
        show_slide(slide, indent)

        # Shows before the prompt
        additional_message = ""
        if warn_first:
            additional_message = f"{Color.RED}(first slide) "
        if index == (len(slides) - 1):
            additional_message = f"{Color.BLACK}(last slide) "

        # User input
        response = input(f"{' ' * indent}{additional_message}{Color.BLACK}> {RESET}")
        warn_first = False
        # CALLOUT: Should go over fallacy of `response == "a" or "b"`
        if response == "b":
            if index > 0:
                index -= 1
            else:
                warn_first = True
        elif response == "q":
            should_exit = True
        else:
            index += 1


question_slide = Slide(
    "Questions",
    strip_margin(
        """
                    |   ____   ____   ____
                    |  / _  \\ / _  \\ / _  \\
                    |  \_ ) / \_ ) / \_ ) /
                    |    /_/    /_/    /_/
                    |    _      _      _
                    |   (_)    (_)    (_)
                    """
    ),
)


def main() -> None:
    show_slides(
        [
            Slide(
                "About me",
                strip_margin(
                    f"""
                    |Hometown: Eugene, OR
                    |Hobbies:
                    | - Trail hiking/running
                    | - Gaming ({Color.BLUE}Swi{Color.RED}tch{RESET} mostly)
                    | - Cooking
                    """
                ),
            ),
            Slide(
                "My background",
                strip_margin(
                    """
                    |- Graduated from Oregon State
                    |- I've worked on:
                    |  - User interfaces (iOS, androind, web)
                    |  - Data processing and ML (python)
                    |  - Streaming events (python, scala)
                    """
                ),
            ),
            Slide(
                "Course goals",
                strip_margin(
                    """
                    |1. Have fun
                    |2. Understand the basic
                    |    principles of programming
                    |3. Learn to read/write Python programs
                    """
                ),
            ),
            question_slide,
            Slide(
                "Python background",
                strip_margin(
                    """
                    |- Free and open-source
                    |- Easy to read (and pretty)
                    |- Expressive power
                    |- Borrows lots of ideas
                    """
                ),
            ),
            question_slide,
            Slide(
                "CLI Example: Wordle",
                strip_margin(
                    f"""
                    |[1/6]> lemon
                    |{Color.YELLOW_BOLD}[L]{Color.GREEN_BOLD}[E]{Color.BLACK_BOLD}[M][O][N]{RESET}
                    |
                    |[2/6]> jewel
                    |{Color.BLACK_BOLD}[J]{Color.GREEN_BOLD}[E]{Color.BLACK_BOLD}[W]{Color.YELLOW_BOLD}[E][L]{RESET}
                    |
                    |[3/6]>
                    """
                ),
            ),
        ]
    )


main()
