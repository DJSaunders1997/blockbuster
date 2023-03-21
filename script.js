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

// This function is called when the "Draw Hexagon" button is clicked
function onDrawHexagonButtonClick() {
    // Initialize the canvas and get its context
    const { canvas, ctx } = initializeCanvas();

    // Clear the canvas before drawing a new hexagon
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Calculate the center of the canvas
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // Set the hexagon's radius and line width
    const radius = 50;
    const lineWidth = 5;

    // Draw the hexagon on the canvas
    drawHexagon(ctx, centerX, centerY, radius, lineWidth);
}
