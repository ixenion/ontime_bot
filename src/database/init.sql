-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- SERIAL автоматически устанавливает id
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
    event_id SERIAL PRIMARY KEY,
    -- Ссылка на пользователя, который отправил событие
    user_id INTEGER,
    -- Время для отправки события с усановленным часовым поясом
    event_time TIMESTAMP WITH TIME ZONE,
    -- Текст сообщения для отправки
    message TEXT,
     -- Флаг, показывающий, отправлено ли событие, по дефолту False(не отправлено)
    is_sent BOOLEAN DEFAULT FALSE,
    -- Время создания события, дефолтно во время создания
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    -- Флаг, показывающий, удалено ли событие, по дефолту False(не удалено)
    is_deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);