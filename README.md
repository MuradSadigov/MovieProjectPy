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
### Running the project
1. **Run the project using the command below:**

   ```
   py ./app/main.py
   ```
   or
   ```
   python3 ./app/main.py
   ```

### Deactivating the Virtual Environment

When you're done working on your project, deactivate the virtual environment:

```bash
deactivate
```
### Environmental variables
1. **Create `.env` file in the `app` directory**

    Create it manually or: **Run the command below inside of the `app` directory**
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

### Running Tests
1. **Run the tests using the command below**

   ```
   py ./app/test.py
   ```
   or
   ```
   python3 ./app/test.py
   ```

## Usage

### Commands and Corresponding Switches

#### List Movies
1. **Command `l`**
   
  - `l` command will list all the movies.
    ```
     Example:
     Input: l
     Output: <title> by <director> in <year>, <length>
    ```

- Available switches `-v`, `-t`, `-d`, `-a`:

- `-v` will list all the movies with its starring
   ```
    Example:
    Input: l -v
    Output: 
          <title> by <director> in <year>, <length>
	Starring:
		- <actor1 name> at age <age in years at the release of the film>
		- <actor2 name> at age <age in years at the release of the film>
   ```
- `-t` will filter all the movies by its title
   ```
    Input: l -t "Title"
   ```

- `-d` will filter all the movies by its director
   ```
    Input: l -d "Director"
   ```
- `-a` will filter all the movies by its director
   ```
    Input: l -a "Actor"
   ```
- `-la` will sort all the movies by its length in ascending order
   ```
    Input: l -la
   ```
- `-ld` will sort all the movies by its length in descending order
   ```
    Input: l -ld
   ```

- There is also a possibility to run the switches together and the order doesn't matter:

   ```
    Example:
    l -v -t "Title" -a "Actor" -d "Director" -la
   ```
2. **Command `a`**
   
- Available switches `-p`, `-m`

- `-p` will be prompted to give a name and the year of birth for the person.
   ```
    Example:
    Input: a -p
   ```
- `-m` will be prompted to give a title, then give the length in hh:mm format, then name 
       the director, then give the year of release, finally name the actors
   ```
    Input: a -m
   ```
3. **Command `d`**
   
- Available switches `-p`:

- `-p` after switch, a string should be added. And it will remove the person.
   ```
    Example:
    Input: d -p "Name"
   ```
