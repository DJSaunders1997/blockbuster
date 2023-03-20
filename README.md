# Blockbusters
This project generates printable game sheets for the game of Blockbusters. The game sheets are created using a Python script that generates a PDF file with hexagonal grids and randomized letters in each grid. The PDF file can be printed and used for playing the game.
## Prerequisites
The following packages are required to run the project:
- matplotlib
- numpy
- Flask
You can install the required packages using pip:
```
pip install matplotlib numpy Flask
```
## How to use
To use the Blockbusters project:
1. Clone the project repository to your local machine.
2. Navigate to the project directory and run the Flask app using the following command:
```
python app.py
```
3. Open a web browser and navigate to `http://localhost:5000/`.
4. Enter the number of pages you want to generate in the text box and click the "Generate Blockbusters" button.
5. The PDF file with the generated game sheets will be downloaded automatically.
## Project structure
The project consists of the following files:
- `app.py`: This file contains the Flask app that serves the HTML pages and generates the PDF file.
- `blockbusters.py`: This file contains the Python script that generates the hexagonal grids and randomized letters.
- `templates/index.html`: This file contains the HTML form that allows the user to enter the number of pages to generate.
- `templates/downloads.html`: This file contains the HTML page that shows the link to download the generated PDF file.
## Acknowledgements
The hexagonal grid code used in this project was adapted from this [Stack Overflow post](https://stackoverflow.com/questions/46525981/how-to-plot-x-y-z-coordinates-in-the-shape-of-a-hexagonal-grid).