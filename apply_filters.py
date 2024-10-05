from PIL import Image, ImageFilter
import os

def apply_filters(filters):
    source_dir = 'photos_for_processing'
    target_dir = 'filtered_images'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    available_filters = {
        'SHARPEN': ImageFilter.SHARPEN,
        'BLUR': ImageFilter.BLUR,
        'CONTOUR': ImageFilter.CONTOUR,
        'SMOOTH': ImageFilter.SMOOTH
    }

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(image_extensions):
            img_path = os.path.join(source_dir, filename)
            if os.path.isfile(img_path):
                try:
                    img = Image.open(img_path)
                    for filter_name in filters:
                        filter_name_upper = filter_name.upper()
                        if filter_name_upper in available_filters:
                            img = img.filter(available_filters[filter_name_upper])
                        else:
                            print(f'Фильтр {filter_name} не поддерживается. Изображение останется без изменений.')
                    filtered_filename = 'filtered_' + filename
                    filtered_path = os.path.join(target_dir, filtered_filename)
                    img.save(filtered_path)
                    print(f'Изображение сохранено: {filtered_path}')
                except Exception as e:
                    print(f'Ошибка при обработке {img_path}: {e}')

filters_input = input('Введите фильтры через запятую (доступные: SHARPEN, BLUR, CONTOUR, SMOOTH): ')
filters_list = [f.strip() for f in filters_input.split(',')] if filters_input else []

apply_filters(filters_list)
