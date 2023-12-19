; Ожидание появления окна "Open"
WinWait("Open", "")

; Перевод окна "Open" в активное состояние
WinActivate("Open", "")

; Ожидание, пока окно "Open" станет активным
WinWaitActive("Open", "")

; Получение пути к текущему каталогу скрипта
Local $scriptDir = @ScriptDir

; Создание относительного пути к файлу C:\Users\AU\Desktop\a.ubasnikov\utilities\avatar.png
Local $filePath = $scriptDir & "\..\utilities\avatar.png"

; Клик в поле "Edit"
ControlClick("Open", "", "[CLASS:Edit; INSTANCE:1]")

; Ввод пути к файлу в поле "Edit"
ControlSetText("Open", "", "[CLASS:Edit; INSTANCE:1]", $filePath)

; Нажатие кнопки "Open"
ControlClick("Open", "", "[CLASS:Button; INSTANCE:1]")