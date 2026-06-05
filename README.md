# Django Channels Real-Time Chat System

Асинхронное веб-приложение для обмена сообщениями в реальном времени, построенное на базе **Django Channels**, **Daphne** и **Redis**. Проект полностью контейнеризирован с помощью **Docker** и оптимизирован для быстрой локальной разработки.

##  Основной стек технологий
* **Backend:** Python 3.12, Django 5.x (или твоя версия)
* **Asynchronous Server:** Daphne (ASGI)
* **Real-time Networking:** Django Channels, WebSockets
* **Message Broker / Channel Layer:** Redis 7 (Alpine)
* **Environment:** Docker, Docker Compose, WSL2 (Ubuntu)
* **Static Management:** WhiteNoise (эффективная раздача статики админки и фронтенда в контейнерах)

---

##  Архитектура и особенности проекта

* **Асинхронный бэкенд:** Обработка WebSocket-соединений изолирована от классического HTTP-потока благодаря интеграции протокола ASGI (Daphne).
* **Масштабируемый Channel Layer:** Использование Redis в качестве брокера сообщений позволяет связывать процессы разных потребителей (Consumers) и транслировать сообщения в комнаты/группы на лету.
* **Умная конфигурация окружения:** Настройки `CHANNEL_LAYERS` автоматически адаптируются: проект понимает, запущен ли он внутри изолированной сети Docker или тестируется локально через интерактивный Python `shell`.
* **Готовность к Docker Compose:** Быстрый запуск всей инфраструктуры (Web-сервер + Redis) одной командой с автоматическим пробросом портов.

---

##  Как запустить проект локально

### 1. Клонирование репозитория и настройка окружения
```bash
git clone [https://github.com/zero1525/Chat_WebSocket.git](https://github.com/zero1525/Chat_WebSocket.git)
cd Chat_WebSocket