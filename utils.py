import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Abrimos la terminal y escribimos jupyter notebook para que se nos habra en el browser

# ANALISIS DE DATOS DE LOS EMPLEADOS

"""
Esta función carga los datos de una tabla de la base de datos MySQL y los devuelve en un DataFrame de Pandas.

Args:
- conn: Conexión a la base de datos MySQL.
- table: Nombre de la tabla de la cual se cargarán los datos.

Returns:
- df: DataFrame de Pandas con los datos de la tabla.
"""
def load_data_tables(conn:mysql.connector, table:str)->pd.DataFrame:
    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, conn)
    return df

# Top 5 empleados que más años llevan en la compañía
def top_5_antiguos(empleados_df):
    top_antiguos = empleados_df.sort_values(by='F_ALTA').head(5)
    return top_antiguos

# Top 5 empleados más recientes
def top_5_recientes(empleados_df):
    top_recientes = empleados_df.sort_values(by='F_ALTA', ascending=False).head(5)
    return top_recientes

# Distribución del número de años de los empleados en la empresa
def distribucion_anios(empleados_df):
    empleados_df['F_ALTA'] = pd.to_datetime(empleados_df['F_ALTA'])
    empleados_df['antiguedad'] = pd.to_datetime('now').year - empleados_df['F_ALTA'].dt.year
    distribucion_antiguedad = empleados_df['antiguedad'].plot.hist(bins=10)
    plt.xlabel('Antigüedad (años)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de la antigüedad de los empleados')
    plt.grid(True)
    plt.show()
    return distribucion_antiguedad

# Evolución temporal de altas por años
def altas_por_anio(empleados_df):
    altas_por_anio = empleados_df['F_ALTA'].dt.year.value_counts().sort_index().plot()
    plt.xlabel('Año')
    plt.ylabel('Número de altas')
    plt.title('Evolución temporal de altas por años')
    plt.grid(True)
    plt.show()
    return altas_por_anio

# Evolución temporal de bajas por años
def bajas_por_anios(empleados_df):
    bajas_por_anio = empleados_df['F_BAJA'].dt.year.value_counts().sort_index().plot()
    return bajas_por_anio

# ¿Cuáles han sido los dos años de mayor crecimiento/decrecimiento de empleados?
def crec_decrec_2_anios(empleados_df):
    empleados_df['F_BAJA'] = pd.to_datetime(empleados_df['F_BAJA'])
    bajas_por_anio = empleados_df['F_BAJA'].dt.year.value_counts().sort_index()
    crecimiento_decrecimiento = bajas_por_anio.diff().sort_values(ascending=False)
    crecimiento_decrecimiento.plot(kind='bar')
    plt.xlabel('Año')
    plt.ylabel('Crecimiento/Decrecimiento')
    plt.title('Crecimiento/Decrecimiento de empleados por año')
    plt.grid(True)
    plt.show()
    return crecimiento_decrecimiento

# Distribución de empleados solteros vs casados
def solt_vs_casado(empleados_df):
    distribucion_estado_civil = empleados_df['CX_EDOCIVIL'].value_counts().plot(kind='bar')
    plt.xlabel('Estado Civil')
    plt.ylabel('Número de empleados')
    plt.title('Distribución de empleados solteros vs casados')
    plt.grid(True)
    plt.show()
    return distribucion_estado_civil

# Distribución de la edad de los empleados
def edad_por_empleado(empleados_df):
    empleados_df['F_NACIMIENTO'] = pd.to_datetime(empleados_df['F_NACIMIENTO'])
    hoy = pd.Timestamp.now().year
    empleados_df['Edad'] = hoy - empleados_df['F_NACIMIENTO'].dt.year
    distribucion_edad = empleados_df['Edad'].value_counts().sort_index().plot(kind='bar')
    plt.xlabel('Edad')
    plt.ylabel('Número de empleados')
    plt.title('Distribución de la edad de los empleados')
    plt.grid(True)
    plt.show()
    return distribucion_edad

# Edad media de los empleados
def edad_media(empleados_df):
    edad_media = empleados_df['Edad'].mean()
    return edad_media

# Desviación típica de los empleados
def desv_tipica(empleados_df):
    desviacion_tipica = empleados_df['Edad'].std()
    return desviacion_tipica


# ANALISIS DE DATOS DE PROYECTOS

# Calcular el número de proyectos activos
def proyectos_activos(proyectos_df):
    num_proyectos_activos = proyectos_df[proyectos_df['F_BAJA'].isnull()].shape[0]
    return num_proyectos_activos

# Finalizados
def proyectos_finalizados(proyectos_df):
    num_proyectos_finalizados = proyectos_df[~proyectos_df['F_BAJA'].isnull()].shape[0]
    return num_proyectos_finalizados

# Totales
def proyectos_total(proyectos_df):
    num_proyectos_total = proyectos_df.shape[0]
    return num_proyectos_total

# Distribución de la duración de los proyectos (histograma)
def distribucion_duracion(proyectos_df):
    proyectos_df['F_INICIO'] = pd.to_datetime(proyectos_df['F_INICIO'])
    proyectos_df['F_FIN'] = pd.to_datetime(proyectos_df['F_FIN'])
    proyectos_df['duracion'] = (proyectos_df['F_FIN'] - proyectos_df['F_INICIO']).dt.days
    # Crear el histograma de la duración de los proyectos
    proyectos_df['duracion'].plot.hist(bins=10, edgecolor='black')
    plt.xlabel('Duración (días)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de la duración de los proyectos')
    plt.grid(True)
    plt.show()

# Distribución de proyectos por lugar
def distribucion_lugar(proyectos_df):
    distribucion_lugar = proyectos_df['TX_LUGAR'].value_counts().plot(kind='bar')
    plt.xlabel('Lugar')
    plt.ylabel('Número de proyectos')
    plt.title('Distribución de proyectos por lugar')
    plt.grid(True)
    plt.show()
    return distribucion_lugar