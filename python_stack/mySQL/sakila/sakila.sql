SELECT first_name, last_name, email, address.address_id, city.city_id FROM customer
	RIGHT JOIN address ON customer.address_id = customer.address_id
    RIGHT JOIN city ON city.city_id = customer.address_id
    WHERE city.city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM film
	LEFT JOIN film_category ON film.film_id = film_category.film_id
    LEFT JOIN category ON category.category_id = film_category.film_id
	WHERE category.name = "Comedy"
    GROUP BY film.title;

SELECT title, description, release_year FROM film 
	RIGHT JOIN film_actor ON film_actor.actor_id = film_actor.actor_id
	WHERE actor_id = 5;
    
SELECT first_name, last_name, email, address.address_id, store.store_id, address.city_id FROM customer
	LEFT JOIN store ON store.store_id = customer.store_id
    LEFT JOIN address ON address.address_id = customer.address_id
    WHERE store.store_id = 1
    AND address.city_id = 1 
    OR store.store_id = 1 AND address.city_id = 42 
    OR store.store_id = 1 AND address.city_id = 312 
    OR store.store_id = 1 AND address.city_id = 459;
    

SELECT title, description, rating, special_features, release_year, film_actor.actor_id FROM film
	JOIN film_actor ON film_actor.film_id = film.film_id
	WHERE rating = "G"
    AND special_features LIKE "behind the scenes"
    AND film_actor.actor_id = 15;

SELECT title, description, release_year, rental_rate, rating, special_features, category.name FROM film
	JOIN film_category ON film_category.film_id = film.film_id
    JOIN category ON film_category.category_id = film_category.category_id
    WHERE category.name = "Drama"
    AND film.rental_rate = 2.99
	
    