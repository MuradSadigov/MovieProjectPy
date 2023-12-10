# Nokia Movie Task

## Virtual Environment Setup

### Prerequisites

- Python 3.x installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
- PostgreSQL installed on your system. Download and install it from [PostgreSQL Downloads](https://www.postgresql.org/download/).

### Setting up a Virtual Environment (venv)

1. **Open a terminal or command prompt:**

    - **On Windows:** `cmd` or `powershell`, and press Enter.
    - **On macOS/Linux:** open the terminal through your preferred method.

2. **Navigate to your project directory:**

    ```bash
    cd path/to/your/project
    ```

3. **Create a virtual environment:**

    ```
    python3 -m venv venv
    ```
    or
    ```
    py -m venv venv
    ```

    This will create a virtual environment named `venv` in your project directory.

4. **Activate the virtual environment:**

    - **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

    - **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

    You should see `(venv)` in your command prompt or terminal, indicating that the virtual environment is active.

### Installing Dependencies

1. **Ensure your virtual environment is activated.**

2. **Install dependencies using `pip`:**

    ```bash
    pip install -r requirements.txt
    ```

### Deactivating the Virtual Environment

When you're done working on your project, deactivate the virtual environment:

```bash
deactivate
```
### Environmental variables
1. **Create `.env` file in the `app` directory**

    You can create it manually or: **Run the command below inside of the `app` directory**
    ```
    cp .env.example .env
    ```


2. **Edit the `.env` file with your PostgreSQL details:**

    ```
    DB_NAME="your_database_name"
    DB_USER="your_database_user"
    DB_PASSWORD="your_database_password"
    DB_HOST="your_database_host"
    DB_PORT="your_database_port"
  
    ```
    Replace the placeholder values with your actual PostgreSQL database details.