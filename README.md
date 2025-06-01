<h1 align="center">🎯 CSGO2-AimBot-YOLOv8</h1>

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWViaTJueHFvMXJ4aWZybjhhNDdsNGZ4NjBkNnNzeDBwYTQwa2cyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/oHuXRj4gvnoOQ7p8nj/giphy.gif" width="260" />
</p>

<p align="center">
  An AI aimbot for Counter-Strike 2 using YOLOv8 to detect enemies and auto-aim.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/Yameteshka/CSGO2-AimBot-YOLOv8?style=for-the-badge&cacheSeconds=10" />
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge" />
  </a>
</p>

---

## 🧠 Disclaimer

This project was built purely for educational and experimental purposes  
to explore YOLOv8 object detection and computer vision in a gaming context.

> ⚠️ The author does **not** support or encourage cheating in multiplayer games.  
> This repository is **not intended** for actual use in online matches.  
> All responsibility lies with the user.

---

## 🗂️ Requirements

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- Virtual camera *(Author used OBS.)*
- **Pre-trained model weights are not included** — train or download your own `.pt` file.
- **Dataset is not provided** — you must collect and annotate your own data.  
  *(Author used [Roboflow](https://roboflow.com) for manual annotation.)*

---

## 📂 Project Structure

- `aimbot.py` — main runtime script for YOLOv8 inference and aiming  
- `aimbot_training.py` — train YOLOv8 model on custom dataset  
- `aimbot_testing.py` — evaluate model on the test set  
- `aimbot_photos_test.py` — save annotated frames for visual inspection  
- `data.yaml` — dataset config (paths and class names)  
- `database_search.py` — optional utility  
- `.gitignore`, `LICENSE`, `README.md` — config and documentation

---

## ⚙️ Setup & Run

```bash
git clone https://github.com/Yameteshka/CSGO2-AimBot-YOLOv8.git
cd CSGO2-AimBot-YOLOv8
pip install -r requirements.txt
python aimbot.py
```

---

## 🧪 Training

```bash
python aimbot_training.py
```

Make sure `train/`, `val/`, and `test/` directories match `data.yaml`.

---

## 📊 Evaluation

```bash
python aimbot_testing.py
```

---

## 🖼️ Visualization

```bash
python aimbot_photos_test.py
```

Outputs are saved in the `output_images/` folder.

---

## 📄 License

This project is licensed under the MIT License.  
See the [`LICENSE`](LICENSE) file for full legal details.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>
</p>
