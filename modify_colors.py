from PIL import Image, ImageOps
import os

def convert_to_grayscale():
    source_dir = 'thumbnails'
    target_dir = 'grayscale_images'

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(image_extensions):
            img_path = os.path.join(source_dir, filename)
            if os.path.isfile(img_path):
                try:
                    img = Image.open(img_path)
                    img_gray = ImageOps.grayscale(img)
                    gray_filename = 'gray_' + filename
                    gray_path = os.path.join(target_dir, gray_filename)
                    img_gray.save(gray_path)
                    print(f'Сохранено серое изображение: {gray_path}')
                except Exception as e:
                    print(f'Ошибка при обработке {img_path}: {e}')

def create_negative_images():
    source_dir = 'thumbnails'
    target_dir = 'negative_images'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(image_extensions):
            img_path = os.path.join(source_dir, filename)
            if os.path.isfile(img_path):
                try:
                    img = Image.open(img_path)
                    img_negative = ImageOps.invert(img.convert('RGB'))
                    negative_filename = 'negative_' + filename
                    negative_path = os.path.join(target_dir, negative_filename)
                    img_negative.save(negative_path)
                    print(f'Сохранено негативное изображение: {negative_path}')
                except Exception as e:
                    print(f'Ошибка при обработке {img_path}: {e}')

convert_to_grayscale()
create_negative_images()
