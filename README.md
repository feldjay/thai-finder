# thai-finder
A lightweight web application for displaying the Thai restaurants with the top 10 health inspection ratings in NYC!

## Schema
![ alt tag](https://i.imgur.com/LayTnEs.png)
Because the data is denormalized in the NYC Open Data CSV--the rows contain information for every health inspection, meaning restaurants appear multiple times)--pandas is used to manipulate the rows into Dataframes, which are then inserted into the SQL database. Using the external ID (header 'CAMIS') as the unique identifier, A table of restaurants is made with the restaurants identifying information. The grade table stores the health rating information about each restaurant, which it foreign keys to. The CSV is maintained externally and scraped from the NYC Open Data website in a background process.
