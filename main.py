import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Rozmiary ekranu
screen_width = 1100
screen_height = 900

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PINK = (255, 182, 193)

# Utworzenie ekranu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scrabble")  # nazwa okna

# Czcionki w głównym menu
title_font = pygame.font.Font(None, 80)
menu_font = pygame.font.Font(None, 40)


class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.hovered = False

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect)

    def is_hovered(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)


class MainMenu:
    def __init__(self):
        self.button_width = 200
        self.button_height = 50
        self.button_x = screen_width // 2 - self.button_width // 2
        self.button_y = screen_height // 2 - self.button_height // 2 - 20

        # Przyciski w menu
        self.play_button = Button(self.button_x, self.button_y, self.button_width, self.button_height)
        self.instruction_button = Button(self.button_x, self.button_y + 70, self.button_width, self.button_height)
        self.exit_button = Button(self.button_x, self.button_y + 140, self.button_width, self.button_height)

    @staticmethod
    def draw_text(text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw(self):
        while True:
            screen.fill(BLUE)

            self.play_button.draw(YELLOW if self.play_button.hovered else GREEN)
            self.instruction_button.draw(YELLOW if self.instruction_button.hovered else GREEN)
            self.exit_button.draw(YELLOW if self.exit_button.hovered else GREEN)

            self.draw_text("Scrabble", title_font, WHITE, screen_width // 2, screen_height // 4)
            self.draw_text("GRAJ", menu_font, BLACK, screen_width // 2, screen_height // 2 - 15)
            self.draw_text("INSTRUKCJA", menu_font, BLACK, screen_width // 2, screen_height // 2 + 50)
            self.draw_text("WYJDŹ", menu_font, BLACK, screen_width // 2, screen_height // 2 + 115)

            # Sprawdzenie pozycji kursora
            mouse_pos = pygame.mouse.get_pos()

            self.play_button.is_hovered(mouse_pos)
            self.instruction_button.is_hovered(mouse_pos)
            self.exit_button.is_hovered(mouse_pos)

            pygame.display.update()

            # Obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # czy jest typu pygame.QUIT
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.hovered:
                        # Kliknięto przycisk GRAJ
                        play_game(dictionary)  # Wywołanie funkcji `play_game()`
                    elif self.instruction_button.hovered:
                        # Kliknięto przycisk INSTRUKCJA
                        instruction_screen = InstructionScreen()  # instancja klasy
                        instruction_screen.draw()  # Wywołanie metody
                    elif self.exit_button.hovered:
                        # Kliknięto przycisk WYJDŹ
                        pygame.quit()
                        sys.exit()


class InstructionScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill(BLUE)
        back_button_width = 200
        back_button_height = 50

        self.back_button = Button(
            self.screen.get_width() // 2 - back_button_width // 2,
            self.screen.get_height() - 100,
            back_button_width,
            back_button_height
        )

    def draw(self):
        back_button_hovered = False

        while True:
            pygame.draw.rect(
                self.screen,
                YELLOW if back_button_hovered else GREEN,
                self.back_button.rect
            )
            MainMenu.draw_text(
                "WSTECZ",
                menu_font,
                BLACK,
                self.back_button.rect.x + self.back_button.rect.width // 2,
                self.back_button.rect.y + self.back_button.rect.height // 2
            )

            instruction_text = [
                "Instrukcja do gry Scrabble:",
                "1. Ułożenie słowa na planszy:",
                "- Kliknij i przeciągnij litery, aby utworzyć słowo.",
                "- Upewnij się, że słowo jest poprawnie ułożone na planszy.",
                "2. Punkty:",
                "- Za każde ułożone słowo otrzymasz punkty.",
                "- Im dłuższe słowo, tym więcej punktów.",
                "Powodzenia i miłej zabawy!"
            ]
            instruction_y = screen_height // 2 - len(instruction_text) * 20

            for line in instruction_text:
                MainMenu.draw_text(line, menu_font, WHITE, screen_width // 2, instruction_y)
                instruction_y += 40

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    back_button_hovered = self.back_button.rect.collidepoint(mouse_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_hovered:
                        # Kliknięto przycisk WSTECZ
                        game.run()


class ScoreCounter:
    def __init__(self):
        self.total = 0


class ScrabbleGame:
    def __init__(self):
        self.main_menu = MainMenu()
        self.instruction_screen = InstructionScreen()

    def run(self):
        self.main_menu.draw()


# instancja klasy z total
score_counter = ScoreCounter()


def generate_tiles():
    letters = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I',
               'I', 'I', 'J', 'K', 'L', 'L', 'L', 'Ł', 'Ł', 'M', 'M', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'P', 'P', 'R',
               'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'U', 'U', 'W', 'W', 'Y', 'Y', 'Z', 'Z', 'Ź', 'Ż', 'Ą', 'Ę',
               'Ć', 'Ń', 'Ó', 'Ś']
    random.shuffle(letters)

    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'S': 1, 'W': 1, 'Z': 1,
        'C': 2, 'D': 2, 'K': 2, 'L': 2, 'M': 2, 'P': 2, 'T': 2, 'Y': 2,
        'B': 3, 'G': 3, 'H': 3, 'J': 3, 'Ł': 3, 'U': 3,
        'Ą': 5, 'Ę': 5, 'F': 5, 'Ó': 5, 'Ś': 5, 'Ż': 5,
        'Ć': 6, 'Ń': 7,
        'Ź': 9
    }

    tiles = [(letter, letter_scores[letter]) for letter in letters[:7]]
    return tiles


def load_dictionary():
    with open('dictionary.txt', 'r') as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary


def play_game(dictionary):
    game_screen = pygame.display.set_mode((screen_width, screen_height))

    placed_tiles = []

    # Inicjalizacja czcionek
    menu_font = pygame.font.Font(None, 32)
    small_font = pygame.font.Font(None, 18)  # do wartości
    punkty_font = pygame.font.Font(None, 45)

    # Inicjalizacja planszy Scrabble
    board_size = 15  # Rozmiar planszy 15x15
    tile_size = 40  # Rozmiar pojedynczego pola na planszy
    board_offset_x = (screen_width - board_size * tile_size) // 2  # Wyliczenie przesunięcia planszy w osi X
    board_offset_y = (screen_height - board_size * tile_size) // 2  # Wyliczenie przesunięcia planszy w osi Y

    # Inicjalizacja płytek literowych
    tiles = generate_tiles()

    # Inicjalizacja pustej planszy
    board = [['' for _ in range(board_size)] for _ in range(board_size)]

    # Inicjalizacja pozycji płytek literowych
    tile_positions = []
    for i in range(7):
        tile_x = (screen_width - 7 * tile_size) // 2 + i * tile_size
        tile_y = screen_height - tile_size - 20
        tile_positions.append((tile_x, tile_y))

    dragged_tile_index = None  # Indeks przeciąganej płytki
    initial_tile_position = None  # Pozycja początkowa przeciąganej płytki

    last_placed_tile = None  # Ostatnio położona płytka

    # Pozycje przycisków w grze
    undo_button_width = 120
    undo_button_height = 40
    undo_button_x = screen_width - undo_button_width - 20
    undo_button_y = screen_height - undo_button_height - 20

    check_button_width = 120
    check_button_height = 40
    check_button_x = screen_width - check_button_width - 20
    check_button_y = screen_height - check_button_height - 140

    exchange_button_width = 120
    exchange_button_height = 40
    exchange_button_x = screen_width - exchange_button_width - 20
    exchange_button_y = screen_height - exchange_button_height - 80

    def exchange_tiles():
        nonlocal tiles  # odwołanie się do zmiennej tiles z zewnatrz

        new_tiles = generate_tiles()
        tiles = new_tiles

        return f"Wymieniono wszystkie litery."

    def check_word(dictionary):

        letter_scores = {
            'A': 1, 'E': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'S': 1, 'W': 1, 'Z': 1,
            'C': 2, 'D': 2, 'K': 2, 'L': 2, 'M': 2, 'P': 2, 'T': 2, 'Y': 2,
            'B': 3, 'G': 3, 'H': 3, 'J': 3, 'Ł': 3, 'U': 3,
            'Ą': 5, 'Ę': 5, 'F': 5, 'Ó': 5, 'Ś': 5, 'Ż': 5,
            'Ć': 6, 'Ń': 7,
            'Ź': 9
        }

        if last_placed_tile:  # jeśli True
            row, col, letter = last_placed_tile
            word_horizontal = ""
            col_start = col
            while col_start > 0 and board[row][col_start - 1]:  # aktualne pole i poprzednie czy ma literke
                col_start -= 1
            for c in range(col_start, board_size):
                if not board[row][c]:  # czy pole na planszy jest puste
                    break
                word_horizontal += board[row][c][0]  # pierwsza literka z planszy
            word_vertical = ""
            row_start = row
            while row_start > 0 and board[row_start - 1][col]:
                row_start -= 1
            for r in range(row_start, board_size):
                if not board[r][col]:  # czy pole na planszy jest puste
                    break
                word_vertical += board[r][col][0]

            # Sprawdzenie poprawności poziomu
            if len(word_horizontal) > 1:
                if word_horizontal.lower() not in dictionary:
                    return f"Niepoprawne słowo: {word_horizontal}"
                else:
                    word_score = sum(letter_scores[letter] for letter in word_horizontal.upper())
                    score_counter.total += word_score

                    # Odjęcie użytych liter od ogólnej liczby posiadanych liter
                    for litera in word_horizontal.upper():
                        if litera in tiles:
                            tiles.remove(litera)
                    missing_tiles = 7 - len(tiles)
                    new_tiles = generate_tiles()
                    for _ in range(missing_tiles):
                        tiles.append(new_tiles.pop())

                    return f"Poprawne słowo: {word_horizontal} - Punkty: {word_score}"

            # Sprawdzenie poprawności pionu
            if len(word_vertical) > 1:
                if word_vertical.lower() not in dictionary:
                    return f"Niepoprawne słowo: {word_vertical}"
                else:
                    word_score = sum(letter_scores[letter] for letter in word_vertical.upper())
                    score_counter.total += word_score

                    # Odjęcie użytych liter od ogólnej liczby posiadanych liter
                    for litera in word_vertical.upper():
                        if litera in tiles:
                            tiles.remove(litera)
                    missing_tiles = 7 - len(tiles)
                    new_tiles = generate_tiles()
                    for _ in range(missing_tiles):
                        tiles.append(new_tiles.pop())

                    return f"Poprawne słowo: {word_vertical} - Punkty: {word_score}"

        return "Nie ułożono słowa."

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Lewy przycisk myszy
                    mouse_position = pygame.mouse.get_pos()

                    # Czy kliknięto na którąś z płytek literowych
                    for i, tile_position in enumerate(tile_positions):  # pętla do iteracji po indeksach
                        tile_rect = pygame.Rect(tile_position[0], tile_position[1], tile_size, tile_size)
                        if tile_rect.collidepoint(mouse_position):
                            dragged_tile_index = i
                            initial_tile_position = tile_position  # początkowa lokalizacja
                            break
                    # Czy kliknięto na przycisk COFNIJ
                    undo_button_rect = pygame.Rect(undo_button_x, undo_button_y, undo_button_width, undo_button_height)
                    if undo_button_rect.collidepoint(mouse_position):
                        if placed_tiles and len(tiles) < 7:  # czy położone i czy mniej niż 7 liter
                            num_tiles_to_undo = min(len(placed_tiles), 7 - len(tiles))  # Liczba liter do cofnięcia
                            for _ in range(num_tiles_to_undo):
                                row, col, letter = placed_tiles.pop()  # Pobranie ostatniej położonej litery
                                board[row][col] = ''
                                tiles.append(letter)
                    # Czy kliknięto na przycisk SPRAWDŹ
                    check_button_rect = pygame.Rect(check_button_x, check_button_y, check_button_width,
                                                    check_button_height)
                    if check_button_rect.collidepoint(mouse_position):
                        result = check_word(dictionary)
                        # Komunikat na ekranie
                        screen.fill(BLUE)
                        MainMenu.draw_text(result, menu_font, WHITE, screen_width // 2, screen_height // 2)
                        pygame.display.update()
                        pygame.time.delay(2500)  # delay

                    # Czy kliknięto na przycisk "WYMIEŃ"
                    exchange_button_rect = pygame.Rect(exchange_button_x, exchange_button_y, exchange_button_width,
                                                       exchange_button_height)
                    if exchange_button_rect.collidepoint(mouse_position):
                        result = exchange_tiles()
                        # Komunikat na ekranie
                        screen.fill(BLUE)
                        MainMenu.draw_text(result, menu_font, WHITE, screen_width // 2, screen_height // 2)
                        pygame.display.update()
                        pygame.time.delay(2500)  # delay

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Lewy przycisk myszy
                    if dragged_tile_index is not None:
                        mouse_position = pygame.mouse.get_pos()
                        dropped_on_board = False
                        # Sprawdzenie, czy upuszczono płytkę na planszy
                        for row in range(board_size):
                            for col in range(board_size):
                                tile_x = board_offset_x + col * tile_size
                                tile_y = board_offset_y + row * tile_size
                                tile_rect = pygame.Rect(tile_x, tile_y, tile_size, tile_size)
                                if tile_rect.collidepoint(mouse_position):
                                    # Umieszczenie płytki na planszy
                                    if not board[row][col]:  # Czy pole na planszy jest puste
                                        board[row][col] = tiles[dragged_tile_index]
                                        last_placed_tile = (row, col, tiles[dragged_tile_index])
                                        tiles.pop(dragged_tile_index)
                                        placed_tiles.append(last_placed_tile)  # Informacja o położonej literze do listy
                                    else:
                                        # Jeśli pole jest już zajęte, wróć na pierwotną pozycję
                                        tile_positions[dragged_tile_index] = initial_tile_position
                                    dropped_on_board = True
                                    break
                            if dropped_on_board:
                                break

                        if not dropped_on_board:
                            # Jeśli płytki nie upuszczono na planszy, wróć na pierwotną pozycję
                            tile_positions[dragged_tile_index] = initial_tile_position

                        dragged_tile_index = None
                        initial_tile_position = None

        game_screen.fill(PINK)  # Tło gry

        MainMenu.draw_text(f"Punkty: {score_counter.total}", punkty_font, BLACK, screen_width // 2,
                           20)  # Aktualny wynik

        # Rysowanie planszy Scrabble
        for row in range(board_size):
            for col in range(board_size):
                tile_x = board_offset_x + col * tile_size
                tile_y = board_offset_y + row * tile_size
                tile_rect = pygame.Rect(tile_x, tile_y, tile_size, tile_size)
                if row == col == board_size // 2:
                    tile_color = RED  # Czerwony środkowy kwadrat
                else:
                    tile_color = YELLOW if board[row][col] else BLUE  # Kolor płytki lub tła planszy
                pygame.draw.rect(game_screen, tile_color, tile_rect)

                pygame.draw.rect(game_screen, BLACK, tile_rect, 1)

                # Rysowanie litery na planszy, jeśli jest ustawiona
                if board[row][col]:
                    letter, score = board[row][col]
                    MainMenu.draw_text(letter, menu_font, BLACK, tile_x + tile_size // 2, tile_y + tile_size // 2)
                    MainMenu.draw_text(str(score), small_font, BLACK, tile_x + tile_size - 10, tile_y + tile_size - 10)

        # Rysowanie płytek literowych
        for i, (tile, score) in enumerate(tiles[:7]):
            tile_x, tile_y = tile_positions[i]
            if i == dragged_tile_index:
                # Czy obecnie rysowana płytka jest przeciągana
                tile_x, tile_y = pygame.mouse.get_pos()
            tile_rect = pygame.Rect(tile_x, tile_y, tile_size, tile_size)
            pygame.draw.rect(game_screen, GREEN, tile_rect)
            pygame.draw.rect(game_screen, BLACK, tile_rect, 1)
            MainMenu.draw_text(tile, menu_font, BLACK, tile_x + tile_size // 2, tile_y + tile_size // 2)
            MainMenu.draw_text(str(score), small_font, BLACK, tile_x + tile_size - 10, tile_y + tile_size - 10)

        # Rysowanie przycisku "COFNIJ"
        undo_button_rect = pygame.Rect(undo_button_x, undo_button_y, undo_button_width, undo_button_height)
        pygame.draw.rect(game_screen, RED, undo_button_rect)
        pygame.draw.rect(game_screen, BLACK, undo_button_rect, 1)  # Obramowanie
        MainMenu.draw_text("COFNIJ", menu_font, BLACK, undo_button_x + undo_button_width // 2,
                           undo_button_y + undo_button_height // 2)

        # Rysowanie przycisku "SPRAWDŹ"
        check_button_rect = pygame.Rect(check_button_x, check_button_y, check_button_width, check_button_height)
        pygame.draw.rect(game_screen, YELLOW, check_button_rect)
        pygame.draw.rect(game_screen, BLACK, check_button_rect, 1)
        MainMenu.draw_text("SPRAWDŹ", menu_font, BLACK, check_button_x + check_button_width // 2,
                           check_button_y + check_button_height // 2)

        # Rysowanie przycisku "WYMIEŃ"
        exchange_button_rect = pygame.Rect(exchange_button_x, exchange_button_y, exchange_button_width,
                                           exchange_button_height)
        pygame.draw.rect(game_screen, YELLOW, exchange_button_rect)
        pygame.draw.rect(game_screen, BLACK, exchange_button_rect, 1)
        MainMenu.draw_text("WYMIEŃ", menu_font, BLACK, exchange_button_x + exchange_button_width // 2,
                           exchange_button_y + exchange_button_height // 2)

        pygame.display.update()  # Uaktualnienie ekranu gry


dictionary = load_dictionary()  # Załadowanie słownika


if __name__ == "__main__":
    game = ScrabbleGame()
    game.run()
