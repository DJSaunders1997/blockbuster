# Blockbusters
This project generates printable game sheets for the game of Blockbusters. The game sheets are created using a Python script that generates a PDF file with hexagonal grids and randomized letters in each grid. The PDF file can be printed and used for playing the game.

http://dsaund.pythonanywhere.com/

## Prerequisites
The following packages are required to run the project:
- matplotlib
- numpy
- Flask

You can install the required packages using pip:
```
pip install -r requirements.txt
```

## How to use
To use the Blockbusters project:
1. Clone the project repository to your local machine.
2. Navigate to the project directory and run the Flask app using the following command:
```
python src/app.py
```
3. Open a web browser and navigate to `http://localhost:5000/`.
4. Enter the number of pages you want to generate in the text box and click the "Generate Blockbusters" button.
5. The PDF file with the generated game sheets will be downloaded automatically.

## Using Docker
You can also run the Blockbusters project using Docker. Follow these steps:

1. Build the Docker image using the following command:
```
docker build -t blockbusters-app .
```
2. Run the Docker container using the following command:
```
docker run -p 5000:5000 blockbusters-app
```
3. Open a web browser and navigate to `http://localhost:5000/` to access the app.

## Deploying to Azure Container Apps
This project is deployed to Azure Container Apps for hosting.

## Project structure
The project consists of the following files:
- `src/app.py`: This file contains the Flask app that serves the HTML pages and generates the PDF file.
- `src/blockbusters.py`: This file contains the Python script that generates the hexagonal grids and randomized letters.
- `src/templates/index.html`: This file contains the HTML form that allows the user to enter the number of pages to generate.
- `src/templates/downloads.html`: This file contains the HTML page that shows the link to download the generated PDF file.
- `src/requirements.txt`: This file lists the dependencies required for the project.
- `src/Dockerfile`: This file contains the instructions to build the Docker image for the project.

## Acknowledgements
The hexagonal grid code used in this project was adapted from this [Stack Overflow post](https://stackoverflow.com/questions/46525981/how-to-plot-x-y-z-coordinates-in-the-shape-of-a-hexagonal-grid).
