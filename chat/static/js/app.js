document.addEventListener("DOMContentLoaded", function() {
    const roomsList = document.getElementById("rooms-ul");
    const roomChat = document.getElementById("room-chat");
    const roomNameElement = document.getElementById("room-name");
    const messagesList = document.getElementById("messages-list");
    const messageInput = document.getElementById("message-input");
    const sendMessageBtn = document.getElementById("send-message-btn");
    const userSelect = document.getElementById("user-select");

    let roomName = null;
    let chatSocket = null;

    // جلب قائمة المستخدمين من الخادم
    fetch('/api/users/')
        .then(response => response.json())
        .then(users => {
            users.forEach(user => {
                const option = document.createElement("option");
                option.value = user.id; // استخدام معرف المستخدم
                option.textContent = user.username; // عرض اسم المستخدم
                userSelect.appendChild(option);
            });
        });

    // إحضار قائمة الغرف من الـ API
    fetch('/api/rooms/')
        .then(response => response.json())
        .then(rooms => {
            rooms.forEach(room => {
                const roomItem = document.createElement('li');
                roomItem.textContent = room.room_name;
                roomItem.addEventListener('click', () => loadRoom(room));
                roomsList.appendChild(roomItem);
            });
        });

    // عند اختيار غرفة
    function loadRoom(room) {
        roomName = room.room_name;
        roomNameElement.textContent = roomName;

        // إنشاء WebSocket
        chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`);

        // استقبال الرسائل من WebSocket
        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            const messageItem = document.createElement('li');
            messageItem.textContent = `${data.user}: ${data.message}`;
            messagesList.appendChild(messageItem);
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
    }

    // إرسال رسالة جديدة
    sendMessageBtn.addEventListener('click', () => {
        const messageContent = messageInput.value.trim();
        const selectedUser = userSelect.value;

        if (messageContent === '' || !chatSocket) return;

        chatSocket.send(JSON.stringify({
            'message': messageContent,
            'username': selectedUser, // تأكد من أن الحقل مطابق لما هو متوقع في الخادم
        }));

        messageInput.value = ''; // مسح خانة الإدخال
    });
});
