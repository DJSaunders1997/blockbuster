// Initialize the canvas and its 2D drawing context
// This function initializes the canvas and its 2D drawing context
function initializeCanvas() {
    // Get the canvas element by its id ("hexagonCanvas")
    // This is the area where we'll draw the hexagon
    const canvas = document.getElementById("hexagonCanvas");

    // Get the 2D drawing context for the canvas
    // The context is an object that provides methods and properties for drawing on the canvas
    // In this case, we're using a 2D context for 2D graphics
    const ctx = canvas.getContext("2d");

    // Return an object containing the canvas and context
    // This object can be used by other functions to draw on the canvas
    return { canvas, ctx };
}

// Draw a hexagon on the canvas with the given context, center coordinates, radius, and line width
function drawHexagon(ctx, centerX, centerY, radius, lineWidth) {
    // Begin a new path on the canvas
    ctx.beginPath();

    // Set the line width for the hexagon
    ctx.lineWidth = lineWidth;

    // Loop through the 6 vertices of the hexagon
    for (let i = 0; i <= 6; i++) {
        // Calculate the angle for each vertex (in radians)
        const angle = (Math.PI / 3) * i;

        // Calculate the x and y coordinates of each vertex
        const x = centerX + radius * Math.cos(angle);
        const y = centerY + radius * Math.sin(angle);

        // If it's the first vertex, move the path to the starting point
        if (i === 0) {
            ctx.moveTo(x, y);
        } else {
            // For the other vertices, draw a line to the next vertex
            ctx.lineTo(x, y);
        }
    }

    // Close the path, connecting the last vertex to the first
    ctx.closePath();

    // Stroke the path, creating the outline of the hexagon
    ctx.stroke();
}

// Draw a grid of hexagons on the canvas
function drawHexagonGrid(ctx, startX, startY, radius, lineWidth, rows, cols) {
    // Calculate the height and width of a hexagon
    const hexHeight = Math.sqrt(3) * radius;
    const hexWidth = 2 * radius;

    // Loop through the rows and columns of the grid
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            // Calculate the offset position for each hexagon
            const offsetX = (col * 3 * radius) / 2;
            const offsetY = (row * hexHeight) + (hexHeight / 2 * (col % 2));

            // Calculate the center position for the current hexagon
            const centerX = startX + offsetX;
            const centerY = startY + offsetY;

            // Draw the hexagon at the calculated position
            drawHexagon(ctx, centerX, centerY, radius, lineWidth);
        }
    }
}

// This function is called when the input fields for rows or columns are changed
function onInputChange() {
    // Initialize the canvas and get its context
    const { canvas, ctx } = initializeCanvas();
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Get values from html element
    const rows = document.getElementById("rows").value;
    const cols = document.getElementById("columns").value;

    const startX = 50;
    const startY = 50;
    const radius = 30;
    const lineWidth = 2;

    // Draw the hexagon grid on the canvas
    drawHexagonGrid(ctx, startX, startY, radius, lineWidth, rows, cols);
}

// Call onInputChange on page load to draw the initial hexagon grid
onInputChange();
