-- Crear tabla companies
CREATE TABLE companies (
    company_id VARCHAR(40) NOT NULL,
    company_name VARCHAR(130) NULL,
    PRIMARY KEY (company_id)
);

-- Crear tabla charges
CREATE TABLE charges (
    id VARCHAR(40) NOT NULL,
    company_id VARCHAR(40) NOT NULL,
    amount DECIMAL(16, 2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
