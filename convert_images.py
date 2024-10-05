from PIL import Image
import os

def convert_and_resize_images(target_format):
    source_dir = 'photos_for_processing'
    target_dir = 'converted_images'
    supported_formats = ['JPEG', 'PNG', 'BMP', 'GIF']
    if target_format.upper() not in supported_formats:
        print('Невозможно конвертировать изображение в выбранный формат')
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(image_extensions):
            img_path = os.path.join(source_dir, filename)
            if os.path.isfile(img_path):
                try:
                    img = Image.open(img_path)
                    img = img.resize((800, 800))
                    base_name = os.path.splitext(filename)[0]
                    new_filename = f'{base_name}.{target_format.lower()}'
                    new_path = os.path.join(target_dir, new_filename)
                    img.save(new_path, target_format.upper())
                    print(f'Изображение сохранено: {new_path}')
                except Exception as e:
                    print(f'Ошибка при обработке {img_path}: {e}')

format_input = input('Введите формат для конвертации (JPEG, PNG, BMP, GIF): ').upper()
convert_and_resize_images(format_input)
