# Toaster2


Toaster2 - это мой пет-проект для удаленного управления своим компьютером. Реализовано управление через телеграм бота, запущенного на компьютере. Изначально он назывался просто **Toaster**, но та версия была устаревшая, и я заново переписал весь проект.

---

## Функции

С помощью этой команды можно получить сообщение с прикрепленной клавиатурой, через которую выполняются все команды:
```
/start
```

На этой клавиатуре есть кнопки, выполняющие следующие функции:

- Свернуть все окна
- Издать звук хи-хи-ха-ха из игры Clash Royale
- Заставить мышь перемещаться из угла в угол как заставка DVD
- Сделать скриншот экрана и отправить мне в телеграме
- Открыть диалоговое окно с текстом, который я напишу боту

Бот имеет некоторые настройки, которые можно изменять прямо в сообщениях:
```
/settings
```
В настройках ожно менять:

- Качество отправляемых скриншотов (высокое/низкое)
- Очистить папку с сохраненными скриншотами
- Выключить бота

Также имеется команда для проверки работы бота. Если бот работает, он отправит стикер:
```
/test
```

---

## Стек технологий



В проекте я использовал (из основного):
 - Pyton 3.11
 - Aiogram 3.3.0 
 - NirCmd 2.86
 - PyInstaller 6.4.0

---

## Установка

*К сожалению, пока что инструкции по установке нет, но в будущем я что-то сделаю (может быть)*
В папке **Assemly** хранится скомпилированный **Bot.exe**, запускать нужно именно его. Также там лежат необходимые для работы бота файлы и папки