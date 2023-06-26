Proyecto Oncoliq

Objetivo: Crear una plataforma que sirva como base de datos de la startup Oncoliq, permitiendo tener un registro de pacientes enroladas, medicos que dan seguimientos a estas pacientes y laboratorio/operarios donde estas pacientes se realizaran el test de Oncoliq.

Navbar:

El Navbar consta de las secciones: Inicio (Padre Html), Laboratorio, Medico, Paciente.

Para agregar items a la base de datos se puede realizar desde las siguientes urls:

Laboratorio: http://127.0.0.1:8000/setLaboratorio

Medico: http://127.0.0.1:8000/setMedico

Paciente: http://127.0.0.1:8000/setPaciente

Para buscar items de la base de datos se puede realizar desde las siguientes urls:

Laboratorio: http://127.0.0.1:8000/getLaboratorio

Medico: http://127.0.0.1:8000/getMedico

Paciente: http://127.0.0.1:8000/getPaciente

Los Modelos de la BD son los siguientes:

Laboratorio: Contiene las columnas laboratorio, operario, email, equipo, fecha, resultado

Medico: Contiene las columnas nombre, apellido, email, institucion, informe, mamografia

Paciente: Contiene las columnas nombre, apellido, email
