## Работа через Docker

Docker **рекомендуется**, если:

- парсер работает **24/7**
- используется **VPS**
- нужен стабильный фоновый режим без привязки к терминалу
- планируется масштабирование или запуск нескольких воркеров

Перед первым запуском **обязательно** настройте файл `config.toml`.

---

### Основные команды (Makefile)

```bash
make build    # собрать Docker-образ
make run      # запустить контейнер в фоне
make restart  # перезапустить контейнер
make rebuild  # полная пересборка: stop → build → run
make stop     # остановить и удалить контейнер
make logs     # посмотреть логи контейнера
make shell    # зайти внутрь контейнера (bash)
make clean    # удалить контейнер и Docker-образ
```

💡 Все команды являются обёртками над docker / docker-compose
и описаны в Makefile. При необходимости их легко адаптировать под себя.

### Запуск через docker-compose

```bash
touch database.db
docker-compose up -d
```

#### Podman / podman-compose

При использовании podman-compose рекомендуется установка из ветки main,
так как в релизных версиях присутствуют баги:

https://github.com/containers/podman-compose/issues/1275

### Сервер (VPS)

Для круглосуточной работы в Docker подойдёт любой недорогой VPS с Ubuntu/Debian (от 1–2 ГБ RAM при включённом `use_webdriver = false` в `config.toml`).

> 💡 Если вы разворачиваете парсер на сервере без графического интерфейса и не хотите тянуть тяжёлый образ с Playwright/Chromium, используйте лёгкую библиотеку **[avito-sdk](https://github.com/eminsk/avito-sdk)** (`pip install avito-sdk`).
