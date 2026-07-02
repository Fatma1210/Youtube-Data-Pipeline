# Project Setup Guide

## Requirements

- Python 3.10

## Install System Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

## Install Python Using Miniconda

1. Download and install **Miniconda**.
2. Create a new virtual environment:

```bash
conda create -n venv
```

3. Activate the environment:

```bash
conda activate venv
```

### Optional: Improve Terminal Readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Update the `.env` file with your own configuration values.

## Running the Application

Start the application with:

```bash
python src/main.py
Verify `youtube_data.db` is created with populated `channels`, `videos`, and `comments` tables.
```

## Pipeline Architecture

```markdown
<img width="1431" height="741" alt="Youtube ETL Pipeline-Page-2 drawio" src="https://github.com/user-attachments/assets/fab7a087-b12f-49b6-b13f-7d1bd809a453" />

```
## Console Output
```markdown
<img width="1115" height="259" alt="image" src="https://github.com/user-attachments/assets/aef8b832-1335-42ef-839d-a010d45d783a" />
```

