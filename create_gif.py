from PIL import Image
from PIL.Image import Resampling
import os

def apply_zoom_effect(image, frames_count=10, zoom_in=True):
    frames = []
    width, height = image.size
    for i in range(frames_count):
        if zoom_in:
            factor = 1 + i / frames_count
        else:
            factor = 1 - i / frames_count
        new_size = (int(width * factor), int(height * factor))
        img_resized = image.resize(new_size, Resampling.LANCZOS)
        left = (img_resized.width - width) // 2
        top = (img_resized.height - height) // 2
        right = left + width
        bottom = top + height
        img_cropped = img_resized.crop((left, top, right, bottom))
        frames.append(img_cropped)
    return frames

def create_gif(duration=500, use_zoom_effect=False):
    source_dir = 'thumbnails'
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')


    image_files = [
        f for f in os.listdir(source_dir)
        if f.lower().endswith(image_extensions) and f != 'animation.gif'
    ]
    image_files.sort()
    image_files = image_files[:10]
    frames = []
    for filename in image_files:
        img_path = os.path.join(source_dir, filename)
        img = Image.open(img_path)
        if use_zoom_effect:
            frames.extend(apply_zoom_effect(img))
        else:
            frames.append(img)

    if frames:
        frames[0].save(
            'animation.gif',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0
        )
        print(f'GIF-анимация сохранена как {'animation.gif'}')
    else:
        print('Нет доступных изображений для создания GIF.')

duration_input = input('Введите длительность показа каждого кадра в миллисекундах (по умолчанию 500): ')
use_zoom = input('Использовать эффект зума? (да/нет): ').lower() == 'да'

try:
    duration = int(duration_input) if duration_input else 500
except ValueError:
    print('Некорректный ввод. Используется значение по умолчанию 500 мс.')
    duration = 500

create_gif(duration=duration, use_zoom_effect=use_zoom)
