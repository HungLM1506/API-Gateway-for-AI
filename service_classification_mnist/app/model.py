import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import  Image
def load_model(model_path):
    # Tải ResNet-18 và chỉnh lớp cuối
    model = models.resnet18()
    model.fc = nn.Linear(model.fc.in_features, 10)
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()
    return model

def predict(model, image):
    # Preprocessing
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=3),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0)  # Thêm batch dimension
    with torch.no_grad():
        outputs = model(image)
        _, predicted_class = outputs.max(1)
    return predicted_class.item()


# model = load_model("mnist_resnet.pth")
# image = Image.open("../../OIP.jpg").convert("L")
# result = predict(model, image)
# print(result)