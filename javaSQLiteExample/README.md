## Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).


## Notas Adicionales del desarrollador
+ Se requiere utilizar el driver de jdbc para sqlite3 `sqlite-jdbc-3.36.0.3`, una vez que se agraga a `Referenced Library` se crea un archivo temporal que se debe considerar en la ejecución ` noSeQueHace.jar`, puede tener un nombre muy críptico, como 'C:\Users\joelm\AppData\Local\Temp\cp_474nycvbwfek1um2gndbsnrmm.jar' .
+ Se compila `javac -d bin src/net/codejava/*.java `
+ Se ejecuta como proyecto de la siguiente forma ` java -cp noSeQuehace.jar net.codejava.SQLiteDemo `
+ El archivo ` noSeQueHace.jar` hace referencia al archivo 'C:\Users\joelm\AppData\Local\Temp\cp_eeh2e2zmab44ffkrk3249uxfu.jar' y se desconoce qué hace este jar