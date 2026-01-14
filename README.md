# software_now_assignment_2

# HIT137 Group Assignment 2 (20% Mark)

This repository contains the solution to **Group Assignment 2** for the HIT137 course. The assignment consists of three questions, and all answers and contributions are recorded in this GitHub repository.

## Submission Guidelines

- Include your GitHub Repository link in a text file `github_link.txt`.
- Zip all the programming files and outputs and `github_link.txt` and upload them to **Learline**.

## Questions

### Question 1: Text File Encryption & Decryption

#### Problem:
Create a program that reads the text file `raw_text.txt`, encrypts its contents using a simple encryption method, and writes the encrypted text to a new file `encrypted_text.txt`. Then, create a function to decrypt the content and a function to verify the decryption was successful.

#### Requirements:
- The encryption should take two user inputs (`shift1`, `shift2`), and follow these rules:
  - For **lowercase letters**:
    - If the letter is in the first half of the alphabet (a-m): shift forward by `shift1 * shift2` positions.
    - If the letter is in the second half (n-z): shift backward by `shift1 + shift2` positions.
  - For **uppercase letters**:
    - If the letter is in the first half (A-M): shift backward by `shift1` positions.
    - If the letter is in the second half (N-Z): shift forward by `shift2^2` positions.
  - Other characters (spaces, tabs, newlines, special characters, and numbers) remain unchanged.

#### Program Behavior:
- Prompt the user for `shift1` and `shift2` values.
- Encrypt the contents of `raw_text.txt`.
- Decrypt the encrypted file.
- Verify the decryption matches the original text file.

---

### Question 2: Temperature Data Analysis

#### Problem:
Create a program that analyzes temperature data collected from multiple weather stations in Australia. The data is stored in multiple CSV files under a `temperatures` folder, with each file representing data from one year. Process **ALL .csv** files in the `temperatures` folder. Ignore missing temperature values (NaN) in calculations.

#### Main Functions to Implement:
- **Seasonal Average**: Calculate the average temperature for each season across all stations and all years. Save the results to `average_temp.txt`.
  - Use Australian seasons: 
    - Summer (Dec-Feb)
    - Autumn (Mar-May)
    - Winter (Jun-Aug)
    - Spring (Sep-Nov)
  - Output format example: `Summer: 28.5°C`
  
- **Temperature Range**: Find the station(s) with the largest temperature range (difference between the highest and lowest temperature ever recorded at that station). Save the results to `largest_temp_range_station.txt`.
  - Output format example: `Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)`
  - If multiple stations tie, list all of them.

- **Temperature Stability**: Find the station(s) with the most stable temperatures (smallest standard deviation) and the most variable temperatures (largest standard deviation). Save the results to `temperature_stability_stations.txt`.
  - Output format example:
    - `Most Stable: Station XYZ: StdDev 2.3°C`
    - `Most Variable: Station DEF: StdDev 12.8°C`
  - If multiple stations tie, list all of them.

---

### Question 3: Recursive Geometric Pattern with Turtle Graphics

#### Problem:
Create a program that uses a recursive function to generate a geometric pattern using Python's Turtle graphics. The pattern starts with a regular polygon and recursively modifies each edge to create intricate designs.

#### Pattern Generation Rules:
- For each edge of the shape:
  1. Divide the edge into three equal segments.
  2. Replace the middle segment with two sides of an equilateral triangle pointing inward (creating an indentation).
  3. This transforms one straight edge into four smaller edges, each 1/3 the length of the original edge.
  4. Apply this same process recursively to each of the four new edges based on the specified depth.


#### User Input Parameters:
The program should prompt the user for:
- Number of sides: Determines the starting shape.
- Side length: The length of each edge of the initial polygon in pixels.
- Recursion depth: How many times to apply the pattern rules.

