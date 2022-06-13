import torch
from PIL import Image
from torchvision import transforms


def predict(data):
    img = Image.open("d:/Work/Softarex/Test/AntWeb/images/media/" + data.get("image"))
    data_transforms = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((48, 48)),
        transforms.ToTensor()
        ])
    batch_t = torch.unsqueeze(data_transforms(img), 0)
    model = torch.load('D:/Work/Softarex/Test/AntWeb/FaceModel',map_location=torch.device('cpu'))
    model.eval()
    print(model(batch_t))
    _, output = torch.max(model(batch_t), dim=1)
    print(output)
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    return emotions[output[0]], data_transforms(img)
