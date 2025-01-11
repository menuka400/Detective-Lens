import cv2
import torch
from ultralytics import YOLO

def Detective_Lens_camera():
    # Select device: GPU if available, else CPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")

    # Load YOLO model
    yolo_model = YOLO('C:\\Users\\menuk\\Desktop\\Detective_Lens_System_YOLOv8\\train\\weights\\best.pt')

    # Move model to the selected device
    yolo_model.model.to(device)

    # Open the default camera (usually the first one)
    video_capture = cv2.VideoCapture(0)

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            if not ret:
                print("Error: Failed to capture frame from the camera.")
                break

            # Resize the frame to (640, 640)
            frame_resized = cv2.resize(frame, (640, 640))

            # Normalize the frame
            frame_resized = frame_resized / 255.0

            # Move frame to GPU, convert to float, and add batch dimension
            frame_tensor = torch.from_numpy(frame_resized).float().to(device).permute(2, 0, 1).unsqueeze(0)

            # Detect objects in the frame
            with torch.no_grad():
                results = yolo_model(frame_tensor)

            # Extract the detections
            detections = results[0].boxes  # assuming the first result contains the detection
            classes = detections.cls
            confidences = detections.conf
            boxes = detections.xyxy

            # Draw boxes and labels
            for i, box in enumerate(boxes):
                if confidences[i] >= 0.5:
                    xmin, ymin, xmax, ymax = box.cpu().numpy()
                    label = f"{yolo_model.names[int(classes[i])]} {confidences[i]:.2f}"
                    color = (0, int(classes[i]), 255)  # This color can be adjusted
                    cv2.rectangle(frame_resized, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color, 2)
                    cv2.putText(frame_resized, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

            # Display the resulting frame
            cv2.imshow('Detective_Lens', frame_resized)

            # Check if the user pressed 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        video_capture.release()
        cv2.destroyAllWindows()

# Call the function to start Detective_Lens from the camera
Detective_Lens_camera()
