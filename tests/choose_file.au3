; Ожидание появления окна "Открытие"
WinWait("Открытие", "")

; Перевод окна "Открытие" в активное состояние
WinActivate("Открытие", "")

; Ожидание, пока окно "Открытие" станет активным
WinWaitActive("Открытие", "")

; Получение пути к текущему каталогу скрипта
Local $scriptDir = @ScriptDir

; Создание относительного пути к файлу C:\Users\AU\Desktop\a.ubasnikov\downloads\avatar.png
Local $filePath = $scriptDir & "\..\downloads\avatar.png"

; Клик в поле "Edit"
ControlClick("Открытие", "", "[CLASS:Edit; INSTANCE:1]")

; Ввод пути к файлу в поле "Edit"
ControlSetText("Открытие", "", "[CLASS:Edit; INSTANCE:1]", $filePath)

; Нажатие кнопки "Открыть"
ControlClick("Открытие", "", "[CLASS:Button; INSTANCE:1]")