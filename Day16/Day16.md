# Day 16 Object Oriented Programming (OOP)

## What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm that helps break down larger tasks into smaller, manageable pieces, each of which can be handled by separate individuals or teams. By structuring code this way, functionalities become modular and reusable, allowing for scalable and maintainable codebases suited to complex projects.


## Why is OOP needed?
Without OOP, procedural programming can quickly become complex and challenging to manage, especially as projects grow. OOP helps organize code in a way that mimics real-world entities, making it easier to work collaboratively and maintain flexibility as project requirements evolve.

## Key Concepts
In OOP, an object represents a combination of **attributes** (data) and **methods** (functions):
- **Attributes**: Variables that store information about the object (e.g., a waiter’s assigned tables).
- **Methods**: Functions that define actions the object can perform (e.g., taking an order).

A **class** acts as a blueprint for creating multiple objects with the same structure and behaviors. For instance, a `Waiter` class allows us to create multiple waiter objects, like "Henry" and "Betty," each with their own attributes and methods.

By using OOP, we model real-life objects and their interactions, creating code that is both flexible and easier to maintain.

## Setup

- **Operating System**: Linux (Xubuntu virtual machine)
- **Editor**: Visual Studio Code
- **Interpreter**: Python 3.10.12 64-bit (Linux built-in Python)
- **Virtual Environment**: Python 3.10.12 64-bit
- **Additional Installation**: If `tkinter` is not installed, you can install it with the following command in Linux terminal:
  
  ```bash
  sudo apt-get install python3-tk


## Installing PrettyTable in a Linux Virtual Environment

This guide explains how to install the `prettytable` package in a Python virtual environment on Linux, using the terminal.

### Step 1. Navigate to Your Project Directory

First, open your terminal and navigate to the directory containing your project and virtual environment. For example, if your project is located in `~/repos/100_day_python/Day16`, run:

```bash
cd ~/repos/100_day_python/Day16
```

### Step 2. Activate the Virtual Environment

Activate the virtual environment by running the following command:

```bash
source .venv/bin/activate
```

> **Note**: Replace `.venv` with the name of your virtual environment folder if it's different.

### Step 3. Install PrettyTable

With the virtual environment activated, use `pip` to install `prettytable`:

```bash
pip install prettytable
```

### Step 4. Verify the Installation

To confirm that `prettytable` is installed, run:

```bash
python -c "import prettytable; print(prettytable.__version__)"
```

This should output the version of `prettytable`, confirming that it has been successfully installed.