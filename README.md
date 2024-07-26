# Wellness Retreat Platform

A backend service Web API to manage the retreat data for a fictional Wellness Retreat Platform. The service provides to fetch the retreat information and allows users to book a retreat.

# Instructions to set up
## For windows:
1) Install [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
2) [Follow up requirements file for installing required modules](https://github.com/MohanPrasadKandru99/Wellness-Retreat-Platform/blob/master/requirements.txt)
3) Clone the github repo from this [link](https://github.com/MohanPrasadKandru99/Wellness-Retreat-Platform.git)

## Run Application:
        1) python app.py


## Database Design
> Retreats in public schema with two tables: 

1. **Retreats**: Store information about available retreats.
2. **Bookings**: Store booking information made by users.

### API Endpoints

1. **GET /retreats**: Fetch a list of all available retreats.
2. **POST /book**: Create a new booking.
   - **Request Body**: 
   ```json
   {
     "user_id": "string",
     "user_name": "string",
     "user_email": "string",
     "user_phone": "string",
     "retreat_id": "string",
     "retreat_title": "string",
     "retreat_location": "string",
     "retreat_price": "number",
     "retreat_duration": "number",
     "payment_details": "string",
     "booking_date": "string"
   }

> PTR - A retreat cannot be double-booked for the same user.

## Deployment Details

- Deployed URL: [Retreat Data](https://wellness-retreat-platform.onrender.com/retreats)
- Additional Endpoints:
  - POST - `/book`
  - GET - `/search=Yoga`
  - GET - `/filter/location=Pune`
  - GET - `/retreats?page=1&limit=10`

# Thank you!
