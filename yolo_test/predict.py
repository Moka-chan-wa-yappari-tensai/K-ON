from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model('https://ultralytics.com/images/bus.jpg')

results[0].save('yolo_result.jpg')
print("识别完成，结果已保存！")