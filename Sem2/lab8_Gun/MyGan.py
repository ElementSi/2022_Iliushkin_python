import pygame as pg
import math
import random as rand

FPS = 60
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750

SKY = (95, 204, 250)
GREY = (28, 43, 28)
RED = (184, 59, 28)

GRAVITATION = 0.9
GROUND_HEIGHT = 250


class ControlButtons:
    def __init__(self, buttons):
        self.to_right = buttons[0]
        self.to_left = buttons[1]


class Particle:
    def __init__(self, surface, size, coordinates, texture):
        self.surface = surface
        self.size = size
        self.coordinates = coordinates
        self.texture = pg.transform.scale(pg.image.load(texture), (self.size[0], self.size[1]))
        self.lifetime = FPS * 1
        self.age = 0

    def draw(self):
        rect_draw_box = (self.coordinates[0] - self.size[0] / 2,
                         self.coordinates[1] - self.size[1] / 2,
                         self.size[0],
                         self.size[1])
        self.surface.blit(self.texture, rect_draw_box)

    def aging(self):
        self.age += 1

    def get_age(self):
        return self.age

    def get_lifetime(self):
        return self.lifetime


class Ground:
    def __init__(self, surface):
        self.surface = surface
        self.draw_box = (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)
        self.texture = pg.transform.scale(pg.image.load("textures/ground.png"), (SCREEN_WIDTH, GROUND_HEIGHT))

    def draw(self):
        self.surface.blit(self.texture, self.draw_box)


def is_in_hitbox_part(point, hitbox_part):
    return abs(point[0] - hitbox_part[0]) < hitbox_part[2] and abs(point[1] - hitbox_part[1]) < hitbox_part[3]


class Projectile:
    def __init__(self, surface, coordinates, velocity):
        self.surface = surface
        self.rad = 0
        self.damage = 0
        self.coordinates = coordinates
        self.velocity = velocity
        self.color = "#000000"

    def draw(self):
        pg.draw.circle(self.surface, self.color, (self.coordinates[0], self.coordinates[1]), self.rad)

    def move(self):
        self.velocity[1] += GRAVITATION
        self.coordinates[0] += self.velocity[0]
        self.coordinates[1] += self.velocity[1]

    def is_hit_vehicle(self, veh):
        lu_corner = [self.coordinates[0] - self.rad, self.coordinates[1] - self.rad]
        ru_corner = [self.coordinates[0] + self.rad, self.coordinates[1] - self.rad]
        rd_corner = [self.coordinates[0] + self.rad, self.coordinates[1] + self.rad]
        ld_corner = [self.coordinates[0] - self.rad, self.coordinates[1] + self.rad]

        for i in range(len(veh.hitbox)):
            if is_in_hitbox_part(lu_corner, veh.hitbox[i]):
                return True
            if is_in_hitbox_part(ru_corner, veh.hitbox[i]):
                return True
            if is_in_hitbox_part(rd_corner, veh.hitbox[i]):
                return True
            if is_in_hitbox_part(ld_corner, veh.hitbox[i]):
                return True

        return False

    def is_hit_ground(self):
        if abs(self.coordinates[1] - (SCREEN_HEIGHT - GROUND_HEIGHT / 2)) < self.rad:
            return True

        return False

    def is_out_of_screen(self):
        if self.coordinates[0] < -self.rad or self.coordinates[0] > SCREEN_WIDTH + self.rad:
            return True

        return False

    def get_damage(self):
        return self.damage

    def get_type(self):
        pass


class Shell(Projectile):
    def __init__(self, surface, coordinates, velocity):
        super().__init__(surface, coordinates, velocity)
        self.rad = 10
        self.damage = 3

    def death(self):
        explosion_particle = Particle(self.surface, (self.rad * 5, self.rad * 5),
                                      (self.coordinates[0], SCREEN_HEIGHT - (GROUND_HEIGHT / 2 + 2.5 * self.rad)),
                                      "textures/land_explosion.png")
        return explosion_particle

    def get_type(self):
        return "Shell"


class Shrapnel(Projectile):
    def __init__(self, surface, coordinates, velocity):
        super().__init__(surface, coordinates, velocity)
        self.rad = 10
        self.damage = 1

    def get_type(self):
        return "Shrapnel"


class Bomb(Projectile):
    def __init__(self, surface, coordinates, velocity):
        super().__init__(surface, coordinates, velocity)
        self.rad = 10
        self.color = RED
        self.damage = 5

    def death(self):
        explosion_particle = Particle(self.surface, (self.rad * 8, self.rad * 8),
                                      (self.coordinates[0], SCREEN_HEIGHT - (GROUND_HEIGHT / 2 + 4 * self.rad)),
                                      "textures/land_explosion.png")
        return explosion_particle

    def get_type(self):
        return "Bomb"


class Vehicle:
    def __init__(self, surface):
        self.surface = surface
        self.exp_points = 0
        self.hit_points = 0
        self.size = []
        self.coordinates = []
        self.velocity = []
        self.hitbox = []

    def update_hitbox(self):
        pass

    def draw(self):
        draw_box = (self.coordinates[0] - self.size[0] / 2,
                    self.coordinates[1] - self.size[1] / 2,
                    self.size[0],
                    self.size[1])
        self.surface.blit(self.texture, draw_box)

    def move(self):
        self.update_hitbox()
        self.coordinates[0] += self.velocity[0]
        self.coordinates[1] += self.velocity[1]

    def take_damage(self, damage):
        self.hit_points -= damage

    def death(self):
        explosion_particle = Particle(self.surface, self.size, self.coordinates, "textures/air_explosion.png")
        return explosion_particle, self.exp_points

    def is_dead(self):
        if self.hit_points < 0:
            return True

        return False

    def get_type(self):
        pass


class Tank(Vehicle):
    def __init__(self, surface, spawn_point, control_buttons):
        super().__init__(surface)
        self.exp_points = 10
        self.hit_points = 10
        self.size = [100, 60]
        self.coordinates = [spawn_point, SCREEN_HEIGHT - (GROUND_HEIGHT / 2 + 30)]
        self.velocity = [0, 0]
        self.hitbox = [[self.coordinates[0], self.coordinates[1] + 21, self.size[0] / 2, 9],
                       [self.coordinates[0], self.coordinates[1] + 4, 36, 7],
                       [self.coordinates[0], self.coordinates[1] - 17, 25, 13]]
        self.texture = pg.transform.scale(pg.image.load("textures/tank.png"), (self.size[0], self.size[1]))
        self.control_buttons = control_buttons
        self.score = 0

    def update_hitbox(self):
        self.hitbox = [[self.coordinates[0], self.coordinates[1] + 21, self.size[0] / 2, 9],
                       [self.coordinates[0], self.coordinates[1] + 4, 36, 7],
                       [self.coordinates[0], self.coordinates[1] - 17, 25, 13]]

    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.control_buttons.to_right:
                self.velocity[0] = 5
            if event.key == self.control_buttons.to_left:
                self.velocity[0] = -5
        if event.type == pg.KEYUP:
            if event.key == self.control_buttons.to_right or event.key == self.control_buttons.to_left:
                self.velocity[0] = 0

    def death(self):
        explosion_particle = Particle(self.surface, [self.size[0] * 2, self.size[1] * 4],
                                      [self.coordinates[0], self.coordinates[1] - 1.5 * self.size[1]],
                                      "textures/land_explosion.png")
        return explosion_particle, self.exp_points

    def get_type(self):
        return "Tank"


class AirBalloon(Vehicle):
    def __init__(self, surface):
        super().__init__(surface)
        self.exp_points = 1
        self.hit_points = 1
        self.size = [90, 120]
        self.coordinates = [rand.randint(self.size[0], SCREEN_WIDTH - self.size[0]),
                            rand.randint(self.size[1], SCREEN_HEIGHT - GROUND_HEIGHT - self.size[1])]
        self.velocity = [0, 0]
        self.hitbox = [[self.coordinates[0], self.coordinates[1] + 44, 8, 16],
                       [self.coordinates[0], self.coordinates[1] + 15, 39, 13],
                       [self.coordinates[0], self.coordinates[1] - 19, self.size[0] / 2, 21],
                       [self.coordinates[0], self.coordinates[1] - 50, 38, 10]]
        self.texture = pg.transform.scale(pg.image.load("textures/air_balloon.png"), (self.size[0], self.size[1]))

    def update_hitbox(self):
        self.hitbox = [[self.coordinates[0], self.coordinates[1] + 44, 8, 16],
                       [self.coordinates[0], self.coordinates[1] + 15, 39, 13],
                       [self.coordinates[0], self.coordinates[1] - 19, self.size[0] / 2, 21],
                       [self.coordinates[0], self.coordinates[1] - 50, 38, 10]]

    def get_type(self):
        return "AirBalloon"


class Airship(Vehicle):
    def __init__(self, surface):
        super().__init__(surface)
        self.exp_points = 3
        self.hit_points = 4
        self.size = [300, 160]
        self.direction = rand.randint(0, 1)
        if self.direction == 0:
            self.coordinates = [SCREEN_WIDTH * self.direction - self.size[0],
                                rand.randint(self.size[1], SCREEN_HEIGHT - GROUND_HEIGHT - self.size[1])]
            self.velocity = [rand.randint(1, 5), 0]
        else:
            self.coordinates = [SCREEN_WIDTH * self.direction + self.size[0],
                                rand.randint(self.size[1], SCREEN_HEIGHT - GROUND_HEIGHT - self.size[1])]
            self.velocity = [rand.randint(-5, -1), 0]
        self.hitbox = [[self.coordinates[0] - 125, self.coordinates[1] - 14, 24, 62],
                       [self.coordinates[0] - 50, self.coordinates[1], 51, 56],
                       [self.coordinates[0] + 42, self.coordinates[1], 40, self.size[1] / 2],
                       [self.coordinates[0] + 114, self.coordinates[1], 36, 10]]
        self.texture = pg.transform.flip(
            pg.transform.scale(pg.image.load("textures/airship.png"), (self.size[0], self.size[1])),
            bool(self.direction), False)

    def update_hitbox(self):
        self.hitbox = [[self.coordinates[0] - 125, self.coordinates[1] - 14, 24, 62],
                       [self.coordinates[0] - 50, self.coordinates[1], 51, 56],
                       [self.coordinates[0] + 42, self.coordinates[1], 40, self.size[1] / 2],
                       [self.coordinates[0] + 114, self.coordinates[1], 36, 10]]

    def drop_bomb(self):
        avia_bomb = Bomb(self.surface, [self.coordinates[0] + 35, self.coordinates[1] + 91], [0, 0])
        return avia_bomb

    def get_type(self):
        return "Airship"


class Gun:
    def __init__(self, surface, coordinates):
        """
        Constructor of Gun object
        """
        self.width = 12
        self.length = 4
        self.surface = surface
        self.coordinates = (coordinates[0], coordinates[1] - 15)
        self.fire_power = 10
        self.fire_on = 0
        self.angle = 1
        self.color = GREY

    def move_to(self, new_coordinates):
        self.coordinates = (new_coordinates[0], new_coordinates[1] - 15)

    def fire_start(self, event):
        """
        Switching to shooting mod
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            self.fire_on = 1

    def fire_end(self, event):
        """
        Projectile shot towards the cursor
        """
        pass

    def targetting(self, event):
        """
        Aiming towards the cursor
        :param event: MOUSEMOTION event
        """
        if event.type == pg.MOUSEMOTION:
            if event.pos[0] - self.coordinates[0] == 0:
                self.angle = math.pi / 2
            elif event.pos[1] - self.coordinates[1] > 0 and event.pos[0] - self.coordinates[0] > 0:
                self.angle = 0
            elif event.pos[1] - self.coordinates[1] > 0 and event.pos[0] - self.coordinates[0] < 0:
                self.angle = math.pi
            elif event.pos[1] - self.coordinates[1] < 0 and event.pos[0] - self.coordinates[0] > 0:
                self.angle = math.atan((event.pos[1] - self.coordinates[1]) / (event.pos[0] - self.coordinates[0]))
            else:
                self.angle = math.atan(
                    (event.pos[1] - self.coordinates[1]) / (event.pos[0] - self.coordinates[0])) + math.pi

    def draw(self):
        """
        Drawing Gun
        """
        pg.draw.polygon(
            self.surface,
            self.color,
            ((self.coordinates[0] - self.width / 2 * math.sin(self.angle),
              self.coordinates[1] + self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] + self.length * 10 * math.cos(self.angle) - self.width / 2 * math.sin(self.angle),
              self.coordinates[1] + self.length * 10 * math.sin(self.angle) + self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] + self.length * 10 * math.cos(self.angle) + self.width / 2 * math.sin(self.angle),
              self.coordinates[1] + self.length * 10 * math.sin(self.angle) - self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] + self.width / 2 * math.sin(self.angle),
              self.coordinates[1] - self.width / 2 * math.cos(self.angle)))
        )

    def power_up(self):
        if self.fire_on:
            if self.fire_power < 50:
                self.fire_power += 1

    def get_type(self):
        pass


class Artillery(Gun):
    def fire_end(self, event):
        """
        Projectile shot towards the cursor
        :param event: MOUSEBUTTONUP event
        """
        if event.type == pg.MOUSEBUTTONUP:
            start_coordinates = [self.coordinates[0] + self.length * 10 * math.cos(self.angle),
                                 self.coordinates[1] + self.length * 10 * math.sin(self.angle)]
            new_projectiles = [Shell(self.surface, start_coordinates, [self.fire_power * math.cos(self.angle),
                                                                       self.fire_power * math.sin(self.angle)])]
            self.fire_on = 0
            self.fire_power = 10
            return new_projectiles

    def draw(self):
        """
        Drawing artillery gun with narrow-angle aim
        """
        trans_surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
        pg.draw.polygon(
            trans_surface,
            RED + (120,),
            ((self.coordinates[0] - self.width / 2 * math.sin(self.angle),
              self.coordinates[1] + self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] +
              self.length * self.fire_power * math.cos(self.angle) - self.width / 2 * math.sin(self.angle),
              self.coordinates[1] +
              self.length * self.fire_power * math.sin(self.angle) + self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] +
              self.length * self.fire_power * math.cos(self.angle) + self.width / 2 * math.sin(self.angle),
              self.coordinates[1] +
              self.length * self.fire_power * math.sin(self.angle) - self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] + self.width / 2 * math.sin(self.angle),
              self.coordinates[1] - self.width / 2 * math.cos(self.angle)))
        )
        self.surface.blit(trans_surface, (0, 0))
        super().draw()

    def get_type(self):
        return "Artillery"


class Shotgun(Gun):
    def fire_end(self, event):
        """
        Projectile shot towards the cursor
        :param event: MOUSEBUTTONUP event
        """
        if event.type == pg.MOUSEBUTTONUP:
            start_coordinates = [self.coordinates[0] + self.length * 10 * math.cos(self.angle),
                                 self.coordinates[1] + self.length * 10 * math.sin(self.angle)]
            print("start coordinates" + str(start_coordinates))
            new_projectiles = [
                Shrapnel(self.surface, start_coordinates, [self.fire_power * math.cos(self.angle + math.pi / 12),
                                                           self.fire_power * math.sin(self.angle + math.pi / 12)]),
                Shrapnel(self.surface, start_coordinates, [self.fire_power * math.cos(self.angle + math.pi / 24),
                                                           self.fire_power * math.sin(self.angle + math.pi / 24)]),
                Shrapnel(self.surface, start_coordinates, [self.fire_power * math.cos(self.angle),
                                                           self.fire_power * math.sin(self.angle)]),
                Shrapnel(self.surface, start_coordinates, [self.fire_power * math.cos(self.angle - math.pi / 24),
                                                           self.fire_power * math.sin(self.angle - math.pi / 24)]),
                Shrapnel(self.surface, start_coordinates, [self.fire_power * math.cos(self.angle - math.pi / 12),
                                                           self.fire_power * math.sin(self.angle - math.pi / 12)])
            ]
            self.fire_on = 0
            self.fire_power = 10
            return new_projectiles

    def draw(self):
        """
        Drawing shotgun with wide-angle aim
        """
        trans_surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
        aim_width = self.width + ((self.fire_power - 10) / 40) * 54
        pg.draw.polygon(
            trans_surface,
            RED + (120,),
            ((self.coordinates[0] - self.width / 2 * math.sin(self.angle),
              self.coordinates[1] + self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] +
              self.length * 10 * math.cos(self.angle) - self.width / 2 * math.sin(self.angle),
              self.coordinates[1] +
              self.length * 10 * math.sin(self.angle) + self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] +
              self.length * self.fire_power * math.cos(self.angle) - aim_width / 2 * math.sin(self.angle),
              self.coordinates[1] +
              self.length * self.fire_power * math.sin(self.angle) + aim_width / 2 * math.cos(self.angle)),
             (self.coordinates[0] +
              self.length * self.fire_power * math.cos(self.angle) + aim_width / 2 * math.sin(self.angle),
              self.coordinates[1] +
              self.length * self.fire_power * math.sin(self.angle) - aim_width / 2 * math.cos(self.angle)),
             (self.coordinates[0] +
              self.length * 10 * math.cos(self.angle) + self.width / 2 * math.sin(self.angle),
              self.coordinates[1] +
              self.length * 10 * math.sin(self.angle) - self.width / 2 * math.cos(self.angle)),
             (self.coordinates[0] + self.width / 2 * math.sin(self.angle),
              self.coordinates[1] - self.width / 2 * math.cos(self.angle)))
        )
        self.surface.blit(trans_surface, (0, 0))
        super().draw()

    def get_type(self):
        return "Shotgun"


pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.update()
clock = pg.time.Clock()
finished = False

ground = Ground(screen)
tanks_list = [Tank(screen, 300, ControlButtons([100, 97])),
              Tank(screen, 1200, ControlButtons([1073741903, 1073741904]))]
tank_under_control = 0
targets_list = []
score_list = [0, 0]
projectiles_list = []
particles_list = []
guns_list = [Artillery(screen, tanks_list[0].coordinates),
             Artillery(screen, tanks_list[1].coordinates)]

while not finished:
    # Рождение новых целей
    if len(targets_list) < 4 and rand.random() < 1 / (FPS * 5):
        if rand.random() < 0.2:
            targets_list.append(Airship(screen))
        else:
            targets_list.append(AirBalloon(screen))

    # Рисование всего
    screen.fill(SKY)
    ground.draw()
    for i in range(len(guns_list)):
        guns_list[i].draw()
    for i in range(len(tanks_list)):
        tanks_list[i].draw()
    for i in range(len(targets_list)):
        targets_list[i].draw()
    print(projectiles_list)
    for i in range(len(projectiles_list)):
        print("drawing " + str(projectiles_list[i]) + " " + str(projectiles_list[i].coordinates))
        projectiles_list[i].draw()
    for i in range(len(particles_list)):
        particles_list[i].draw()
    print("\n")

    # Вывод на дисплей всего
    pg.display.update()
    clock.tick(FPS)

    # Обработка ввода
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if len(tanks_list) == 1:
                pass
            if event.key == 32 and tank_under_control == 0:
                tanks_list[tank_under_control].velocity = [0, 0]
                tank_under_control = 1
            elif event.key == 32 and tank_under_control == 1:
                tanks_list[tank_under_control].velocity = [0, 0]
                tank_under_control = 0
            if event.key == 1073742048 and guns_list[tank_under_control].get_type() == "Artillery":
                guns_list[tank_under_control] = Shotgun(screen, tanks_list[0].coordinates)
            elif event.key == 1073742048 and guns_list[tank_under_control].get_type() == "Shotgun":
                guns_list[tank_under_control] = Artillery(screen, tanks_list[0].coordinates)
        tanks_list[tank_under_control].control(event)
        guns_list[tank_under_control].targetting(event)
        guns_list[tank_under_control].fire_start(event)
        new_projectiles = guns_list[tank_under_control].fire_end(event)
        if new_projectiles != None:
            projectiles_list = projectiles_list + new_projectiles

    # Двигаем всё
    for i in range(len(tanks_list)):
        tanks_list[tank_under_control].move()
    for i in range(len(targets_list)):
        targets_list[i].move()
    print(projectiles_list)
    for i in range(len(projectiles_list)):
        print("moving " + str(projectiles_list[i]) + " " + str(projectiles_list[i].coordinates))
        projectiles_list[i].move()
    print("\n")
    guns_list[tank_under_control].move_to(tanks_list[tank_under_control].coordinates)
    guns_list[tank_under_control].power_up()

    # Дирижабль бросает бомбы
    for i in range(len(targets_list)):
        if targets_list[i].get_type() == "Airship" and rand.random() < 1 / (FPS * 5):
            projectiles_list.append(targets_list[i].drop_bomb())

    # Проверяем на попадание
    for j in range(len(targets_list)):
        i = 0
        while i < len(projectiles_list):
            if projectiles_list[i].is_hit_vehicle(targets_list[j]):
                targets_list[j].take_damage(projectiles_list[i].get_damage())
                projectiles_list.pop(i)
            else:
                i += 1

    for j in range(len(tanks_list)):
        i = 0
        while i < len(projectiles_list):
            if projectiles_list[i].is_hit_vehicle(tanks_list[j]):
                tanks_list[j].take_damage(projectiles_list[i].get_damage())
                projectiles_list.pop(i)
            else:
                i += 1

    i = 0
    while i < len(projectiles_list):
        if projectiles_list[i].is_hit_ground():
            if projectiles_list[i].get_type() == "Shell" or projectiles_list[i].get_type() == "Bomb":
                particles_list.append(projectiles_list[i].death())
            projectiles_list.pop(i)
        else:
            i += 1

    i = 0
    while i < len(projectiles_list):
        if projectiles_list[i].is_out_of_screen():
            projectiles_list.pop(i)
        else:
            i += 1

    # Смерть старых целей и танков
    i = 0
    while i < len(targets_list):
        if targets_list[i].is_dead():
            new_particle, new_experience = targets_list[i].death()
            particles_list.append(new_particle)
            score_list[tank_under_control] += new_experience
            targets_list.pop(i)
        else:
            i += 1

    i = 0
    while i < len(tanks_list):
        if tanks_list[i].is_dead():
            new_particle, new_experience = tanks_list[i].death()
            particles_list.append(new_particle)
            score_list[tank_under_control] += new_experience
            tanks_list.pop(i)
            guns_list.pop(i)
        else:
            i += 1

    if len(tanks_list) == 0:
        finished = True

    # Обработка частиц
    i = 0
    while i < len(particles_list):
        particles_list[i].aging()
        if particles_list[i].get_age() > particles_list[i].get_lifetime():
            particles_list.pop(i)
        else:
            i += 1
pg.quit()
