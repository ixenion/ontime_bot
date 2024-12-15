-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY AUTO_INCREMENT,
    -- Если пользователь указал имя пользователя в своем профиле,
    -- его можно сохранить для удобства.
    username VARCHAR(255) UNIQUE NOT NULL,
    -- Идентификатор чата (chat_id): Уникальный идентификатор,
    -- который позволяет идентифицировать пользователя в системе
    -- Telegram. Это основной ключ для связи с пользователем.
    chat_id VARCHAR(255) NOT NULL
);

--Cоздание таблицы самих событий для отправки
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY AUTO_INCREMENT,
    -- Ссылка на пользователя, который отправил событие
    user_id BIGINT,
    -- Время для отправки события
    event_time TIMESTAMP,
    -- Текст сообщения для отправки
    message TEXT,
     -- Флаг, показывающий, отправлено ли событие, по дефолту False(не отправлено)
    is_sent BOOLEAN DEFAULT FALSE,
    -- Время создания события
    created_at TIMESTAMP,
    -- Флаг, показывающий, удалено ли событие, по дефолту False(не удалено)
    is_deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (username, chat_id) VALUES
('HitrayaPechenka', '12345')