CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_description TEXT,
    product_price DECIMAL(10, 2),
    product_category VARCHAR(50),
    in_stock BIT
);

CREATE TABLE sellers (
    seller_id INT PRIMARY KEY,
    seller_name VARCHAR(100),
    seller_email VARCHAR(100),
    seller_contact_number VARCHAR(15),
    seller_address TEXT
);


CREATE TABLE sales_transaction (
    transaction_id INT PRIMARY KEY,
    product_id INT,
    seller_id INT,
    quantity INT,
    transaction_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);