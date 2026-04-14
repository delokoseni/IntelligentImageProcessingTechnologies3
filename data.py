from torchvision import datasets, transforms
import string
import os

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

dataset = datasets.EMNIST(
    root="./data",
    split="letters",
    train=True,
    download=True,
    transform=transform
)

base_dir = "emnist_letters_folder"

for letter in string.ascii_uppercase:
    os.makedirs(os.path.join(base_dir, letter), exist_ok=True)

for img, label in dataset:
    letter = chr(label + 64)
    img = img.squeeze(0)
    img_pil = transforms.ToPILImage()(img)
    save_path = os.path.join(base_dir, letter)
    file_name = f"{len(os.listdir(save_path))}.png"
    img_pil.save(os.path.join(save_path, file_name))

