
# Uso de os.system
import os
os.system("ls")

# Uso de subprocess.run
import subprocess
subprocess.run(["ls"])

# Uso de subprocess.run con dos argumentos
subprocess.run(["ls","-l"])

# Uso de subprocess.run con tres argumentos
subprocess.run(["ls","-l","README.md"])

# Recuperación de información del sistema
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Recuperación de información sobre el espacio en disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
