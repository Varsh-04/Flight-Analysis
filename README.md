# Navigating the skies: Analysing flight data with python

## Project Overview
This project aims to analyze flight data to uncover trends in air travel, focusing on flight traffic, delays, airline performance, and seasonal variations. Using Python libraries like Pandas, Matplotlib, we will explore the busiest routes, common delay causes, and air traffic patterns. Geospatial mapping will help visualize flight routes and congestion. The analysis will provide insights into airline efficiency and seasonal trends, helping to understand operational challenges in the aviation industry.

## Project Goals
- To Analyze Flight Traffic Trends 
- To Examine Flight Delays 
- To Perform Geospatial Analysis 
- To Compare Airline Performance
- to Identify Seasonal Trends

## Data Structure Overview
The dataset consists of multiple attributes related to flight schedules, durations, pricing, and stops. Below is an overview of the data structure:

Time Attributes
- Date: The date of the flight.
- Year: The year of the flight.
- Month: The month in which the flight occurs.
- Dep_hours, Dep_min: Departure time in hours and minutes.
- Arrival_hours, Arrival_min: Arrival time in hours and minutes.
  
Flight Route Information
- Source: The origin airport or city of the flight.
- Destination: The destination airport or city of the flight.
- Total_Stops: Number of stops between source and destination.

Duration Attributes
- Duration_hours: Flight duration in hours.
- Duration_min: Flight duration in minutes.

Airline & Pricing Information
- IndiGo: Indicates if the airline is IndiGo.
- Price: The actual price of the flight ticket.
- AvgPrice: The average flight price for the given route.

![Flight Data Structure](https://github.com/user-attachments/assets/7b439ac4-3a9d-4a02-a9ad-fe1fbc0cec0f)

## Executive Summary
This project explores flight data to uncover trends in air travel, including flight schedules, delays, and pricing patterns. By analyzing factors like departure times, total stops, and flight durations, we aim to understand how different variables impact travel efficiency. Visualizations and insights from the data will help identify the busiest routes, airline performance, and seasonal variations. This project provides a clear picture of flight operations and travel patterns, making it easier to understand industry trends.

## Insights Deepdive
### Flight Traffic Trends
- Time Series Analysis
- Route Popularity
- Seasonal Analysis
- Correlation Analysis

#### Time Series Analysis
The plot represents the number of flights recorded from March to June in 2019. It shows a significant drop in April, reaching the lowest point of around 1,100 flights, followed by a sharp increase in May, peaking at approximately 3,500 flights. March and June have relatively high flight counts, indicating fluctuations in air traffic during this period. The trend suggests a possible external factor influencing flight numbers in April. 

![Screenshot 2025-02-02 163838](https://github.com/user-attachments/assets/76feea11-7803-41c2-a007-e89d7f393c6f)

#### Route Popularity
The bar chart represents the top 10 most popular flight routes based on the number of flights. The "Delhi to Cochin" route has the highest number of flights, significantly surpassing other routes. "Kolkata to Bangalore" follows as the second most popular route, while routes like "Chennai to Kolkata" have relatively lower flight counts. The visualization highlights major air traffic corridors, suggesting key travel demand patterns. 

![Route Popularity](https://github.com/user-attachments/assets/403ae126-7adf-42a2-b464-bd5399947a02)

### Seasonal Analysis








