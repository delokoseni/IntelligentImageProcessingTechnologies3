import os
import random
import shutil

base_dir = "emnist_letters_folder"
train_dir = os.path.join(base_dir, "train")
test_dir = os.path.join(base_dir, "test")
split_ratio = 0.8  # 80% train 20% test

for letter in os.listdir(base_dir):
    letter_path = os.path.join(base_dir, letter)

    if not os.path.isdir(letter_path):
        continue
    if letter in ["train", "test"]:
        continue

    images = os.listdir(letter_path)
    random.shuffle(images)
    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    test_images = images[split_index:]
    os.makedirs(os.path.join(train_dir, letter), exist_ok=True)
    os.makedirs(os.path.join(test_dir, letter), exist_ok=True)

    for img in train_images:
        shutil.move(
            os.path.join(letter_path, img),
            os.path.join(train_dir, letter, img)
        )

    for img in test_images:
        shutil.move(
            os.path.join(letter_path, img),
            os.path.join(test_dir, letter, img)
        )
    os.rmdir(letter_path)

print("Готово")