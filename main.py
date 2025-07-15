from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from ultralytics import YOLO
import cv2
import numpy as np
import io
from PIL import Image
import uvicorn

app = FastAPI()

model = YOLO('weights/best.pt') 

@app.post('/segment')
async def segment_image(file: UploadFile = File(...)):

    try:
 
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)
        
        results = model(image_np)
        
        img = Image.fromarray(results[0].plot())
        
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        
        return Response(
            content=img_buffer.getvalue(),
            media_type='image/png'
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error processing image: {str(e)}')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=1234)

