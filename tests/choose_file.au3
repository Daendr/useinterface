; Получение пути к текущему каталогу скрипта
Local $scriptDir = @ScriptDir

; Создание относительного пути к файлу
Local $filePath = $scriptDir & "\..\downloads\avatar.png"

; Ввод пути к файлу в поле "Edit"
ControlSetText("Открытие", "", "[CLASS:Edit; INSTANCE:1]", $filePath)

; Нажатие кнопки "Открыть"
ControlClick("Открытие", "", "[CLASS:Button; INSTANCE:1]")