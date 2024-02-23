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

    ```
    python find_centroid.py city1,city2,city3,...
    ```

Replace `city1,city2,city3,...` with the comma-separated list of city names for which you want to find the centroid.

Example:
    
    ```
    python main.py London,Paris,Berlin
    ```


This will calculate the centroid of London, Paris, and Berlin, and find the closest city to that centroid globally.
