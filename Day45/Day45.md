# Day 45 Web Scraping with Beautiful Soup

## Introduction to Web Scraping

Even though API (Application Programming Interface) is useful, but not every website has APIs that we can use, or their APIs do not let us do all the things we want to do.

As a solution, we can use web scraping to get information that we want from the website.

For example, an HTML parser is a useful tool to do that.

## What is HTML parser

HTML parser is a program/software by which useful statement can be extracted, leaving html tages (like `<h1>`, `<span>`, `<p>` etc.) behind.

## What is Beautiful Soup

Beautiful Soup is a Python package from parsing HTML and XML documents, including those with malformed markup.

## Installing Beautifulsoup4 in a Virtual Environment (Recommended)
To install beautifulsoup4 in a **virtual environment** and **not globally**, follow these steps:

### Step 1: Create a virtual environment
If you haven't created a virtual environment yet, you can create one by running the following command in your project directory:

```bash
python3 -m venv .venv
```
This will create a directory named `.venv` (you can choose a different name) that will contain your isolated Python environment.

Alternatively, in **VS Code**, you can open the Command Palette by pressing `Ctrl+Shift+P`, then type and select **Python: Create Environment** to create a virtual environment through the IDE.

### Step 2: Activate the virtual environment

After creating the virtual environment, activate it using the following command:

- On Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```

- On Windows:
  ```bash
  .venv\Scripts\activate
  ```

Once activated, your terminal prompt should change to show that the virtual environment is active (it should look something like `(.venv)` before the prompt).

### Step 3: Install Beautifulsoup4 in the virtual environment

Now that the virtual environment is active, you can install beautifulsoup4 specifically within it by running the following command:

```bash
python3 -m pip install beautifulsoup4
```

This will install beautifulsoup4 **only** within the virtual environment.

### Step 4: Verify the installation

You can verify that Selenium was installed correctly in the virtual environment by running:

```bash
pip show beautifulsoup4
```

This should display details about the beautifulsoup4 package, confirming it's installed in the virtual environment.

### Step 5: Deactivate the virtual environment

Once you're done working in the virtual environment, you can deactivate it by simply running:

```bash
deactivate
```

This will return you to the global Python environment.

---

By following these steps, **beautifulsoup4 will only be available in the virtual environment** and not in your global Python environment. Each time you want to use beautifulsoup4, make sure to activate the virtual environment first.
