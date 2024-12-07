import os
import cv2
import torch
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def select_video():
    """동영상 파일 선택."""
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    if video_path:
        video_entry.delete(0, tk.END)
        video_entry.insert(0, video_path)


def select_weights():
    """가중치 파일 선택."""
    weight_path = filedialog.askopenfilename(
        title="Select Weights File",
        filetypes=[("PT files", "*.pt"), ("All files", "*.*")]
    )
    if weight_path:
        weight_entry.delete(0, tk.END)
        weight_entry.insert(0, weight_path)


def run_detection():
    """YOLOv5 분석 실행."""
    video_path = video_entry.get()
    weight_path = weight_entry.get()

    if not os.path.exists(video_path):
        messagebox.showerror("Error", "Invalid video file path.")
        return
    if not os.path.exists(weight_path):
        messagebox.showerror("Error", "Invalid weights file path.")
        return

    try:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=weight_path)
        cap = cv2.VideoCapture(video_path)

        # FPS 값을 가져옵니다 (원래 속도의 프레임 속도)
        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / fps)  # 원래의 지연 시간 (밀리초 단위)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # YOLOv5 모델로 추론
            results = model(frame)

            # 결과 렌더링
            result_frame = results.render()[0]
            result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)

            # tkinter에 표시할 이미지로 변환
            img = Image.fromarray(result_frame)

            # tkinter Label 크기에 맞게 이미지 크기 조정
            label_width = video_label.winfo_width()
            label_height = video_label.winfo_height()
            img_resized = img.resize((label_width, label_height), Image.Resampling.LANCZOS)

            imgtk = ImageTk.PhotoImage(image=img_resized)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            video_label.update()

            # 2배 속도로 처리하기 위해 2프레임씩 건너뛰기
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 1)

            # 2배 속도에 맞게 지연 시간 조정 (지연을 줄임)
            cv2.waitKey(int(delay / 2))  # 원래 지연 시간의 절반으로 설정

        cap.release()
        messagebox.showinfo("Info", "Detection completed!")

    except Exception as e:
        messagebox.showerror("Error", f"Detection failed: {e}")


# GUI 설계
root = tk.Tk()
root.title("Wild Boar Detection")

# 동영상 경로 입력
tk.Label(root, text="Video File:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
video_entry = tk.Entry(root, width=50)
video_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_video).grid(row=0, column=2, padx=5, pady=5)

# 가중치 경로 입력
tk.Label(root, text="Weights File:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
weight_entry = tk.Entry(root, width=50)
weight_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_weights).grid(row=1, column=2, padx=5, pady=5)

# 동영상 표시할 Label
video_label = tk.Label(root)
video_label.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")

# 실행 버튼
tk.Button(root, text="Run Detection", command=run_detection, bg="green", fg="white").grid(row=3, column=0, columnspan=3,
                                                                                          pady=10)

# 창 크기 조정 가능하게 만들기
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
