# DNIAdivino
El script comienza por solicitar al usuario que ingrese su DNI (Documento Nacional de Identidad). A continuación, se verifica si el DNI tiene el formato correcto, es decir, si tiene 8 dígitos y una letra final. Si el formato es incorrecto, el script muestra un mensaje de error y solicita al usuario que ingrese un DNI válido.

Si el formato es correcto, el script procede a calcular la letra correspondiente al DNI. Para ello, se divide el número del DNI por 23 y se obtiene el resto. Luego, se busca en una tabla predefinida la letra correspondiente al resto obtenido. Si la letra encontrada coincide con la letra final del DNI, el script muestra un mensaje indicando que el DNI es válido. Si no coincide, el script muestra un mensaje indicando que el DNI es inválido.

En resumen, el script verifica si el DNI tiene el formato correcto y calcula su letra correspondiente para determinar si es válido o no. Este script puede ser muy útil en aplicaciones que requieren verificar la identidad de los usuarios, como en el registro de usuarios en una plataforma en línea, en el acceso a servicios financieros, entre otros.
