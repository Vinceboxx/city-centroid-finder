# City Centroid Finder

This Python program calculates the centroid of a given list of cities and finds the closest city to that centroid globally using the Geopy API.
If you have a set of friends and you want to find the closest point to all of you to where you can meet, this is the script you were looking for :D .

## Prerequisites

Before running this program, ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Installation

1. Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/your-username/city-centroid-finder.git
    ```

2. Navigate to the project directory:

    ```
    cd city-centroid-finder
    ```

3. Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

## Usage

Run the program using the following command:

    
    python find_centroid.py city1,city2,city3,...
    

Replace `city1,city2,city3,...` with the comma-separated list of city names for which you want to find the centroid.

Example:
    
    python find_centroid.py London,Paris,Berlin
    2024-02-23 17:11:13,187 - INFO - Finding coordinates of London
    2024-02-23 17:11:13,505 - INFO - Finding coordinates of Paris
    2024-02-23 17:11:13,982 - INFO - Finding coordinates of Berlin


    Centroid coordinates: [50.95328836666667, 5.197732105157438]


    The closest city to the centroid is: 11, Minstraat, Schulen, Herk-de-Stad, Hasselt, Limburg, 3540, België / Belgique / Belgien
    


This will calculate the centroid of London, Paris, and Berlin, and find the closest city to that centroid globally.
