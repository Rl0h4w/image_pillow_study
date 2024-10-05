from PIL import Image, ImageOps
import os

def create_collage():
    source_dir = 'thumbnails'
    collage_width = 600
    collage_height = 600
    images_per_row = 4
    images_per_column = 4
    image_width = collage_width // images_per_row
    image_height = collage_height // images_per_column
    collage_image = Image.new('RGB', (collage_width, collage_height), color='white')
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(image_extensions)]

    image_files.sort()

    index = 0
    for row in range(images_per_column):
        for col in range(images_per_row):
            if index >= len(image_files):
                break
            img_path = os.path.join(source_dir, image_files[index])
            try:
                img = Image.open(img_path)
                img = img.resize((image_width, image_height))
                img = ImageOps.expand(img, border=2, fill='black')
                x = col * image_width
                y = row * image_height
                collage_image.paste(img, (x, y))
                index += 1
            except Exception as e:
                print(f'Ошибка при обработке {img_path}: {e}')
                index += 1
    collage_image.save('collage.jpg')
    print('Коллаж сохранён как collage.jpg')
create_collage()
