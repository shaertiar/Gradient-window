import pygame as pg
import os

# Иниацилизация
pg.init()

# Функция для обновления градиента
def gradient(window):
    from PIL import Image
    import random

    # Попытка найти папку / создать папку
    try: os.mkdir('gradient')
    except: None

    # Попытка найти фото / удалить фото
    try: os.remove('gradient/gradient.png')
    except: None

    # Получение разрпешения экрана
    window_size = WW, WH = window.get_width(), window.get_height()

    # Создание изображения
    image = Image.new('RGBA', (WW//2, WH//2))

    # Значения
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    c = random.randint(0, 1)

    aa = random.randint(1, 10)
    bb = random.randint(1, 10)
    cc = random.randint(1, 10)

    # Окрашивание в градиент
    for i in range(WW//2):
        for j in range(WH//2):
            image.putpixel((i, j), (
                (i if a == 0 else j)//aa, 
                (i if b == 0 else j)//bb, 
                (i if c == 0 else j)//cc))

    # Сохранение фото
    image.save('gradient/gradient.png')

    # Оптимизация фото под размер окна
    image = pg.transform.scale(pg.image.load('gradient/gradient.png'), window_size)

    # Вставка фото в окно
    window.blit(image, (0, 0))

# Создание окна
window = pg.display.set_mode()
pg.display.set_caption('Gradient')

# Скрытие мыши
is_visible_mouse = False
pg.mouse.set_visible(is_visible_mouse)

# Создание часов
clock = pg.time.Clock()

# Установка градиента
gradient(window)
pg.display.update()

# Игровой цикл
is_game = True
while is_game:
    # Обработка событий
    for event in pg.event.get():
        # Обработка выхода
        if event.type == pg.QUIT: is_game = False

        # Обработка нажатий на клавиши
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                gradient(window)

                # Обнволение экрана
                pg.display.update()

            if event.key == pg.K_LCTRL:
                if is_visible_mouse: is_visible_mouse = False
                else: is_visible_mouse = True

                # Скрытие мыши
                pg.mouse.set_visible(is_visible_mouse)

    # Тик
    clock.tick(10)