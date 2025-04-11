# 🫠 Django Channels Chat API

## 📌 Overview
This is a real-time chat application built with **Django**, **Django Channels**, and **WebSockets**. It supports **1:1 private messaging**, real-time updates, and a simple frontend chat interface. The system also exposes RESTful APIs to manage chat rooms and messages.

## 🚀 Features
- 🔌 Real-time messaging using **WebSockets** via **Django Channels**  
- 🔐 **1:1 private chat rooms** between users  
- 📡 **REST API** to manage chat rooms and messages  
- 💬 Chat UI inspired by WhatsApp (basic version)  

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework, Django Channels  
- **Real-time Communication**: WebSockets (Django Channels)  
- **Database**: PostgreSQL  
- **Frontend**: HTML, CSS, JavaScript (Vanilla)  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository-link.git
cd your-repository-directory
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Make sure you set up your PostgreSQL credentials in `settings.py`. Then run:
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📡 API Endpoints

### 🔹 Get All Chat Rooms
- **URL**: `/api/rooms/`  
- **Method**: `GET`  
- **Response**:
```json
[
  {
    "room_uuid": "room-uuid",
    "users": ["user1", "user2"],
    "room_name": "Room Name",
    "created_at": "2025-04-11T14:30:11Z"
  }
]
```

---

### 🔹 Get Messages from a Room
- **URL**: `/api/messages/?room_uuid=<room-uuid>`  
- **Method**: `GET`  
- **Response**:
```json
[
  {
    "message_uuid": "message-uuid",
    "content": "Hello! How are you?",
    "room": "Room Name",
    "user": "username",
    "created_at": "2025-04-11T14:30:11Z"
  }
]
```

---

### 🔹 Send a Message
- **URL**: `/api/messages/`  
- **Method**: `POST`  
- **Body**:
```json
{
  "room": "room_uuid",
  "content": "Your message here",
  "user": "username"
}
```

---

## 💬 Frontend
The frontend is a minimal chat UI using HTML/CSS/JS.  
It allows sending/receiving messages in real-time and is available at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔄 WebSocket (Real-Time Messaging)
- WebSocket connections are handled using **Django Channels**.
- Messages are broadcasted instantly to all connected users in the same room.

---

## 🧱️ Models

### 📁 Room
- `room_uuid`: UUID  
- `users`: Many-to-many with User model  
- `room_name`: string  
- `created_at`: datetime  

### 💬 Message
- `message_uuid`: UUID  
- `content`: text  
- `room`: ForeignKey → Room  
- `user`: ForeignKey → User  
- `created_at`: datetime  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes  
4. Push to your fork (`git push origin feature-branch`)  
5. Create a Pull Request  

---

## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgements
- [Django Channels](https://channels.readthedocs.io/) for WebSocket support  
- [Django REST Framework](https://www.django-rest-framework.org/) for APIs  

