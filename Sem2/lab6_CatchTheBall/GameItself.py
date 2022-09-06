import pygame
import pygame.draw as dr
import random as rand

pygame.init()

FPS = 60
GAME_DURATION = 1800

SCR_WIDTH = 1500
SCR_HEIGHT = 750
SCORE_PANEL_WIDTH = SCR_WIDTH // 4

MAX_FIGURE_SIZE = 50
MAX_FIGURE_SPEED = 800

SKY = (204, 247, 255)
RED = (199, 28, 28)
BLUE = (29, 182, 209)
YELLOW = (209, 200, 29)
GREEN = (47, 209, 29)
MAGENTA = (209, 29, 203)
CYAN = (35, 222, 178)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [SKY, RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]


class Figure:
    """
    Abstract figure without realization of appearance and hitbox
    """

    def __init__(self):
        """
        Setting the basic kinematic properties of the figure, size, lifespan and color
        """
        self.x_velocity = rand.gauss(0, 200)
        self.y_velocity = rand.gauss(0, 200)
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.x_coordinate = rand.uniform(SCORE_PANEL_WIDTH + MAX_FIGURE_SIZE, SCR_WIDTH - MAX_FIGURE_SIZE)
        self.y_coordinate = rand.uniform(MAX_FIGURE_SIZE, SCR_HEIGHT - MAX_FIGURE_SIZE)
        self.radius = rand.uniform(MAX_FIGURE_SIZE / 5, MAX_FIGURE_SIZE)
        self.time_limit = abs(rand.gauss(20, 7))
        self.age = 0
        self.color = COLORS[rand.randint(1, 6)]

    def draw_figure(self):
        """
        Drawing figure (for abstract figure realization is absent)
        """
        pass

    def is_hit_left_wall(self):
        """
        Checking collision with left wall
        :return: Is figure colliding with left wall
        """
        x_delta = self.x_velocity * 1 / FPS
        return self.x_coordinate + x_delta < SCORE_PANEL_WIDTH + self.radius

    def is_hit_right_wall(self):
        """
        Checking collision with right wall
        :return: Is figure colliding with right wall
        """
        x_delta = self.x_velocity * 1 / FPS
        return self.x_coordinate + x_delta > SCR_WIDTH - self.radius

    def is_hit_up_wall(self):
        """
        Checking collision with up wall
        :return: Is figure colliding with up wall
        """
        y_delta = self.y_velocity * 1 / FPS
        return self.y_coordinate + y_delta < self.radius

    def is_hit_down_wall(self):
        """
        Checking collision with down wall
        :return: Is figure colliding with down wall
        """
        y_delta = self.y_velocity * 1 / FPS
        return self.y_coordinate + y_delta > SCR_HEIGHT - self.radius

    def move_figure(self):
        """
        Moving, aging and collision handling
        """
        self.age += 1 / FPS
        speed = (self.x_velocity ** 2 + self.y_velocity ** 2) ** 0.5

        if self.is_hit_left_wall():
            self.x_velocity = rand.uniform(speed / 3, speed)
            self.y_velocity = rand.randrange(-1, 2, 2) * (speed ** 2 - self.x_velocity ** 2) ** 0.5

        if self.is_hit_right_wall():
            self.x_velocity = -rand.uniform(speed / 3, speed)
            self.y_velocity = rand.randrange(-1, 2, 2) * (speed ** 2 - self.x_velocity ** 2) ** 0.5

        if self.is_hit_up_wall():
            self.y_velocity = rand.uniform(speed / 3, speed)
            self.x_velocity = rand.randrange(-1, 2, 2) * (speed ** 2 - self.y_velocity ** 2) ** 0.5

        if self.is_hit_down_wall():
            self.y_velocity = -rand.uniform(speed / 3, speed)
            self.x_velocity = rand.randrange(-1, 2, 2) * (speed ** 2 - self.y_velocity ** 2) ** 0.5

        self.x_coordinate += self.x_velocity * 1 / FPS
        self.y_coordinate += self.y_velocity * 1 / FPS

    def is_caught(self, click_event):
        """
        Checking if player has caught the figure (for abstract figure realization is absent)
        :param click_event: Click event (from pygame library)
        :return:Has player caught the figure
        """
        pass

    def get_type(self):
        """
        Checking a type of the figure (for abstract figure realization is absent)
        :return: Type of figure (string)
        """
        pass


class Ball(Figure):
    """
    Ball, which has constant speed and reflects from walls at a random angle
    """

    def draw_figure(self):
        """
        Drawing ball
        """
        dr.circle(Screen, self.color, (self.x_coordinate, self.y_coordinate), self.radius)

    def is_caught(self, click_event):
        """
        Checking if player has caught the ball
        :param click_event: Click event (from pygame library)
        :return:Has player caught the ball
        """
        return ((click_event.pos[0] - self.x_coordinate) ** 2 + (
                click_event.pos[1] - self.y_coordinate) ** 2) ** 0.5 < self.radius

    def get_type(self):
        """
        Checking a type of the figure
        :return: Type of figure ('Ball')
        """
        return 'Ball'


class Block(Figure):
    """
    Block, which has dynamic acceleration and reflects from walls at a random angle
    """

    def draw_figure(self):
        """
        Drawing block
        """
        x_left = self.x_coordinate - self.radius
        y_top = self.y_coordinate - self.radius
        dr.rect(Screen, self.color, (x_left, y_top, 2 * self.radius, 2 * self.radius))

    def move_figure(self):
        """
        Adding acceleration to standard move pattern
        """
        super().move_figure()
        self.x_acceleration += rand.uniform(-1, 1)
        self.y_acceleration += rand.uniform(-1, 1)

        if (self.x_velocity ** 2 + self.y_velocity ** 2) ** 0.5 < MAX_FIGURE_SPEED:
            self.x_velocity += self.x_acceleration
            self.y_velocity += self.y_acceleration

        else:
            if self.x_acceleration < 0:
                self.x_velocity += self.x_acceleration
            if self.y_acceleration < 0:
                self.y_velocity += self.y_acceleration

    def is_caught(self, click_event):
        """
        Checking if player has caught the block
        :param click_event: Click event (from pygame library)
        :return:Has player caught the block
        """
        return abs(click_event.pos[0] - self.x_coordinate) < self.radius or abs(
            click_event.pos[1] - self.y_coordinate) < self.radius

    def get_type(self):
        """
        Checking a type of the figure
        :return: Type of figure ('Block')
        """
        return 'Block'


def draw_interface_panel(surface, color, name, score, ticks, hit):
    """
    Drawing interface panel
    :param surface: Target surface
    :param color: Color of a score panel
    :param name: Name of current player
    :param score: Score of current player at this moment
    :param ticks: Time from start of current game in ticks
    :param hit: Points awarded for the last hit
    """
    font = pygame.font.SysFont('consolas', 38)
    dr.rect(surface, WHITE, (0, 0, SCORE_PANEL_WIDTH, SCR_HEIGHT))
    dr.rect(surface, color, (0, 0, SCORE_PANEL_WIDTH - 3, SCR_HEIGHT))

    text_name = name + "'s game"
    text_surface_name = font.render(text_name, True, WHITE)
    surface.blit(text_surface_name, (5, 0))

    text_score = "Score: " + str(score)
    text_surface_score = font.render(text_score, True, WHITE)
    surface.blit(text_surface_score, (5, 50))

    time_left = GAME_DURATION - ticks
    text_time_left = "Time left: " + str(time_left // 60) + 's'
    text_time_left = font.render(text_time_left, True, WHITE)
    surface.blit(text_time_left, (5, 100))

    if hit == 1:
        text_hit = "+" + str(hit)
        text_hit = font.render(text_hit, True, WHITE)
        surface.blit(text_hit, (5, 150))

    elif hit == 5:
        font = pygame.font.SysFont('consolas', 58)
        text_hit = "+" + str(hit)
        text_hit = font.render(text_hit, True, GREEN)
        surface.blit(text_hit, (5, 150))

    elif hit == -1:
        font = pygame.font.SysFont('consolas', 38)
        text_hit = str(hit)
        text_hit = font.render(text_hit, True, RED)
        surface.blit(text_hit, (5, 150))


def draw_player_score(surface, color, name, score):
    """
    Drawing score of player when time is out
    :param surface: Target surface
    :param color: Color of a score
    :param name: Name of current player
    :param score: Total score of current player
    """
    font = pygame.font.SysFont('consolas', 130)
    text = name + "'s score: " + str(score)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (10, 300))


def hit_registration(figures, score, finish, hit):
    """
    Accepts key parameters: list of figures, player's score, last hit and modify them in dependence of current click
    :param figures: List of figures
    :param score: Current player's score
    :param finish: Is it necessary to stop game
    :param hit: Points from last hit
    :return: Modified in dependence of current click arguments
    """
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            finish = True
        elif eve.type == pygame.MOUSEBUTTONDOWN:
            k = 0
            caught = False
            while k < len(figures_array):
                if figures_array[k].is_caught(eve):
                    if figures_array[k].get_type() == 'Ball':
                        score += 1
                        caught = True
                        hit = 1
                    elif figures_array[k].get_type() == 'Block':
                        score += 5
                        caught = True
                        hit = 5
                    figures_array.pop(k)
                else:
                    k += 1
            if not caught:
                score -= 1
                hit = -1
    return figures, score, finish, hit


def sort_double_component_array(array):
    """
    Sorting array with elements of the form: [smth | int]
    :param array: Original array
    :return: Sorted from min to max array
    """
    for i1 in range(len(array)):
        for i2 in range(len(array) - 1 - i1):
            if array[i2][1] < array[i2 + 1][1]:
                array[i2], array[i2 + 1] = array[i2 + 1], array[i2]
    return array


# Reading old champion list from file
with open("Champions.txt", mode='r') as f:
    OldChampionsArray = f.readlines()
for i in range(len(OldChampionsArray)):
    OldChampionsArray[i] = [OldChampionsArray[i].split(' ')[0], int(OldChampionsArray[i].split(' ')[1].split('\n')[0])]

# Creating list of new players
NumberOfPlayers = int(input('Enter the number of players: '))
PlayersArray = []

for j in range(NumberOfPlayers):
    player_name = input('Enter the name of player {}: '.format(j + 1))

    Screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))

    pygame.display.update()
    clock = pygame.time.Clock()
    number_of_ticks = 0
    finished = False

    figures_array = []
    player_score = 0
    last_hit = 0

    while not (finished or number_of_ticks > GAME_DURATION):
        # Adding figures
        if len(figures_array) < 20 and rand.randint(1, FPS) == 1:
            if rand.random() < 0.1:
                figures_array.append(Block())
            else:
                figures_array.append(Ball())

        # Killing figures if their time has come
        i = 0
        while i < len(figures_array):
            if figures_array[i].age > figures_array[i].time_limit:
                figures_array.pop(i)
            else:
                i += 1

        # Drawing background
        Screen.fill(SKY)

        # Moving and drawing figures
        for i in range(len(figures_array)):
            figures_array[i].move_figure()
            figures_array[i].draw_figure()

        # Drawing user interface
        draw_interface_panel(Screen, BLACK, player_name, player_score, number_of_ticks, last_hit)

        # Displaying the image on the screen
        pygame.display.update()

        # Waiting for player's reaction
        clock.tick(FPS)
        number_of_ticks += 1

        figures_array, player_score, finished, last_hit = hit_registration(figures_array, player_score, finished,
                                                                           last_hit)

    while not (finished or number_of_ticks > GAME_DURATION + 600):
        # Drawing TOTAL SCORE of player
        if number_of_ticks % 60 == 0:
            Screen.fill(BLACK)
        if number_of_ticks % 120 == 0:
            draw_player_score(Screen, RED, player_name, player_score)

        # Displaying the image on the screen
        pygame.display.update()

        # Waiting next tick
        number_of_ticks += 1
        clock.tick(FPS)

        # Registering click on quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    PlayersArray.append([player_name, player_score])

    pygame.display.quit()

# Creating sorted new champions list
NewChampionsArray = sort_double_component_array(OldChampionsArray + PlayersArray)

# Writing old champion list to file
with open("Champions.txt", mode='w') as f:
    for i in range(min(10, len(NewChampionsArray))):
        f.write(NewChampionsArray[i][0] + ' ' + str(NewChampionsArray[i][1]) + '\n')

pygame.quit()
