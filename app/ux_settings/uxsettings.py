from colorama import Fore


class PrintLogo:
    def print_app_logo(self) -> None:
        logo_detailed = """
        +-----------+
        | A         |
        |           |
        |    +21    |
        |           |
        |         A |
        +-----------+
        """
        print(logo_detailed)


class ColorForInfo:
    #Логіка кольору для справжного рахунку
    def color_for_true_count(self, true_count: float) -> str:
        if true_count < 1:
            count_color = Fore.RED
        elif true_count < 2:
            count_color = Fore.WHITE
        elif true_count < 5:
            count_color = Fore.YELLOW
        elif true_count < 10:
            count_color = Fore.CYAN
        else:
            count_color = Fore.MAGENTA
        
        return f"{count_color}{true_count}{Fore.GREEN}"
