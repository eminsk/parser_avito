# Avito Parser (Community Edition by [@eminsk](https://github.com/eminsk))

[![Release v3.2.29](https://img.shields.io/badge/release-v3.2.29-brightgreen.svg?logo=github)](https://github.com/eminsk/parser_avito/releases/tag/v3.2.29)
[![Tests](https://img.shields.io/badge/tests-61%20passed-success.svg)](https://github.com/eminsk/parser_avito/actions)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Avito SDK Pro](https://img.shields.io/badge/Avito_SDK_Pro-v0.4.4_GUI_%26_SDK-38bdf8.svg)](https://github.com/eminsk/avito-sdk/releases/latest)
[![Telegram Канал](https://img.shields.io/badge/Telegram_Канал-@avito__sdk__pro-26A5E4?logo=telegram&logoColor=white)](https://t.me/avito_sdk_pro)
[![Бесплатный тест прокси 3 часа](https://img.shields.io/badge/Прокси_без_VPN-Тест_3_часа_бесплатно-00C853?logo=cloudflare&logoColor=white)](https://mobileproxy.rent/user.html?free&p=279117)

> **Актуальная поддерживаемая редакция настольного парсера Авито от [@eminsk](https://github.com/eminsk/parser_avito) с графическим интерфейсом (Flet GUI) и фоновым режимом.**  
> Включает все исправления 2026 года: устранение ошибки `curl: (77)`, безопасную авторизацию через аккаунт без зависаний в asyncio, глубокий сбор характеристик («О помещении» и др.), отслеживание изменения цен и имена продавцов.

---

### 🚀 Вышло новое автономное приложение — [Avito SDK Pro](https://github.com/eminsk/avito-sdk/releases/latest)
Ищете более лёгкую, быструю и полностью независимую альтернативу **без Playwright, без Flet и без стороннего `spfa.pro`**?  
Попробуйте флагманский проект от **@eminsk** — **[Avito SDK Pro](https://github.com/eminsk/avito-sdk)**:
- 💻 **Готовый Windows GUI `.exe` (~28 МБ)** на CustomTkinter с живой лентой снайпинга, проверкой прокси/Telegram в 1 клик и экспортом в Excel;
- 🌐 **Любые прокси:** обычные серверные IPv4, экономные Pay-As-You-Go (AstroProxy, Asocks) и [MobileProxy (mobileproxy.rent)](https://mobileproxy.rent/?p=279117);
- ⚡ **Python SDK, CLI и MCP-сервер:** `pip install "avito-sdk[gui]"` для многопоточного парсинга и серверов.

---

### 🚀 Быстрый старт (Windows)

1. Скачайте готовый архив из **[Релизов v3.2.29](https://github.com/eminsk/parser_avito/releases/tag/v3.2.29)**: архив `AvitoParser_3.2.29.zip`.
2. Распакуйте архив в любую удобную папку.
3. Запустите `AvitoParser.exe`.
4. Вставьте ссылки поиска с Авито, настройте фильтры и нажмите **Старт**.

---

### 🌟 Что нового в версиях 3.2.24 – 3.2.27

* **Версия 3.2.27 (24.11.2026)**:
  - Все ссылки UI, Docker-образов (`ghcr.io/eminsk/parser_avito`) и документации полностью переведены на актуальный репозиторий [@eminsk/parser_avito](https://github.com/eminsk/parser_avito);
  - Удалены устаревшие сторонние реферальные ссылки; добавлено актуальное руководство по бюджетным серверным и Pay-As-You-Go мобильным прокси;
  - Настроена автоматическая генерация подробных примечаний к релизам из `CHANGELOG.md`.
* **Версия 3.2.26 (17.11.2026)**:
  - Устранена ошибка `Playwright Sync API inside the asyncio loop` при попытке входа в аккаунт через Flet UI;
  - Устранен критический баг бесконечного дублирования окон парсера в PyInstaller `.exe` (вызов Playwright теперь идёт через встроенный Node.js драйвер, а не через `sys.executable`);
  - Улучшено логирование ошибок при запуске браузера.
* **Версия 3.2.25 (16.11.2026)**:
  - Полное устранение ошибки `curl: (77) error setting certificate verify locations` при парсинге просмотров и описаний;
  - Динамический поиск CA-сертификатов в каталоге `_MEIPASS` и переменных окружения;
  - Преобразование путей на Windows в короткий формат 8.3 (`GetShortPathNameW`) для корректной работы `libcurl` с кириллицей в именах пользователей;
  - Автоматический fallback сессии на `verify=False` при сбое загрузки сертификатов.
* **Версия 3.2.24 (01.10.2026)**:
  - Глубокий сбор характеристик и параметров объявлений (блок «О помещении», площадь, этаж, спецификации авто и товаров);
  - Отслеживание изменения цен в базе данных SQLite с расчетом динамики и уведомлениями о падении/росте;
  - Извлечение имени продавца (`seller_name`) для всех типов профилей и магазинов.

---

### 📌 Возможности

#### ⚙️ Гибкая фильтрация и сбор
- Мониторинг новых объявлений на Avito в реальном времени.
- Глубокий парсинг: полное описание, количество просмотров, структурированные характеристики.
- Чёрный и белый списки ключевых слов в названии и описании.
- Фильтрация по географии (городу/району), диапазону цен и продавцам.
- Игнорирование резервов и продвинутых объявлений.

#### 📬 Уведомления и выгрузка
- Мгновенные уведомления в Telegram (поддержка нескольких Chat ID).
- Отправка уведомлений в ВКонтакте.
- Отслеживание изменения цены объявлений в SQLite БД.
- Выгрузка результатов в форматированный Excel (`.xlsx`).

#### 🛡️ Обход ограничений и безопасность
- Поддержка мобильных и серверных прокси с автоматической сменой IP по URL.
- Поддержка внешних сервисов cookies.
- Безопасная авторизация через свой аккаунт.

#### 🐳 Варианты запуска
- **GUI (графический интерфейс)**: `python AvitoParser.py` или готовый `AvitoParser.exe`.
- **CLI (фоновый серверный режим)**: `python parser_cls.py`.
- **Docker**: развертывание через `docker-compose.yml`.

---

### 💻 Запуск из исходного кода

Требуется Python 3.10–3.12:

```bash
# Клонирование репозитория
git clone https://github.com/eminsk/parser_avito.git
cd parser_avito

# Установка зависимостей
pip install -r requirements.txt
# или через uv:
uv sync

# Запуск программы
python AvitoParser.py
```

---

### 🛠️ Обратная связь и поддержка

Если вы обнаружили ошибку или у вас есть предложение по улучшению программы, создайте обращение или напишите в сообщество:
- 📢 **[Telegram-канал и чат @avito_sdk_pro](https://t.me/avito_sdk_pro)** — новые релизы `.exe`, советы по прокси и помощь в комментариях.
- 👉 **[Создать Issue на GitHub](https://github.com/eminsk/parser_avito/issues)**

При создании Issue укажите:
1. Вашу операционную систему (Windows, Linux, macOS).
2. Способ запуска (`exe` или исходный код).
3. Версию парсера.
4. Логи из файла `logs/app.log` или скриншот ошибки.
