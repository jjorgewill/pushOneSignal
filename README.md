# pushOneSignal
Backend de notificaciones Push usando OneSignal 

Paso 1: Clona el proyecto o descargalo a tu pc  
Paso 2: Crear un entorno virtual  
Paso 3: Instalar las dependencias que estan en conf/base/requeriment.txt   
-- *para agilizar el proceso se puede ejecutar el comando:* **pip install -r conf/base/requeriment.txt**  
Paso 4: Copiar tus credenciales de OneSignal.com en el archivo apps.core.properties
Paso 5: el fichero apps.core.helpers contiene una clase **OneSignalHelper** que es la encargada de realizar la notificación push hacia todos los dispositivos suscritos

**NOTA:** para agregar mas funcionalidades pueden apoyarse en la guia de https://pypi.org/project/onesignal-sdk/
