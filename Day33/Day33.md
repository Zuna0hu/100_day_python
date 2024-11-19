# Day 33 API Endpoints and API Parameters

## Introduction to API

API stands for Application Programming Interface. APIs allow programs to interact with external systems by following a set of rules and protocols. Websites often carry valuable data, such as weather forecasts, cryptocurrency prices, and basketball player statistics, and APIs offer a way to access this data in a structured manner.

APIs can be likened to a restaurant menu, providing a list of available services (or data) that a user or program can request. Just as a customer cannot directly access a restaurant's kitchen, a program cannot directly access a website's data without following the API's rules. Instead, the API acts as an intermediary, allowing programs to make requests for specific pieces of data. 

### API Endpoints and Requests
In this lesson, we learned about API endpoints, which are the locations where data is stored and accessed via a URL. For example, if you wanted to get cryptocurrency data, you would use an API endpoint like `api.coinbase.com`. To retrieve data from an endpoint, you need to make an API request, similar to going to a bank and asking for money. The API acts as an interface between your program and the external system, ensuring that requests are properly authenticated and processed.

A common format for the data returned by APIs is JSON, which is lightweight and easy to transfer over the internet. JSON can be compared to a flat-packed item from Ikea that can be easily reassembled into its original form once received. JSON is preferred because it's minimalistic and efficient for data transmission.

API call and API request are often used interchangeably and generally mean the same thing: the action of sending a request to an API to retrieve or manipulate data.

To make an API request in Python, we use the `requests` library. By importing this library and calling the `get()` method, you can fetch data from an API endpoint. The data returned is usually in JSON format, which can then be processed and used within your program.

---
### API Parameters

## How to Install `requests` in a Virtual Environment on Ubuntu Linux

Follow these steps to create a virtual environment and install the `requests` library in it on Ubuntu Linux.

### Step 1: Create a Virtual Environment (.venv)
If you haven't created a virtual environment yet, you can create one by running the following command in your project directory:

```bash
python3 -m venv .venv
```
This will create a directory named `.venv` (you can choose a different name) that will contain your isolated Python environment.

Alternatively, in **VS Code**, you can open the Command Palette by pressing `Ctrl+Shift+P`, then type and select **Python: Create Environment** to create a virtual environment through the IDE.

### Step 2: Activate the Virtual Environment
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

### Step 3: Install the `requests` Library in the Virtual Environment

```bash
python3 -m pip install requests
```

Now that the virtual environment is active, use `pip` to install requests:

### Step 4: Verify the Installation
You can verify that `requests` was installed correctly in the virtual environment by running:

```bash
pip show requests
```

### Step 5: Deactivate the Virtual Environment

Once you're done working in the virtual environment, you can deactivate it by simply running:

```bash
deactivate
```

This will return you to the global Python environment.

## Summary
To summarize, an API is a set of predefined functions that allow programs to request and receive data from external sources, and understanding how to interact with APIs is key to pulling live data from websites.