# Elevators simulation

## Description

This project's goal is to simulate two types of lift-controle systems

**First** system will have a simple logic and some minor optimizations

**Second** system will be more complicated and customizable (read more below)

1. The system knows the summary weight of people standing on the first floor
2. The system knows the max capaity of each elevator

Knowing that we can optimize the time in which people will be transfered 
to the desired floors

### For instanse:
> If one of the elevators started to move to the first floor and it's max capacity is already less than the summary weight of the people standing on the first floor,
> we can already send the second lift to the first floor

-----

## The goal

The actual goal of this project is the following:
> **Figure out if it is worth to install such system in a real building**