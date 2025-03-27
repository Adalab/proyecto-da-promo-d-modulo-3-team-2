import pandas as pd
import mysql.connector

def extract_data(csv_path):
    """Lee datos desde un archivo CSV."""
    try:
        df = pd.read_csv(csv_path, index_col=0)
        return df
    except FileNotFoundError:
        print(f"Error: El archivo CSV '{csv_path}' no fue encontrado.")
        return None

def transform_data(df):
    """Limpia y formatea los datos."""
    if df is None:
        return None

    # Limpiar nombres de columnas (eliminar espacios y convertirlos a snake_case)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Limpiar la columna employee_number
    if 'employee_number' in df.columns:
        df['employee_number'] = pd.to_numeric(df['employee_number'], errors='coerce').fillna(0).astype(int)
    else:
        print("Advertencia: La columna 'employee_number' no se encontró.")

    # Asegurar tipos de datos correctos 
    if 'distance_from_home' in df.columns:
        df['distance_from_home'] = pd.to_numeric(df['distance_from_home'], errors='coerce')
    if 'education' in df.columns:
        df['education'] = pd.to_numeric(df['education'], errors='coerce').fillna(0).astype(int)
    if 'hourly_rate' in df.columns:
        df['hourly_rate'] = pd.to_numeric(df['hourly_rate'], errors='coerce')
    if 'job_involvement' in df.columns:
        df['job_involvement'] = pd.to_numeric(df['job_involvement'], errors='coerce').fillna(0).astype(int)
    if 'job_level' in df.columns:
        df['job_level'] = pd.to_numeric(df['job_level'], errors='coerce').fillna(0).astype(int)
    if 'job_satisfaction' in df.columns:
        df['job_satisfaction'] = pd.to_numeric(df['job_satisfaction'], errors='coerce').fillna(0).astype(int)
    if 'monthly_income' in df.columns:
        df['monthly_income'] = pd.to_numeric(df['monthly_income'], errors='coerce')
    if 'monthly_rate' in df.columns:
        df['monthly_rate'] = pd.to_numeric(df['monthly_rate'], errors='coerce').fillna(0).astype(int)
    if 'num_companies_worked' in df.columns:
        df['num_companies_worked'] = pd.to_numeric(df['num_companies_worked'], errors='coerce').fillna(0).astype(int)
    if 'percent_salary_hike' in df.columns:
        df['percent_salary_hike'] = pd.to_numeric(df['percent_salary_hike'], errors='coerce').fillna(0).astype(int)
    if 'performance_rating' in df.columns:
        df['performance_rating'] = pd.to_numeric(df['performance_rating'], errors='coerce')
    if 'relationship_satisfaction' in df.columns:
        df['relationship_satisfaction'] = pd.to_numeric(df['relationship_satisfaction'], errors='coerce').fillna(0).astype(int)
    if 'stock_option_level' in df.columns:
        df['stock_option_level'] = pd.to_numeric(df['stock_option_level'], errors='coerce').fillna(0).astype(int)
    if 'total_working_years' in df.columns:
        df['total_working_years'] = pd.to_numeric(df['total_working_years'], errors='coerce')
    if 'training_times_last_year' in df.columns:
        df['training_times_last_year'] = pd.to_numeric(df['training_times_last_year'], errors='coerce').fillna(0).astype(int)
    if 'work_life_balance' in df.columns:
        df['work_life_balance'] = pd.to_numeric(df['work_life_balance'], errors='coerce')
    if 'years_at_company' in df.columns:
        df['years_at_company'] = pd.to_numeric(df['years_at_company'], errors='coerce').fillna(0).astype(int)
    if 'years_since_last_promotion' in df.columns:
        df['years_since_last_promotion'] = pd.to_numeric(df['years_since_last_promotion'], errors='coerce').fillna(0).astype(int)
    if 'years_with_curr_manager' in df.columns:
        df['years_with_curr_manager'] = pd.to_numeric(df['years_with_curr_manager'], errors='coerce').fillna(0).astype(int)

    return df

def load_data(df, db_config):
    """Inserta los datos en las tablas de MySQL."""
    if df is None:
        return

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # --- Inserción en la tabla Employees ---
        employees_query = """
            INSERT INTO Employees (EmployeeID, Attrition, BusinessTravel, DistanceFromHome, Education, EducationField, Gender, MaritalStatus, RemoteWork)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        employees_data_to_insert = [
            (row.get('employee_number'), row.get('attrition'), row.get('business_travel'),
             row.get('distance_from_home'), row.get('education'), row.get('education_field'),
             row.get('sex'), row.get('marital_status'), row.get('remote_work'))
            for index, row in df.iterrows()
        ]
        cursor.executemany(employees_query, employees_data_to_insert)
        print(f"{cursor.rowcount} registros insertados en la tabla Employees.")

        # --- Inserción en la tabla JobDetails ---
        job_details_query = """
            INSERT INTO JobDetails (EmployeeID, JobInvolvement, JobLevel, JobRole, JobSatisfaction, YearsAtCompany, YearsSinceLastPromotion, YearsWithCurrManager)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        job_details_data_to_insert = [
            (row.get('employee_number'), row.get('job_involvement'), row.get('job_level'),
             row.get('job_role'), row.get('job_satisfaction'), row.get('years_at_company'),
             row.get('years_since_last_promotion'), row.get('years_with_curr_manager'))
            for index, row in df.iterrows()
        ]
        cursor.executemany(job_details_query, job_details_data_to_insert)
        print(f"{cursor.rowcount} registros insertados en la tabla JobDetails.")

        # --- Inserción en la tabla Salaries ---
        salaries_query = """
            INSERT INTO Salaries (EmployeeID, MonthlyIncome, MonthlyRate, PercentSalaryHike, StockOptionLevel)
            VALUES (%s, %s, %s, %s, %s)
        """
        salaries_data_to_insert = [
            (row.get('employee_number'), row.get('monthly_income'), row.get('monthly_rate'),
             row.get('percent_salary_hike'), row.get('stock_option_level'))
            for index, row in df.iterrows()
        ]
        cursor.executemany(salaries_query, salaries_data_to_insert)
        print(f"{cursor.rowcount} registros insertados en la tabla Salaries.")

        # --- Inserción en la tabla Performance ---
        performance_query = """
            INSERT INTO Performance (EmployeeID, EnvironmentSatisfaction, PerformanceRating, RelationshipSatisfaction, TrainingTimesLastYear, WorkLifeBalance)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        performance_data_to_insert = [
            (row.get('employee_number'), row.get('environment_satisfaction'), row.get('performance_rating'),
             row.get('relationship_satisfaction'), row.get('training_times_last_year'), row.get('work_life_balance'))
            for index, row in df.iterrows()
        ]
        cursor.executemany(performance_query, performance_data_to_insert)
        print(f"{cursor.rowcount} registros insertados en la tabla Performance.")

        # --- Inserción en la tabla Demographics ---
        demographics_query = """
            INSERT INTO Demographics (EmployeeID, NumCompaniesWorked, TotalWorkingYears, OverTime, HourlyRate)
            VALUES (%s, %s, %s, %s, %s)
        """
        demographics_data_to_insert = [
            (row.get('employee_number'), row.get('num_companies_worked'), row.get('total_working_years'),
             row.get('overtime'), row.get('hourly_rate'))
            for index, row in df.iterrows()
        ]
        cursor.executemany(demographics_query, demographics_data_to_insert)
        print(f"{cursor.rowcount} registros insertados en la tabla Demographics.")

        connection.commit()
        print("Cambios guardados en la base de datos.")

    except mysql.connector.Error as err:
        print(f"Error al insertar datos en MySQL: {err}")
        if connection and connection.is_connected():
            connection.rollback()
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    csv_path = "Transformando_el_talento_Final.csv"
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'AlumnaAdalab',
        'database': 'Optimización de Talento'
    }

    # Ejecutar el proceso ETL
    data = extract_data(csv_path)
    transformed_data = transform_data(data)

    if transformed_data is not None:
        load_data(transformed_data, db_config)