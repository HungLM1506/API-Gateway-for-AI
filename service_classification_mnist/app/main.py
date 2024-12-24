from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from model import load_model, predict
import uvicorn

app = FastAPI()

# Tải mô hình
model = load_model("mnist_resnet.pth")

@app.post("/predict/")
async def predict_digit(file: UploadFile = File(...)):
    try:
        # Đọc ảnh từ file upload
        image = Image.open(file.file).convert("L")
        
        # Dự đoán số
        predicted_class = predict(model, image)
        return JSONResponse(content={"digit": predicted_class})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Khởi chạy ứng dụng FastAPI khi chạy trực tiếp bằng Python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
