from Colors import Colors
from Converter import Converter
from Plotter import Plotter

from typing import List, Tuple, Dict, Any

import random
import datetime
import numpy as np
from psychopy import visual, event, core


class Experiment(object):
    """
    Class to run the experiment and manage the stages and rounds.
    """

    def __init__(self, stages: int = 1, rounds_per_stage: int = 5,
                 path_to_results: str = "results/", fullscreen: bool = True) -> None:
        """
        Initializes the Experiment object with the given parameters.

        :param stages: Number of stages in the experiment. Default is 4.
        :param rounds_per_stage: Number of rounds per stage. Default is 20.
        :param path_to_results: Path where the results will be saved. Default is "results/".
        :param fullscreen: Boolean indicating whether to use fullscreen mode. Default is True.
        """
        self.stages: int = stages
        self.rounds_per_stage: int = rounds_per_stage
        self.path_to_results: str = path_to_results
        self.win: visual.Window = visual.Window(fullscr=fullscreen, color=Colors.BACKGROUND.value, units='height')
        self.session_number: int = 1
        self.results_list: List[Dict[str, Any]] = []
        self.mouse: event.Mouse = event.Mouse(win=self.win)
        self.mouse.setVisible(True)

    def __str__(self) -> str:
        """
        Return a string representation of the Experiment object.

        :return: String representation of the Experiment object.
        """
        return f"Experiment with {self.stages} stages and {self.rounds_per_stage} rounds per stage."

    def draw_grid(self, grid_size: int, selected_squares: List[Tuple[int, int]],
                  square_size: float = 0.1, gap: float = 0.02) -> List[Tuple[visual.Rect, Tuple[int, int]]]:
        """
        Draws a grid of squares on the screen, highlighting selected squares in yellow.

        :param grid_size: The size of the grid (number of rows and columns).
        :param selected_squares: List of tuples indicating the positions of the squares to be highlighted in yellow.
        :param square_size: The size of each square. Default is 0.1 (height units).
        :param gap: The gap between the squares. Default is 0.02 (height units).
        :return: List of tuples, each containing a visual.Rect object and its position.
        """
        offset: float = (square_size + gap) * (grid_size - 1) / 2
        squares: List[Tuple[visual.Rect, Tuple[int, int]]] = []
        for row in range(grid_size):
            for col in range(grid_size):
                x: float = col * (square_size + gap) - offset
                y: float = row * (square_size + gap) - offset
                color: str = Colors.YELLOW.value if (row, col) in selected_squares else Colors.BLUE.value
                square: visual.Rect = visual.Rect(self.win, width=square_size, height=square_size,
                                                  fillColor=color, pos=(x, y))
                squares.append((square, (row, col)))
        return squares

    def show_stage_info(self, stage_number: int, round_number: int, mistakes_in_stage: int) -> None:
        """
        Displays stage information on the screen.

        :param stage_number: The current stage number.
        :param round_number: The current round number.
        :param mistakes_in_stage: The number of mistakes made in the current stage.
        :return: None
        """
        info_text: str = f"Etap: {stage_number + 1}\nRunda: {round_number + 1}\nSzanse: {3 - mistakes_in_stage}/3"
        info: visual.TextStim = visual.TextStim(self.win, text=info_text, color=Colors.WHITE.value, height=0.05)
        info.draw()
        self.win.flip()
        core.wait(1)

    def show_instruction(self) -> None:
        """
        Displays the instructions for the experiment.

        :return: None
        """
        instruction_text: str = """
        Witamy w eksperymencie dotyczącym pamięci operacyjnej.\n
        Celem badania jest ocena Twojej zdolności do zapamiętywania przedstawianych Ci sekwencji elementów.
        Prosimy o dokładne zapoznanie się z poniższymi instrukcjami i postępowanie zgodnie z nimi.

        1. Na początku każdej rundy wyświetlana będzie plansza z losowo ułożonymi, żółtymi, kwadratowymi polami. Twoim zadaniem będzie zapamiętanie ich położenia.
        2. Po 2 sekundach pojawi się nowa plansza, gdzie wszystkie kwadraty będą niebieskie. Twoim zadaniem jest wskazanie, które pola były żółte.
        3. Jeżeli klikniesz w odpowiedni kwadrat zmieni on barwę z niebieskiej na żółtą. W przypadku kliknięcia w niewłaściwe pole, wciśnięty kwadrat zniknie.
        4. W przypadku wybrania kolejnego niewłaściwego pola, liczba szans zmniejszy się o 1, a runda zostanie przerwana, przejdziesz do kolejnej.
        5. Po trzech błędach etap zostanie przerwany.
        6. W przypadku wskazania wszystkich poprawnych pól, przejdziesz do kolejnej rundy, gdzie liczba żółtych kwadratów wzrośnie o jeden.
        7. Rozmiar planszy będzie się stopniowo zwiększał wraz ze wzrostem liczby żółtych kwadratów w kolejnych rundach.
        8. Etap składa się z maksymalnie 20 rund.
        9. Przed i po każdym etapie pojawi się krótka informacja o jego rozpoczęciu lub zakończeniu.
        10. Po każdej rundzie zostanie wyświetlony komunikat o poprawności wykonania zadania.
        11. Pred każdą rundą wyświetlana będzie informacja o numerze etapu, rundy oraz liczbie pozostałych szans.
        12. Masz do wykonania łącznie 4 etapy, z czego pierwszy jest treningowy, a trzy pozostałe stanowią właściwe badanie.
        13. Pamiętaj, że ważne jest by wykonywać zadanie w ciszy i skupieniu.
        14. Mierzony będzie również czas wykonania zadania - jak szybko uda Ci się wskazać wszystkie żółte pola. Staraj się działać jak najszybciej, ale jednocześnie dokładnie.
        
        Twoje wyniki zostaną anonimowo zapisane, nie będą one w żaden sposób powiązane z Twoją tożsamością. 
        W przypadku jakichkolwiek pytań prosimy o kontakt z prowadzącym badanie.

        Jeżeli jesteś gotowy_a, kliknij spację, aby zacząć test.
        """
        instruction: visual.TextStim = visual.TextStim(self.win, text=instruction_text, color=Colors.WHITE.value,
                                                       height=0.03, wrapWidth=1.5)
        instruction.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"])

    def show_ending(self) -> None:
        """
        Displays the ending message of the experiment.

        :return: None
        """
        ending_text: str = "Twoje wyniki zostały zapisane.\n\nDziękujemy za udział w badaniu!"
        ending: visual.TextStim = visual.TextStim(self.win, text=ending_text, color=Colors.WHITE.value, height=0.05)
        ending.draw()
        self.win.flip()
        core.wait(5)

    def show_stage_start(self, stage_number: int) -> None:
        """
        Displays the start message of a stage.

        :param stage_number: The current stage number.
        :return: None
        """
        text: str = "Rozpoczynasz etap 1\n(treningowy)\n\nNaciśnij spację, aby kontynuować." if stage_number == 0 \
            else f"Rozpoczynasz etap {stage_number + 1}\n\nNaciśnij spację, aby kontynuować."
        stage_start: visual.TextStim = visual.TextStim(self.win, text=text, color=Colors.WHITE.value, height=0.05)
        stage_start.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"])

    def show_stage_end(self, stage_number: int) -> None:
        """
        Displays the end message of a stage.

        :param stage_number: The current stage number.
        :return: None
        """
        text: str = f"Zakończyłeś etap {stage_number + 1}\n\nNaciśnij spację, aby kontynuować."
        stage_end: visual.TextStim = visual.TextStim(self.win, text=text, color=Colors.WHITE.value, height=0.05)
        stage_end.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"])

    def run(self) -> int:
        """
        Runs the experiment, displaying instructions, stages, rounds, and saving the results to files.

        :return: 0 if the experiment was successful.
        """
        self.show_instruction()

        for stage_number in range(self.stages):
            self.show_stage_start(stage_number)
            mistakes_in_stage: int = 0
            selected_squares_count: int = 3
            grid_size: int = 3

            for round_number in range(self.rounds_per_stage):
                self.show_stage_info(stage_number, round_number, mistakes_in_stage)

                if selected_squares_count >= (grid_size * grid_size) / 2:
                    grid_size += 1

                selected_squares: List[Tuple[int, int]] = random.sample([(i, j)
                                                                         for i in range(grid_size)
                                                                         for j in range(grid_size)],
                                                                        selected_squares_count)
                squares: List[Tuple[visual.Rect, Tuple[int, int]]] = self.draw_grid(grid_size, selected_squares)
                for square, _ in squares:
                    square.draw()
                self.win.flip()
                core.wait(2)
                #memorization_start_time: float = core.getTime()

                squares = self.draw_grid(grid_size, [])
                for square, _ in squares:
                    square.draw()
                self.win.flip()

                clicked_squares: List[Tuple[int, int]] = []
                click_times: List[float] = []
                correct_clicks: int = 0
                mistakes_in_round: int = 0
                misclicked_square: Tuple[int, int] = ()

                self.mouse.clickReset()

                start_time: float = core.getTime()

                while correct_clicks < selected_squares_count and mistakes_in_stage < 3:
                    mouse_clicks = self.mouse.getPressed(getTime=True)
                    if mouse_clicks[0][0]:
                        mouse_click_pos = self.mouse.getPos()
                        click_time = core.getTime()
                        for square, pos in squares:
                            if (square.contains(mouse_click_pos)
                                    and pos not in clicked_squares
                                    and not np.array_equal(square.fillColor, Colors.YELLOW.value)
                                    and square.opacity != 0):
                                if pos in selected_squares:
                                    square.fillColor = Colors.YELLOW.value
                                    correct_clicks += 1
                                else:
                                    square.opacity = 0
                                    mistakes_in_round += 1
                                    misclicked_square = pos
                                clicked_squares.append(pos)
                                click_times.append(click_time - start_time)
                                print(click_times)
                                for sq, _ in squares:
                                    sq.draw()
                                self.win.flip()
                                core.wait(0.2)
                        while self.mouse.getPressed()[0]:
                            core.wait(0.01)
                        if mistakes_in_round > 1:
                            mistakes_in_stage += 1
                            result_text: str = "Źle!"
                            result: visual.TextStim = visual.TextStim(self.win, text=result_text, pos=(0, -0.1),
                                                                      color=Colors.WHITE.value, height=0.05)
                            result.draw()
                            self.win.flip()
                            core.wait(2)
                            break

                #memorization_time: float = core.getTime() - memorization_start_time

                if mistakes_in_stage == 3:
                    new_result: Dict[str, Any] = {
                        "Session": self.session_number,
                        "Stage": stage_number + 1,
                        "Round": round_number + 1,
                        "Selected_squares": selected_squares,
                        "Clicked_positions": clicked_squares,
                        "Mistakes_in_stage": mistakes_in_stage,
                        "Click_times": click_times
                    }
                    self.results_list.append(new_result)
                    break

                if mistakes_in_round > 1:
                    new_result = {
                        "Session": self.session_number,
                        "Stage": stage_number + 1,
                        "Round": round_number + 1,
                        "Selected_squares": selected_squares,
                        "Clicked_positions": clicked_squares,
                        "Mistakes_in_stage": mistakes_in_stage,
                        "Click_times": click_times
                    }
                    self.results_list.append(new_result)
                    continue

                if mistakes_in_round == 1:
                    clicked_squares_copy: List[Tuple[int, int]] = clicked_squares.copy()
                    clicked_squares_copy.remove(misclicked_square)
                    correct: bool = all(pos in clicked_squares_copy for pos in selected_squares)
                else:
                    correct = all(pos in clicked_squares for pos in selected_squares)

                if correct:
                    selected_squares_count += 1

                new_result = {
                    "Session": self.session_number,
                    "Stage": stage_number + 1,
                    "Round": round_number + 1,
                    "Selected_squares": selected_squares,
                    "Clicked_positions": clicked_squares,
                    "Mistakes_in_stage": mistakes_in_stage,
                    "Click_times": click_times
                }
                self.results_list.append(new_result)

                result_text = "Dobrze!" if correct else "Źle!"
                result = visual.TextStim(self.win, text=result_text, pos=(0, -0.1), color=Colors.WHITE.value, height=0.05)
                result.draw()
                self.win.flip()
                core.wait(2)

                self.show_stage_info(stage_number, round_number, mistakes_in_stage)

                if mistakes_in_stage >= 3:
                    break

            for remaining_round in range(round_number + 1, self.rounds_per_stage):
                new_result = {
                    "Session": self.session_number,
                    "Stage": stage_number + 1,
                    "Round": remaining_round + 1,
                    "Selected_squares": [],
                    "Clicked_positions": [],
                    "Mistakes_in_stage": mistakes_in_stage,
                    "Click_times": []
                }
                self.results_list.append(new_result)

            self.show_stage_end(stage_number)
    
        self.show_ending()

        save_time_end: datetime.datetime = datetime.datetime.now()
        timestamp: str = save_time_end.strftime("%Y%m%d%H%M")
        filename: str = f"{self.path_to_results}{timestamp}"

        converter: Converter = Converter(self.results_list, filename)
        converter.save_to_csv()
        converter.save_to_txt()
        converter.save_to_json()

        plotter: Plotter = Plotter(f"{filename}.csv")
        plotter.plot_average_time_per_square()
        plotter.plot_overall_average_accuracy()

        return 0
    