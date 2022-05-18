# Shopify Backend Intern Summer 2022 Application

A web application coded in Python for inventory management. Utilizes all CRUD functionality along with the CSV export feature.

## Installation

Ensure the latest version of Python is downloaded according to the instructions [here](https://www.python.org/downloads/)

Begin by downloading all files from this repository. To ensure all external dependencies are downloaded, open the command prompt and enter the directory of this downloaded repository.
```bash
cd {your directory here}
```
 Download all dependencies detailed in requirements.txt by using the below command.

```bash
pip install -r requirements.txt
```

## Usage

Begin by going navigating to the directory containing Main.py through the command prompt. Use the command below to start the application.
```bash
py Main.py
```

Head to the URL `HTTP://localhost:5000` on your browser of choice. This has only been tested on Chrome and Firefox and may not work with older browsers.

From there, a menu will appear to add your first inventory item. Ensure all fields are filled and add the new item. You can edit and delete the item later, so don't worry about making any mistakes.

Once you have an inventory to your liking, it can be downloaded as a CSV using the export button on the main page.
