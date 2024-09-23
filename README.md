# Big Al's Inventory Problem

## Overview

This project solves the inventory management problem for Big Al's car dealership. It analyzes a database of car information and provides various insights about the inventory, such as counts of specific types of cars, mileage statistics, and financial calculations related to leasing.

## Data Structure

The car inventory is stored in a list of lists (`carDB`), where each inner list contains the following attributes for a car:

1. **Year** (int) - The year the car was built.
2. **Manufacturer** (str) - The manufacturer of the car.
3. **Model** (str) - The model of the car.
4. **Price** (float) - The price of the car.
5. **Miles** (int) - The number of miles driven.
6. **Color** (str) - The color of the car.
7. **SiriusXM** (str) - Indicates whether the car has Sirius XM (`Y` for yes, `N` for no).

## Features

The script performs the following analyses:

1. **Print Car Details**: Displays the year, mileage, manufacturer, model, and price of each car.
2. **Count Red Cars**: Counts how many cars are red.
3. **Count Cars Before 2010**: Counts how many cars were manufactured before 2010.
4. **Count and List Honda Cars**: Counts how many Hondas are in the inventory and lists their types.
5. **Count Cars with Sirius XM**: Counts how many cars have Sirius XM and lists their manufacturers and models.
6. **Count Cars with Specific Mileage**: Counts how many cars have mileage between 80,000 and 90,000 and lists their manufacturers and models.
7. **Check for Specific Car**: Checks if a specific Toyota Camry XLE exists in the inventory.
8. **Calculate Lease Payments**: Calculates the total income from a three-year lease and the monthly lease payment for each car.

## Requirements

- Python 3.x

## Usage

To run the script, simply execute it in a Python environment. The output will be printed to the console.

```bash
python big_als_inventory.py
