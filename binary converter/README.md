# Binary to Decimal Converter

This simple Python script provides a graphical user interface (GUI) for converting binary numbers to their decimal equivalent. The program allows you to input a binary number, and it will display the corresponding decimal value.

## How to Use

1. Run the script, and a window will open displaying the GUI.

2. Enter a binary number into the input field labelled "Binary."

3. Click the "Calculate" button to convert the binary number to its decimal equivalent.

4. The result will be displayed in the field labelled "Decimal."

## Algorithm Explanation

The conversion process follows these steps:

1. Input a binary number.

2. Count the number of digits in the binary number and subtract 1 from the count. Assign the result to the starting power of the most significant bit.

3. Create a loop to iterate over each digit in the binary number.

4. For each digit, calculate the product by multiplying the digit by 2 raised to the corresponding power based on its position in the binary number.

5. Sum all the products obtained in the previous step to get the decimal equivalent of the binary number.

## Dependencies

- Python 3.x
- Tkinter (included in most standard Python installations)

## Screenshots

![Binary to Decimal Converter](screenshot.png)

## Acknowledgments

This Binary to Decimal Converter was developed as a handy utility to practice Python programming and provide an easy way to convert binary numbers to decimals using a user-friendly GUI.

Enjoy using the Binary to Decimal Converter and exploring the world of binary and decimal numbers!
