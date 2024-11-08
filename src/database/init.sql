-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    -- Если пользователь указал имя пользователя в своем профиле,
    -- его можно сохранить для удобства.
    username VARCHAR(100) UNIQUE NOT NULL,
    -- Идентификатор чата (chat_id): Уникальный идентификатор,
    -- который позволяет идентифицировать пользователя в системе
    -- Telegram. Это основной ключ для связи с пользователем.
    chat_id VARCHAR(255) NOT NULL
);

INSERT INTO users (username, chat_id) VALUES
('HitrayaPechenka', '12345'),
('SomeoneElse', '67890');
