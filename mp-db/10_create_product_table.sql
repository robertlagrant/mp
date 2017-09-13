CREATE TABLE product(
  id SERIAL,
  name character varying(80) COLLATE pg_catalog."default",
  price numeric,
  product_code character varying(10) COLLATE pg_catalog."default",
  CONSTRAINT product_pkey PRIMARY KEY (id),
  CONSTRAINT product_name_key UNIQUE (name),
  CONSTRAINT product_product_code_key UNIQUE (product_code)
)
