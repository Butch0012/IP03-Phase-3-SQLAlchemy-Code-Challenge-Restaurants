# 🍔 Phase 3 Code Challenge: Restaurants 🌮

Welcome to the culinary code adventure! In this challenge, let's explore the world of restaurant reviews using the magic of SQLAlchemy. 🚀

## Topics

- **SQLAlchemy Migrations**
- **SQLAlchemy Relationships**
- **Class and Instance Methods**
- **SQLAlchemy Querying**

---

## Instructions

Your mission, should you choose to accept it, is to build out the methods listed in the deliverables below. Feel free to tackle them in any order, but beware, some methods depend on others.

⚠️ **Remember:** This challenge doesn't have tests, so no running `pytest`. Test your code in the console as you write.

You're encouraged to use the `seeds.py` file to cook up some sample data for testing your models and relationships. Writing error-free code is more important than completing all deliverables. Prioritize methods that work over quantity.

Before you submit, taste your code! Save and run it to ensure it works as expected. If a method is still in the oven, leave comments describing your progress.

---

## What You Need

Ensure you have migrations and models for the initial `Restaurant` and `Customer` models. Seed data for some `Restaurants` and `Customers` is a must.

**Schema Snapshot:**

**Restaurants Table**
| Column   | Type   |
|----------|--------|
| name     | String |
| price    | Integer|

**Customers Table**
| Column      | Type   |
|-------------|--------|
| first_name  | String |
| last_name   | String |

Now, let's dive into the sizzling deliverables!

---

## Deliverables

### Migrations

Before the feast, create a migration for all tables:

- A `Review` belongs to a `Restaurant` and a `Customer`. In your migration, add columns for these relationships.
- The `reviews` table should also have a `star_rating` column storing an integer.

👨‍🍳 *Chef's Tip:* Use `seeds.py` to prep instances of all your classes for testing.

### Object Relationship Methods

#### Review
- `Review.customer()`: Returns the `Customer` instance for this review.
- `Review.restaurant()`: Returns the `Restaurant` instance for this review.

#### Restaurant
- `Restaurant.reviews()`: Returns all reviews for the `Restaurant`.
- `Restaurant.customers()`: Returns all customers who reviewed the `Restaurant`.

#### Customer
- `Customer.reviews()`: Returns all reviews left by the `Customer`.
- `Customer.restaurants()`: Returns all restaurants the `Customer` has reviewed.

---

### Aggregate and Relationship Methods

#### Customer
- `Customer.full_name()`: Returns the full name of the customer, Western style.
- `Customer.favorite_restaurant()`: Returns the restaurant with the highest star rating from this customer.
- `Customer.add_review(restaurant, rating)`: Adds a new review for the restaurant with the given `restaurant_id`.
- `Customer.delete_reviews(restaurant)`: Removes all reviews for this restaurant.

#### Review
- `Review.full_review()`: Returns a string formatted as: "Review for {restaurant name} by {customer's full name}: {review star rating} stars."

#### Restaurant
- `Restaurant.fanciest()`: Class method. Returns the restaurant with the highest price.
- `Restaurant.all_reviews()`: Returns a list of strings with all reviews for this restaurant.

---

Bon appétit, fellow coder! May your code be as flavorful as your favorite dish! 🍕✨
## CODER: ELNATHAN M.
