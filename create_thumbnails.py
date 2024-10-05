from PIL import Image
import os

def create_thumbnails(thumbnail_size=(150, 150)):
    source_dir = 'photos_for_processing'
    target_dir = 'thumbnails'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(image_extensions):
            img_path = os.path.join(source_dir, filename)
            if os.path.isfile(img_path):
                try:
                    img = Image.open(img_path)
                    img.thumbnail(thumbnail_size)
                    thumb_filename = 'thumb_' + filename
                    thumb_path = os.path.join(target_dir, thumb_filename)
                    img.save(thumb_path)
                    print(f'Миниатюра сохранена: {thumb_path}')
                except Exception as e:
                    print(f'Ошибка при обработке {img_path}: {e}')

user_input = input('Введите размер миниатюры в формате "ширина,высота" или нажмите Enter для значения по умолчанию (150,150): ')
if user_input:
    try:
        width, height = map(int, user_input.strip().split(','))
        thumbnail_size = (width, height)
    except ValueError:
        print('Некорректный ввод. Используется размер по умолчанию.')
        thumbnail_size = (150, 150)
else:
    thumbnail_size = (150, 150)

create_thumbnails(thumbnail_size)
