#! usr/bin/bash
#создание переменных, извлекающих данные из аргументов
SOURCE="$1"
EXEFILE="$2"
 #выполняем компиляцию, запускаем exefile
if gcc  "$SOURCE" -o "$EXEFILE"; then
    ./"$EXEFILE"
else 
#если не найден исходный файл, то выводим строку
    echo "Compilation finish with error(s)"
fi
