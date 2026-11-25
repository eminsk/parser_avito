# 🛠️ Архитектура и гайд для разработчиков (`v3.2.29`)

Документ описывает устройство поддерживаемой редакции **[Avito Parser Community Edition](https://github.com/eminsk/parser_avito)** (Flet GUI + `curl_cffi` + Playwright) для тех, кто дорабатывает парсер под свои задачи или расширяет интеграции.

> ⚡ **Разрабатываете Telegram-ботов, FastAPI-сервисы или MCP-инструменты для ИИ?** Для библиотечного и серверного использования проще подключать готовый пакет [`avito-sdk`](https://github.com/eminsk/avito-sdk) (`pip install avito-sdk`, sync/async клиенты без Chromium).

---

## Общая структура проекта

- `AvitoParser.py` — графический интерфейс на Flet (настройка фильтров, модальные окна прокси, запуск фонового потока `AvitoParse`).
- `parser_cls.py` — ядро циклического мониторинга (`AvitoParse`), работает автономно без GUI и читает `config.toml` через `load_config.py`.
- `parser/http/client.py` — HTTP-транспорт на `curl_cffi` с динамическим поиском CA-сертификатов (`get_ca_bundle()`) и конвертацией кириллических путей Windows в короткий формат `8.3` для защиты от ошибки `curl: (77)`.
- `playwright_setup.py` и `utils/prompt_user_login.py` — безопасный запуск встроенного Chromium и ручной вход в аккаунт (`storage/own_cookies.json`) с обходом конфликта `Playwright Sync API inside asyncio loop`.
- `db_service.py` — локальное SQLite-хранилище просмотренных объявлений и истории цен (`seen` / сравнение цены для алертов снижения).
- `filters/ads_filter.py` — конвейер фильтрации (цены, белые/чёрные слова, чёрный список продавцов, гео, резервы, продвижения, возраст объявления).
- `tests/` — автотесты `pytest` (60+ модульных тестов на фильтры, БД, извлечение характеристик/продавца/описания, CA-сертификаты, Excel-экспорт и Playwright-логин).

---

## Точки расширения

### 1. Новый канал уведомлений (`integrations/notifications/`)
1. Создайте класс-наследник от `Notifier` в `integrations/notifications/` и реализуйте метод `notify(ad, message)`.
2. Зарегистрируйте провайдера в `integrations/notifications/factory.py`.
3. При необходимости выведите поля настройки в панель **«📨 Уведомления»** в `AvitoParser.py`.

### 2. Новый формат экспорта (`parser/export/`)
1. Реализуйте класс-наследник `ResultStorage` с методом `save(ads: list)`.
2. Подключите его в `parser/export/factory.py` (с учётом режима `one_file_for_link` из `parser/export/naming/`).

### 3. Новый провайдер cookies (`parser/cookies/`)
1. Унаследуйте `CookiesProvider` и реализуйте получение (`get`) и разблокировку (`handle_block`) сессии.
2. По умолчанию поддерживаются собственные cookies браузера и внешнее API (`spfa.pro`), а при использовании мобильных 4G-прокси ([MobileProxy](https://mobileproxy.rent/?p=279117), [бесплатный тест 3 часа](https://mobileproxy.rent/user.html?free&p=279117)) смена IP идёт через `proxy_change_url`.

---

## Запуск тестов и сборка `.exe`

```bash
# Через uv (рекомендуется)
uv run --with-requirements requirements.txt --with pytest pytest -v
```

- Сборка автономного `AvitoParser.exe` автоматизирована в `.github/workflows/release.yml` (включая `--collect-all curl_cffi`, `playwright`, `flet` и упаковку `assets/`).
- Перед отправкой PR или созданием Issue загляните в сообщество **[@avito_sdk_pro](https://t.me/avito_sdk_pro)** и [антиблок-гайд](ANTIBLOCK.md).
